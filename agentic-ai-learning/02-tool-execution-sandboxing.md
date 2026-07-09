# Chapter 2: Tool Execution & Sandboxing

To be useful, an agent must interact with its environment: reading files, querying databases, calling external APIs, and executing code. However, giving an LLM the ability to run code on your system introduces massive security and operational risks.

---

## 🔌 Tool & Function Calling Mechanics

Modern LLMs support **native function calling**. Instead of writing complex regex parsers to read text prompts, you register your native functions with the LLM API using **JSON Schema**.

```text
+--------------+                   +--------------------+
|  LLM Prompt  | ----------------> |   Engine Executes  |
|  & Function  |                   |   Native Function  |
|  Definitions |                   |                    |
+--------------+                   +--------------------+
       ^                                     |
       |                                     v
+--------------+                   +--------------------+
| Model returns| <---------------- |  Return Result as  |
| ToolCall JSON|                   |  Observation to LL |
+--------------+                   +--------------------+
```

### JSON Schema Specification Example
When registering a tool (e.g. `get_weather`), you send its description and parameter specification:
```json
{
  "name": "get_weather",
  "description": "Get the current weather for a specific city.",
  "parameters": {
    "type": "object",
    "properties": {
      "city": {
        "type": "string",
        "description": "The city name, e.g., San Francisco, CA"
      }
    },
    "required": ["city"]
  }
}
```

---

## 🚧 The Danger of Host Execution

If an agent is given access to a shell or Python interpreter running directly on the host machine, it can cause catastrophic damage:
1.  **Destructive Actions:** A hallucination or incorrect logic could execute `rm -rf /` or delete a critical database.
2.  **Data Theft:** The agent can access local environment variables, credentials, SSH keys, and source code, uploading them to external servers.
3.  **Resource Hijacking:** An agent caught in an infinite loop can consume 100% CPU/RAM, crash the host, or run cryptocurrency miners.

---

## 🔒 Sandboxing Architectures

To run untrusted code safely, agents must execute tasks in isolated sandboxes. There are three common production architectures:

### 1. Container Isolation (Docker / Podman)
*   **How it works:** Each agent task runs inside a clean Docker container containerized away from the host file system.
*   **Tuning:** Limit memory, CPU shares, and network access (e.g., disable outbound internet unless strictly required).

### 2. MicroVMs (AWS Firecracker / gVisor)
*   **How it works:** Provides virtualization-level security with extremely fast boot times (~5ms). This is what serverless providers (like AWS Lambda) use.
*   **Tuning:** Offers hard hardware-level isolation, preventing container escapes.

### 3. API-Based Code Sandboxes (E2B / Fly.io / e2b.dev)
*   **How it works:** Third-party developer platforms provide hosted cloud environments specifically designed for LLMs to run code. You spin up a sandboxed environment via a single SDK, write files, run Python/Bash, and destroy the sandbox when the session completes.

---

## 🏋️ Coding Challenge: Build a Secure Sandbox Runner

Create a Node.js or Python program that allows an agent to safely run Python scripts.

### Requirements:
1.  Start a Docker container using a minimal Python base image (`python:3.10-alpine`).
2.  Mount an isolated directory containing the agent's scripts.
3.  Run the script inside the container with strict constraints:
    *   Set execution timeout (e.g., kill the process if it runs longer than 5 seconds).
    *   Limit memory to `128mb` and CPU usage.
    *   Disable network access inside the container.
4.  Capture the exit code, stdout, and stderr, and return them back to the agent.
