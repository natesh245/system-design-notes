# TCP (Transmission Control Protocol) Deep Dive

TCP is a transport-layer protocol that guarantees reliable, ordered, and error-checked delivery of a stream of octets (bytes) between applications running on hosts communicating over an IP network.

---

## 🤝 Connection Management

### The 3-Way Handshake
Before data transmission begins, TCP establishes a virtual circuit to align sequence numbers and buffer sizes.

```
Client                                     Server
  |                                          |
  | -------- SYN (Seq = ISN_C) ------------> | [Server allocates resources]
  |                                          |
  | <------- SYN-ACK (Seq=ISN_S, Ack=ISN_C+1)|
  |                                          |
  | -------- ACK (Ack = ISN_S+1) ----------> | [Connection Established]
  v                                          v
```

1.  **`SYN` (Synchronize):** Client sends a packet with its initial sequence number ($ISN_C$).
2.  **`SYN-ACK`:** Server acknowledges the client's packet ($Ack = ISN_C + 1$) and sends its own initial sequence number ($ISN_S$).
3.  **`ACK` (Acknowledge):** Client acknowledges the server's sequence number ($Ack = ISN_S + 1$). The connection transitions to `ESTABLISHED`.

---

### The 4-Way Handshake (Teardown)
Because TCP is full-duplex, each direction of the connection must be closed independently.

```
Client                                     Server
  |                                          |
  | -------- FIN --------------------------> | [Active close]
  | <------- ACK --------------------------- | [Passive close / Server FIN-WAIT]
  |                                          |
  |             (Server finishes sending data)
  |                                          |
  | <------- FIN --------------------------- |
  | -------- ACK --------------------------> | [Client enters TIME_WAIT]
  v                                          v
```
*   **`TIME_WAIT` State:** After sending the final `ACK`, the client waits for $2\times MSL$ (Maximum Segment Lifetime, usually 1–4 minutes) before releasing resources. This ensures the final `ACK` is received by the server, and prevents late/stale segments from a closed connection from corrupting new connections sharing the same socket port.

---

## 🌊 Flow Control vs. Congestion Control

These are two distinct mechanisms designed to protect the **receiver** and the **network** respectively:

### 1. Flow Control (Protecting the Receiver)
Flow control prevents a fast sender from overwhelming a slow receiver's buffer space.
*   **Mechanism:** Sliding Window. The receiver advertises its available buffer space in the TCP header using the window size field (`rwnd`).
*   **Zero Window:** If `rwnd` drops to `0`, the sender halts data transmission and periodically sends probe packets to check if buffer space has cleared.

### 2. Congestion Control (Protecting the Network)
Congestion control prevents the sender from flooding the network nodes (routers/links) with more packets than they can route.
*   **Mechanism:** The sender maintains a Congestion Window (`cwnd`). The volume of unacknowledged data cannot exceed $\min(cwnd, rwnd)$.
*   **States:**
    1.  **Slow Start:** `cwnd` starts small (e.g., 10 MSS) and doubles every Round Trip Time (RTT) to probe network capacity.
    2.  **Congestion Avoidance:** Once `cwnd` hits a threshold (`ssthresh`), it grows linearly (+1 MSS per RTT) rather than exponentially.
    3.  **Fast Retransmit & Fast Recovery:** Initiated when 3 duplicate ACKs are received, indicating packet loss. It retransmits immediately without waiting for a timeout.

#### Congestion Control Algorithms
*   **Loss-Based (Cubic / Reno):** Standard algorithms. They assume **packet loss = network congestion**. They scale up throughput until packets drop, then cut `cwnd` aggressively. This performs poorly on modern networks with high packet loss (e.g., Wi-Fi) or high bandwidth-delay product (BDP) links.
*   **Model/Delay-Based (BBR - Bottleneck Bandwidth and RTT):** Developed by Google. BBR measures actual network propagation delay and bottleneck bandwidth. It sends data at the physical capacity of the pipe without dropping packets, yielding much higher throughput and lower latency.
