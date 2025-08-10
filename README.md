# Awesome Artificial Intelligence

A curated collection of **must-use, actively maintained resources** for building and shipping AI systems.  

Focus: **AI engineering** (RAG, agents, evals, guardrails, deploy) plus the best tools, courses, books, papers, and topic-specific references.

![](https://media.giphy.com/media/jeAQYN9FfROX6/giphy.gif)

## 📚 Books

**Modern & Practical**
- [Designing Machine Learning Systems](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) — Scalable, maintainable ML pipelines (Chip Huyen).
- [Generative Deep Learning (2nd Edition)](https://www.oreilly.com/library/view/generative-deep-learning/9781098134174/) — GANs, VAEs, diffusion models (David Foster).
- [AI Engineering](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) — End-to-end AI product building (Chip Huyen).

**Foundational**
- [Artificial Intelligence: A Modern Approach](https://aima.cs.berkeley.edu/) — Comprehensive AI theory (Russell & Norvig).
- [Deep Learning](https://www.deeplearningbook.org/) — Neural networks & architectures (Goodfellow, Bengio, Courville).
- [Reinforcement Learning: An Introduction (2nd Edition)](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf) — RL fundamentals (Sutton & Barto).

## 🏗 AI Engineering

Core tools, frameworks, and practices for building production-grade AI systems — from RAG pipelines to evals, guardrails, and deployment. (Personal note: you don't need tons of frameworks. Start with simple LLM calls and work up from there).

### Retrieval-Augmented Generation (RAG)
- [LlamaIndex](https://www.llamaindex.ai/) — Data framework for ingesting, indexing, and querying private data with LLMs.
- [Haystack](https://haystack.deepset.ai/) — Open-source search/RAG framework with modular pipelines.

### Orchestration & Agents
- [Pydantic-AI](https://ai.pydantic.dev/) — Typed, structured LLM orchestration framework built on Pydantic models for safe, predictable outputs.
- [LangGraph](https://www.langchain.com/langgraph) — Build multi-agent workflows with stateful graphs on top of LangChain.
- [CrewAI](https://www.crewai.com/) — Agent orchestration with structured tasks and human-in-the-loop controls.
- [AutoGen](https://microsoft.github.io/autogen/) — Microsoft’s framework for multi-agent conversation and collaboration.

### Evaluation & Testing

...

### 📖 Guides & Playbooks

- **[Building Effective Agents (Anthropic)](https://www.anthropic.com/engineering/building-effective-agents)** — ⭐ Patterns, pitfalls, and tradeoffs for designing AI agents.
- [OpenAI Cookbook](https://cookbook.openai.com/) — Example code, recipes, and best practices for working with OpenAI APIs.
- [RAG From Scratch (Pinecone)](https://www.pinecone.io/learn/retrieval-augmented-generation/) — A step-by-step guide to building a retrieval-augmented generation pipeline.
- [RAG Evaluation Guide (Hugging Face)](https://huggingface.co/blog/rag-evaluation) — Techniques for measuring RAG performance beyond accuracy.
- [Full-Stack RAG Tutorial (LlamaIndex)](https://docs.llamaindex.ai/en/stable/getting_started/full_stack_rag/) — End-to-end example from ingestion to querying.
- [LLM Evaluation & Testing Best Practices (DeepLearning.AI)](https://www.deeplearning.ai/short-courses/evaluating-and-testing-llm-applications/) — Covers regression tests, prompt robustness, and safety checks.
- [Productionizing AI Systems (Full Stack Deep Learning)](https://fullstackdeeplearning.com/) — MLOps patterns adapted for modern LLM/RAG systems.

## 💬 Tools (LLMs & Generative)

**LLM Assistants**
- [ChatGPT](https://openai.com/chatgpt/overview/) — Multimodal assistant for coding, reasoning, and tool use.
- [Claude](https://www.anthropic.com/claude) — Long-context analysis & coding.
- [Gemini](https://gemini.google.com/) — Google’s multimodal assistant.
- [Perplexity](https://www.perplexity.ai/) — Answer engine with live citations.

**Code & Developer Tools**
- [GitHub Copilot](https://github.com/features/copilot) — In-IDE code completion, chat, and refactors across VS Code/JetBrains/Neovim.
- [Claude Code](https://www.anthropic.com/claude) — Anthropic’s coding model with IDE extensions; strong long-context code understanding and edits.
- [Cursor](https://cursor.sh/) — LLM-powered IDE for multi-file edits, codebase-aware chat, and inline refactors.
- [JetBrains AI Assistant](https://www.jetbrains.com/ai/) — Integrated code chat/completion across JetBrains IDEs.
- [Amazon Q Developer](https://aws.amazon.com/q/developer/) — AWS-native coding assistant with cloud/resource context.

##  🎨 Multimedia AI Tools (Image, Video, & Audio)

### 🖼 Image Generation
- [ChatGPT-4o Image Generation](https://openai.com/chatgpt) — Integrated image creation directly within ChatGPT; excels at prompt adherence and realism.
- [Midjourney](https://www.midjourney.com/) — Renowned for hyper-realistic, artistic image renderings; still a powerhouse. Supports cinematic video gen.
- [Adobe Firefly](https://www.adobe.com/sensei/generative-ai/firefly.html) — Part of Creative Cloud; now features Firefly Image 4/4 Ultra with ethical training and Photoshop integration.
- [Ideogram](https://ideogram.ai/) — Generates images with precise, legible text output.
- [Flux](https://blackforestlabs.ai/) — German-developed model offering high-res, prompt-editable images; various licensing tiers.
  
### 🎥 Video Generation
- [Kling](https://klingai.com/) — Industry-leading video model producing highly realistic, cinematic scenes with complex motion; strong physics and camera movement simulation.  
- [Google Veo 3](https://deepmind.google/technologies/veo/) — Generates realistic videos with synchronized audio, lip-sync, and scene coherence. 
- [Runway](https://runwayml.com/) — Creative video editing and generation, including motion capture and dynamic scene alteration. 

### 🎙 Audio & Music Generation
- [ElevenLabs](https://elevenlabs.io/) — Lifelike text-to-speech in 70+ languages with emotional range and API access.
- [Suno](https://suno.ai/) — AI music creation from text prompts with multi-instrument compositions.
- [Aiva](https://www.aiva.ai/) — AI music composition for games, films, and commercial projects.
## 🎓 Courses

**Beginner**
- [Google Generative AI Learning Path](https://www.cloudskillsboost.google/paths/118) — Free, self-paced introduction to LLMs, RAG, and Responsible AI.
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) — Hands-on transformers & LLMs.
- [fast.ai — Practical Deep Learning](https://course.fast.ai/) — Practical, project-driven deep learning.

**Intermediate / Advanced**
- [Stanford CS324: Large Language Models](https://stanford-cs324.github.io/winter2022/) — LLM theory & practice.
- [Full Stack Deep Learning](https://fullstackdeeplearning.com/) — From notebook to production.
- [MIT 6.S191: Intro to Deep Learning](https://introtodeeplearning.com/) — Modern DL methods.

**Focused**
- [DeepLearning.AI Short Courses](https://learn.deeplearning.ai/) — RAG, prompt engineering, agents, evals.
- [Karpathy’s LLM Zero-to-Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) — Build LLMs from scratch.

## 📰 Newsletters (Entertainment/News)

- [The Rundown AI](https://www.therundown.ai/) — Daily AI updates & tools.
- [AlphaSignal](https://alphasignal.ai/) — Developer-focused AI news.
- [Superhuman AI](https://www.superhuman.ai/) — Tools and workflow tips.
- [AI Engineer](https://newsletter.owainlewis.com) — Practical tutorials on building software with AI.

## 📄 Papers

**Landmarks**
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — Transformer architecture.
- [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) — Model/data/compute scaling.
- [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) — GPT-3 capabilities.
- [Constitutional AI](https://arxiv.org/abs/2212.08073) — Safer model alignment.