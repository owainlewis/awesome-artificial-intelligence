# Curation policy

This repository is a small, opinionated guide for software developers learning AI engineering. Every resource must serve at least one of three pillars:

1. **AI foundations:** durable books, papers, courses, and technical explanations of machine learning, deep learning, language models, and generative AI.
2. **Building AI systems:** resources for designing, evaluating, securing, deploying, and operating useful AI applications and agents.
3. **Agentic software engineering:** coding-agent harnesses, agent skills, software factories, orchestration, evaluation, and workflows that improve software delivery.

The goal is not comprehensive coverage. Every entry must be unusually useful, credible, and distinct. A missing topic should remain a documented gap until a resource clears the bar.

## Scope gate

Apply scope before quality scoring. A strong resource that does not directly serve one of the three pillars does not belong in this repository.

In scope:

- technical foundations that help developers understand modern AI;
- practical methods and tools for building production AI systems;
- open-source or broadly accessible coding agents and agent harnesses with meaningful capability, documentation, and maintenance;
- durable material about agent skills, context, evals, orchestration, isolated execution, and software factories;
- high-quality books, courses, and tutorials that teach developers these subjects.

Out of scope unless there is exceptional, pillar-specific engineering value:

- general directories, news feeds, launch roundups, prompt collections, or affiliate lists;
- narrow end-user AI products, media-generation tools, chat front ends, and domain-specific applications;
- vendor homepages that do not teach or document a technical capability;
- personal projects submitted mainly for promotion;
- early demos with little documentation, maintenance evidence, or working implementation;
- resources whose main value is unrelated to developers building or using AI systems.

## Hard gates

Reject a resource if any of these are true:

- its link is broken or its description cannot be verified;
- it is deprecated, abandoned, or superseded without durable historical value;
- it substantially duplicates a stronger entry;
- it is primarily a product homepage, announcement, shallow collection, or marketing asset;
- claims about its quality, maintenance, adoption, or production use lack evidence;
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

- model, deep-learning, and generative-AI foundations;
- LLM application design, prompting, structured outputs, tools, and security;
- retrieval, data ingestion, fine-tuning, and model serving;
- evals, observability, testing, and production reliability;
- agent design, context, memory, orchestration, and human approval;
- synchronous request-response systems and asynchronous, event-driven, durable agents;
- coding-agent harnesses, agent skills, isolated execution, CI feedback, and software factories.

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

These are ceilings, not targets. No change is a successful result. The automation maintains at most one automation-owned weekly curation pull request whose head branch matches `codex/curation-*`, and it may update that branch from the latest `origin/master`. It skips creating a new automation-owned weekly proposal when one of those pull requests was merged or closed within the last eight days. Contributor resource pull requests do not trigger this cooldown.

The automation may squash-merge an automation-owned weekly proposal or a contributor resource pull request only when all of these are true on the exact head commit:

- the pull request changes only `README.md`;
- every resource passes the hard gates and scores at least 80;
- the weekly churn and replacement-margin rules pass;
- local unit, structure, churn, and live-link checks pass;
- a fresh independent reviewer returns Approve with no blocker or important findings;
- the GitHub Quality workflow passes;
- the pull request is cleanly mergeable and has no unresolved material feedback.

Any head change invalidates the prior review and checks. The automation must never lower a policy, test, permission, or review gate to make a pull request mergeable.

The final merge must atomically match the reviewed head SHA, for example with `gh pr merge --squash --match-head-commit <sha>`. A mismatch stops the merge and requires fresh review and checks.

## Repository setup

The local weekly curator needs:

- an active Codex desktop automation with authenticated GitHub access;
- permission to create an isolated worktree, push or update its curation branch, and merge its verified pull request;
- branch protection that requires the quality workflow before merge.

The scheduled repository steward must read `AUTOMATION.md` before selecting work. The specialist weekly curator runs each Monday at 09:00 in the desktop timezone. It uses a dated `codex/curation-YYYY-MM-DD` branch, creates or updates one pull request, and squash-merges it automatically only after every exact-head gate above passes. GitHub Actions remains responsible for deterministic quality checks.
