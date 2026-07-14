# Networking Labs: Hands-on Networking in Node.js

This module contains practical, step-by-step labs to understand networking fundamentals at the code level. By running these scripts, you will observe the mechanics of DNS queries, TCP connection states, UDP packet flows, and HTTP server routing.

## 📁 Directory Structure
*   **`01-dns-lookup/`**: Contains the DNS resolution script and conceptual deep dive.
*   **`02-tcp-socket/`**: A low-level TCP Server and Client demonstrating the 3-way handshake and streaming data exchange.
*   **`03-udp-socket/`**: A UDP Sender and Receiver illustrating connectionless, fire-and-forget datagram delivery.
*   **`04-http-server/`**: A native HTTP server handling request routing, headers, and responding with custom status codes.

---

## 🛠️ Lab Guide

### Lab 1: DNS Resolution CLI
*   **Goal:** Inspect DNS record resolution dynamically.
*   **File:** [`dns-lookup.js`](file:///Users/natesh/projects/system-design/networking-labs/01-dns-lookup/dns-lookup.js)
*   **Run:** `node 01-dns-lookup/dns-lookup.js youtube.com`

### Lab 2: Low-Level TCP Streams
*   **Goal:** Establish a TCP connection, stream text, and observe socket termination.
*   **Files:** [`server.js`](file:///Users/natesh/projects/system-design/networking-labs/02-tcp-socket/server.js), [`client.js`](file:///Users/natesh/projects/system-design/networking-labs/02-tcp-socket/client.js)
*   **Run:** 
    1. Start server: `node 02-tcp-socket/server.js`
    2. Start client (in a new terminal): `node 02-tcp-socket/client.js`

### Lab 3: Fire-and-Forget UDP Datagrams
*   **Goal:** Send stateless packets and observe how UDP doesn't guarantee delivery order.
*   **Files:** [`receiver.js`](file:///Users/natesh/projects/system-design/networking-labs/03-udp-socket/receiver.js), [`sender.js`](file:///Users/natesh/projects/system-design/networking-labs/03-udp-socket/sender.js)
*   **Run:**
    1. Start receiver: `node 03-udp-socket/receiver.js`
    2. Run sender: `node 03-udp-socket/sender.js`

### Lab 4: Native HTTP Server
*   **Goal:** Inspect raw HTTP headers, write status codes, and handle simple routes.
*   **File:** [`server.js`](file:///Users/natesh/projects/system-design/networking-labs/04-http-server/server.js)
*   **Run:** `node 04-http-server/server.js` (Open `http://localhost:3000` in your browser)
