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
- [Software Engineer Resume](https://newsletter.systemdesign.one/p/software-engineer-resume)

## 2. Fundamentals of System Design
### What is a system design?
- Introduction to system design
- [11 System Design Concepts Explained, Simply](https://newsletter.systemdesign.one/p/11-system-design-concepts-explained)
- [114 System Design Concepts - Part 1](https://newsletter.systemdesign.one/p/system-design-concepts)
- [114 System Design Concepts - Part 2](https://newsletter.systemdesign.one/p/system-design-core-concepts)
- [114 System Design Concepts - Part 3](https://newsletter.systemdesign.one/p/system-design-fundamentals)
- [The Entire Computer Science Stack, Explained In 51 Images](https://newsletter.systemdesign.one/p/computer-science-101)
- Mobile System Design Concepts - Part 1, 2

### Scalability
- What is scalability?
- Scalability vs Performance

### Availability
- What is availability?
- [What Is High Availability](https://newsletter.systemdesign.one/p/what-is-high-availability)
- How is availability measured?
- What causes low availability?
- How to achieve high availability?
- Types of failures in distributed systems?
- What are availability patterns?

### Reliability
- What is reliability and why it matters?
- SLAs, SLOs, and SLIs explained

### Fault tolerance
- What is Fault tolerance?
- Fault tolerance vs availability
- Graceful degradation strategies

### Consistency
- What is Consistency?
- A word on Consistency patterns.
- [Consistency Patterns](https://systemdesign.one/consistency-patterns/)
- Eventual consistency in distributed systems

### CAP theorem
- A word on CAP theorem.
- PACELC theorem explained

### Concurrency
- What is Concurrency?
- [Concurrency Is Not Parallelism](https://newsletter.systemdesign.one/p/concurrency-is-not-parallelism)
- Introduction to threads, deadlock & starvation.
- Race conditions and synchronization

### Idempotency
- What is idempotency and why it matters?
- Implementing idempotent operations

### Clock and time in distributed systems
- Why time is hard in distributed systems
- Introduction to logical clocks and NTP
- Vector clocks and causality

### Retry, timeout and backoff strategies
- Introduction to timeouts and retries
- What is exponential backoff?

### Networking
- Latency vs. through-put vs. bandwidth.
- Introduction to DNS (domain name system)
- [How DNS Works](https://newsletter.systemdesign.one/p/what-is-a-dns-server-and-how-does-it-work)
- TCP vs UDP in system design
- HTTP/HTTPS and REST principles
- [What Happens When You Type a URL Into Your Browser?](https://systemdesign.one/what-happens-when-you-type-url-into-your-browser/)
- [How to Troubleshoot if You Can’t Access a Particular Website?](https://systemdesign.one/how-to-troubleshoot-if-you-cannot-access-a-website/)

### A basic intro to core components
- Introduction to CDN
- Introduction to Load balancer
- Introduction to Caching
- Introduction to API Gateway
- [How API Gateway Works](https://newsletter.systemdesign.one/p/how-api-gateway-works)
- [API Gateway vs Load Balancer vs Reverse Proxy](https://newsletter.systemdesign.one/p/api-gateway-load-balancer-reverse-proxy)
- [Forward proxy vs Reverse proxy](https://newsletter.systemdesign.one/p/forward-proxy-vs-reverse-proxy)

### Service Discovery & Heartbeats
- What is service discovery?
- [Service Discovery](https://systemdesign.one/what-is-service-discovery/)
- How do heartbeats help detect failures?
- Service registry patterns

### Estimation & Back-of-envelope calculations
- System design estimation fundamentals
- Capacity planning basics
- QPS, storage, and bandwidth calculations

## 3. Architectural Patterns and Design Principles

### Monolithic vs Microservices
- Monolithic architecture pros and cons
- Introduction to microservices
- When to choose microservices vs monolith
- Service decomposition strategies
- [1 Simple Technique to Scale Microservices Architecture](https://newsletter.systemdesign.one/p/how-to-scale-microservices)

### Event-Driven Architecture
- What is event-driven architecture?
- Event sourcing patterns
- CQRS (Command Query Responsibility Segregation)
- Pub/Sub messaging patterns

### Resilience Patterns
- Circuit breaker pattern
- Bulkhead pattern
- Retry and timeout patterns
- Saga pattern for distributed transactions

### Migration Patterns
- Strangler fig pattern
- Blue-green deployment
- Canary deployment

### API Design Patterns
- RESTful API design principles
- GraphQL vs REST
- API versioning strategies
- [API Versioning](https://newsletter.systemdesign.one/p/api-versioning)
- API rate limiting and throttling
- [Best Practices for API Design](https://newsletter.systemdesign.one/p/best-practices-for-api-design)
- [How Does HTTPS Work](https://newsletter.systemdesign.one/p/how-does-https-work)
- [Must Know HTTP Headers](https://newsletter.systemdesign.one/p/http-headers)

### Advanced Communication Protocols
- [How Do Websockets Work](https://newsletter.systemdesign.one/p/how-do-websockets-work)
- [How Do Webhooks Work](https://newsletter.systemdesign.one/p/how-do-webhooks-work)
- [How Remote Procedure Call Works](https://newsletter.systemdesign.one/p/how-rpc-works)
- Serialization Formats: Protocol Buffers (Protobuf), Apache Thrift, Apache Avro

### Additional Patterns
- [Actor Model](https://newsletter.systemdesign.one/p/actor-model)
- [Cell Based Architecture](https://newsletter.systemdesign.one/p/cell-based-architecture)
- [How Sidecar Pattern Works](https://newsletter.systemdesign.one/p/sidecar-pattern)

## 4. Database Engineering Fundamentals

### ACID
- Atomicity.
- Consistency.
- Isolation.
- Durability.
- Understanding ACID properties with a live example.

### Database Transactions
- What are database transactions?
- Transaction isolation levels
- Phantom Reads.
- Dirty reads and non-repeatable reads
- Serialization vs. Repeatable Read
- [How Databases Keep Passwords Securely](https://newsletter.systemdesign.one/p/how-to-store-passwords-in-database)

### Database Fundamentals
- OLTP vs OLAP systems
- Database normalization
- Primary keys, foreign keys, and constraints

## 5. Database Scaling Concepts

### Database Indexing
- Indexing - data structure that powers your database.
- How database indexing actually works internally?
- B-tree and B+ tree indexes
- Hash indexes and bitmap indexes
- Composite indexes and index optimization

### Database Locking
- Introduction to database locking.
- Row-level vs table-level locking
- Deadlock detection and prevention

### Database Tuning & Optimizations
- What is database performance tuning?
- Query optimization techniques
- Database connection pooling
- Analyzing query execution plans

### Database Replication
- What is database replication?
- Master-slave replication
- Master-master replication
- Replication lag and consistency

### Database Partitioning
- What is database partitioning?
- Horizontal partitioning (sharding)
- Vertical partitioning
- Sharding strategies and challenges
- Consistent hashing for sharding
- [Consistent Hashing](https://systemdesign.one/consistent-hashing-explained/)

### Designing Database Schema
- Database schema design principles
- Choosing the right data types
- Database migration strategies

## 6. Database Internals

### Storage Engine Internals
- How tables and indexes are stored on disk?
- B-tree and LSM-tree storage structures
- Page layouts and buffer pool management
- Write-ahead logging (WAL) mechanisms
- [How Timsort Algorithm Works](https://newsletter.systemdesign.one/p/timsort-algorithm)

### Query Processing
- Query parsing and optimization
- Execution plan generation
- Join algorithms and optimization
- Cost-based optimization

### MySQL Internals
- InnoDB storage engine architecture
- Sorting algorithm behind ORDER BY query in MySQL?
- MySQL replication internals
- Transaction isolation in InnoDB

### NoSQL Database Internals
- MongoDB document storage and indexing
- Cassandra ring architecture and partitioning
- Redis data structures and persistence
- Elasticsearch inverted index structure

## 7. Data Storages (Databases)

### SQL Databases
- Introduction to SQL databases
- Popular SQL databases (MySQL, PostgreSQL, SQL Server)
- SQL transactions and ACID compliance
- When to choose SQL databases

### NoSQL Databases
- Introduction to NoSQL databases
- Document databases (MongoDB, CouchDB)
- Key-value stores (Redis, DynamoDB)
- Wide-column stores (Cassandra, HBase)
- Graph databases (Neo4j, Amazon Neptune)
- bonusSQL vs NoSQL - which, when, where & why?

### Specialized Databases
- Time Series Database - Everything you need to know
- Why to choose a time-series database?
- Search engines (Elasticsearch, Solr)
- In-memory databases (Redis, Memcached)

### Data Warehouses & Analytics
- What is a data warehouse?
- Columnar databases (Redshift, BigQuery)
- Data lakes vs data warehouses
- ETL vs ELT pipelines

### Storage Systems
- Introduction to blob storage (S3, Azure Blob)
- File storage systems
- Object storage vs block storage
- Distributed file systems (HDFS, GFS)

## 8. Asynchronous Communication Patterns

### Message Queue Fundamentals
- What are message queues?
- [How Message Queues Work](https://newsletter.systemdesign.one/p/what-is-a-message-queue)
- Synchronous vs asynchronous communication
- Point-to-point vs publish-subscribe
- Message ordering and delivery guarantees

### Popular Message Queue Systems
- Apache Kafka architecture and use cases
- [How Kafka Works](https://newsletter.systemdesign.one/p/how-kafka-works)
- RabbitMQ and AMQP protocol
- Amazon SQS and cloud message queues
- Redis pub/sub capabilities

### Message Processing Patterns
- Dead letter queues
- Message deduplication strategies
- Batch processing vs stream processing
- Consumer groups and load balancing

### Stream Processing
- Introduction to stream processing
- Apache Kafka Streams
- Apache Flink and real-time processing
- Windowing and aggregations

## 9. Caching Patterns and Strategies

### Caching Fundamentals
- What is caching and why it matters?
- Cache hit ratio and performance metrics
- Cache invalidation strategies
- Cache coherence and consistency

### Caching Patterns
- Cache-aside (lazy loading)
- Write-through caching
- Write-behind (write-back) caching
- Refresh-ahead caching
- [Top 5 Caching Patterns](https://newsletter.systemdesign.one/p/caching-patterns)

### Cache Technologies
- Redis deep dive
- [Redis Use Cases](https://newsletter.systemdesign.one/p/redis-use-cases)
- Memcached vs Redis
- Application-level caching
- Database query result caching

### Distributed Caching
- Distributed cache architecture
- Cache sharding and partitioning
- Cache replication strategies
- Handling cache failures

## 10. Load Balancing and Traffic Management

### Load Balancing Fundamentals
- What is load balancing?
- Layer 4 vs Layer 7 load balancing
- Hardware vs software load balancers
- Load balancer placement strategies

### Load Balancing Algorithms
- Round robin and weighted round robin
- Least connections algorithm
- IP hash and consistent hashing
- Least response time algorithm
- [How Load Balancing Algorithms Work](https://newsletter.systemdesign.one/p/load-balancing-algorithms)

### Health Checks & Failover
- Health check strategies
- Active vs passive health checks
- Failover and failback strategies
- Circuit breaker integration

### Advanced Traffic Management
- Sticky sessions and session affinity
- Rate limiting and throttling
- [Rate Limiting Strategies Explained](https://newsletter.systemdesign.one/p/rate-limiting)
- Traffic shaping and QoS
- Global load balancing

## 11. Advanced Distributed Systems

### Consensus Algorithms
- What is consensus in distributed systems?
- Raft consensus algorithm
- Paxos algorithm explained
- Byzantine fault tolerance

### Distributed Transactions
- Two-phase commit (2PC) protocol
- Three-phase commit (3PC) protocol
- Saga pattern for long-running transactions
- Eventual consistency patterns

### Coordination & Synchronization
- Distributed locks and leader election
- Apache Zookeeper coordination service
- etcd for distributed coordination
- Gossip protocols for information dissemination
- [Gossip Protocol](https://systemdesign.one/gossip-protocol/)
- [Hinted Handoff](https://systemdesign.one/hinted-handoff/)

### Partitioning & Replication
- Data partitioning strategies
- Consistent hashing deep dive
- Replication strategies (master-slave, master-master)
- Quorum-based systems
- [Distributed Systems Deep Dive](https://newsletter.systemdesign.one/p/distributed-systems)

## 12. Probabilistic & Advanced Data Structures
- [Bloom Filter](https://systemdesign.one/bloom-filters-explained/)
- [Quotient Filter](https://systemdesign.one/quotient-filter-explained/)
- HyperLogLog (Unique counting at scale)
- Count-Min Sketch (Frequency counting in streams)
- Geohashes & Quadtrees (Location-based services)
- Merkle Trees (Anti-entropy in Dynamo/Cassandra)
- Tries & Inverted Indexes (Search and Typeahead)

## 13. Performance Optimization

### Performance Fundamentals
- Performance metrics and KPIs
- Latency vs throughput trade-offs
- Performance testing strategies
- Capacity planning and forecasting

### Application Performance
- Code-level optimization techniques
- Memory management and garbage collection
- Asynchronous programming patterns
- Connection pooling and resource management

### Database Performance
- Query optimization and indexing strategies
- Database connection pooling
- Read replicas and write optimization
- Database partitioning for performance

### System Performance
- CPU, memory, and I/O optimization
- Network performance optimization
- Container and orchestration performance
- CDN and edge computing optimization

## 14. Modern Infrastructure and DevOps

### Containerization
- Docker fundamentals for system design
- Container orchestration with Kubernetes
- Microservices deployment patterns
- Service mesh architecture (Istio, Linkerd)

### Cloud Architecture
- Cloud-native application design
- Serverless architecture patterns
- Multi-cloud and hybrid cloud strategies
- Edge computing and CDN integration
- [15 Pitfalls That Break Cloud Systems](https://newsletter.systemdesign.one/p/cloud-system-design)

### Deployment Strategies
- CI/CD pipeline design
- Blue-green deployment
- Canary deployment strategies
- Rolling deployment and rollback
- [Deployment Patterns](https://newsletter.systemdesign.one/p/deployment-patterns)

### Infrastructure as Code & Practices
- Infrastructure automation principles
- Configuration management
- Auto-scaling and resource management
- Disaster recovery and backup strategies
- [21 Git Commands](https://newsletter.systemdesign.one/p/commands-in-git)
- [How to Scale Code Reviews](https://newsletter.systemdesign.one/p/how-to-do-code-review)
- [Code Review Best Practices](https://newsletter.systemdesign.one/p/code-review-best-practices)
- [Stacked Diffs](https://newsletter.systemdesign.one/p/stacked-diffs)

## 15. Security

### Authentication & Authorization
- Authentication vs authorization
- OAuth 2.0 and OpenID Connect
- JWT tokens and session management
- [How JWT Works](https://newsletter.systemdesign.one/p/how-jwt-works)
- Single Sign-On (SSO) systems

### API Security
- API authentication strategies
- API keys vs tokens
- Rate limiting for security
- Input validation and sanitization
- [Best Practices for API Security](https://newsletter.systemdesign.one/p/api-security-best-practices)

### Security Patterns
- Defense in depth strategy
- Zero trust architecture
- Principle of least privilege
- Security by design

### Common Security Threats
- DDoS attacks and mitigation
- SQL injection prevention
- Cross-site scripting (XSS) prevention
- Data encryption at rest and in transit
- [Cybersecurity Terms Every Software Engineer Must Know](https://newsletter.systemdesign.one/p/cybersecurity-fundamentals)

## 16. Monitoring and Observability

### Monitoring Fundamentals
- What is observability?
- Metrics, logs, and traces (three pillars)
- Monitoring vs observability
- SLIs, SLOs, and error budgets

### Metrics & Alerting
- Application metrics and KPIs
- Infrastructure monitoring
- Alerting strategies and alert fatigue
- Dashboards and visualization

### Logging Strategies
- Structured logging best practices
- Centralized logging architecture
- Log aggregation and analysis
- Log retention and storage

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

## 18. Real-World System Design Case Studies & Practice
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
- [Amazon Frugal Architecture Explained](https://newsletter.systemdesign.one/p/frugal-architecture)

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

## 19. Software White Papers
- [Amazon Dynamo](https://newsletter.systemdesign.one/p/amazon-dynamo-architecture)
- [Google Spanner](https://newsletter.systemdesign.one/p/cloud-spanner-database)
- [Meta Serverless Architecture: XFaaS](https://newsletter.systemdesign.one/p/serverless-architecture)
