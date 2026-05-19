# Comprehensive System Design Notes

## 🗺️ 3-Month Interview Preparation Roadmap

Follow this 12-week structured curriculum using the resources linked below.

### Month 1: Fundamentals & Databases
* **Week 1: Core Fundamentals & Networking**
  * Focus on: Scalability, Availability, Reliability, Fault Tolerance, CAP Theorem, and basic Networking (DNS, TCP/UDP, Latency vs Throughput).
* **Week 2: Core Infrastructure Components**
  * Focus on: Load Balancing, Reverse Proxies, CDNs, and API Gateways.
* **Week 3: Database Engineering 101**
  * Focus on: SQL vs NoSQL, ACID properties, Database Transactions, and Schema Design.
* **Week 4: Database Scaling at Large**
  * Focus on: Database Replication (Master-Slave/Master-Master), Partitioning (Sharding & Consistent Hashing), and Database Indexing.

### Month 2: Architecture & Communication
* **Week 5: System Architecture Patterns**
  * Focus on: Monoliths vs Microservices, Event-Driven Architecture, CQRS, and Serverless architectures.
* **Week 6: Caching Patterns & Strategies**
  * Focus on: Caching concepts (Read-through, Write-through, Write-behind), Eviction Policies (LRU, LFU), and Distributed Caching systems.
* **Week 7: Asynchronous Communication**
  * Focus on: Message Brokers, Pub/Sub mechanisms, Event Sourcing, and Message Queues (Kafka, RabbitMQ).
* **Week 8: API Design & Advanced Protocols**
  * Focus on: REST vs GraphQL vs gRPC, WebSockets, Long Polling, and Webhooks.

### Month 3: Advanced Systems, Security & Practice
* **Week 9: Advanced Distributed Systems**
  * Focus on: Consensus Algorithms (Paxos, Raft), Service Discovery, Distributed Locks, Rate Limiting, and Resilience Patterns (Circuit Breakers).
* **Week 10: Infrastructure, Security & Observability**
  * Focus on: Containerization (Docker, K8s), Authentication/Authorization (OAuth 2.0, SSO), SSL/mTLS, and the three pillars of Observability.
* **Week 11: Trade-offs & Deep Dives**
  * Focus on: System Design Trade-offs matrices, Probabilistic Data Structures (Bloom Filters), and reading classic Engineering White Papers.
* **Week 12: Mock Interviews & Real-World Case Studies**
  * Focus on: Interview Methodology, Back-of-the-envelope calculations, and practicing Mock Interviews (URL Shortener, Twitter, WhatsApp, Uber, Netflix).

---



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
- [Performance vs scalability (Donne Martin)](https://github.com/donnemartin/system-design-primer#performance-vs-scalability)
- [Scalability (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#scalability)
- [Scalability](https://algomaster.io/learn/system-design/scalability)
- What is scalability?
- Scalability vs Performance

### Availability
- [Availability patterns (Donne Martin)](https://github.com/donnemartin/system-design-primer#availability-patterns)
- [Availability in numbers (Donne Martin)](https://github.com/donnemartin/system-design-primer#availability-in-numbers)
- [Availability (AlgoMaster)](https://algomaster.io/learn/system-design/availability)
- [Availability (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#availability)
- What is availability?
- [What Is High Availability](https://newsletter.systemdesign.one/p/what-is-high-availability)
- How is availability measured?
- What causes low availability?
- How to achieve high availability?
- Types of failures in distributed systems?
- What are availability patterns?

### Reliability
- [Reliability (AlgoMaster)](https://algomaster.io/learn/system-design/reliability)
- [SPOF (AlgoMaster)](https://algomaster.io/learn/system-design/single-point-of-failure-spof)
- What is reliability and why it matters?
- SLAs, SLOs, and SLIs explained

### Fault tolerance
- [Fault Tolerance (AlgoMaster)](https://www.cockroachlabs.com/blog/what-is-fault-tolerance/)
- What is Fault tolerance?
- Fault tolerance vs availability
- Graceful degradation strategies

### Consistency
- What is Consistency?
- A word on Consistency patterns.
- [Consistency Patterns](https://systemdesign.one/consistency-patterns/)
- Eventual consistency in distributed systems

### CAP theorem
- [Availability vs consistency (Donne Martin)](https://github.com/donnemartin/system-design-primer#availability-vs-consistency)
- [CAP theorem (Donne Martin)](https://github.com/donnemartin/system-design-primer#cap-theorem)
- [Consistency patterns (Donne Martin)](https://github.com/donnemartin/system-design-primer#consistency-patterns)
- [CAP Theorem (AlgoMaster)](https://algomaster.io/learn/system-design/cap-theorem)
- [CAP theorem (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#cap-theorem)
- [PACELC Theorem (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#pacelc-theorem)
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
- [Latency vs throughput (Donne Martin)](https://github.com/donnemartin/system-design-primer#latency-vs-throughput)
- [Domain name system (Donne Martin)](https://github.com/donnemartin/system-design-primer#domain-name-system)
- [Transmission control protocol (TCP) (Donne Martin)](https://github.com/donnemartin/system-design-primer#transmission-control-protocol-tcp)
- [User datagram protocol (UDP) (Donne Martin)](https://github.com/donnemartin/system-design-primer#user-datagram-protocol-udp)
- [Latency vs Throughput vs Bandwidth (AlgoMaster)](https://algomaster.io/learn/system-design/latency-vs-throughput)
- [IP (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#ip)
- [OSI Model (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#osi-model)
- [TCP and UDP (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#tcp-and-udp)
- [OSI Model](https://algomaster.io/learn/system-design/osi)
- [IP Addresses](https://algomaster.io/learn/system-design/ip-address)
- [Domain Name System (DNS)](https://blog.algomaster.io/p/how-dns-actually-works)
- [Proxy vs Reverse Proxy](https://blog.algomaster.io/p/proxy-vs-reverse-proxy-explained)
- [HTTP/HTTPS](https://algomaster.io/learn/system-design/http-https)
- [TCP vs UDP](https://algomaster.io/learn/system-design/tcp-vs-udp)
- [Load Balancing](https://blog.algomaster.io/p/load-balancing-algorithms-explained-with-code)
- [Checksums](https://algomaster.io/learn/system-design/checksums)
- Latency vs. through-put vs. bandwidth.
- Introduction to DNS (domain name system)
- [How DNS Works](https://newsletter.systemdesign.one/p/what-is-a-dns-server-and-how-does-it-work)
- TCP vs UDP in system design
- HTTP/HTTPS and REST principles
- [What Happens When You Type a URL Into Your Browser?](https://systemdesign.one/what-happens-when-you-type-url-into-your-browser/)
- [How to Troubleshoot if You Can’t Access a Particular Website?](https://systemdesign.one/how-to-troubleshoot-if-you-cannot-access-a-website/)

### A basic intro to core components
- [Content delivery network (Donne Martin)](https://github.com/donnemartin/system-design-primer#content-delivery-network)
- [Load balancer (Donne Martin)](https://github.com/donnemartin/system-design-primer#load-balancer)
- [Reverse proxy (web server) (Donne Martin)](https://github.com/donnemartin/system-design-primer#reverse-proxy-web-server)
- [Load Balancing (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#load-balancing)
- [Clustering (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#clustering)
- [Proxy (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#proxy)
- Introduction to CDN
- Introduction to Load balancer
- Introduction to Caching
- Introduction to API Gateway
- [How API Gateway Works](https://newsletter.systemdesign.one/p/how-api-gateway-works)
- [API Gateway vs Load Balancer vs Reverse Proxy](https://newsletter.systemdesign.one/p/api-gateway-load-balancer-reverse-proxy)
- [Forward proxy vs Reverse proxy](https://newsletter.systemdesign.one/p/forward-proxy-vs-reverse-proxy)

### Service Discovery & Heartbeats
- [Service discovery (Donne Martin)](https://github.com/donnemartin/system-design-primer#service-discovery)
- [Service Discovery (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#service-discovery)
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
- [Application layer (Donne Martin)](https://github.com/donnemartin/system-design-primer#application-layer)
- [Microservices (Donne Martin)](https://github.com/donnemartin/system-design-primer#microservices)
- [Monoliths and Microservices (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#monoliths-and-microservices)
- Monolithic architecture pros and cons
- Introduction to microservices
- When to choose microservices vs monolith
- Service decomposition strategies
- [1 Simple Technique to Scale Microservices Architecture](https://newsletter.systemdesign.one/p/how-to-scale-microservices)

### Event-Driven Architecture
- [Event-Driven Architecture (EDA) (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#event-driven-architecture-eda)
- [Event Sourcing (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#event-sourcing)
- [Command and Query Responsibility Segregation (CQRS) (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#command-and-query-responsibility-segregation-cqrs)
- What is event-driven architecture?
- Event sourcing patterns
- CQRS (Command Query Responsibility Segregation)
- Pub/Sub messaging patterns

### Resilience Patterns
- [Circuit breaker (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#circuit-breaker)
- Circuit breaker pattern
- Bulkhead pattern
- Retry and timeout patterns
- Saga pattern for distributed transactions

### Migration Patterns
- Strangler fig pattern
- Blue-green deployment
- Canary deployment

### API Design Patterns
- [APIs](https://algomaster.io/learn/system-design/what-is-an-api)
- [API Gateway](https://blog.algomaster.io/p/what-is-an-api-gateway)
- [REST vs GraphQL](https://blog.algomaster.io/p/rest-vs-graphql)
- [WebSockets](https://blog.algomaster.io/p/websockets)
- [Webhooks](https://algomaster.io/learn/system-design/webhooks)
- [Idempotency](https://algomaster.io/learn/system-design/idempotency)
- [Rate limiting](https://blog.algomaster.io/p/rate-limiting-algorithms-explained-with-code)
- [API Design](https://abdulrwahab.medium.com/api-architecture-best-practices-for-designing-rest-apis-bf907025f5f)
- RESTful API design principles
- GraphQL vs REST
- API versioning strategies
- [API Versioning](https://newsletter.systemdesign.one/p/api-versioning)
- API rate limiting and throttling
- [Best Practices for API Design](https://newsletter.systemdesign.one/p/best-practices-for-api-design)
- [How Does HTTPS Work](https://newsletter.systemdesign.one/p/how-does-https-work)
- [Must Know HTTP Headers](https://newsletter.systemdesign.one/p/http-headers)

### Advanced Communication Protocols
- [Remote procedure call (RPC) (Donne Martin)](https://github.com/donnemartin/system-design-primer#remote-procedure-call-rpc)
- [Representational state transfer (REST) (Donne Martin)](https://github.com/donnemartin/system-design-primer#representational-state-transfer-rest)
- [REST, GraphQL, gRPC (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#rest-graphql-grpc)
- [Long polling, WebSockets, Server-Sent Events (SSE) (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#long-polling-websockets-server-sent-events-sse)
- [How Do Websockets Work](https://newsletter.systemdesign.one/p/how-do-websockets-work)
- [How Do Webhooks Work](https://newsletter.systemdesign.one/p/how-do-webhooks-work)
- [How Remote Procedure Call Works](https://newsletter.systemdesign.one/p/how-rpc-works)
- Serialization Formats: Protocol Buffers (Protobuf), Apache Thrift, Apache Avro

### Additional Patterns
- [Client-Server Architecture](https://algomaster.io/learn/system-design/client-server-architecture)
- [Microservices Architecture](https://medium.com/hashmapinc/the-what-why-and-how-of-a-microservices-architecture-4179579423a9)
- [Serverless Architecture](https://blog.algomaster.io/p/2edeb23b-cfa5-4b24-845e-3f6f7a39d162)
- [Event-Driven Architecture](https://www.confluent.io/learn/event-driven-architecture/)
- [Peer-to-Peer (P2P) Architecture](https://www.spiceworks.com/tech/networking/articles/what-is-peer-to-peer/)
- [Actor Model](https://newsletter.systemdesign.one/p/actor-model)
- [Cell Based Architecture](https://newsletter.systemdesign.one/p/cell-based-architecture)
- [How Sidecar Pattern Works](https://newsletter.systemdesign.one/p/sidecar-pattern)

## 4. Database Engineering Fundamentals

### Database Fundamentals
- [Database (Donne Martin)](https://github.com/donnemartin/system-design-primer#database)
- [Relational database management system (RDBMS) (Donne Martin)](https://github.com/donnemartin/system-design-primer#relational-database-management-system-rdbms)
- [Databases and DBMS (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#databases-and-dbms)
- [Database Federation (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#database-federation)
- [ACID Transactions](https://algomaster.io/learn/system-design/acid-transactions)
- [SQL vs NoSQL](https://algomaster.io/learn/system-design/sql-vs-nosql)
- [Database Indexes](https://algomaster.io/learn/system-design/indexing)
- [Database Sharding](https://algomaster.io/learn/system-design/sharding)
- [Data Replication](https://redis.com/blog/what-is-data-replication/)
- [Database Scaling](https://blog.algomaster.io/p/system-design-how-to-scale-a-database)
- [Databases Types](https://blog.algomaster.io/p/15-types-of-databases)
- [Bloom Filters](https://algomaster.io/learn/system-design/bloom-filters)
- [Database Architectures](https://www.mongodb.com/developer/products/mongodb/active-active-application-architectures/)
- OLTP vs OLAP systems
- Database normalization
- Primary keys, foreign keys, and constraints

### ACID
- [ACID and BASE consistency models (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#acid-and-base-consistency-models)
- Atomicity.
- Consistency.
- Isolation.
- Durability.
- Understanding ACID properties with a live example.

### Database Transactions
- [Transactions (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#transactions)
- What are database transactions?
- Transaction isolation levels
- Phantom Reads.
- Dirty reads and non-repeatable reads
- Serialization vs. Repeatable Read
- [How Databases Keep Passwords Securely](https://newsletter.systemdesign.one/p/how-to-store-passwords-in-database)



## 5. Database Scaling Concepts

### Database Indexing
- [Indexes (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#indexes)
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
- [Master-slave replication (Donne Martin)](https://github.com/donnemartin/system-design-primer#master-slave-replication)
- [Master-master replication (Donne Martin)](https://github.com/donnemartin/system-design-primer#master-master-replication)
- [Database Replication (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#database-replication)
- What is database replication?
- Master-slave replication
- Master-master replication
- Replication lag and consistency

### Database Partitioning
- [Federation (Donne Martin)](https://github.com/donnemartin/system-design-primer#federation)
- [Sharding (Donne Martin)](https://github.com/donnemartin/system-design-primer#sharding)
- [Consistent Hashing (AlgoMaster)](https://algomaster.io/learn/system-design/consistent-hashing)
- [Sharding (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#sharding)
- [Consistent Hashing (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#consistent-hashing)
- What is database partitioning?
- Horizontal partitioning (sharding)
- Vertical partitioning
- Sharding strategies and challenges
- Consistent hashing for sharding
- [Consistent Hashing](https://systemdesign.one/consistent-hashing-explained/)

### Designing Database Schema
- [Denormalization (Donne Martin)](https://github.com/donnemartin/system-design-primer#denormalization)
- [SQL tuning (Donne Martin)](https://github.com/donnemartin/system-design-primer#sql-tuning)
- [Normalization and Denormalization (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#normalization-and-denormalization)
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
- [SQL databases (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#sql-databases)
- Introduction to SQL databases
- Popular SQL databases (MySQL, PostgreSQL, SQL Server)
- SQL transactions and ACID compliance
- When to choose SQL databases

### NoSQL Databases
- [NoSQL (Donne Martin)](https://github.com/donnemartin/system-design-primer#nosql)
- [Key-value store (Donne Martin)](https://github.com/donnemartin/system-design-primer#key-value-store)
- [Document store (Donne Martin)](https://github.com/donnemartin/system-design-primer#document-store)
- [Wide column store (Donne Martin)](https://github.com/donnemartin/system-design-primer#wide-column-store)
- [Graph Database (Donne Martin)](https://github.com/donnemartin/system-design-primer#graph-database)
- [SQL or NoSQL (Donne Martin)](https://github.com/donnemartin/system-design-primer#sql-or-nosql)
- [NoSQL databases (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#nosql-databases)
- [SQL vs NoSQL databases (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#sql-vs-nosql-databases)
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
- [Storage (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#storage)
- Introduction to blob storage (S3, Azure Blob)
- File storage systems
- Object storage vs block storage
- Distributed file systems (HDFS, GFS)

## 8. Asynchronous Communication Patterns

### Message Queue Fundamentals
- [Asynchronism (Donne Martin)](https://github.com/donnemartin/system-design-primer#asynchronism)
- [Message queues (Donne Martin)](https://github.com/donnemartin/system-design-primer#message-queues)
- [Task queues (Donne Martin)](https://github.com/donnemartin/system-design-primer#task-queues)
- [Back pressure (Donne Martin)](https://github.com/donnemartin/system-design-primer#back-pressure)
- [Message Brokers (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#message-brokers)
- [Message Queues (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#message-queues)
- [Publish-Subscribe (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#publish-subscribe)
- [Enterprise Service Bus (ESB) (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#enterprise-service-bus-esb)
- [Pub/Sub](https://algomaster.io/learn/system-design/pub-sub)
- [Message Queues](https://algomaster.io/learn/system-design/message-queues)
- [Change Data Capture (CDC)](https://algomaster.io/learn/system-design/change-data-capture-cdc)
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
- [Cache (Donne Martin)](https://github.com/donnemartin/system-design-primer#cache)
- [Client caching (Donne Martin)](https://github.com/donnemartin/system-design-primer#client-caching)
- [CDN caching (Donne Martin)](https://github.com/donnemartin/system-design-primer#cdn-caching)
- [Web server caching (Donne Martin)](https://github.com/donnemartin/system-design-primer#web-server-caching)
- [Database caching (Donne Martin)](https://github.com/donnemartin/system-design-primer#database-caching)
- [Application caching (Donne Martin)](https://github.com/donnemartin/system-design-primer#application-caching)
- [When to update the cache (Donne Martin)](https://github.com/donnemartin/system-design-primer#when-to-update-the-cache)
- [Caching 101](https://algomaster.io/learn/system-design/what-is-caching)
- [Caching Strategies](https://algomaster.io/learn/system-design/caching-strategies)
- [Cache Eviction Policies](https://blog.algomaster.io/p/7-cache-eviction-strategies)
- [Distributed Caching](https://blog.algomaster.io/p/distributed-caching)
- [Content Delivery Network (CDN)](https://algomaster.io/learn/system-design/content-delivery-network-cdn)
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
- [Fail-over (Donne Martin)](https://github.com/donnemartin/system-design-primer#fail-over)
- [Failover (AlgoMaster)](https://www.druva.com/glossary/what-is-a-failover-definition-and-related-faqs)
- Health check strategies
- Active vs passive health checks
- Failover and failback strategies
- Circuit breaker integration

### Advanced Traffic Management
- [Rate Limiting (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#rate-limiting)
- Sticky sessions and session affinity
- Rate limiting and throttling
- [Rate Limiting Strategies Explained](https://newsletter.systemdesign.one/p/rate-limiting)
- Traffic shaping and QoS
- Global load balancing

## 11. Advanced Distributed Systems

### Consensus Algorithms
- [HeartBeats](https://blog.algomaster.io/p/heartbeats-in-distributed-systems)
- [Service Discovery](https://blog.algomaster.io/p/service-discovery-in-distributed-systems)
- [Consensus Algorithms](https://medium.com/@sourabhatta1819/consensus-in-distributed-system-ac79f8ba2b8c)
- [Distributed Locking](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html)
- [Gossip Protocol](http://highscalability.com/blog/2023/7/16/gossip-protocol-explained.html)
- [Circuit Breaker](https://medium.com/geekculture/design-patterns-for-microservices-circuit-breaker-pattern-276249ffab33)
- [Disaster Recovery](https://cloud.google.com/learn/what-is-disaster-recovery)
- [Distributed Tracing](https://www.dynatrace.com/news/blog/what-is-distributed-tracing/)
- What is consensus in distributed systems?
- Raft consensus algorithm
- Paxos algorithm explained
- Byzantine fault tolerance

### Distributed Transactions
- [Distributed Transactions (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#distributed-transactions)
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
- [Geohashing and Quadtrees (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#geohashing-and-quadtrees)
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
- [Virtual Machines (VMs) and Containers (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#virtual-machines-vms-and-containers)
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
- [Disaster recovery (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#disaster-recovery)
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
- [Security (Donne Martin)](https://github.com/donnemartin/system-design-primer#security)
- [OAuth 2.0 and OpenID Connect (OIDC) (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#oauth-20-and-openid-connect-oidc)
- [Single Sign-On (SSO) (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#single-sign-on-sso)
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
- [SSL, TLS, mTLS (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#ssl-tls-mtls)
- DDoS attacks and mitigation
- SQL injection prevention
- Cross-site scripting (XSS) prevention
- Data encryption at rest and in transit
- [Cybersecurity Terms Every Software Engineer Must Know](https://newsletter.systemdesign.one/p/cybersecurity-fundamentals)

## 16. Monitoring and Observability

### Monitoring Fundamentals
- [SLA, SLO, SLI (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#sla-slo-sli)
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
- [Design Pastebin.com (or Bit.ly) (Donne Martin)](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/pastebin#design-pastebincom-or-bitly)
- [Design the Twitter timeline and search (Donne Martin)](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/twitter#design-the-twitter-timeline-and-search-or-facebook-feed-and-search)
- [Design a web crawler (Donne Martin)](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/web_crawler#design-a-web-crawler)
- [Design Mint.com (Donne Martin)](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/mint#design-mintcom)
- [Design the data structures for a social network (Donne Martin)](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/social_graph#design-the-data-structures-for-a-social-network)
- [Design a key-value store for a search engine (Donne Martin)](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/query_cache#design-a-key-value-store-for-a-search-engine)
- [Design Amazon's sales ranking by category feature (Donne Martin)](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/sales_rank#design-amazons-sales-ranking-by-category-feature)
- [Design a system that scales to millions of users on AWS (Donne Martin)](https://github.com/donnemartin/system-design-primer/tree/master/solutions/system_design/scaling_aws#design-a-system-that-scales-to-millions-of-users-on-aws)
- [URL Shortener (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#url-shortener)
- [WhatsApp (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#whatsapp)
- [Twitter (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#twitter)
- [Netflix (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#netflix)
- [Uber (Karan Pratap Singh)](https://github.com/karanpratapsingh/system-design#uber)
#### Easy Problems (YouTube)
- [Design URL Shortener like TinyURL](https://algomaster.io/learn/system-design-interviews/design-url-shortener)
- [Design Autocomplete for Search Engines](https://algomaster.io/learn/system-design-interviews/design-instagram)
- [Design Load Balancer](https://algomaster.io/learn/system-design-interviews/design-load-balancer)
- [Design Content Delivery Network (CDN)](https://www.youtube.com/watch?v=8zX0rue2Hic)
- [Design Parking Garage](https://www.youtube.com/watch?v=NtMvNh0WFVM)
- [Design Vending Machine](https://www.youtube.com/watch?v=D0kDMUgo27c)
- [Design Distributed Key-Value Store](https://www.youtube.com/watch?v=rnZmdmlR-2M)
- [Design Distributed Cache](https://www.youtube.com/watch?v=iuqZvajTOyA)
- [Design Authentication System](https://www.youtube.com/watch?v=uj_4vxm9u90)
- [Design Unified Payments Interface (UPI)](https://www.youtube.com/watch?v=QpLy0_c_RXk)
#### Medium Problems (YouTube)
- [Design WhatsApp](https://algomaster.io/learn/system-design-interviews/design-whatsapp)
- [Design Spotify](https://algomaster.io/learn/system-design-interviews/design-spotify)
- [Design Instagram](https://algomaster.io/learn/system-design-interviews/design-instagram)
- [Design Notification Service](https://algomaster.io/learn/system-design-interviews/design-notification-service)
- [Design Distributed Job Scheduler](https://blog.algomaster.io/p/design-a-distributed-job-scheduler)
- [Design Tinder](https://www.youtube.com/watch?v=tndzLznxq40)
- [Design Facebook](https://www.youtube.com/watch?v=9-hjBGxuiEs)
- [Design Twitter](https://www.youtube.com/watch?v=wYk0xPP_P_8)
- [Design Reddit](https://www.youtube.com/watch?v=KYExYE_9nIY)
- [Design Netflix](https://www.youtube.com/watch?v=psQzyFfsUGU)
- [Design Youtube](https://www.youtube.com/watch?v=jPKTo1iGQiE)
- [Design Google Search](https://www.youtube.com/watch?v=CeGtqouT8eA)
- [Design E-commerce Store like Amazon](https://www.youtube.com/watch?v=EpASu_1dUdE)
- [Design TikTok](https://www.youtube.com/watch?v=Z-0g_aJL5Fw)
- [Design Shopify](https://www.youtube.com/watch?v=lEL4F_0J3l8)
- [Design Airbnb](https://www.youtube.com/watch?v=YyOXt2MEkv4)
- [Design Rate Limiter](https://www.youtube.com/watch?v=mhUQe4BKZXs)
- [Design Distributed Message Queue like Kafka](https://www.youtube.com/watch?v=iJLL-KPqBpM)
- [Design Flight Booking System](https://www.youtube.com/watch?v=qsGcfVGvFSs)
- [Design Online Code Editor](https://www.youtube.com/watch?v=07jkn4jUtso)
- [Design an Analytics Platform (Metrics & Logging)](https://www.youtube.com/watch?v=kIcq1_pBQSY)
- [Design Payment System](https://www.youtube.com/watch?v=olfaBgJrUBI)
- [Design a Digital Wallet](https://www.youtube.com/watch?v=4ijjIUeq6hE)
#### Hard Problems (YouTube)
- [Design Location Based Service like Yelp](https://www.youtube.com/watch?v=M4lR_Va97cQ)
- [Design Uber](https://www.youtube.com/watch?v=umWABit-wbk)
- [Design Food Delivery App like Doordash](https://www.youtube.com/watch?v=iRhSAR3ldTw)
- [Design Google Docs](https://www.youtube.com/watch?v=2auwirNBvGg)
- [Design Google Maps](https://www.youtube.com/watch?v=jk3yvVfNvds)
- [Design Zoom](https://www.youtube.com/watch?v=G32ThJakeHk)
- [Design File Sharing System like Dropbox](https://www.youtube.com/watch?v=U0xTu6E2CT8)
- [Design Ticket Booking System like BookMyShow](https://www.youtube.com/watch?v=lBAwJgoO3Ek)
- [Design Distributed Web Crawler](https://www.youtube.com/watch?v=BKZxZwUgL3Y)
- [Design Code Deployment System](https://www.youtube.com/watch?v=q0KGYwNbf-0)
- [Design Distributed Cloud Storage like S3](https://www.youtube.com/watch?v=UmWtcgC96X8)
- [Design Distributed Locking Service](https://www.youtube.com/watch?v=v7x75aN9liM)

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

## 19. Software White Papers, Articles, and Papers
## 📜 Must-Read Engineering Articles
- [How Discord stores trillions of messages](https://discord.com/blog/how-discord-stores-trillions-of-messages)
- [Building In-Video Search at Netflix](https://netflixtechblog.com/building-in-video-search-936766f0017c)
- [How Canva scaled Media uploads from Zero to 50 Million per Day](https://www.canva.dev/blog/engineering/from-zero-to-50-million-uploads-per-day-scaling-media-at-canva/)
- [How Airbnb avoids double payments in a Distributed Payments System](https://medium.com/airbnb-engineering/avoiding-double-payments-in-a-distributed-payments-system-2981f6b070bb)
- [Stripe’s payments APIs - The first 10 years](https://stripe.com/blog/payment-api-design)
- [Real time messaging at Slack](https://slack.engineering/real-time-messaging/)

## 🗞️ Must-Read Distributed Systems Papers
- [Paxos: The Part-Time Parliament](https://lamport.azurewebsites.net/pubs/lamport-paxos.pdf)
- [MapReduce: Simplified Data Processing on Large Clusters](https://research.google.com/archive/mapreduce-osdi04.pdf)
- [The Google File System](https://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf)
- [Dynamo: Amazon’s Highly Available Key-value Store](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf)
- [Kafka: a Distributed Messaging System for Log Processing](https://notes.stephenholiday.com/Kafka.pdf)
- [Spanner: Google’s Globally-Distributed Database](https://static.googleusercontent.com/media/research.google.com/en//archive/spanner-osdi2012.pdf)
- [Bigtable: A Distributed Storage System for Structured Data](https://static.googleusercontent.com/media/research.google.com/en//archive/bigtable-osdi06.pdf)
- [ZooKeeper: Wait-free coordination for Internet-scale systems](https://www.usenix.org/legacy/event/usenix10/tech/full_papers/Hunt.pdf)
- [The Log-Structured Merge-Tree (LSM-Tree)](https://www.cs.umb.edu/~poneil/lsmtree.pdf)
- [The Chubby lock service for loosely-coupled distributed systems](https://static.googleusercontent.com/media/research.google.com/en//archive/chubby-osdi06.pdf)


- [Amazon Dynamo](https://newsletter.systemdesign.one/p/amazon-dynamo-architecture)
- [Google Spanner](https://newsletter.systemdesign.one/p/cloud-spanner-database)
- [Meta Serverless Architecture: XFaaS](https://newsletter.systemdesign.one/p/serverless-architecture)

## 20. System Design Tradeoffs
- [Top 15 Tradeoffs](https://blog.algomaster.io/p/system-design-top-15-trade-offs)
- [Vertical vs Horizontal Scaling](https://algomaster.io/learn/system-design/vertical-vs-horizontal-scaling)
- [Concurrency vs Parallelism](https://blog.algomaster.io/p/concurrency-vs-parallelism)
- [Long Polling vs WebSockets](https://blog.algomaster.io/p/long-polling-vs-websockets)
- [Batch vs Stream Processing](https://blog.algomaster.io/p/batch-processing-vs-stream-processing)
- [Stateful vs Stateless Design](https://blog.algomaster.io/p/stateful-vs-stateless-architecture)
- [Strong vs Eventual Consistency](https://blog.algomaster.io/p/strong-vs-eventual-consistency)
- [Read-Through vs Write-Through Cache](https://blog.algomaster.io/p/59cae60d-9717-4e20-a59e-759e370db4e5)
- [Push vs Pull Architecture](https://blog.algomaster.io/p/af5fe2fe-9a4f-4708-af43-184945a243af)
- [REST vs RPC](https://blog.algomaster.io/p/106604fb-b746-41de-88fb-60e932b2ff68)
- [Synchronous vs. asynchronous communications](https://blog.algomaster.io/p/aec1cebf-6060-45a7-8e00-47364ca70761)
- [Latency vs Throughput](https://aws.amazon.com/compare/the-difference-between-throughput-and-latency/)


## 21. Additional Learning Resources
## 📇 Courses
- [May 11th: 5-Hour System Design Course (Mukul Raina)](https://mukulraina.notion.site/May-11th-5-Hour-System-Design-Course-Complete-Foundations-for-Interviews-3549faa09e6e80168d15c3713517e4a3)
- [March 25th: 5-Hour System Design Course (Mukul Raina)](https://mukulraina.notion.site/March-25th-5-Hour-System-Design-Course-3399faa09e6e8076a80ee8b65f990317)
- [System Design Fundamentals](https://algomaster.io/learn/system-design/course-introduction)
- [System Design Interviews](https://algomaster.io/learn/system-design-interviews/introduction)

## 📩 Newsletters
- [AlgoMaster Newsletter](https://blog.algomaster.io/)

## 📚 Books
- [Designing Data-Intensive Applications](https://www.amazon.in/dp/9352135245)

## 📺 YouTube Channels
- [Tech Dummies Narendra L](https://www.youtube.com/@TechDummiesNarendraL)
- [Gaurav Sen](https://www.youtube.com/@gkcs)
- [codeKarle](https://www.youtube.com/@codeKarle)
- [ByteByteGo](https://www.youtube.com/@ByteByteGo)
- [System Design Interview](https://www.youtube.com/@SystemDesignInterview)
- [sudoCODE](https://www.youtube.com/@sudocode)
- [Success in Tech](https://www.youtube.com/@SuccessinTech/videos)


