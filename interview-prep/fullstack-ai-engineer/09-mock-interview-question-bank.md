# Module 09: Fullstack AI Engineer Mock Question Bank

This document contains 20+ technical interview questions with model answers across AI/LLMOps, Backend Concurrency, System Design, Data Engineering, and DevOps.

---

## 🤖 1. AI & LLMOps Questions

### Q1: How do you prevent context window exhaustion during long multi-agent code refactoring sessions?
**Answer:**
1. **Context Summarization:** Periodically compress past agent interaction turns into structured summaries.
2. **Explicit Skill Scoping:** Supply only the instructions (`skills/`) required for the specific subagent's task.
3. **Targeted File Scoping:** Avoid dumping full directory trees into the context window; pass explicit file references (`@file`) and line ranges.

---

### Q2: Compare HNSW and ScaNN vector indexing algorithms.
**Answer:**
- **HNSW:** Multi-layer proximity graph algorithm. Delivers high accuracy and fast search, but consumes higher memory to maintain graph structures.
- **ScaNN:** Google Research score-aware quantization algorithm. Optimized for inner-product vector search at scale (billions of vectors) with a lower memory footprint.

---

## 🌐 2. Backend & System Design Questions

### Q3: Why use Server-Sent Events (SSE) instead of WebSockets for LLM token streaming?
**Answer:**
SSE is a unidirectional HTTP/1.1 or HTTP/2 protocol (`text/event-stream`). Since LLM token delivery is server-to-client, SSE avoids the complexity of WebSocket TCP socket handshakes, works natively through corporate HTTP proxies/load balancers, and has native browser reconnection support via `EventSource`.

---

### Q4: How do you prevent CPU-heavy tasks from blocking Python's `asyncio` event loop?
**Answer:**
Python's `asyncio` runs a single-threaded cooperative event loop. CPU-heavy tasks (like matrix multiplication or embedding processing) do not yield control and block incoming HTTP requests. They should be offloaded to `concurrent.futures.ProcessPoolExecutor` or background worker tasks (Cloud Tasks/Celery).

---

## ☁️ 3. Cloud & Data Architecture Questions

### Q5: Explain the difference between BigQuery partitioning and clustering.
**Answer:**
- **Partitioning:** Divides a large table into segments based on a date or integer column, reducing the amount of data scanned per query.
- **Clustering:** Sorts data within each partition based on high-cardinality columns (e.g. `tenant_id`, `model_name`), allowing BigQuery to skip unnecessary data blocks within partitions.
