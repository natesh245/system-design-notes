# Week 1: Core Fundamentals & Networking

## Focus Areas
*   **Scalability** (Vertical vs. Horizontal, Dimensions of Load, Statelessness, Performance vs. Scalability)
*   **Availability** (Measuring Availability, Sequence vs. Parallel Components, Failover Patterns)
*   **Reliability** (MTBF, MTTR, MTTF, SLAs/SLOs/SLIs)
*   **Fault Tolerance** (Graceful Degradation, Active Redundancy, Isolation / Bulkheads, Heartbeats)
*   **CAP Theorem** (Consistency, Availability, Partition Tolerance, PACELC Theorem)

---

### **1. Scalability**

#### **Definition**
Scalability is the measure of a system's ability to handle increasing volumes of load without degrading its performance (such as latency or error rates) by proportionally adding resources.

#### **Scalability vs. Performance**
*   **Performance:** Focuses on the speed of a single request or transaction (e.g., reducing response time from $100\text{ ms}$ to $10\text{ ms}$).
*   **Scalability:** Focuses on maintaining that speed as the number of concurrent requests grows (e.g., keeping response time at $100\text{ ms}$ when load increases from 1 to 100,000 concurrent requests).

#### **Scaling Efficiency & Constraints**
When you add resources to a system, the return on investment is rarely perfectly linear due to two main factors modeled by the **Universal Scalability Law (USL)**:
1.  **Contention (Amdahl's Law):** The bottleneck caused by waiting for shared resources (e.g., database locks, single-threaded CPU queues).
2.  **Crosstalk (Coordination Overhead):** The cost of communication and state synchronization between multiple nodes. At high node counts, crosstalk can cause a system's total throughput to actually *decrease* as more servers are added.

$$\text{Scaling Efficiency} = \frac{\text{Throughput with } N \text{ resources}}{N \times \text{Throughput with } 1 \text{ resource}}$$

#### **Dimensions of Load**
To scale, you must first define what "load" means for your specific workload:
*   **Request Volume:** Queries per second (QPS) or Requests per second (RPS).
*   **Concurrently Connected Users:** Simultaneous open sockets (e.g. WebSockets in chat apps).
*   **Data Volume:** Storage capacity and database read/write throughput.
*   **Processing Complexity:** CPU-bound tasks (e.g., rendering) vs. I/O-bound tasks (e.g., disk reads).

#### **Scaling Strategies**
*   **Vertical Scaling (Scale Up):** Adding more CPU, RAM, or faster storage to a single server.
    *   *Pros:* Simple; no architectural changes required.
    *   *Cons:* Hard physical hardware limits; single point of failure (SPOF); cost scales exponentially.
*   **Horizontal Scaling (Scale Out):** Adding more instances/nodes to the pool.
    *   *Pros:* Virtually infinite scale limits; built-in redundancy.
    *   *Cons:* Requires load balancers; introduces network latency; requires application **statelessness** (session data stored in a shared cache like Redis rather than local server memory).
