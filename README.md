# Comprehensive System Design Notes

A complete guide to system design, combining concepts from [The System Design Academy](https://www.systemdesignacademy.com/) and [System Design One (systemdesign.one)](https://github.com/systemdesign42/system-design-academy).

## 1. System Design Interview Methodology
- [System Design Interview Framework](https://newsletter.systemdesign.one/p/how-to-prepare-for-system-design-interview)
- Requirement Gathering: Functional vs. Non-Functional requirements
- [Back of the Envelope](https://systemdesign.one/back-of-the-envelope/)
- Defining the System Interface (API Design)
- High-Level Design & Component Diagram
- Deep Dives & Bottleneck Identification
- [System Design Interview Cheat Sheet](https://systemdesign.one/system-design-interview-cheatsheet/)
- [7 Simple Ways to Fail System Design Interview](https://newsletter.systemdesign.one/p/design-system-newsletter)
- [Software Engineer Interview Learning Resources](https://systemdesign.one/software-engineer-interview-learning-resources/)
- [Behavioral Interview Playbook](https://newsletter.systemdesign.one/p/common-behavioral-interview-questions)
- [Mobile System Design Interview Framework](https://newsletter.systemdesign.one/p/mobile-system-design-interview)

## 2. Fundamentals of System Design
### What is system design?
- Introduction to system design
- [11 System Design Concepts Explained, Simply](https://newsletter.systemdesign.one/p/11-system-design-concepts-explained)
- [114 System Design Concepts - Part 1](https://newsletter.systemdesign.one/p/system-design-concepts)
- [114 System Design Concepts - Part 2](https://newsletter.systemdesign.one/p/system-design-core-concepts)
- [114 System Design Concepts - Part 3](https://newsletter.systemdesign.one/p/system-design-fundamentals)
- [The Entire Computer Science Stack, Explained In 51 Images](https://newsletter.systemdesign.one/p/computer-science-101)

### Scalability, Availability & Reliability
- What is scalability?
- Scalability vs Performance
- What is availability?
- [What Is High Availability](https://newsletter.systemdesign.one/p/what-is-high-availability)
- How is availability measured?
- What causes low availability?
- How to achieve high availability?
- Types of failures in distributed systems?
- What are availability patterns?
- What is reliability and why it matters?
- SLAs, SLOs, and SLIs explained

### Fault Tolerance & Consistency
- What is Fault tolerance?
- Fault tolerance vs availability
- Graceful degradation strategies
- What is Consistency?
- [Consistency Patterns](https://systemdesign.one/consistency-patterns/)
- Eventual consistency in distributed systems

### CAP & PACELC Theorems
- A word on CAP theorem
- PACELC theorem explained

## 3. Networking Fundamentals
- Latency vs. through-put vs. bandwidth
- [How DNS Works](https://newsletter.systemdesign.one/p/what-is-a-dns-server-and-how-does-it-work)
- TCP vs UDP in system design
- [What Happens When You Type a URL Into Your Browser?](https://systemdesign.one/what-happens-when-you-type-url-into-your-browser/)
- [How to Troubleshoot if You Can’t Access a Particular Website?](https://systemdesign.one/how-to-troubleshoot-if-you-cannot-access-a-website/)

## 4. API Design & Communication Protocols
### API Design Patterns
- [Must Know HTTP Headers](https://newsletter.systemdesign.one/p/http-headers)
- [How Does HTTPS Work](https://newsletter.systemdesign.one/p/how-does-https-work)
- RESTful API design principles
- GraphQL vs REST
- [API Versioning](https://newsletter.systemdesign.one/p/api-versioning)
- [Best Practices for API Design](https://newsletter.systemdesign.one/p/best-practices-for-api-design)
- API rate limiting and throttling

### Advanced Communication Protocols
- [How Do Websockets Work](https://newsletter.systemdesign.one/p/how-do-websockets-work)
- [How Do Webhooks Work](https://newsletter.systemdesign.one/p/how-do-webhooks-work)
- [How Remote Procedure Call Works](https://newsletter.systemdesign.one/p/how-rpc-works)
- Serialization Formats: Protocol Buffers (Protobuf), Apache Thrift, Apache Avro

## 5. Basic Intro to Core Components
- Introduction to CDN
- Introduction to Load balancer
- Introduction to Caching
- [How API Gateway Works](https://newsletter.systemdesign.one/p/how-api-gateway-works)
- [API Gateway vs Load Balancer vs Reverse Proxy](https://newsletter.systemdesign.one/p/api-gateway-load-balancer-reverse-proxy)
- [Forward proxy vs Reverse proxy](https://newsletter.systemdesign.one/p/forward-proxy-vs-reverse-proxy)

## 6. Database Engineering Fundamentals
### ACID & Transactions
- Atomicity, Consistency, Isolation, Durability
- What are database transactions?
- Transaction isolation levels (Phantom Reads, Dirty reads, Serialization)
- [How Databases Keep Passwords Securely](https://newsletter.systemdesign.one/p/how-to-store-passwords-in-database)

### Database Fundamentals
- OLTP vs OLAP systems
- Database normalization
- Primary keys, foreign keys, and constraints
- Designing Database Schema (principles, data types, migrations)

## 7. Data Storages (Databases)
- SQL Databases (MySQL, PostgreSQL, SQL Server)
- NoSQL Databases (MongoDB, CouchDB, Redis, DynamoDB, Cassandra, HBase, Neo4j)
- SQL vs NoSQL - which, when, where & why?
- Time Series Database
- Data Warehouses & Analytics (Redshift, BigQuery, ETL vs ELT)
- Distributed file systems (HDFS, GFS, S3, Azure Blob)

## 8. Load Balancing and Traffic Management
- [How Load Balancing Algorithms Work](https://newsletter.systemdesign.one/p/load-balancing-algorithms)
- [Rate Limiting Strategies Explained](https://newsletter.systemdesign.one/p/rate-limiting)
- Health check strategies (Active vs passive)
- Failover and failback strategies
- Sticky sessions and session affinity

## 9. Caching Patterns and Strategies
- [Top 5 Caching Patterns](https://newsletter.systemdesign.one/p/caching-patterns)
- Cache-aside, Write-through, Write-behind, Refresh-ahead
- [Redis Use Cases](https://newsletter.systemdesign.one/p/redis-use-cases)
- Memcached vs Redis
- Distributed cache architecture (sharding, partitioning)

## 10. Asynchronous Communication Patterns
- [How Message Queues Work](https://newsletter.systemdesign.one/p/what-is-a-message-queue)
- [How Kafka Works](https://newsletter.systemdesign.one/p/how-kafka-works)
- RabbitMQ and AMQP protocol
- Dead letter queues
- Message deduplication strategies

## 11. Database Scaling Concepts
- [Consistent Hashing](https://systemdesign.one/consistent-hashing-explained/)
- Database Indexing (B-tree, B+ tree, Hash indexes, Bitmap)
- Database Locking (Row-level vs table-level, Deadlocks)
- Database Replication (Master-slave, Master-master)
- Database Partitioning (Horizontal/Sharding, Vertical)

## 12. Architectural Patterns and Design Principles
- Monolithic vs Microservices
- [1 Simple Technique to Scale Microservices Architecture](https://newsletter.systemdesign.one/p/how-to-scale-microservices)
- Event-Driven Architecture (Event sourcing, CQRS)
- Resilience Patterns (Circuit breaker, Bulkhead, Retry/timeout)
- [Actor Model](https://newsletter.systemdesign.one/p/actor-model)
- [Cell Based Architecture](https://newsletter.systemdesign.one/p/cell-based-architecture)
- [How Sidecar Pattern Works](https://newsletter.systemdesign.one/p/sidecar-pattern)

## 13. Probabilistic & Advanced Data Structures
- [Bloom Filter](https://systemdesign.one/bloom-filters-explained/)
- [Quotient Filter](https://systemdesign.one/quotient-filter-explained/)
- HyperLogLog (Unique counting at scale)
- Count-Min Sketch (Frequency counting in streams)
- Geohashes & Quadtrees (Location-based services)
- Merkle Trees (Anti-entropy in Dynamo/Cassandra)
- Tries & Inverted Indexes (Search and Typeahead)

## 14. Advanced Distributed Systems
- [Distributed Systems Deep Dive](https://newsletter.systemdesign.one/p/distributed-systems)
- [Concurrency Is Not Parallelism](https://newsletter.systemdesign.one/p/concurrency-is-not-parallelism)
- [Service Discovery](https://systemdesign.one/what-is-service-discovery/)
- [Gossip Protocol](https://systemdesign.one/gossip-protocol/)
- [Hinted Handoff](https://systemdesign.one/hinted-handoff/)
- Consensus & Coordination (Raft, Paxos, Zookeeper, etcd)

## 15. Global Architecture & Multi-Data Center Design
- Multi-Data Center deployments (Active-Active vs. Active-Passive)
- Edge computing and advanced CDN architectures

## 16. Database Internals
- B-tree and LSM-tree storage structures
- Write-ahead logging (WAL) mechanisms
- Query parsing and execution plan generation
- Transaction isolation in InnoDB
- [How Timsort Algorithm Works](https://newsletter.systemdesign.one/p/timsort-algorithm)

## 17. Search & AI System Design (AI Engineering)
- [How AI Agents Work](https://newsletter.systemdesign.one/p/ai-agents-explained)
- [How to design your own AI agent](https://newsletter.systemdesign.one/p/how-do-ai-agents-work)
- [11 AI Concepts Explained, Simply](https://newsletter.systemdesign.one/p/ai-concepts)
- [AI Coding Workflow](https://newsletter.systemdesign.one/p/ai-coding-workflow)
- [What is Context Engineering?](https://newsletter.systemdesign.one/p/what-is-context-engineering)
- [Context Engineering vs Prompt Engineering](https://newsletter.systemdesign.one/p/context-engineering-vs-prompt-engineering)
- [How ChatGPT Apps Work](https://newsletter.systemdesign.one/p/apps-in-chatgpt)
- [Design a personal AI chat assistant](https://newsletter.systemdesign.one/p/ai-chat-assistant)
- [Agentic Design Patterns](https://newsletter.systemdesign.one/p/agentic-design-patterns)
- [29 LLM Evaluation Concepts](https://newsletter.systemdesign.one/p/llm-evals)
- [Everything You Need to Know to Design GenAI Systems From Scratch](https://newsletter.systemdesign.one/p/generative-ai-system-design)
- [LLM Concepts, Simply Explained](https://newsletter.systemdesign.one/p/llm-concepts)
- [MCP - A Deep Dive](https://newsletter.systemdesign.one/p/how-mcp-works)
- [Multi-Agent Architectures](https://newsletter.systemdesign.one/p/multi-agent-system)
- [How ML Systems Actually Work](https://newsletter.systemdesign.one/p/machine-learning-system-design-interview)
- [AI Agents: State, Memory, Consistency](https://newsletter.systemdesign.one/p/ai-agent-memory)
- [What Is Reinforcement Learning](https://newsletter.systemdesign.one/p/what-is-reinforcement-learning)
- [How RAG Works](https://newsletter.systemdesign.one/p/how-rag-works)
- [Vector Database - A Deep Dive](https://newsletter.systemdesign.one/p/what-is-a-vector-database)

## 18. Performance Optimization
- [21 Frontend System Design Concepts](https://newsletter.systemdesign.one/p/frontend-system-design)
- [Micro Frontends](https://newsletter.systemdesign.one/p/micro-frontends)
- Component Optimization
- Database Performance

## 19. Modern Infrastructure and DevOps
- [15 Pitfalls That Break Cloud Systems](https://newsletter.systemdesign.one/p/cloud-system-design)
- [Deployment Patterns](https://newsletter.systemdesign.one/p/deployment-patterns)
- [21 Git Commands](https://newsletter.systemdesign.one/p/commands-in-git)
- [How to Scale Code Reviews](https://newsletter.systemdesign.one/p/how-to-do-code-review)
- [Code Review Best Practices](https://newsletter.systemdesign.one/p/code-review-best-practices)
- [Stacked Diffs](https://newsletter.systemdesign.one/p/stacked-diffs)

## 20. Security
- [Cybersecurity Terms Every Software Engineer Must Know](https://newsletter.systemdesign.one/p/cybersecurity-fundamentals)
- [Best Practices for API Security](https://newsletter.systemdesign.one/p/api-security-best-practices)
- [How JWT Works](https://newsletter.systemdesign.one/p/how-jwt-works)

## 21. Real-World System Design Case Studies & Practice
### Mock Interviews
- [Design Airbnb](https://newsletter.systemdesign.one/p/airbnb-system-design)
- [Design ChatGPT](https://newsletter.systemdesign.one/p/chatgpt-system-design)
- [Design Spotify](https://newsletter.systemdesign.one/p/spotify-system-design)
- [Design Web Crawler and Search Engine](https://newsletter.systemdesign.one/p/web-crawler-system-design)
- [Design Amazon S3](https://newsletter.systemdesign.one/p/aws-s3-system-design)
- [Design Twitter/X Timeline](https://newsletter.systemdesign.one/p/system-design-interview-twitter)
- [Design WhatsApp](https://newsletter.systemdesign.one/p/whatsapp-system-design) | [Part 2](https://newsletter.systemdesign.one/p/design-a-chat-system)
- [Design YouTube](https://newsletter.systemdesign.one/p/youtube-system-design)
- [Design a Distributed Counter](https://systemdesign.one/distributed-counter-system-design/)
- [Design Real Time Presence Platform](https://systemdesign.one/real-time-presence-platform-system-design/)
- [Design Real-Time Gaming Leaderboard](https://systemdesign.one/leaderboard-system-design/)
- [Design Real-Time Live Comments](https://systemdesign.one/live-comment-system-design/)
- [Design Stock Exchange - Part 1](https://newsletter.systemdesign.one/p/stock-exchange-system-design) | [Part 2](https://newsletter.systemdesign.one/p/disruptor-pattern) | [Part 3](https://newsletter.systemdesign.one/p/system-design-stock-exchange)

### Architecture Deep Dives
- [How Amazon Lambda Works](https://newsletter.systemdesign.one/p/how-does-aws-lambda-work)
- [How Amazon S3 Works](https://newsletter.systemdesign.one/p/s3-architecture)
- [How Do Apple AirTags Work](https://newsletter.systemdesign.one/p/how-do-airtags-work)
- [How Does Bluesky Work](https://newsletter.systemdesign.one/p/how-does-bluesky-work)
- [How Google Search Works](https://newsletter.systemdesign.one/p/search-engine-architecture)
- [How Google Docs Works](http://newsletter.systemdesign.one/p/how-does-google-docs-work)
- [How Does Netflix Work?](https://newsletter.systemdesign.one/p/how-does-netflix-work)
- [How Reddit Works](https://newsletter.systemdesign.one/p/reddit-architecture)
- [Slack Architecture](https://systemdesign.one/slack-architecture/)
- [Pastebin](https://systemdesign.one/system-design-pastebin/)
- [Bitly URL Shortener Architecture](https://systemdesign.one/url-shortening-system-design/)
- [Wechat Architecture](https://newsletter.systemdesign.one/p/chat-application-architecture)

### Scale & Scaling Strategies
- [How to Scale an App to 10 Million Users on AWS](https://newsletter.systemdesign.one/p/aws-scale)
- [How to Scale an App to 100 Million Users on GCP](https://newsletter.systemdesign.one/p/google-cloud-scalability)
- [How Airbnb Adopted HTTP Streaming](https://newsletter.systemdesign.one/p/what-is-critical-rendering-path)
- [Amazon Prime Video Microservices Top Failure](https://newsletter.systemdesign.one/p/prime-video-microservices)
- [How Apple Pay Handles 41 Million Transactions](https://newsletter.systemdesign.one/p/how-does-apple-pay-work)
- [How Canva Supports Real-Time Collaboration](https://newsletter.systemdesign.one/p/rsocket)
- [How Cloudflare Supports 55 Million Requests/Sec with 15 Postgres Clusters](https://newsletter.systemdesign.one/p/postgresql-scalability)
- [How Disney+ Hotstar Delivered 5 Billion Emojis](https://newsletter.systemdesign.one/p/hotstar-architecture)
- [How Disney+ Hotstar Scaled to 25 Million Concurrent Users](https://newsletter.systemdesign.one/p/hotstar-scaling)
- [How Disney+ Scaled to 11 Million Users](https://newsletter.systemdesign.one/p/disney-architecture)
- [How Discord Boosts Performance With Code-Splitting](https://newsletter.systemdesign.one/p/what-is-code-splitting-in-react)
- [How Dropbox Scaled to 100 Thousand Users](https://newsletter.systemdesign.one/p/dropbox-architecture)
- [How Facebook Scaled Live Video](https://newsletter.systemdesign.one/p/live-streaming-architecture)
- [How Facebook Supports a Billion Users via Software Load Balancer](https://newsletter.systemdesign.one/p/facebook-load-balancer)
- [How Figma Scaled Postgres to 4M Users](https://newsletter.systemdesign.one/p/postgres-scale)
- [How Giphy Delivers 10 Billion GIFs](https://newsletter.systemdesign.one/p/cdn-explained)
- [How Hashnode Generates Feed](https://newsletter.systemdesign.one/p/feed-architecture)
- [How Halo Scaled to 11.6 Million Users](https://newsletter.systemdesign.one/p/saga-design-pattern)
- [How Instagram Scaled to 2.5 Billion Users](https://newsletter.systemdesign.one/p/instagram-infrastructure)
- [How Khan Academy Scaled](https://newsletter.systemdesign.one/p/khan-academy-architecture)
- [How LinkedIn Scaled to 930 Million Users](https://newsletter.systemdesign.one/p/scalable-software-architecture)
- [How LinkedIn Adopted Protocol Buffers](https://newsletter.systemdesign.one/p/protocol-buffers-vs-json)
- [Tech Stack Evolution at Levels fyi](https://newsletter.systemdesign.one/p/levels-fyi-google-sheets)
- [How Lyft Support Rides](https://newsletter.systemdesign.one/p/lyft-engineering)
- [How McDonald’s Food Delivery Platform Handles 20k Orders/Sec](https://newsletter.systemdesign.one/p/mcdonalds-architecture)
- [How Meta Achieves 99.99999999% Cache Consistency](https://newsletter.systemdesign.one/p/cache-consistency)
- [Microservices Lessons From Netflix](https://newsletter.systemdesign.one/p/netflix-microservices)
- [How Netflix Uses Chaos Engineering](https://newsletter.systemdesign.one/p/chaos-engineering)
- [How PayPal Supports a Billion Transactions With Only 8 VMs](https://newsletter.systemdesign.one/p/actor-model)
- [How Quora Shards MySQL](https://newsletter.systemdesign.one/p/mysql-sharding)
- [How Razorpay Scaled to Handle Flash Sales](https://newsletter.systemdesign.one/p/payment-gateway-architecture)
- [Virtual Waiting Room Architecture at SeatGeek](https://newsletter.systemdesign.one/p/virtual-waiting-room)
- [How Shopify Handles Flash Sales at 32M Requests/Min](https://newsletter.systemdesign.one/p/shopify-flash-sale)
- [How Shopify Handled 30TB per Minute With Modular Monolith](https://newsletter.systemdesign.one/p/modular-monolith)
- [How Stripe Does Rate Limiting](https://newsletter.systemdesign.one/p/rate-limiter)
- [How Stripe Prevents Double Payment Using Idempotent API](https://newsletter.systemdesign.one/p/idempotent-api)
- [Tumblr Database Migration Strategy](https://newsletter.systemdesign.one/p/how-to-migrate-a-mysql-database)
- [6 Proven Guidelines on Open Sourcing From Tumblr](https://newsletter.systemdesign.one/p/open-source-guidelines)
- [How Tinder Scaled to 1.6 Billion Swipes per Day](https://newsletter.systemdesign.one/p/tinder-architecture)
- [How Uber Computes ETA](https://newsletter.systemdesign.one/p/uber-eta)
- [How Uber Finds Nearby Drivers](https://newsletter.systemdesign.one/p/how-does-uber-find-nearby-drivers)
- [How Uber Payment System Handles 30 Million Transactions](https://newsletter.systemdesign.one/p/payment-system-design)
- [8 Reasons WhatsApp Supported 50 Billion Messages With Only 32 Engineers](https://newsletter.systemdesign.one/p/whatsapp-engineering)
- [11 Reasons YouTube Supported 100 Million Views With Only 9 Engineers](https://newsletter.systemdesign.one/p/youtube-scalability)
- [How YouTube Supported 2.49 Billion Users With MySQL](https://newsletter.systemdesign.one/p/vitess-mysql)
- [5 Reasons Zoom Supported 300 Million Video Calls a Day](https://newsletter.systemdesign.one/p/zoom-architecture)
- [How Zapier Automates Billions of Tasks](https://newsletter.systemdesign.one/p/zapier-architecture)
- [How Nginx Supports 1 Million Concurrent Connections](https://newsletter.systemdesign.one/p/how-does-nginx-work)

## 22. Software White Papers
- [Amazon Dynamo](https://newsletter.systemdesign.one/p/amazon-dynamo-architecture)
- [Google Spanner](https://newsletter.systemdesign.one/p/cloud-spanner-database)
- [Meta Serverless Architecture: XFaaS](https://newsletter.systemdesign.one/p/serverless-architecture)
