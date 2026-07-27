# 🛠️ Prerequisites for AI Systems & Agentic Engineering

Before diving into Prompt, Context, Loop, Harness, and Agentic Engineering, you should have solid foundational knowledge in **5 core technical domains**. Missing these prerequisites will make debugging, scaling, and sandboxing AI agents significantly harder.

---

## 1. LLM Mechanics & API Fundamentals
- **Tokenization**: Understanding subword tokens, BPE (Byte Pair Encoding), token-to-word ratios, and how tokenization impacts costs and context limits.
- **Sampling Parameters**: How `Temperature`, `Top-P`, `Top-K`, `Frequency/Presence Penalty`, and `Stop Sequences` affect model determinism and creativity.
- **Transformer Intuition**: Basic conceptual understanding of self-attention, context windows, KV-caching, and input-vs-output token latency/cost dynamics.

### 🧠 Deep Learning & Neural Networks: What is Required vs. Optional?

| Category | AI Systems / Agentic Engineer (Applied) | ML / Research Scientist (Core ML) |
| :--- | :--- | :--- |
| **Primary Goal** | Build autonomous software systems using LLM APIs & inference engines | Train, fine-tune, or design base model architectures |
| **Neural Net Math** | **Not Required** (No backpropagation, matrix calculus, or loss derivation needed) | **Required** (Calculus, linear algebra, gradient descent, loss functions) |
| **Frameworks** | **Not Required** (PyTorch/TensorFlow optional; Pydantic/vLLM/LangGraph core) | **Required** (PyTorch, JAX, CUDA, DeepSpeed, Megatron) |
| **What You MUST Know** | **Conceptual Intuition**: How autoregressive generation works, token limits, KV-cache, LoRA/PEFT (when to fine-tune vs prompt/RAG), Quantization (int4/8 VRAM impact), and inference engines (vLLM, Ollama). | **Deep Theory**: Model weights initialization, attention variants (FlashAttention implementation), RLHF loss, dataset tokenization pipelines. |

> [!TIP]
> **Key Takeaway**: You **do NOT** need a master's degree in Deep Learning or to write PyTorch code from scratch to excel at Agentic & AI Systems Engineering. You need **architectural intuition** of how LLMs process tokens and fail, combined with **strong software engineering, systems design, and async programming**.

---

## 2. Modern Software Engineering & Async Systems
- **Async & Concurrent Programming**: Mastery of `async/await`, asynchronous streams (SSE - Server-Sent Events), event loops, and non-blocking I/O (in Python or TypeScript/Node.js).
- **Data Validation & Schemas**: Using data validation libraries like **Pydantic** (Python) or **Zod** (TypeScript) to enforce strict JSON schemas for LLM tool calling and structured outputs.
- **Resilience Engineering**: Implementing exponential backoff, jitter, retry loops, rate-limiting handlers, and circuit breakers for API calls.

---

## 3. Database & Retrieval Systems (RAG Foundations)
- **Vector Embeddings**: How text embeddings work, distance metrics (Cosine Similarity, Dot Product, Euclidean distance), and vector indexing (HNSW, IVF).
- **Vector & Relational Databases**: Basic usage of Vector DBs (e.g., Qdrant, Pinecone, Chroma, `pgvector`) alongside traditional SQL/NoSQL databases for state storage.
- **Hybrid Search**: Understanding BM25 (lexical keyword search) + Dense Vector (semantic search) fusion, and Reranking models (Cross-Encoders).

---

## 4. Operating Systems, Sandboxing & Security Basics
- **Process Isolation & Sandboxing**: Docker basics, Linux containers, process IPC (Inter-Process Communication), sub-process streams (stdin/stdout/stderr), and virtualized runtimes (WASM, Firecracker).
- **AI Security Fundamentals**: Threat vectors including **Prompt Injection** (direct & indirect), SSRF (Server-Side Request Forgery), unauthorized tool execution, and secret management.

---

## 5. Observability & Evals Mindset
- **Tracing & Telemetry**: OpenTelemetry principles, distributed tracing, spans, and monitoring agent execution trajectories (e.g., LangSmith, Phoenix, Arize).
- **Basic LLM Benchmarking**: Ground truth dataset creation, LLM-as-a-Judge patterns, Precision/Recall for retrieval, and deterministic unit testing for prompts/tools.
