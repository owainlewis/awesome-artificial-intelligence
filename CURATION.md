# Curation policy

This repository is a small, opinionated guide for software developers learning AI engineering. It has two equal pillars:

1. Serious foundations: durable books, papers, courses, and research that explain how AI systems work.
2. Practical engineering: resources that help developers build, evaluate, secure, operate, and improve generative AI and agentic systems.

The goal is not comprehensive coverage. Every entry must be unusually useful, credible, and distinct. A missing topic should remain a documented gap until a resource clears the bar.

## Hard gates

Reject a resource if any of these are true:

- its link is broken or its description cannot be verified;
- it is deprecated, abandoned, or superseded without durable historical value;
- it substantially duplicates a stronger entry;
- it is primarily a product homepage, announcement, shallow collection, or marketing asset;
- its quality, maintenance, adoption, or production-use claims lack evidence;
- it serves a very narrow audience without exceptional technical value and an explicit niche label.

Stars, downloads, release frequency, and social attention are signals, not proof. Use primary sources for factual claims and credible independent sources for adoption or production-use claims. Record unknown evidence as unknown.

## Scoring

Score only after every hard gate passes. Resources need at least 80 out of 100.

### Foundational resources

| Criterion | Weight |
| --- | ---: |
| Technical and intellectual quality | 30 |
| Durability and influence | 25 |
| Value to software developers | 20 |
| Authority and evidence | 15 |
| Distinctiveness | 10 |

Age is not a penalty for foundational work. Judge whether the resource still explains an important idea accurately and better than its alternatives.

### Practical resources and software

| Criterion | Weight |
| --- | ---: |
| Technical or production quality | 25 |
| Applicability to AI engineers | 20 |
| Currentness and maintenance | 20 |
| Real-world evidence | 20 |
| Documentation and learning value | 10 |
| Distinctiveness | 5 |

Currentness means more than a recent release. Check whether the project reflects current models and engineering practices, responds to important issues, and has a credible path forward.

## Coverage

Review developer problems before looking for products. Important areas include:

- model and deep-learning foundations;
- LLM application design, prompting, structured outputs, tools, and security;
- retrieval, data ingestion, fine-tuning, and model serving;
- evals, observability, testing, and production reliability;
- agent design, context, memory, orchestration, and human approval;
- synchronous request-response systems and asynchronous, event-driven, durable agents;
- coding agents, isolated execution, CI feedback, and software factories.

Expand concepts into adjacent terms when researching. For example, software factories include issue-to-PR agents, planner-worker-reviewer systems, isolated runners, CI feedback loops, and coding-agent orchestration. Asynchronous AI systems include background agents, queues, events, checkpointing, retries, resumption, durable execution, and human approval.

## Weekly change rules

The weekly curator may add, correct, replace, or remove entries. It must:

- change no more than six resource entries;
- add no more than three net new entries;
- change no more than one foundational entry;
- avoid cosmetic rewrites, reordering, and category renaming;
- replace an incumbent only when a challenger scores at least 10 points higher or the incumbent fails a hard gate;
- leave uncertain resources unchanged;
- inspect recent curation commits and any open automation pull request before repeating work.

These are ceilings, not targets. No change is a successful result. The automation opens at most one curation pull request and skips future runs until that proposal is merged or closed. A maintainer decides what merges.

## Repository setup

The local weekly curator needs:

- an active Codex desktop automation with authenticated GitHub access;
- permission to create an isolated worktree, push a curation branch, and open a draft pull request;
- branch protection that requires the quality workflow before merge.

The local automation runs each Monday at 09:00 in the desktop timezone. It uses a dated `codex/curation-YYYY-MM-DD` branch, opens a draft pull request for human review, and never merges automatically. GitHub Actions remains responsible only for deterministic quality checks.
