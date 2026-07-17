# Awesome Artificial Intelligence

An opinionated, actively maintained collection of resources for software developers learning to build and ship generative AI and agentic systems.

![Artificial intelligence](https://media.giphy.com/media/jeAQYN9FfROX6/giphy.gif)

This list is for developers who want to:

- understand the foundations behind modern AI systems;
- build applications with language models, retrieval, tools, and agents;
- evaluate, observe, and deploy AI systems in production;
- use coding agents to improve software engineering work.

This is not a comprehensive directory of AI products. Every entry must clear an absolute quality bar for technical depth, practical value, evidence, and distinctiveness. Categories are not quotas, and a short category is better than one padded with weak choices.

The list is reviewed weekly by an evidence-backed automation that proposes small changes for human review. See [how resources are evaluated](CURATION.md).

## Learn

### Books

- [Artificial Intelligence: A Modern Approach](https://aima.cs.berkeley.edu/): The broad reference for classical AI, including search, reasoning, planning, learning, and robotics.
- [Reinforcement Learning: An Introduction](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf): Sutton and Barto's foundational treatment of reinforcement learning concepts and algorithms.
- [Designing Machine Learning Systems](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/): Scalable, maintainable machine learning systems by Chip Huyen.
- [AI Engineering](https://www.oreilly.com/library/view/ai-engineering/9781098166298/): Building applications with foundation models by Chip Huyen.
- [Build a Large Language Model from Scratch](https://www.manning.com/books/build-a-large-language-model-from-scratch): Implement transformers in PyTorch with Sebastian Raschka.
- [Hands-On Large Language Models](https://www.llm-book.com/): A visual and practical guide by Jay Alammar and Maarten Grootendorst.
- [LLM Engineer's Handbook](https://www.packtpub.com/en-us/product/llm-engineers-handbook-9781836200079): LLMOps, fine-tuning, serving, and production workflows.
- [The 100-Page Language Models Book](https://www.thelmbook.com/): A concise, technical introduction by Andriy Burkov.
- [Deep Learning](https://www.deeplearningbook.org/): Mathematical foundations by Ian Goodfellow, Yoshua Bengio, and Aaron Courville.
- [Deep Learning: Foundations and Concepts](https://www.bishopbook.com/): A probability-grounded treatment by Christopher and Hugh Bishop.
- [Understanding Deep Learning](https://udlbook.github.io/udlbook/): Theory, intuition, and practical notebooks by Simon Prince.
- [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/): The continuously updated NLP reference by Dan Jurafsky and James Martin.

### Courses

- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1): Transformers, fine-tuning, datasets, and modern NLP tooling.
- [Full Stack Deep Learning](https://fullstackdeeplearning.com/): The full lifecycle of building and shipping AI products.
- [Fast.ai Practical Deep Learning](https://course.fast.ai/): A code-first introduction to deep learning.
- [Karpathy's Neural Networks: Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ): Build neural networks and language models from first principles.
- [Stanford CS336: Language Modeling from Scratch](https://cs336.stanford.edu/): Build language models from data preparation through evaluation and deployment.
- [MIT 6.S191: Introduction to Deep Learning](https://introtodeeplearning.com/): Deep learning foundations and applications.
- [Google Generative AI Learning Path](https://www.cloudskillsboost.google/paths/118): An introductory path through generative AI concepts and Google Cloud tooling.
- [DeepLearning.AI Short Courses](https://learn.deeplearning.ai/): Focused courses on current generative AI engineering techniques.
- [Made With ML](https://madewithml.com/): An open course on designing, developing, deploying, and iterating on production ML systems.

### Foundational papers

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762): Introduced the Transformer architecture.
- [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361): Explored relationships between model performance, data, and compute.
- [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556): Showed how model size and training data should scale together under a compute budget.
- [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165): Demonstrated in-context learning at scale.
- [Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401): Combined parametric language models with external retrieval for knowledge-intensive tasks.
- [LoRA](https://arxiv.org/abs/2106.09685): Introduced low-rank adaptation for parameter-efficient model fine-tuning.
- [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155): Established the instruction tuning and RLHF recipe used by InstructGPT.
- [ReAct](https://arxiv.org/abs/2210.03629): Combined reasoning traces with actions for tool-using language-model agents.
- [Constitutional AI](https://arxiv.org/abs/2212.08073): A method for training helpful and harmless AI assistants using written principles.
- [Direct Preference Optimization](https://arxiv.org/abs/2305.18290): Reframed preference alignment as a simple classification objective without explicit reward modelling.

## Build AI systems

### Guides and playbooks

- [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents): Anthropic's practical patterns and tradeoffs for agentic systems.
- [A Practical Guide to Building Agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf): OpenAI's guide to models, tools, instructions, orchestration, and guardrails.

### LLM application engineering

- [OpenAI Cookbook](https://cookbook.openai.com/): Code examples for structured outputs, tool use, retrieval, evals, and other LLM application patterns.
- [Anthropic Prompt Engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview): Techniques for defining success criteria, testing prompts, and improving model behaviour.
- [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents): How to select, structure, and manage the context available to long-running agents.
- [12-Factor Agents](https://github.com/humanlayer/12-factor-agents): Practical principles for building controllable LLM applications around deterministic software.
- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/): Risks and mitigations for developing and deploying generative AI applications.

### Agent frameworks

- [Pydantic AI](https://ai.pydantic.dev/): Typed agent development built around Pydantic.
- [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview): Low-level orchestration for long-running, stateful agents.
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/): A small SDK for tools, handoffs, guardrails, tracing, and agent orchestration.
- [Google Agent Development Kit](https://google.github.io/adk-docs/): Google's framework for developing and evaluating agents.
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/): Microsoft's successor to AutoGen and Semantic Kernel for agents and graph-based workflows.

### Durable and asynchronous agents

- [Effective Harnesses for Long-Running Agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents): Patterns for agents that make progress across multiple context windows and recover from failure.
- [Running Agents](https://openai.github.io/openai-agents-python/running_agents/): Lifecycle, session, exception, and durable-execution patterns in the OpenAI Agents SDK.
- [Human-in-the-Loop](https://openai.github.io/openai-agents-python/human_in_the_loop/): Pause, inspect, approve, reject, and resume tool calls without losing agent state.
- [Gemini and Temporal Durable Agent](https://ai.google.dev/gemini-api/docs/temporal-example): A concrete implementation of durable execution, retries, and human approval for an agent workflow.

### Retrieval and data

- [LlamaIndex](https://docs.llamaindex.ai/): Data ingestion, indexing, retrieval, and agent workflows.
- [Haystack](https://docs.haystack.deepset.ai/): Modular pipelines for retrieval and generative AI applications.
- [Docling](https://github.com/docling-project/docling): Document parsing and conversion for AI applications.

### Evals and reliability

- [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents): A practical method for building task suites, graders, transcripts, and evaluation harnesses.
- [OpenAI Evals](https://github.com/openai/evals): An open-source framework and registry for evaluating language models and systems.
- [Promptfoo](https://www.promptfoo.dev/docs/): Test cases, assertions, model comparisons, and red-team checks for LLM applications.
- [Ragas](https://docs.ragas.io/): Evaluation and experimentation for retrieval and generative AI applications.

### Deployment and observability

- [Langfuse](https://langfuse.com/docs): Tracing, evaluation, prompt management, and metrics for LLM applications.
- [vLLM](https://docs.vllm.ai/): An inference and serving engine for language models.
- [LiteLLM](https://docs.litellm.ai/): A model gateway and unified interface for multiple model providers.

## Agentic software engineering

Coding agents help developers plan, implement, review, test, and debug software. For independent capability comparisons, see [SWE-bench](https://www.swebench.com/) and [Terminal-Bench](https://www.tbench.ai/leaderboard/terminal-bench/2.1).

### Coding agents

- [Claude Code](https://code.claude.com/): A terminal agent with hooks, subagents, skills, and repository-level instructions.
- [Codex CLI](https://github.com/openai/codex): An open-source terminal agent with sandbox and approval controls.
- [Gemini CLI](https://github.com/google-gemini/gemini-cli): An open-source terminal agent built around Gemini and extensible tools.
- [Cursor CLI](https://cursor.com/cli): A terminal agent connected to Cursor's editor and cloud workflows.
- [GitHub Copilot coding agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent): An asynchronous agent that works from GitHub issues and opens pull requests.
- [Aider](https://aider.chat/): An open-source pair programmer with Git integration and broad model support.
- [OpenCode](https://opencode.ai/): An open-source, provider-independent terminal agent with a client-server architecture.
- [OpenHands](https://docs.all-hands.dev/): An open-source platform for running software development agents locally or in the cloud.
- [Cline](https://github.com/cline/cline): An open-source coding agent available as an editor extension, CLI, and SDK.
- [Continue](https://www.continue.dev/): Open-source coding agents for IDE and CI workflows with source-controlled configuration.

### Software factories and agent orchestration

- [Harness Engineering](https://openai.com/index/harness-engineering/): OpenAI's field report on building software with coding agents, repository constraints, automated checks, and human steering.
- [Codex Orchestration with Symphony](https://openai.com/index/open-source-codex-orchestration-symphony/): A reference architecture that turns project work into isolated, observable coding-agent runs.
- [How We Built Our Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system): Production lessons on orchestrator-worker agents, parallel search, evaluation, and operational reliability.

## Contributing

Suggestions are welcome, but this list is intentionally selective. Read [the curation policy](CURATION.md) before opening an issue or pull request.

A proposed resource should:

- serve software developers learning or practising AI engineering;
- provide technical or practical value beyond a product homepage;
- be current and maintained, unless its value is foundational and durable;
- add something meaningfully different from the existing entries;
- use a factual description supported by a primary source.

Explain which developer problem the resource solves and why it clears the rubric. If it overlaps an existing entry, explain why it is materially better. Disclose any affiliation with the resource.
