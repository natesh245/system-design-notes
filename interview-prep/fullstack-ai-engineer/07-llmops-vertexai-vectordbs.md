# Module 07: LLMOps & Vector Infrastructure

This module covers model hosting, fine-tuning vs RAG, vector indexing algorithms (**HNSW vs ScaNN**), and vector database selection (**pgvector, Pinecone, ChromaDB, Vertex AI Vector Search**).

---

## 🤖 1. Model Hosting & Vertex AI Prediction

```python
from google.cloud import aiplatform

def predict_custom_endpoint(endpoint_id: str, prompt: str):
    endpoint = aiplatform.Endpoint(endpoint_name=f"projects/my-proj/locations/us-central1/endpoints/{endpoint_id}")
    response = endpoint.predict(instances=[{"prompt": prompt}])
    return response.predictions
```

---

## 🔍 2. HNSW vs. ScaNN Algorithms

- **HNSW (Hierarchical Navigable Small World):** Multi-layer graph algorithm used by Pinecone, pgvector, and ChromaDB. Provides high recall but requires high memory footprint to construct graphs.
- **ScaNN (Score-Aware Vector Quantization):** Google Research algorithm used in Vertex AI Vector Search. Uses vector quantization for ultra-fast inner-product search on high-dimensional data at billion-vector scale.

---

## 🗄️ 3. Vector DB Decision Matrix

| Vector Store | Scale Limit | Latency | Key Benefit |
| :--- | :--- | :--- | :--- |
| **Vertex AI Vector Search** | Billions | < 10ms | Enterprise scale + GCP native integration |
| **pgvector (PostgreSQL)** | Millions | 10-30ms | Transactional SQL joins + vector search |
| **Pinecone** | Billions | 10-20ms | Managed multi-cloud SaaS |
| **ChromaDB** | Thousands | Local | Easy Python setup for local prototypes |
