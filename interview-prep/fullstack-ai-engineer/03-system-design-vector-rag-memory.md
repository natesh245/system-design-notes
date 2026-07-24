# Module 03: System Design — Enterprise RAG & Vector Memory

This module details the production architecture for Enterprise Retrieval-Augmented Generation (RAG), Hybrid Search, and Long-Term Agentic Memory.

---

## 🏛️ 1. RAG Data Ingestion & Search Pipeline

```
  ┌──────────────────┐
  │ Enterprise Docs  │ (PDFs, Markdown, SQL Logs)
  └────────┬─────────┘
           │
           ▼
  ┌──────────────────┐
  │ Data Pipeline    │ (Dataflow / Apache Beam / LangChain Splitters)
  └────────┬─────────┘
           │
           ▼
  ┌──────────────────┐
  │ Embeddings Engine│ (Text-Embedding-004, OpenAI Ada, Cohere)
  └────────┬─────────┘
           │
           ├───────────────────────────────────┐
           ▼                                   ▼
  ┌──────────────────┐               ┌──────────────────┐
  │ Vector Database  │               │ Relational Metadata│
  │ (HNSW / ScaNN)   │               │ (PostgreSQL/BQ)  │
  └────────┬─────────┘               └─────────┬────────┘
           │                                   │
           └─────────────────┬─────────────────┘
                             │
                             ▼
              ┌─────────────────────────────┐
              │  Hybrid Search & Reranker   │
              └──────────────┬──────────────┘
                             │
                             ▼
              ┌─────────────────────────────┐
              │ Context Injected LLM Prompt │
              └─────────────────────────────┘
```

---

## 🔍 2. Hybrid Search (Dense + Sparse Retrieval)

- **Dense Vectors:** Semantic embedding search capturing conceptual meaning.
- **Sparse Vectors (BM25 / Keyword Search):** Full-text search capturing exact key matches (e.g. part numbers, exact names, IDs).
- **Reciprocal Rank Fusion (RRF):** Merges dense and sparse search rankings:

$$RRF\_Score(d) = \sum_{m \in M} \frac{1}{k + r_m(d)}$$

---

## 🧠 3. Short-Term vs. Long-Term Agent Memory

| Memory Type | Storage Mechanism | Retention & Scope |
| :--- | :--- | :--- |
| **Short-Term Context** | Sliding window buffer in Redis / Memory | Current active conversation session |
| **Long-Term Memory** | Vector Database (pgvector, ChromaDB, Vertex AI) | Cross-session entity facts, past solution trajectories |
