# Module 09: Enterprise DevOps, Multi-Cloud & Data Validation

This module covers the DevOps, multi-cloud, and runtime data validation requirements from the Aviato job description: **GCP serverless compute** (Cloud Run, Cloud Functions), **Azure exposure**, containerized **CI/CD pipelines**, version control, and data validation schemas using **Pydantic** and **Zod**.

---

## 🛡️ 1. Runtime Data Validation Schemas

Data validation prevents invalid AI outputs or API inputs from corrupting downstream services.

### Python: Pydantic V2 Schema (FastAPI Backend)

```python
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional

class LLMPredictionRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=4096, description="User prompt")
    temperature: float = Field(default=0.2, ge=0.0, le=1.0)
    top_k: int = Field(default=40, ge=1, le=100)
    user_id: str = Field(..., pattern=r"^usr_[a-zA-Z0-9]+$")

    @field_validator("prompt")
    @classmethod
    def sanitize_prompt(cls, v: str) -> str:
        # Strip potential prompt injection control characters
        return v.strip()

class VectorSearchMatch(BaseModel):
    document_id: str
    score: float
    content: str
    metadata: dict
```

---

### TypeScript: Zod Schema (Next.js / Node.js Frontend & API)

```typescript
import { z } from 'zod';

export const AIResponseSchema = z.object({
  id: z.string().uuid(),
  model: z.string(),
  tokens: z.object({
    prompt: z.number().int().nonnegative(),
    completion: z.number().int().nonnegative(),
  }),
  output: z.string().min(1),
});

export type AIResponse = z.infer<typeof AIResponseSchema>;
```

---

## 🐳 2. Containerized GCP Cloud Run & Docker Setup

### Production Dockerfile (FastAPI Backend)

```dockerfile
# Use minimal Python base image
FROM python:3.11-slim as base

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8080

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY . .

# Expose port for Cloud Run
EXPOSE 8080

# Run Uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "4"]
```

---

## 🚀 3. Multi-Cloud & CI/CD Pipelines (GCP Cloud Build + Azure)

```yaml
# cloudbuild.yaml (Google Cloud Build pipeline)
steps:
  # 1. Run Unit Tests & Schema Validations
  - name: 'python:3.11-slim'
    entrypoint: 'pytest'
    args: ['tests/']

  # 2. Build Container Image
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/aviato-prod/ai-backend:$SHORT_SHA', '.']

  # 3. Push Image to Artifact Registry
  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'gcr.io/aviato-prod/ai-backend:$SHORT_SHA']

  # 4. Deploy to GCP Cloud Run
  - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
    entrypoint: 'gcloud'
    args:
      - 'run'
      - 'deploy'
      - 'aviato-ai-backend'
      - '--image=gcr.io/aviato-prod/ai-backend:$SHORT_SHA'
      - '--region=us-central1'
      - '--platform=managed'
      - '--allow-unauthenticated'

images:
  - 'gcr.io/aviato-prod/ai-backend:$SHORT_SHA'
```

---

## ❓ DevOps & Multi-Cloud Interview Questions

### Q: How do you handle secrets (API keys, DB URIs) safely across GCP Cloud Run and Azure App Service?
**Answer:**
Never hardcode secrets in repository files or Docker images! Use **GCP Secret Manager** or **Azure Key Vault**. Inject secrets as environment variables into Cloud Run containers at runtime using IAM service account permissions (`roles/secretmanager.secretAccessor`).
