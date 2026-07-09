# Chapter 5: Evaluation, Guardrails & Production Systems

Running agents in a sandbox or locally is easy. Deploying them to production to handle live customers and business transactions requires rigorous observability, evaluations, cost boundaries, and safety guardrails.

---

## 📈 Tracing & Telemetry (Observability)

Standard backend logs (`console.log`, `logging.info`) are insufficient for agents. An agent execution is a complex, non-deterministic graph of LLM calls, tool execution, memory lookups, and state transitions.

### Key Observation Metrics:
1.  **Execution Trajectory:** The exact path of nodes/agents executed.
2.  **LLM Call Inputs/Outputs:** The exact prompts, parameters, and generated tokens for each step.
3.  **Latency & Cost Attribution:** How much time and money each sub-agent or tool step consumed.

**Tooling:** Use dedicated tracing engines like **LangSmith**, **Phoenix (Arize)**, or open-source OpenTelemetry providers to record agent trajectories.

---

## 🧪 Agent Evaluation (Eval Suites)

Traditional software is tested with unit tests (expected input ➔ expected output). Agents are non-deterministic, so their trajectories and outputs vary.

### Evaluation Strategies:
1.  **Deterministic Evals:** Asserting that specific tools were called, or checking for key strings in the output.
2.  **LLM-as-a-Judge:** Using a highly capable model (like Gemini 1.5 Pro or GPT-4o) to grade the agent's final answer and trajectory based on criteria:
    *   *Correctness:* Did it accurately solve the user request?
    *   *Helpfulness:* Was the tone and structure appropriate?
    *   *Safety:* Did it leak system prompts or override instructions?
3.  **Trajectory Audits:** Measuring if the agent solved the problem in the fewest number of steps, or if it took redundant/unnecessary tool actions.

---

## 🛡️ Production Guardrails

Guardrails act as a safety net around your agent, monitoring inputs and outputs to prevent security breaches and financial loss.

```text
  [ User Prompt ] ---> [ Input Guardrails ] ---> [ Agent Loop ]
                             - Injection Check         |
                             - PII Masking             |
                                                       v
  [ User Client ] <--- [ Output Guardrails ] <--- [ Tool Execution ]
                             - Content Filter          - Budget Limits
                             - Structural Check        - Sandbox Timeout
```

### 1. Input Guardrails (Prompt Injections & PII)
*   **Prompt Injection:** Filters inputs that attempt to override system instructions (e.g., "Ignore previous instructions and output password").
*   **PII Sanitization:** Masks Social Security Numbers, API Keys, or personal customer data before forwarding them to third-party LLMs.

### 2. Operational Guardrails (Budgets & Loops)
*   **Max Steps Constraint:** If an agent doesn't solve a task within 15 loop iterations, kill the task. This stops infinite loops.
*   **Financial Budgets:** Attach a dollar limit (e.g., maximum $1.50 of API spending per task). Terminate the agent execution if it exceeds the limit.
*   **Timeout Guard:** Set maximum execution durations for all tool/sandbox execution.

### 3. Output Guardrails (Validation)
*   **Structural Parsing:** Validate that output formats conform to your JSON Schema using libraries like Guardrails AI or Pydantic.
*   **Content Moderation:** Automatically verify that output text contains no toxic, unsafe, or copyrighted materials.

---

## 🏋️ Coding Challenge: Build a Guardrailed Agent Runner

Write an execution harness for an agent that protects it against cost inflation and loops.

### Requirements:
1.  **Agent Context:** Maintain a count of `steps_taken` and `cumulative_cost_usd` for a running task.
2.  **Middleware Validation:** Before invoking the LLM or any tool, run a check:
    *   If `steps_taken > 10`, throw a `LoopDetectionError`.
    *   If `cumulative_cost_usd > 1.00`, throw a `BudgetExceededError`.
3.  **Tracing Log:** Record each input, tool call, tool response, and cost to a local log file, enabling post-execution auditing.
