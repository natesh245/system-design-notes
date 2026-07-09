# Chapter 1: Agentic Foundations & Reasoning Patterns

To transition from building standard Chatbots to autonomous agents, you must understand how to structure an LLM's computation path so it can plan, execute actions, and correct its mistakes.

---

## 🧠 Chain-of-Thought (CoT) & System Prompts

Traditional prompting sends a question and expects a direct answer. **Chain-of-Thought (CoT)** forces the LLM to generate intermediate reasoning steps before arriving at a final response. 

By detailing its "thinking" process, the model decomposes complex problems, significantly improving accuracy in logic, math, and structured tool selection.

### Under the Hood: Why CoT Works
LLMs generate tokens sequentially. When asked a complex question directly, the model has to pack all of its planning, calculations, and final answers into the very next few tokens. By forcing the model to write down its reasoning steps, it uses the generated tokens as working memory (a "scratchpad") to compute the final answer.

---

## 🔄 The ReAct (Reason + Act) Design Pattern

The **ReAct** pattern combines reasoning (planning, assessing) and acting (invoking external tools) in an iterative loop:

```text
  +--------------------------------------------+
  |                 User Input                 |
  +--------------------------------------------+
                        |
                        v
  +--------------------------------------------+
  |    THOUGHT: Reason about the current state | <---------+
  +--------------------------------------------+           |
                        |                                  |
                        v                                  |
  +--------------------------------------------+           |
  |    ACTION: Select tool and parameters      |           |
  +--------------------------------------------+           |
                        |                                  |
                        v                                  |
  +--------------------------------------------+           |
  |   OBSERVATION: Execute tool & get result   | ----------+
  +--------------------------------------------+
                        | (When goal is achieved)
                        v
  +--------------------------------------------+
  |              Final Response                |
  +--------------------------------------------+
```

### The ReAct Prompt Structure
A classical ReAct prompt instructs the model to follow a strict text syntax:
```text
Question: [The user input]
Thought: [Reasoning process about what to do next]
Action: [The tool name to call]
Action Input: [The parameters for the tool]
Observation: [The result returned by executing the tool]
... (Repeat Thought/Action/Observation if needed)
Thought: I have the final answer.
Final Answer: [The response to the user]
```

---

## 🛠️ Structured Output Generation

Agents must interact with software APIs, databases, and code execution blocks. Because of this, their output must be structured (typically as JSON) rather than free-form text.

### High-Level Strategies:
1.  **Manual JSON/XML Prompting:** Instructing the model to write JSON in code blocks. This is fragile because LLMs can produce syntax errors, trailing commas, or markdown formatting (e.g., ` ```json `).
2.  **JSON Mode:** Forcing the LLM's JIT token selection to only allow characters that form valid JSON, guaranteeing structural parsing correctness.
3.  **Structured Tool/Function Calling (Native):** Modern LLMs (like Gemini, OpenAI, Claude) accept a JSON Schema representing the desired structure, adjusting the model's output generation logic to guarantee the output matches the schema exactly.

### Python / Pydantic Example for Tool Structuring:
```python
from pydantic import BaseModel, Field

class CalculateInterest(BaseModel):
    principal: float = Field(description="The initial principal amount.")
    rate: float = Field(description="The annual interest rate (as a decimal, e.g., 0.05).")
    years: int = Field(description="The number of years the money is invested.")
```

---

## 🪞 Self-Correction & Reflection (Self-Eval)

Autonomous agents frequently fail. A robust agent must inspect its own work and correct failures dynamically.

### Core Patterns:
1.  **Compiler Feedback:** If the agent generates code that crashes, feed the stack trace back into the prompt:
    > "The code you generated threw this error: `TypeError: undefined is not a function`. Rewrite the code to fix this issue."
2.  **Critic/Generator Separation:** Having two separate LLM prompts (or agents): one generating the solution, and another inspecting it for safety, logic, and format compliance.

---

## 🏋️ Coding Challenge: Build a Raw ReAct Loop

Write a simple Python or JavaScript script that implements the ReAct loop without using any external framework (like LangChain or AutoGen).

### Requirements:
1.  Create a tool registry containing a simple function (e.g., `calculate_tax(amount)`).
2.  Feed a prompt to the LLM instructing it to output `Action: calculate_tax` and `Action Input: [number]`.
3.  Write code that parses this action out of the LLM's text output, runs the physical python function, formats the result as `Observation: [result]`, appends it back to the prompt history, and calls the LLM again to get the `Final Answer`.
