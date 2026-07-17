import socket
import ssl
import unittest
import urllib.error

from scripts.validate_readme import (
    classify_exception,
    classify_status,
    normalize_url,
    validate_churn,
    validate_text,
)


VALID = """# List

### Books

- [A Book](https://example.com/book): A useful book.
"""


class ValidateReadmeTests(unittest.TestCase):
    def test_valid_resource(self):
        resources, errors, warnings = validate_text(VALID)
        self.assertEqual(1, len(resources))
        self.assertEqual([], errors)
        self.assertEqual([], warnings)

    def test_malformed_resource(self):
        _, errors, _ = validate_text("### Books\n\n- [A Book](http://example.com): No TLS.\n")
        self.assertIn("malformed resource entry", errors[0])

    def test_duplicate_title_and_normalized_url(self):
        text = """### Books

- [A Book](https://EXAMPLE.com/book/): First entry.
- [a book](https://example.com/book#section): Second entry.
"""
        _, errors, _ = validate_text(text)
        self.assertTrue(any("duplicate title" in error for error in errors))
        self.assertTrue(any("duplicate URL" in error for error in errors))

    def test_empty_category(self):
        _, errors, _ = validate_text("### Books\n\nSome prose.\n")
        self.assertIn("category 'Books' has no resources", errors[0])

    def test_level_two_heading_resets_category(self):
        text = VALID + "\n## Contributing\n\n- [A Tool](https://example.com/tool): A tool.\n"
        _, errors, _ = validate_text(text)
        self.assertTrue(any("outside a level-three category" in error for error in errors))

    def test_same_category_name_in_different_sections(self):
        text = """## First

### Tools

## Second

### Tools

- [A Tool](https://example.com/tool): A tool.
"""
        _, errors, _ = validate_text(text)
        self.assertTrue(any("section 'First'" in error for error in errors))

    def test_description_needs_period(self):
        _, errors, _ = validate_text(
            "### Books\n\n- [A Book](https://example.com/book): Missing punctuation\n"
        )
        self.assertIn("description must end with a period", errors[0])

    def test_normalize_url(self):
        self.assertEqual(
            "https://example.com/path?q=1",
            normalize_url("HTTPS://EXAMPLE.COM:443/path/?q=1#fragment"),
        )

    def test_invalid_url_is_an_error(self):
        _, errors, _ = validate_text(
            "### Books\n\n- [A Book](https://example.com:bad/book): Invalid port.\n"
        )
        self.assertIn("invalid URL", errors[0])

    def test_link_status_classification(self):
        self.assertEqual("error", classify_status(404, "https://example.com")[0])
        self.assertEqual("error", classify_status(400, "https://example.com")[0])
        self.assertEqual("error", classify_status(451, "https://example.com")[0])
        self.assertEqual("warning", classify_status(403, "https://example.com")[0])
        self.assertEqual("warning", classify_status(408, "https://example.com")[0])
        self.assertEqual("warning", classify_status(503, "https://example.com")[0])
        self.assertIsNone(classify_status(200, "https://example.com"))

    def test_link_exception_classification(self):
        url = "https://example.invalid"
        dns_error = urllib.error.URLError(socket.gaierror("not found"))
        tls_error = urllib.error.URLError(ssl.SSLError("bad certificate"))
        timeout = urllib.error.URLError(TimeoutError("timed out"))
        self.assertEqual("error", classify_exception(dns_error, url)[0])
        self.assertEqual("error", classify_exception(tls_error, url)[0])
        self.assertEqual("warning", classify_exception(timeout, url)[0])

    def test_churn_limits(self):
        base = "## Learn\n\n### Books\n\n- [Book](https://example.com/book): A book.\n\n"
        base += "## Build\n\n### Tools\n\n"
        base += "\n".join(
            f"- [Tool {index}](https://example.com/{index}): A tool."
            for index in range(6)
        )
        acceptable = base.replace("A tool.", "A better tool.", 6)
        self.assertEqual([], validate_churn(base, acceptable))

        too_many = acceptable + "\n- [Tool 7](https://example.com/7): A tool.\n"
        self.assertTrue(any("resource entries" in error for error in validate_churn(base, too_many)))

        four_additions = base + "\n" + "\n".join(
            f"- [New {index}](https://example.com/new-{index}): A tool."
            for index in range(4)
        )
        self.assertTrue(any("net entries" in error for error in validate_churn(base, four_additions)))

        two_foundations = base.replace("A book.", "A revised book.")
        two_foundations = two_foundations.replace(
            "\n## Build",
            "\n- [Second Book](https://example.com/book-2): A book.\n\n## Build",
        )
        self.assertTrue(
            any("foundational entries" in error for error in validate_churn(base, two_foundations))
        )

        moved_to_foundations = base.replace("A book.", "A revised book.")
        moved_to_foundations = moved_to_foundations.replace(
            "\n## Build\n\n### Tools\n\n- [Tool 0](https://example.com/0): A tool.",
            "\n- [Tool 0](https://example.com/0): A tool.\n\n## Build\n\n### Tools",
        )
        self.assertTrue(
            any(
                "foundational entries" in error
                for error in validate_churn(base, moved_to_foundations)
            )
        )


if __name__ == "__main__":
    unittest.main()
