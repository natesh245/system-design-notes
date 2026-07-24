# Module 07: Cloud Data Architecture (BigQuery, Dataflow & Apache Beam)

This module covers the data engineering requirements from the Aviato job description: processing, organizing, and structuring massive datasets using **Google Cloud BigQuery**, and designing streaming and batch pipelines via **GCP Cloud Dataflow** and **Apache Beam**.

---

## 🏗️ 1. BigQuery Architecture & Optimization

### Partitioning & Clustering Strategy
When storing logs, token metrics, or document embeddings in BigQuery, partitioning and clustering minimize cost and accelerate query performance.

- **Partitioning:** Divide table by date (`INGESTION_DATE` or `TIMESTAMP`).
- **Clustering:** Sort data within partitions by high-cardinality keys (`tenant_id`, `user_id`, `model_name`).

```sql
CREATE TABLE `aviato-prod.ai_analytics.model_invocations`
(
  invocation_id STRING REQUIRED,
  tenant_id STRING REQUIRED,
  model_name STRING REQUIRED,
  prompt_tokens INT64,
  completion_tokens INT64,
  latency_ms FLOAT64,
  created_at TIMESTAMP REQUIRED
)
PARTITION BY DATE(created_at)
CLUSTER BY tenant_id, model_name;
```

---

## ⚡ 2. GCP Dataflow Pipeline with Apache Beam (Python)

Below is an Apache Beam streaming pipeline in Python that reads LLM logs from **Pub/Sub**, calculates rolling token consumption per tenant, and writes the output directly to **BigQuery**.

```python
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions
import json

class ParseAndTransformDoFn(beam.DoFn):
    def process(self, element):
        try:
            payload = json.loads(element.decode('utf-8'))
            yield {
                'invocation_id': payload.get('invocation_id'),
                'tenant_id': payload.get('tenant_id'),
                'model_name': payload.get('model_name'),
                'prompt_tokens': int(payload.get('prompt_tokens', 0)),
                'completion_tokens': int(payload.get('completion_tokens', 0)),
                'latency_ms': float(payload.get('latency_ms', 0.0)),
                'created_at': payload.get('timestamp')
            }
        except Exception as e:
            # Drop malformed records to dead-letter queue
            pass

def run_pipeline():
    options = PipelineOptions()
    options.view_as(StandardOptions).streaming = True

    with beam.Pipeline(options=options) as p:
        (
            p
            | "ReadFromPubSub" >> beam.io.ReadFromPubSub(subscription="projects/aviato-prod/subscriptions/llm-logs-sub")
            | "ParseJSON" >> beam.ParDo(ParseAndTransformDoFn())
            | "WriteToBigQuery" >> beam.io.WriteToBigQuery(
                table="aviato-prod:ai_analytics.model_invocations",
                schema="invocation_id:STRING, tenant_id:STRING, model_name:STRING, prompt_tokens:INT64, completion_tokens:INT64, latency_ms:FLOAT64, created_at:TIMESTAMP",
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED
            )
        )

if __name__ == '__main__':
    run_pipeline()
```

---

## 🌊 3. BigQuery Storage Write API vs Legacy Streaming Inserts

| Feature | Storage Write API (Recommended) | Legacy Streaming Inserts (`insertAll`) |
| :--- | :--- | :--- |
| **Throughput** | High throughput (GB/s stream ingest) | Moderate (Rate limits per project) |
| **Cost** | ~50% cheaper ingestion rate | Higher cost per megabyte |
| **Semantics** | Exactly-once stream guarantees | At-least-once (can produce duplicates) |

---

## ❓ Common Data Architecture Interview Questions

### Q: How do you handle out-of-order log events in Apache Beam / GCP Dataflow?
**Answer:**
Dataflow uses **Watermarks** (estimates of data completeness based on event time vs processing time) combined with **Allowed Lateness**. Windows process events based on their event timestamp (`created_at`). Late-arriving events within the allowed lateness window trigger window recalculations or side-outputs.
