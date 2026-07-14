# DNS (Domain Name System) Deep Dive

DNS translates human-friendly hostnames (e.g., `youtube.com`) into computer-routable IP addresses. It functions as a hierarchical, globally distributed database.

---

## 🗺️ Hierarchical Resolution Architecture

DNS is structured as an inverted tree hierarchy, reducing bottlenecks and preventing single points of failure.

```
       [ . ] (Root Server)
      /     \
   [.com]  [.org] (Top-Level Domain - TLD)
     /         \
[youtube.com] [wikipedia.org] (Authoritative DNS)
```

1. **Root Nameservers (`.`):** There are 13 logical root server IP addresses (implemented across hundreds of physical nodes using Anycast). They direct queries to the appropriate TLD nameserver (e.g., `.com`).
2. **TLD Nameservers (`.com` / `.net` / etc.):** Managed by registries (e.g., Verisign for `.com`). They point resolvers to the specific Authoritative Nameserver.
3. **Authoritative Nameservers:** The definitive host for the DNS records of a specific domain. This server returns the final IP address.

---

## 🔄 Recursive vs. Iterative Queries

*   **Recursive Query (Client to Resolver):** The client requests the resolver to handle the entire search. The resolver must either return the resolved address or an error.
*   **Iterative Query (Resolver to DNS Hierarchy):** The resolver iteratively contacts nameservers down the tree. Each server returns a referral (e.g., "I don't know the IP, but ask this TLD server next") until the final authoritative record is fetched.

---

## 📋 Common DNS Record Types

*   **`A` (Address Record):** Maps a hostname to an **IPv4** address.
*   **`AAAA` (IPv6 Address Record):** Maps a hostname to an **IPv6** address.
*   **`CNAME` (Canonical Name):** Maps a hostname to an alias hostname (e.g., mapping `images.youtube.com` to `sharded-cdn.provider.net`). CNAME queries require an extra lookup round-trip.
*   **`NS` (Name Server):** Specifies which DNS servers are authoritative for a domain.
*   **`MX` (Mail Exchange):** Routes email to mail servers. Contains a priority score (lower value = higher priority).
*   **`TXT` (Text Record):** Stores arbitrary text, used for domain security (SPF/DKIM email verification, Google Search Console ownership verification).

---

## ⏳ DNS TTL (Time To Live)

TTL determines how long a record can reside in local caching layers (browser, OS, router, recursive resolver) before requiring a refresh.

*   **Long TTL (e.g., 24 hours):**
    *   *Pros:* Low latency for subsequent user requests, lower query volume (costs) on authoritative DNS.
    *   *Cons:* Infrastructure modifications (changing server IP) propagate slowly across the globe.
*   **Short TTL (e.g., 60 seconds):**
    *   *Pros:* High agility. Allows fast routing updates and rapid failover.
    *   *Cons:* Elevated latency for users (requires recurrent resolutions), high query costs.

---

## 🏗️ System Design Context

### 1. GSLB (Global Server Load Balancing)
Authoritative DNS servers can inspect the incoming resolver's IP address (using EDNS Client Subnet client metadata) and dynamically return different IP records:
*   **Geolocation Routing:** Route European users to Dublin data centers and US users to Virginia data centers.
*   **Health Failover:** If data center A is offline, route DNS records to data center B.

### 2. Anycast DNS
Using Anycast routing, multiple physical DNS servers in different continents advertise the same IP address via BGP (Border Gateway Protocol). Routers send the packet to the topologically closest server. This keeps DNS resolution latency extremely low ($<10\text{ ms}$).
