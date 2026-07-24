# Module 05: Mock Technical Question Bank & Solutions

This document contains 15 high-frequency technical interview questions with model answers for **Senior Fullstack AI Engineer / FDE** roles.

---

## 🤖 Category 1: AI, LLMOps & Context Management

### Q1: How do you prevent context window exhaustion and token bloat in multi-agent workflows?
**Answer:**
1. **Context Window Summarization:** Periodically condense past agent interactions into concise structural summaries instead of appending full raw dialogue logs.
2. **Explicit Skill Isolation:** Use modular skill files (`skills/`) so sub-agents receive only the prompt instructions relevant to their assigned domain.
3. **Retrieval-Augmented Prompting:** Store historical code snippets or facts in a Vector DB (pgvector / Vertex AI Vector Search) and dynamically retrieve top-$K$ chunks only when relevant to the current user query.

---

### Q2: What is the difference between Cosine Similarity, Dot Product, and Euclidean Distance for vector search?
**Answer:**
- **Cosine Similarity:** Measures the angle between two vectors, normalizing for magnitude. Ideal for text embeddings where document length varies.
- **Dot Product:** Measures both angle and magnitude. If vectors are normalized (length = 1), Dot Product is mathematically identical to Cosine Similarity but significantly faster to compute!
- **Euclidean (L2) Distance:** Measures straight-line distance between points in space. Sensitive to vector magnitude.

---

## 🌐 Category 2: Backend Concurrency & Real-Time APIs

### Q3: Why choose Server-Sent Events (SSE) over WebSockets for LLM streaming applications?
**Answer:**
- **Unidirectional Efficiency:** LLM response generation is strictly unidirectional (Server ➔ Client). SSE is built natively over HTTP/1.1 and HTTP/2 without requiring custom WebSocket handshake protocols.
- **Infrastructure Support:** SSE works out of the box with standard HTTP load balancers, API Gateways, and HTTP/2 multiplexing.
- **Native Reconnection:** The browser `EventSource` API automatically attempts reconnects with event IDs if the network drops.

---

### Q4: What happens if a CPU-heavy task is executed directly inside a Python `async` function in FastAPI?
**Answer:**
It blocks the single-threaded `asyncio` event loop! Because Python does not preemptively interrupt Python code inside async tasks, no other incoming HTTP requests can be processed until the CPU task completes.
*Fix:* Offload CPU-heavy computation to `asyncio.to_thread()` or a `ProcessPoolExecutor`.

---

## ☁️ Category 3: GCP & Cloud Data Architecture

### Q5: When would you use GCP BigQuery vs Vertex AI Vector Search vs pgvector?
**Answer:**
- **BigQuery:** For large-scale analytical queries, structured log storage, and offline dataset indexing. BigQuery also supports SQL-based vector search for batch processing.
- **Vertex AI Vector Search:** For ultra-low latency (<10ms) real-time vector retrieval across millions to billions of embeddings at enterprise scale.
- **pgvector:** For relational database applications (Cloud SQL PostgreSQL) where vector embeddings must be joined transactionally with user tables in a single SQL query.

---

### Q6: How do you handle real-time streaming data ingestion on GCP for continuous AI model evaluation?
**Answer:**
Use **GCP Cloud Dataflow (Apache Beam)** listening to a **GCP Pub/Sub** topic. Dataflow processes streaming events in sliding time windows, extracts feature embeddings via Vertex AI API, and pushes metrics to BigQuery and Cloud Monitoring for real-time model drift detection.
