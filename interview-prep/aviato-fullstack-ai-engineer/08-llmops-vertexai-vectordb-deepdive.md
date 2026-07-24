# Module 08: LLMOps & Vertex AI Vector Search Deep-Dive

This module covers the core machine learning and vector database requirements from the Aviato job description: model deployment, optimization, and scaling within **Google Cloud Vertex AI**, and implementing semantic search and long-term memory across vector databases (**Vertex AI Vector Search, Pinecone, ChromaDB, pgvector**).

---

## 🤖 1. Google Cloud Vertex AI Architecture

### Vertex AI Model Deployment Lifecycle

```
  ┌────────────────┐       ┌─────────────────┐       ┌─────────────────┐
  │  Fine-Tuning   │ ───>  │  Vertex AI      │ ───>  │ Vertex AI       │
  │  / Prompt Spec │       │  Model Registry │       │ Online Endpoint │
  └────────────────┘       └─────────────────┘       └────────┬────────┘
                                                              │
                                                   (Low-latency prediction)
                                                              ▼
                                                   [ FastAPI API Gateway ]
```

### Python Vertex AI SDK Code Snippet

```python
from google.cloud import aiplatform

def init_vertex_ai():
    aiplatform.init(
        project="aviato-prod",
        location="us-central1",
        staging_bucket="gs://aviato-vertex-staging"
    )

def invoke_model_endpoint(endpoint_id: str, prompt: str):
    endpoint = aiplatform.Endpoint(endpoint_name=f"projects/aviato-prod/locations/us-central1/endpoints/{endpoint_id}")
    
    response = endpoint.predict(instances=[{"prompt": prompt, "temperature": 0.2, "max_tokens": 512}])
    return response.predictions
```

---

## 🔍 2. Vector Indexing Algorithms: HNSW vs. ScaNN

Vector databases rely on Approximate Nearest Neighbor (ANN) search algorithms to retrieve matching embeddings quickly.

### 1. HNSW (Hierarchical Navigable Small World)
- **Mechanism:** Multi-layer graph where top layers have long-range links and bottom layers have short-range links.
- **Used by:** Pinecone, pgvector (HNSW index), ChromaDB.
- **Pros/Cons:** Fast search speed and high recall, but requires high RAM to build and maintain the graph.

### 2. ScaNN (Score-Aware Vector Quantization)
- **Mechanism:** Developed by Google Research. Uses Vector Quantization (VQ) and anisotropic quantization to optimize inner product search.
- **Used by:** Vertex AI Vector Search.
- **Pros/Cons:** Outperforms HNSW on high-dimensional vectors at massive scale (millions to billions of vectors).

---

## 🗄️ 3. Vector Database Selection Matrix

```sql
-- pgvector (Cloud SQL PostgreSQL) Hybrid Search Example
SELECT id, document_chunk, 
       1 - (embedding <=> '[0.012, -0.043, 0.089, ...]'::vector) AS similarity_score
FROM document_embeddings
WHERE tenant_id = 'tenant-42' 
  AND created_at >= '2026-01-01'
ORDER BY embedding <=> '[0.012, -0.043, 0.089, ...]'::vector
LIMIT 5;
```

| Vector DB | Scalability | Latency | GCP Integration | Best Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **Vertex AI Vector Search** | Billions of vectors | < 10 ms | Native (IAM, BigQuery, GCS) | Enterprise-wide RAG & real-time search |
| **pgvector (Cloud SQL)** | Millions of vectors | 10 - 30 ms | Native PostgreSQL | Relational transactional joins + embeddings |
| **Pinecone** | Billions of vectors | 10 - 20 ms | SaaS Connector | Cloud-agnostic SaaS workflows |
| **ChromaDB** | Thousands to Millions | Local / Fast | Python Library | Local development, scratchpads, testing |

---

## ❓ LLMOps Interview Questions

### Q: What is the difference between RAG (Retrieval-Augmented Generation) and Model Fine-Tuning?
**Answer:**
- **RAG:** Injects dynamic, external factual context into the prompt at inference time without modifying model weights. Ideal for rapidly changing knowledge bases, enterprise document search, and strict security filtering.
- **Fine-Tuning:** Updates model weights on specialized dataset formatting, style, or specific task patterns. Ideal for enforcing precise output formats, domain-specific terminology, or tone, but cannot keep up with dynamic real-time data updates.
