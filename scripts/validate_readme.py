#!/usr/bin/env python3
"""Validate the structure and links in the curated README."""

from __future__ import annotations

import argparse
import concurrent.futures
import http.client
import re
import socket
import ssl
import subprocess
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


RESOURCE_RE = re.compile(r"^- \[([^\]]+)]\((https://[^)\s]+)\): (.+)$")
LINK_RE = re.compile(r"^- \[")
USER_AGENT = "awesome-ai-resource-validator/1.0"


@dataclass(frozen=True)
class Resource:
    line: int
    section: str
    category: str
    title: str
    url: str
    description: str


def normalize_url(url: str) -> str:
    parts = urlsplit(url)
    hostname = (parts.hostname or "").lower()
    port = parts.port
    if port and not (parts.scheme.lower() == "https" and port == 443):
        hostname = f"{hostname}:{port}"
    path = parts.path.rstrip("/") or "/"
    return urlunsplit((parts.scheme.lower(), hostname, path, parts.query, ""))


def validate_text(text: str) -> tuple[list[Resource], list[str], list[str]]:
    resources: list[Resource] = []
    errors: list[str] = []
    warnings: list[str] = []
    section = ""
    category = ""
    category_lines: dict[tuple[str, str], int] = {}
    category_counts: dict[tuple[str, str], int] = {}

    for line_number, line in enumerate(text.splitlines(), start=1):
        if line.startswith("## "):
            section = line[3:].strip()
            category = ""
            continue
        if line.startswith("### "):
            category = line[4:].strip()
            category_key = (section, category)
            category_lines[category_key] = line_number
            category_counts[category_key] = 0
            continue
        if not LINK_RE.match(line):
            continue
        match = RESOURCE_RE.match(line)
        if not match:
            errors.append(f"line {line_number}: malformed resource entry")
            continue
        if not category:
            errors.append(f"line {line_number}: resource is outside a level-three category")
            continue
        title, url, description = match.groups()
        if not description.endswith("."):
            errors.append(f"line {line_number}: description must end with a period")
        resource = Resource(line_number, section, category, title.strip(), url, description.strip())
        resources.append(resource)
        category_counts[(section, category)] += 1

    for category_key, count in category_counts.items():
        if count == 0:
            section_name, category_name = category_key
            location = f" in section '{section_name}'" if section_name else ""
            errors.append(
                f"line {category_lines[category_key]}: category '{category_name}'{location} "
                "has no resources"
            )

    seen_titles: dict[str, Resource] = {}
    seen_urls: dict[str, Resource] = {}
    for resource in resources:
        title_key = resource.title.casefold()
        if title_key in seen_titles:
            errors.append(
                f"line {resource.line}: duplicate title '{resource.title}' "
                f"(first used on line {seen_titles[title_key].line})"
            )
        else:
            seen_titles[title_key] = resource

        try:
            url_key = normalize_url(resource.url)
        except ValueError as error:
            errors.append(f"line {resource.line}: invalid URL '{resource.url}' ({error})")
            continue
        if url_key in seen_urls:
            errors.append(
                f"line {resource.line}: duplicate URL '{resource.url}' "
                f"(first used on line {seen_urls[url_key].line})"
            )
        else:
            seen_urls[url_key] = resource

    return resources, errors, warnings


def classify_status(status: int, url: str) -> tuple[str, str] | None:
    if status in {404, 410}:
        return "error", f"broken link ({status}): {url}"
    if status in {401, 403, 429}:
        return "warning", f"link check blocked ({status}): {url}"
    if status == 408:
        return "warning", f"link check timed out ({status}): {url}"
    if status >= 500:
        return "warning", f"remote server error ({status}): {url}"
    if status >= 400:
        return "error", f"broken link ({status}): {url}"
    return None


def classify_exception(error: BaseException, url: str) -> tuple[str, str]:
    reason = error.reason if isinstance(error, urllib.error.URLError) else error
    if isinstance(reason, (TimeoutError, socket.timeout)):
        return "warning", f"link check timed out: {url} ({reason})"
    if isinstance(reason, (ssl.SSLError, socket.gaierror)):
        return "error", f"unreachable link: {url} ({reason})"
    if isinstance(reason, http.client.HTTPException):
        return "warning", f"link check interrupted: {url} ({reason})"
    return "error", f"unreachable link: {url} ({reason})"


def check_link(resource: Resource) -> tuple[str, str] | None:
    headers = {"User-Agent": USER_AGENT}
    request = urllib.request.Request(resource.url, headers=headers, method="HEAD")
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            return classify_status(response.status, resource.url)
    except urllib.error.HTTPError as error:
        if error.code not in {405, 501}:
            return classify_status(error.code, resource.url)
    except (OSError, http.client.HTTPException) as error:
        return classify_exception(error, resource.url)

    request = urllib.request.Request(resource.url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            return classify_status(response.status, resource.url)
    except urllib.error.HTTPError as error:
        return classify_status(error.code, resource.url)
    except (OSError, http.client.HTTPException) as error:
        return classify_exception(error, resource.url)


def check_links(resources: list[Resource]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        for result in executor.map(check_link, resources):
            if result is None:
                continue
            severity, message = result
            (errors if severity == "error" else warnings).append(message)
    return sorted(errors), sorted(warnings)


def validate_churn(base_text: str, current_text: str) -> list[str]:
    base_resources, base_errors, _ = validate_text(base_text)
    current_resources, current_errors, _ = validate_text(current_text)
    if base_errors or current_errors:
        return ["cannot calculate churn until both README versions are structurally valid"]

    def resource_map(resources: list[Resource]) -> dict[str, Resource]:
        return {resource.title.casefold(): resource for resource in resources}

    base = resource_map(base_resources)
    current = resource_map(current_resources)

    def signature(resource: Resource | None) -> tuple[str, str, str, str] | None:
        if resource is None:
            return None
        return resource.section, resource.category, resource.url, resource.description

    changed_titles = {
        title
        for title in base.keys() | current.keys()
        if signature(base.get(title)) != signature(current.get(title))
    }
    foundational_changes = sum(
        1
        for title in changed_titles
        if any(
            resource and resource.section.casefold() == "learn"
            for resource in (base.get(title), current.get(title))
        )
    )
    net_additions = len(current_resources) - len(base_resources)
    errors: list[str] = []
    if len(changed_titles) > 6:
        errors.append(f"churn limit exceeded: {len(changed_titles)} resource entries changed (maximum 6)")
    if net_additions > 3:
        errors.append(f"churn limit exceeded: {net_additions} net entries added (maximum 3)")
    if foundational_changes > 1:
        errors.append(
            f"churn limit exceeded: {foundational_changes} foundational entries changed (maximum 1)"
        )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("readme", nargs="?", default="README.md", type=Path)
    parser.add_argument("--check-links", action="store_true")
    parser.add_argument("--base", help="Git revision used to enforce weekly churn limits")
    args = parser.parse_args()

    resources, errors, warnings = validate_text(args.readme.read_text(encoding="utf-8"))
    if args.check_links:
        link_errors, link_warnings = check_links(resources)
        errors.extend(link_errors)
        warnings.extend(link_warnings)
    if args.base:
        base_text = subprocess.run(
            ["git", "show", f"{args.base}:{args.readme.as_posix()}"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout
        errors.extend(validate_churn(base_text, args.readme.read_text(encoding="utf-8")))

    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    print(f"Validated {len(resources)} resources with {len(errors)} errors and {len(warnings)} warnings.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
