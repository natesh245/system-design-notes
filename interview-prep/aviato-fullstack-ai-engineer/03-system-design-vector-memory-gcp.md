# Module 03: System Design — GCP Vector & Memory Pipeline

This document details the production architecture for an enterprise Retrieval-Augmented Generation (RAG) and long-term memory system using **Google Cloud Vertex AI Vector Search**, **GCP BigQuery**, **Cloud Dataflow (Apache Beam)**, and **pgvector**.

---

## 🏛️ End-to-End Enterprise RAG Data Pipeline

```
  ┌─────────────────┐
  │ Enterprise Data │ (PDFs, Docs, SQL Logs)
  └────────┬────────┘
           │
           ▼
  ┌─────────────────────────────────┐
  │ Cloud Dataflow (Apache Beam)    │  <-- Batch & Stream Chunking
  └────────┬────────────────────────┘
           │
           ▼
  ┌─────────────────────────────────┐
  │ Vertex AI Embeddings API        │  <-- Text-Embedding-Gecko
  └────────┬────────────────────────┘
           │
           ├─────────────────────────────────────────┐
           ▼                                         ▼
  ┌─────────────────────────────────┐   ┌───────────────────────────┐
  │ Vertex AI Vector Search Index   │   │ GCP BigQuery Storage      │
  │ (Low Latency Vector Similarity) │   │ (Raw Text & Rich Metadata)│
  └────────────────┬────────────────┘   └─────────────┬─────────────┘
                   │                                  │
                   └────────────────┬─────────────────┘
                                    │
                                    ▼
                     ┌──────────────────────────────┐
                     │  FastAPI Hybrid Search Engine│
                     └──────────────┬───────────────┘
                                    │
                                    ▼
                     ┌──────────────────────────────┐
                     │ Vertex AI LLM Generation     │
                     └──────────────────────────────┘
```

---

## 🔬 Core Architectural Patterns

### 1. Ingestion & Chunking via GCP Dataflow (Apache Beam)
- **Document Preprocessing:** Dataflow processes massive PDF/text streams, sanitizes markup, and splits text into semantic chunks (e.g., 512 tokens with 50-token overlap).
- **Parallel Embedding Generation:** Asynchronously invokes Vertex AI Embedding API in batch micro-bursts to avoid quota throttling.

### 2. Hybrid Search (Dense Vectors + Sparse Metadata Filtering)
- **Dense Retrieval:** Vertex AI Vector Search retrieves top-$K$ nearest neighbors based on Cosine Similarity / Dot Product.
- **Metadata Filtering:** Query metadata parameters (e.g., `user_id`, `department`, `tenant_id`, `created_date > 2026-01-01`) are pushed directly to vector filters or joined against BigQuery / pgvector for strict security isolation.

### 3. Long-Term Agentic Memory Architecture
- **Short-Term Context:** Window buffer of the last $N$ turns stored in Redis or GCP Memorystore.
- **Long-Term Memory:** User interaction logs are embedded and pushed to pgvector / Vertex AI Vector Search. During new interactions, the agent queries past context memories to recall user preferences across sessions.

---

## 📊 Comparison Matrix: Vector Store Choices

| Feature | Vertex AI Vector Search | pgvector (Cloud SQL) | Pinecone / ChromaDB |
| :--- | :--- | :--- | :--- |
| **Scale** | Billions of vectors (SCAaNN algorithm) | Millions of vectors | Millions to Billions |
| **GCP Integration** | Native IAM, BigQuery export, serverless | Native SQL joins, PostgreSQL transactional safety | Managed SaaS / Local DB |
| **Latency** | Sub-10ms at scale | 10ms - 50ms depending on index size | Sub-20ms |
| **Best Use Case** | Enterprise enterprise-wide search | Structured relational data + embeddings | Rapid prototype / SaaS |
