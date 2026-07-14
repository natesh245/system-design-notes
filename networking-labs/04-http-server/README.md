# HTTP, HTTPS, & Idempotency Patterns Deep Dive

HTTP is the primary application-layer protocol for web clients and servers. This document explains HTTP methods, status codes, and implementation patterns for distributed systems.

---

## 🚦 HTTP Methods & Idempotency

*   **Safe Methods:** Reading data. They do not modify server state. (Cachable)
*   **Idempotent Methods:** Sending the request multiple times results in the same server state as sending it once.

| Method | Safe | Idempotent | Description | System Design Context |
| :--- | :--- | :--- | :--- | :--- |
| **`GET`** | Yes | Yes | Retrieve resource state | CDN caching, proxy caching, browser caching. |
| **`POST`** | No | No | Create new resource | Non-idempotent. Retries can cause duplicates (e.g. duplicate checkouts). |
| **`PUT`** | No | Yes | Replace entire resource state | Idempotent. Re-sending replaces the item with the exact same details. |
| **`DELETE`**| No | Yes | Delete resource | Idempotent. Repeated deletions result in the same state (resource is deleted). |
| **`PATCH`** | No | No | Partial update | Usually non-idempotent (e.g. `{ $inc: { count: 1 } }`). |

---

## 🔒 The Idempotency Key Pattern
When a client sends a non-idempotent request (like `POST /payments`), network timeouts can occur. The client doesn't know if the server received the request before dropping, or if the response got lost. 

To safely retry without side effects, we implement **Idempotency Keys**:

```
Client                             Server                             Redis
  |                                  |                                  |
  | -- POST /payment (Key: K) -----> |                                  |
  |                                  | -- SETNX lock:K true ----------->|
  |                                  | <-- 1 (Success) -----------------| [Lock acquired]
  |                                  |                                  |
  |                                  | (Process payment: charge card)   |
  |                                  |                                  |
  |                                  | -- SET result:K (Response) ----->|
  |                                  | -- DEL lock:K ------------------>|
  | <-- Response ------------------- |                                  |
  v                                  v                                  v
```

### The Step-by-Step Flow:
1.  **Key Generation:** The client generates a unique UUID (Idempotency Key) and sends it in the HTTP header: `Idempotency-Key: f2d58a80-e822-4931-869c-d32915981a24`.
2.  **Locking (`SETNX`):** The server receives the key and tries to store a lock in a distributed cache (e.g., Redis) using `SET key lock EX 10 NX`.
    *   *If lock fails:* Another request is currently processing. Return an error or block/wait.
3.  **Check Cache:** The server checks if the key already has a cached response (indicating a previous attempt succeeded).
    *   *Cache Hit:* Return the cached response immediately to the client. Do not process again.
4.  **Process and Save:** On a cache miss, the server executes the payment logic, saves the success/fail response in Redis (with a TTL, e.g., 24 hours), releases the lock, and returns the response.

---

## 🛠️ HTTP Status Codes in System Design

Status codes are critical for monitoring service health, diagnosing network bottlenecks, and triggering circuit breakers.

*   **`429 Too Many Requests`:** Returned by Rate Limiters when a client exceeds their allowance. Typically contains a `Retry-After: 60` header.
*   **`502 Bad Gateway`:** The reverse proxy/load balancer could not connect to or parse the response of the upstream application server. Indicates the app server process has crashed.
*   **`503 Service Unavailable`:** The server is overloaded or down for maintenance. In microservices, this status code triggers **Circuit Breakers** to fail-fast and stop cascading failures.
*   **`504 Gateway Timeout`:** The gateway (Nginx/API Gateway) did not receive a timely response from the backend service. Indicates a database bottleneck, deadlock, or resource exhaustion downstream.

---

## 🔑 HTTPS & The TLS Handshake
HTTPS is HTTP encrypted inside a Transport Layer Security (TLS) tunnel.

1.  **Asymmetric Cryptography:** The server sends its SSL Certificate containing its public key. The client verifies the certificate against root authorities and negotiates a symmetric key using Diffie-Hellman key exchange.
2.  **Symmetric Cryptography:** Once the symmetric key (session key) is established, all requests and responses are encrypted using it. Symmetric encryption is highly performant and does not bottleneck server CPUs.
3.  **ALPN (Application-Layer Protocol Negotiation):** Dynamically decides the HTTP version (e.g., HTTP/2) during the TLS handshake, saving network round trips.
