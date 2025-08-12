# Awesome Artificial Intelligence

A curated collection of **must-use, actively maintained resources** for building and shipping AI systems.  

Focus: **AI engineering** (RAG, agents, evals, guardrails, deploy) plus the best books, guides, papers, and a *carefully selected* set of tools.

![](https://media.giphy.com/media/jeAQYN9FfROX6/giphy.gif)

---

## 🏛 Core Resources (Evergreen)

_The foundations — these will still be valuable five years from now, even if today’s tools are gone._

### 📚 Books
**Modern & Practical**
- [Designing Machine Learning Systems](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) — Scalable, maintainable ML pipelines (Chip Huyen).
- [Generative Deep Learning (2nd Edition)](https://www.oreilly.com/library/view/generative-deep-learning/9781098134174/) — GANs, VAEs, diffusion models (David Foster).
- [AI Engineering](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) — End-to-end AI product building (Chip Huyen).
- [100 Page Language Models Book](https://www.thelmbook.com/) — This book guides you through the evolution of language models, starting from machine learning fundamentals.

**Foundational**
- [Artificial Intelligence: A Modern Approach](https://aima.cs.berkeley.edu/) — Comprehensive AI theory (Russell & Norvig).
- [Deep Learning](https://www.deeplearningbook.org/) — Neural networks & architectures (Goodfellow, Bengio, Courville).
- [Reinforcement Learning: An Introduction (2nd Edition)](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf) — RL fundamentals (Sutton & Barto).

---

### 🏗 AI Engineering
_Frameworks and design patterns for building robust, production-grade AI systems._  
_Personal note: you don't need tons of frameworks — start with simple LLM calls and work up._

#### 📖 Guides & Playbooks
- **[Building Effective Agents (Anthropic)](https://www.anthropic.com/engineering/building-effective-agents)** — ⭐ Patterns, pitfalls, and tradeoffs for designing AI agents.
- [OpenAI Agents Guide](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) — Practical guide on building agents
- [Google AI Agents Paper](https://www.kaggle.com/whitepaper-agents) - Practical guide to building AI agents from Google
- [Google Agents Companion Paper](https://www.kaggle.com/whitepaper-agent-companion) - Guide from Google
- [OpenAI Cookbook](https://cookbook.openai.com/) — Example code, recipes, and best practices for working with OpenAI APIs.
- [LLM Engineer Handbook](https://github.com/SylphAI-Inc/LLM-engineer-handbook) — A goldmine of useful links for AI engineers

#### 🤖 Frameworks 
- [PocketFlow](https://the-pocket.github.io/PocketFlow/) — Extremely minimalist AI agent framework in just 100 lines of code. Fantastic way to learn.
- [Google ADK](https://google.github.io/adk-docs/) — Google's Agent Development Kit (Python, Java). Great local development experience + A2A + MCP.
- [Pydantic-AI](https://ai.pydantic.dev/) — Typed, structured LLM orchestration framework built on Pydantic models for safe, predictable outputs.
- [LangGraph](https://www.langchain.com/langgraph) — Build multi-agent workflows with stateful graphs on top of LangChain.
- [CrewAI](https://www.crewai.com/) — Agent orchestration with structured tasks and human-in-the-loop controls.
- [AutoGen](https://microsoft.github.io/autogen/) — Microsoft’s framework for multi-agent conversation and collaboration.

#### 📦 Retrieval-Augmented Generation (RAG)
- [LlamaIndex](https://www.llamaindex.ai/) — Data framework for ingesting, indexing, and querying private data with LLMs.
- [Haystack](https://haystack.deepset.ai/) — Open-source search/RAG framework with modular pipelines.
- [Docling](https://github.com/docling-project/docling) — Great library for ingesting any kind of document for RAG ⭐

#### Evals 

- [OpenAI Evals](https://github.com/openai/evals) — OpenAI's framework for writing evals

---

### 📄 Landmark Papers
_Research that shaped modern AI — worth reading to understand the "why" behind today’s architectures._
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — Transformer architecture.
- [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) — Model/data/compute scaling.
- [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) — GPT-3 capabilities.
- [Constitutional AI](https://arxiv.org/abs/2212.08073) — Safer model alignment.

---

## 🎓 Courses
_Learn from the best — structured content for every level._

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
- [Google Deepmind| Introduction to Reinforcement Learning](https://www.youtube.com/playlist?list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ)
- [Karpathy’s LLM Zero-to-Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)
- [Neural Nets - Zero-to-Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)

---

## 📰 Newsletters
_Stay current with AI developments without drowning in noise._
- [The Rundown AI](https://www.therundown.ai/)
- [AlphaSignal](https://alphasignal.ai/)
- [Superhuman AI](https://www.superhuman.ai/)
- [AI Engineer](https://newsletter.owainlewis.com)

## ⚡ Tools

Tools for building and deploying AI applications. 

### 💬 Models
- [ChatGPT](https://openai.com/chatgpt/overview/) — Best for general coding + reasoning.
- [Claude](https://www.anthropic.com/claude) — Best for long-context analysis and structured thinking.
- [Gemini](https://gemini.google.com/) — Best for Google ecosystem integration.
- [Perplexity](https://www.perplexity.ai/) — Best for quick research with live citations.
- [Cohere](https://cohere.com/) — Best for enterprise LLMs with strong retrieval-augmented generation APIs.
- [Mistral](https://mistral.ai/) — Best for lightweight, high-performance open-weight models.
- [Qwen](https://qwenlm.github.io/) — Best for multilingual and Chinese-first applications.
- [DeepSeek](https://deepseek.com/) — Best for efficient, cost-optimized large models with competitive reasoning.
  
### 👨‍💻 Code & Developer Tools
- [Claude Code](https://www.anthropic.com/claude) — IDE extensions with long-context code edits.
- [GitHub Copilot](https://github.com/features/copilot) — In-IDE code completion, chat, and refactors.
- [Cursor](https://cursor.sh/) — LLM-powered IDE for multi-file edits and codebase-aware chat.
  
### 🎨 Multimedia AI Tools

#### 🖼 Image
- [ChatGPT-4o Image Generation](https://openai.com/chatgpt) — Integrated image creation with style control.
- [Midjourney](https://www.midjourney.com/) — Artistic and photorealistic images and video.
- [Adobe Firefly](https://www.adobe.com/sensei/generative-ai/firefly.html) — Integrated into Creative Cloud.
- [Ideogram](https://ideogram.ai/) — Precise, legible text in generated images.
- [Flux](https://blackforestlabs.ai/) — High-res, prompt-editable images.

#### 🎥 Video
- [Kling](https://klingai.com/) — Cinematic, realistic video generation.
- [Google Veo 3](https://deepmind.google/technologies/veo/) — High-quality video with synchronized audio.
- [Runway](https://runwayml.com/) — Video editing + generation.

#### 🎙 Audio
- [ElevenLabs](https://elevenlabs.io/) — High-quality text-to-speech.
- [Suno](https://suno.ai/) — AI music from text prompts.
- [Aiva](https://www.aiva.ai/) — Music composition for media.

---
