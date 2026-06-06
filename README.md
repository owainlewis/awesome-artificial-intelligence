# Awesome Artificial Intelligence

A curated collection of **must-use, actively maintained resources** for building and shipping AI systems.

Focus: **AI engineering** (RAG, agents, evals, guardrails, deploy) plus the best books, guides, papers, and a *carefully selected* set of tools.

![](https://media.giphy.com/media/jeAQYN9FfROX6/giphy.gif)

---

## 📚 Learn
_Deep, durable knowledge — still valuable five years from now._

### Books
**Modern & Practical**
- [Designing Machine Learning Systems](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) — Scalable, maintainable ML pipelines (Chip Huyen).
- [AI Engineering](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) — End-to-end AI product building (Chip Huyen).
- [Build a Large Language Model from Scratch](https://www.manning.com/books/build-a-large-language-model-from-scratch) — Transformers in raw PyTorch, layer by layer (Sebastian Raschka).
- [Hands-On Large Language Models](https://www.llm-book.com/) — Visual + practical guide to LLM applications (Jay Alammar, Maarten Grootendorst).
- [LLM Engineer's Handbook](https://www.packtpub.com/en-us/product/llm-engineers-handbook-9781836200079) — Production LLMOps: fine-tuning, quantization, serving (Labonne, Iusztin).
- [The 100-Page Language Models Book](https://www.thelmbook.com/) — Concise, math-grounded path from n-grams to transformers (Andriy Burkov).
- [Generative Deep Learning (2nd Edition)](https://www.oreilly.com/library/view/generative-deep-learning/9781098134174/) — GANs, VAEs, diffusion models (David Foster).

**Foundational**
- [Artificial Intelligence: A Modern Approach](https://aima.cs.berkeley.edu/) — The canonical AI theory text (Russell, Norvig).
- [Deep Learning](https://www.deeplearningbook.org/) — Mathematical foundations of neural networks (Goodfellow, Bengio, Courville).
- [Deep Learning: Foundations and Concepts](https://www.bishopbook.com/) — Bishop's 2024 update; probability-grounded modern DL (Bishop & Bishop).
- [Understanding Deep Learning](https://udlbook.github.io/udlbook/) — Math + intuition + Python notebooks (Simon Prince).
- [Speech and Language Processing (3rd Edition)](https://web.stanford.edu/~jurafsky/slp3/) — The NLP reference, kept current through the deep learning era (Jurafsky, Martin).
- [Reinforcement Learning: An Introduction (2nd Edition)](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf) — RL foundations (Sutton, Barto).

### Courses

**Beginner**
- [Google Generative AI Learning Path](https://www.cloudskillsboost.google/paths/118)
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1)
- [Fast.ai — Practical Deep Learning](https://course.fast.ai/)

**Intermediate / Advanced**
- [Stanford CS324: Large Language Models](https://stanford-cs324.github.io/winter2022/)
- [Full Stack Deep Learning](https://fullstackdeeplearning.com/)
- [MIT 6.S191: Intro to Deep Learning](https://introtodeeplearning.com/)

**Focused**
- [DeepLearning.AI Short Courses](https://learn.deeplearning.ai/)
- [Google DeepMind — Introduction to Reinforcement Learning](https://www.youtube.com/playlist?list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ)
- [Karpathy — Neural Networks: Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)

### Landmark Papers
_Research that shaped modern AI — worth reading to understand the "why" behind today's architectures._
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — Transformer architecture.
- [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) — Model/data/compute scaling.
- [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) — GPT-3 capabilities.
- [Constitutional AI](https://arxiv.org/abs/2212.08073) — Safer model alignment.

---

## 🛠 Build
_The toolchain for building with AI._
_Personal note: you don't need tons of frameworks — start with simple LLM calls and work up._

### Guides & Playbooks
- **[Building Effective Agents (Anthropic)](https://www.anthropic.com/engineering/building-effective-agents)** — ⭐ Patterns, pitfalls, and tradeoffs for designing AI agents.
- [OpenAI Agents Guide](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) — Practical guide on building agents.
- [Google AI Agents Paper](https://www.kaggle.com/whitepaper-agents) — Practical guide to building AI agents from Google.
- [Google Agents Companion Paper](https://www.kaggle.com/whitepaper-agent-companion) — Companion guide from Google.
- [OpenAI Cookbook](https://cookbook.openai.com/) — Example code, recipes, and best practices for working with OpenAI APIs.
- [LLM Engineer Handbook](https://github.com/SylphAI-Inc/LLM-engineer-handbook) — A goldmine of useful links for AI engineers.

### Frameworks
- [PocketFlow](https://the-pocket.github.io/PocketFlow/) — Extremely minimalist AI agent framework in just 100 lines of code. Fantastic way to learn.
- [Google ADK](https://google.github.io/adk-docs/) — Google's Agent Development Kit (Python, Java). Great local development experience + A2A + MCP.
- [Pydantic-AI](https://ai.pydantic.dev/) — Typed, structured LLM orchestration framework built on Pydantic models for safe, predictable outputs.
- [LangGraph](https://www.langchain.com/langgraph) — Build multi-agent workflows with stateful graphs on top of LangChain.
- [CrewAI](https://www.crewai.com/) — Agent orchestration with structured tasks and human-in-the-loop controls.
- [AutoGen](https://microsoft.github.io/autogen/) — Microsoft's framework for multi-agent conversation and collaboration.
- [LlamaIndex](https://www.llamaindex.ai/) — Data framework for ingesting, indexing, and querying private data with LLMs.
- [Haystack](https://haystack.deepset.ai/) — Open-source search/RAG framework with modular pipelines.
- [Docling](https://github.com/docling-project/docling) — Great library for ingesting any kind of document for RAG ⭐

### Evals
- [OpenAI Evals](https://github.com/openai/evals) — OpenAI's framework for writing evals.

### IDEs
- [Cursor](https://cursor.sh/) — LLM-powered IDE for multi-file edits and codebase-aware chat.
- [GitHub Copilot](https://github.com/features/copilot) — In-IDE code completion, chat, and refactors.

---

## 🤖 Agents
_Harnesses that turn LLMs into autonomous workers. The model is swappable; the harness is the product._

### Coding
_For live capability comparison, see [Terminal-Bench](https://www.tbench.ai/leaderboards) and [SWE-bench](https://www.swebench.com/)._

- [Claude Code](https://code.claude.com/) — Anthropic's CLI agent; multi-file codebase refactoring with long context.
- [Codex CLI](https://github.com/openai/codex) — OpenAI's Rust-based local terminal agent; lightweight and fast.
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) — Google's official open-source terminal agent; long-context repo exploration.
- [Cursor CLI](https://cursor.com/cli) — Cursor's terminal-native agent with sandboxed permissions.
- [Aider](https://aider.chat/) — Git-integrated pair programming with surgical edits and undo.
- [OpenCode](https://opencode.ai/) — Provider-agnostic terminal harness with a strong TUI.
- [OpenHands](https://docs.all-hands.dev/) — Open-source autonomous SWE platform; browser + shell + editor loop.
- [Cline](https://github.com/cline/cline) — Open-source agentic IDE extension with strong multi-provider support.
- [Continue](https://www.continue.dev/) — Open-source IDE + CLI assistant with source-controlled rules.
- [Goose](https://block.github.io/goose/) — Block's extensible, MCP-driven local agent.
- [Factory Droid](https://factory.ai/product/cli) — Benchmark-leading multi-model harness with BYOK local execution.
- [Amp](https://ampcode.com/) — Sourcegraph's commercial agentic coding tool with strong product UX.
- [Mistral Vibe](https://mistral.ai/products/vibe) — Mistral's agentic coding CLI, powered by Devstral.
- [Qwen Code](https://github.com/QwenLM/qwen-code) — Alibaba's terminal coding agent, optimized for Qwen models.
- [Pi](https://pi.dev/) — Highly customizable terminal harness; minimal base prompt, extension-driven.
- [Nanocoder](https://github.com/Nano-Collective/nanocoder) — Private, local-first agent for Ollama and LM Studio.
- [Kilo CLI](https://kilo.ai/cli) — Multi-mode agent with a unified gateway to 500+ models.
- [OpenClaw Monitor](https://github.com/flik2002/openclaw-monitor) — Free open-source monitoring dashboard for OpenClaw AI agents; token usage, session tracking, 7-day trends, multi-model support.

---

## 🧠 Models
_State-of-the-art models by modality._

### 💬 Language
The major frontier labs.

- [ChatGPT](https://openai.com/chatgpt/overview/) — Best for general reasoning, tool use, and the broadest ecosystem.
- [Claude](https://www.anthropic.com/claude) — Best for long-context analysis, coding, and structured thinking.
- [Gemini](https://gemini.google.com/) — Best for multimodal tasks and Google ecosystem integration.
- [Grok](https://x.ai/) — Best for real-time information via X and very long context.
- [Llama](https://www.llama.com/) — Best open-weight family for self-hosting and fine-tuning.
- [Mistral](https://mistral.ai/) — Best for lightweight, high-performance open-weight models.
- [DeepSeek](https://deepseek.com/) — Best for cost-efficient reasoning with open weights.
- [Qwen](https://qwenlm.github.io/) — Best for multilingual and Chinese-first applications.
- [Kimi](https://www.kimi.com/) — Best for long-context instruction following.
- [GLM](https://chatglm.cn/) — Frontier-tier Chinese model with open weights.
- [Cohere](https://cohere.com/) — Best for enterprise LLMs with strong retrieval-augmented generation APIs.

### 🖼 Image
- [GPT Image](https://openai.com/index/introducing-chatgpt-images-2-0/) — OpenAI's integrated image generation with near-perfect text rendering.
- [Midjourney](https://www.midjourney.com/) — Artistic and photorealistic images.
- [Adobe Firefly](https://www.adobe.com/sensei/generative-ai/firefly.html) — Integrated into Creative Cloud; commercial-safe.
- [Ideogram](https://ideogram.ai/) — Precise, legible text in generated images.
- [Flux](https://blackforestlabs.ai/) — High-res, prompt-editable, open-weight images.

### 🎥 Video
- [Google Veo](https://deepmind.google/technologies/veo/) — High-quality video with synchronized audio.
- [Runway](https://runwayml.com/) — Video editing + generation with granular creative control.
- [Kling](https://klingai.com/) — Cinematic, realistic video generation.

### 🎙 Audio
- [ElevenLabs](https://elevenlabs.io/) — High-quality text-to-speech and voice cloning.
- [Suno](https://suno.ai/) — AI music from text prompts.

### 📊 Compare
_Live benchmarks, pricing, and the latest model versions._
- [OpenRouter](https://openrouter.ai/models) — Unified API + live pricing across ~300 models.
- [LMArena](https://lmarena.ai/leaderboard) — Human-preference Elo rankings for text, image, and video.
- [Artificial Analysis](https://artificialanalysis.ai/) — Speed, price, and quality benchmarks across providers.

---

## 📡 Follow
_Stay current without drowning in noise._

### Newsletters
- [The Rundown AI](https://www.therundown.ai/)
- [AlphaSignal](https://alphasignal.ai/)
- [Superhuman AI](https://www.superhuman.ai/)
- [AI Engineer](https://newsletter.owainlewis.com)

---
