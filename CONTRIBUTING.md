# Contributing

Thanks for helping improve this collection. It is intentionally selective, so a useful project or article may still be out of scope.

## Before proposing a resource

Read `CURATION.md`. Your proposal must directly serve at least one pillar:

1. AI foundations.
2. Building AI systems.
3. Agentic software engineering.

Apply the scope gate before the quality rubric. Do not submit general product directories, shallow launch material, narrow end-user tools, or personal projects whose main purpose is promotion.

Search the README and existing issues and pull requests for duplicates. Prefer an issue when you are unsure whether a resource clears the bar.

## Evidence to provide

Every proposal should explain:

- which pillar it serves and which developer problem it solves;
- what makes it materially different from the strongest existing entry;
- a primary source for factual claims, such as official documentation, a paper, releases, or the source repository;
- credible independent evidence for adoption or production use when making those claims;
- current maintenance status and any important limitations;
- your affiliation with the resource, including employment, ownership, sponsorship, or authorship.

Self-promotion is not disqualifying, but undisclosed promotion is. Stars and launch attention are signals, not proof of quality.

## Pull requests

Keep resource changes small. Use the existing entry format:

```markdown
- [Resource name](https://example.com/): One factual sentence explaining its value to developers.
```

Descriptions must be specific, neutral, verifiable, and end with a period. Do not reorder unrelated entries or rewrite neighbouring descriptions without a reason.

Before opening a pull request, run:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_readme.py README.md --base origin/master
python3 scripts/validate_readme.py README.md --check-links --base origin/master
```

Complete the pull-request template. A maintainer may decline an entry that passes mechanical checks but fails the scope or quality policy.
