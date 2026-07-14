# UDP (User Datagram Protocol) Deep Dive

UDP is a simple, connectionless transport protocol. Unlike TCP, it does not build streams, verify order, or recover lost packets. It is a "fire-and-forget" protocol designed for speed and low overhead.

---

## ⚡ Key Characteristics & Overhead Comparison

*   **No Connection Handshake:** UDP sends packets (datagrams) immediately without verifying if the receiver is online, resulting in **0-RTT startup latency**.
*   **Packet-Boundary Based:** UDP transmits data in discrete datagram boundaries. A single `send()` call translates to exactly one UDP packet.
*   **Minimal Headers:** UDP has a fixed header size of **8 bytes** (Source Port, Destination Port, Length, Checksum) compared to TCP's 20-60 bytes.

```
TCP Header (Min 20 Bytes)                   UDP Header (Fixed 8 Bytes)
+-------------------+-------------------+   +-------------------+-------------------+
|    Source Port    |  Destination Port |   |    Source Port    |  Destination Port |
+-------------------+-------------------+   +-------------------+-------------------+
|                  Sequence Number      |   |      Length       |     Checksum      |
+---------------------------------------+   +-------------------+-------------------+
|               Ack Number              |
+---------------------------------------+
|  Length |  Flags  |      Window       |
+---------+---------+-------------------+
|     Checksum      |   Urgent Pointer  |
+-------------------+-------------------+
```

---

## 🏗️ System Design: When to Choose UDP?

Selecting UDP is a deliberate choice to prioritize **speed / low-latency** over **guaranteed delivery**.

### 1. Live Media Streaming & VoIP (e.g., Zoom, WebRTC, Discord)
*   **Why:** In a live conversation, losing a few audio/video packets results in a tiny flicker or audio pop (which is barely noticeable). However, waiting for TCP to retransmit lost packets would freeze the video stream, resulting in lag. **Real-time interaction values latency over complete reliability.**

### 2. Multiplayer Gaming (State Replication)
*   **Why:** Fast-paced multiplayer games send 30-60 state packets per second (player positions, orientation). If packet #10 is lost, there is no point retransmitting it, because packet #11 is already arriving with the latest coordinates.

### 3. Lightweight Request-Response Queries (DNS, DHCP, NTP)
*   **Why:** Setting up a TCP connection for a single query (e.g., "what is the IP for youtube.com?") is inefficient. If a UDP query is lost, the client simply retries after a timeout.

---

## 🚀 The Future of Networking: HTTP/3 and QUIC

To overcome TCP's limits, Google designed **QUIC (Quick UDP Internet Connections)**, which forms the transport layer of **HTTP/3**.

### How QUIC Works:
QUIC runs on top of **UDP** in user space (application layer). It implements security (TLS 1.3) and reliability features natively:

1.  **Eliminates Head-of-Line (HOL) Blocking:** In HTTP/2 (over TCP), if one packet is lost, the operating system blocks all concurrent streams until the lost packet is retransmitted. QUIC manages streams independently: a lost packet on Stream A only blocks Stream A, while Streams B and C continue processing data.
2.  **Connection Migration:** TCP identifies connections using a 4-tuple: `(Source IP, Source Port, Dest IP, Dest Port)`. Shifting from LTE to Wi-Fi changes your IP, dropping the TCP connection. QUIC identifies connections using a unique **Connection ID**. You can switch networks seamlessly without dropping active connections.
3.  **0-RTT Handshake:** Combines transport connection and TLS security negotiation, allowing clients to send encrypted application data on the first RTT.
