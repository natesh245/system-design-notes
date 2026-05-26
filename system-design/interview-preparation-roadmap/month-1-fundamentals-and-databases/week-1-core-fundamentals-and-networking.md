# Week 1: Core Fundamentals & Networking

## Focus Areas
- Scalability
- Availability
- Reliability
- Fault Tolerance
- CAP Theorem
- Basic Networking (DNS, TCP/UDP, Latency vs Throughput)

## Study Notes

### Scalability
Scalability is the measure of a system's ability to handle increased load by dynamically adding resources without impacting performance or reliability. A system is considered scalable if it can grow its capacity proportionally to the resources added.

#### 1. Dimensions of Load
To scale a system, you must first define what "load" means for your specific application:
*   **Request Volume:** Requests per second (RPS) or queries per second (QPS).
*   **Concurrent Users:** Number of active simultaneous connections.
*   **Data Volume:** Storage size, read/write throughput to disks.
*   **Processing Complexity:** CPU-bound tasks (e.g., video rendering) vs. I/O-bound tasks (e.g., fetching from DB).

#### 2. Scaling Strategies
There are two primary ways to scale a system:
*   **Vertical Scaling (Scale Up):** Adding more power (CPU, RAM, faster SSDs) to a single machine.
    *   *Pros:* Simple, no application changes required, low network latency (single process).
    *   *Cons:* Hard hardware limits, single point of failure (SPOF), cost increases exponentially.
*   **Horizontal Scaling (Scale Out):** Adding more instances/machines to the pool.
    *   *Pros:* Practically infinite scaling potential, built-in redundancy/high availability.
    *   *Cons:* Requires load balancers, introduces network latency, requires application statelessness, increases architectural complexity.

#### 3. Key Concepts & Patterns
*   **Statelessness:** Application servers should not store user session state locally. Sessions should be moved to a shared, fast cache (e.g., Redis) so any server can handle any request.
*   **Scalability vs. Performance:** 
    *   *Scalability:* How well the system maintains performance under heavy concurrent load. If a system is fast for one user but crashes under load, it has a scalability problem.

#### 4. How to Measure Scalability
Scalability is measured by assessing how system performance changes as you scale both load and resources. To evaluate this, you must distinguish between **Load Metrics** and **Performance Metrics**.

| Metric Type | Definition | Key Examples | Purpose in Scalability |
| :--- | :--- | :--- | :--- |
| **Load Metrics (Input)** | Describe the demand placed on the system by external actors. | Requests Per Second (RPS/QPS), Active concurrent users, Data ingestion volume (GB/day), Database write rate. | Acts as the **independent variable** in tests. You increase this to see where the system breaks. |
| **Performance Metrics (Output / Health)** | Describe how the system behaves and responds under a given load. | Latency ($p95, p99$), Throughput (successful responses/sec), CPU/Memory saturation, Disk I/O wait, HTTP Error Rates. | Acts as the **dependent variable**. You track these to verify if the system maintains acceptable health as load rises. |

*   **Resource Scaling Efficiency:**
    $$\text{Scaling Efficiency} = \frac{\text{Throughput with } N \text{ resources}}{N \times \text{Throughput with } 1 \text{ resource}}$$
    *   **Linear Scale ($100\%$ efficiency):** Throughput doubles when resources double (rare in practice due to coordination overhead).
    *   **Sub-linear Scale ($<100\%$ efficiency):** Throughput increases, but at a diminishing rate as you add resources.
    *   **Negative Scale:** Adding more resources actually *decreases* throughput due to contention and communication overhead.

*   **Load Testing & Key Performance Indicators (KPIs):**
    1.  **Throughput vs. Load:** Plotting concurrent users/RPS against actual throughput. The curve should rise steadily. A flatline indicates a bottleneck.
    2.  **Latency Percentiles ($p50, p90, p99, p99.9$):** Average latency is misleading. Scalability is measured by tracking tail latencies ($p99$ or $p99.9$—meaning the slowest $1\%$ or $0.1\%$ of requests). If $p99$ spikes exponentially under load while average latency rises slowly, the system is hitting queueing bottlenecks.
    3.  **Resource Saturation:** Monitoring CPU, Memory, Network I/O, and Disk I/O. A scalable system saturates resources evenly rather than having a single resource lock up at $100\%$ (e.g., database lock contention).

*   **Mathematical Models:**
    *   **Amdahl's Law:** Shows that the speedup of a system is limited by its serial (non-parallelizable) components.
    *   **Universal Scalability Law (USL):** Extends Amdahl's law to account for **coordination overhead** (crosstalk between nodes) and **contention** (waiting for shared resources). It explains why systems eventually hit a peak throughput and then decline as more nodes are added.


### Availability
Availability is the percentage of time a system remains operational, functional, and accessible to process incoming requests. High Availability (HA) ensures that a service is online with minimal to no downtime, even during component failures.

#### 1. Measuring Availability ("The Nines")
Availability is typically calculated as:
$$\text{Availability} = \frac{\text{Uptime}}{\text{Uptime} + \text{Downtime}} \times 100$$

It is measured in "Nines" of uptime per year:
*   **99% (Two Nines):** ~3.65 days of downtime/year.
*   **99.9% (Three Nines):** ~8.76 hours of downtime/year (standard target for many web services).
*   **99.99% (Four Nines):** ~52.6 minutes of downtime/year (premium enterprise standard).
*   **99.999% (Five Nines):** ~5.26 minutes of downtime/year (highly critical infrastructure like telecoms or banking).

#### 2. Sequence vs. Parallel Components
When multiple components make up a system, the overall availability depends on their configuration:
*   **In Sequence (Dependency Chain):** The system relies on all components working.
    $$\text{Availability}_{\text{Total}} = A_1 \times A_2$$
    *Example:* If a web server ($99.9\%$) depends on a database ($99.9\%$) in sequence, total availability drops to **$99.8\%$**.
*   **In Parallel (Redundancy):** The system has backup paths.
    $$\text{Availability}_{\text{Total}} = 1 - (1 - A_1) \times (1 - A_2)$$
    *Example:* If two redundant web servers ($99.9\%$) are configured in parallel via a load balancer, total web tier availability rises to **$99.9999\%$**.

#### 3. Key High Availability Patterns
*   **Failover:** Routing traffic to a backup system when a failure is detected.
    *   *Active-Passive:* The standby backup server runs but does not take traffic until the active server fails.
    *   *Active-Active:* Both servers handle traffic concurrently. If one dies, the other takes over 100% of the load.
*   **Redundancy:** Eliminating Single Points of Failure (SPOFs) by duplicating critical components.

### Reliability
Reliability is the probability that a system will perform its intended function correctly under stated conditions for a specified period of time. While availability is about the system being *reachable*, reliability is about the system *producing correct results without errors*.

#### 1. Availability vs. Reliability
A system can be highly available but completely unreliable:
*   *Example:* An e-commerce API is online $99.99\%$ of the time (high availability), but $15\%$ of shopping cart checkout requests fail with a database error (low reliability). 

#### 2. Key Reliability Metrics
*   **MTBF (Mean Time Between Failures):** The average time elapsed between inheritable failures of a system during operation.
*   **MTTR (Mean Time To Repair):** The average time required to troubleshoot, fix, and restore a failed component back to service.
*   **MTTF (Mean Time To Failure):** The average time a non-repairable system is expected to operate before failing.

---

### Fault Tolerance
Fault Tolerance is the ability of a system to continue functioning correctly even in the event of hardware, software, or network failures in one or more of its sub-components.

#### 1. Graceful Degradation
Instead of failing catastrophically, a fault-tolerant system degrades its service quality gracefully.
*   *Example:* If a personalized recommendation service fails on a streaming site, the home page doesn't crash; it degrades gracefully by displaying a cached list of static, popular videos.

#### 2. Strategies for Fault Tolerance
*   **Active Redundancy:** Multiple components process the same inputs in parallel. If one returns a faulty result, a voting mechanism (like Paxos or Raft) decides the correct state.
*   **Isolation (Bulkheads):** Segmenting components so that a failure in one area does not cascade and bring down the entire system (e.g., separating thread pools for different API services).
*   **Heartbeats & Health Checks:** Periodically sending small ping requests between nodes to quickly detect when a node goes offline.

---

### CAP Theorem
The CAP Theorem states that in a distributed computer system, it is impossible to simultaneously provide more than two of the following three guarantees:
1.  **Consistency (C):** Every read receives the most recent write or an error.
2.  **Availability (A):** Every non-failing node returns a response (without guarantee that it contains the most recent write).
3.  **Partition Tolerance (P):** The system continues to operate despite network partitions (dropped or delayed messages between nodes).

```text
                [ CAP Theorem ]
                 /     |     \
                /      |      \
               /       |       \
     [ Consistency ]   |   [ Partition Tolerance ]
                       |
               [ Availability ]
```

#### 1. The Partition Constraint (CP vs. AP)
Since physical networks are inherently unreliable, **Partition Tolerance (P) is mandatory**. You cannot choose "CA". Therefore, when a network partition occurs, you must choose:
*   **CP (Consistency & Partition Tolerance):** Cancel/block the operation to guarantee data correctness. If Node A and Node B cannot communicate, a write to Node A will block because it cannot replicate to Node B. (Good for banking/ledger systems).
*   **AP (Availability & Partition Tolerance):** Allow the write on Node A, making it immediately available, but accept that Node B will temporarily serve stale/inconsistent data until the partition heals. (Good for social feeds, comments, shopping carts).

#### 2. PACELC Theorem (An Extension)
CAP only describes behavior during a network partition. **PACELC** adds behavior during normal operation:
*   If there is a **P**artition, choose **A**vailability vs **C**onsistency.
*   **E**lse (normal state), choose **L**atency vs **C**onsistency.
    *   *Example:* MongoDB/Cassandra are typically **PA/EL** (Available during partitions; low latency during normal states, relying on asynchronous replication).
    *   *Example:* Traditional SQL DBs are **PC/EC** (Consistent during partitions; synchronous replication for absolute consistency during normal states, sacrificing speed).

---

### Basic Networking for System Design

#### 1. DNS (Domain Name System)
The internet's phone book. DNS translates human-readable domain names (e.g., `google.com`) into machine-readable IP addresses.
*   **Resolution Flow:** Browser Cache $\rightarrow$ OS Cache $\rightarrow$ Router Cache $\rightarrow$ ISP Recursive Resolver $\rightarrow$ Root Name Server $\rightarrow$ TLD Server $\rightarrow$ Authoritative Name Server.
*   **TTL (Time To Live):** The time a DNS record is allowed to reside in local cache before expiring and requesting a refresh.

#### 2. Protocols: TCP vs. UDP
*   **TCP (Transmission Control Protocol):** Connection-oriented. Establishes a virtual connection via a **3-Way Handshake** (SYN $\rightarrow$ SYN-ACK $\rightarrow$ ACK).
    *   *Features:* Guaranteed delivery, ordered packets, flow control, congestion control, and error checking.
    *   *Use Cases:* HTTP/HTTPS, Database connections, SMTP (Email), SSH.
*   **UDP (User Datagram Protocol):** Connectionless. Packets (datagrams) are sent without handshakes or delivery confirmation.
    *   *Features:* Lightweight, fast, low latency, no ordering guarantees, no congestion control.
    *   *Use Cases:* Live streaming, VoIP (video/voice calls), Online gaming, DNS queries.

#### 3. Latency vs. Throughput vs. Bandwidth
*   **Latency:** The time it takes for a single packet of data to travel from client to server and back (round-trip time, RTT). (Target: lower is better).
*   **Throughput:** The actual rate at which data is successfully transmitted over a communication channel in a given time period (e.g., MB/s or QPS). (Target: higher is better).
*   **Bandwidth:** The maximum theoretical capacity of a network link (e.g., a 1 Gbps connection).

