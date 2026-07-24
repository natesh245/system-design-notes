# Module 06: Cloud Data Pipelines (BigQuery, Dataflow & Apache Beam)

This module covers cloud data architecture, batch and streaming pipelines, and warehouse optimization using **Google Cloud BigQuery** and **GCP Dataflow (Apache Beam)**.

---

## 🏗️ 1. BigQuery Optimization & Partitioning

To optimize query performance and reduce cost in large AI data platforms:
- **Partitioning:** Divide tables by date (`PARTITION BY DATE(created_at)`).
- **Clustering:** Order data within partitions by high-cardinality query keys (`CLUSTER BY tenant_id, model_name`).

---

## ⚡ 2. Apache Beam Streaming Pipeline (Python)

```python
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import json

class TransformLogDoFn(beam.DoFn):
    def process(self, element):
        payload = json.loads(element.decode('utf-8'))
        yield {
            'invocation_id': payload.get('id'),
            'tenant_id': payload.get('tenant_id'),
            'prompt_tokens': int(payload.get('prompt_tokens', 0)),
            'completion_tokens': int(payload.get('completion_tokens', 0)),
            'created_at': payload.get('timestamp')
        }

def run():
    options = PipelineOptions(streaming=True)
    with beam.Pipeline(options=options) as p:
        (
            p
            | "ReadPubSub" >> beam.io.ReadFromPubSub(subscription="projects/my-proj/subscriptions/ai-logs-sub")
            | "Transform" >> beam.ParDo(TransformLogDoFn())
            | "WriteBQ" >> beam.io.WriteToBigQuery(
                table="my-proj:ai_data.invocations",
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
            )
        )
```

---

## 🌊 3. Storage Write API vs Legacy Inserts

- **Storage Write API:** High throughput, lower cost, exactly-once delivery guarantees.
- **Legacy Streaming Inserts (`insertAll`):** Higher per-MB cost, at-least-once delivery (potential duplicates).
