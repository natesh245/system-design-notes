# Module 08: Enterprise DevOps, Multi-Cloud & Data Validation

This module covers runtime data validation (**Pydantic V2, Zod**), containerization (**Docker, Cloud Run**), multi-cloud (GCP/Azure), and CI/CD pipelines.

---

## 🛡️ 1. Runtime Data Validation Schemas

### Pydantic V2 (Python FastAPI)

```python
from pydantic import BaseModel, Field, field_validator

class InferenceRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=4096)
    temperature: float = Field(default=0.2, ge=0.0, le=1.0)
    user_id: str = Field(..., pattern=r"^usr_[a-zA-Z0-9]+$")

    @field_validator("prompt")
    @classmethod
    def sanitize(cls, v: str) -> str:
        return v.strip()
```

### Zod (TypeScript Node.js / Next.js)

```typescript
import { z } from 'zod';

export const StreamPayloadSchema = z.object({
  token: z.string(),
  index: z.number().int().nonnegative(),
  isDone: z.boolean().optional(),
});
```

---

## 🐳 2. Production Dockerfile & Cloud Run Deployment

```dockerfile
FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1 PORT=8080
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
```
