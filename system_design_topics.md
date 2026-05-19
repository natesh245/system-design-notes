# Comprehensive System Design Roadmap

A complete guide to system design, combining content extracted from [The System Design Academy](https://www.systemdesignacademy.com/) and essential industry standards, arranged progressively from beginner to advanced.

## 1. System Design Interview Methodology
- Requirement Gathering: Functional vs. Non-Functional requirements
- Capacity Planning & Back-of-the-envelope calculations
- Defining the System Interface (API Design)
- High-Level Design & Component Diagram
- Deep Dives & Bottleneck Identification

## 2. Fundamentals of System Design
### What is system design?
- Introduction to system design

### Scalability, Availability & Reliability
- What is scalability?
- Scalability vs Performance
- What is availability?
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
- A word on Consistency patterns
- Eventual consistency in distributed systems

### CAP & PACELC Theorems
- A word on CAP theorem
- PACELC theorem explained

### Estimation & Back-of-envelope calculations
- System design estimation fundamentals
- Capacity planning basics
- QPS, storage, and bandwidth calculations

## 3. Networking Fundamentals
- Latency vs. through-put vs. bandwidth
- Introduction to DNS (domain name system)
- TCP vs UDP in system design

## 4. API Design & Communication Protocols
### API Design Patterns
- HTTP/HTTPS and REST principles
- RESTful API design principles
- GraphQL vs REST
- API versioning strategies
- API rate limiting and throttling

### Advanced Communication Protocols
- WebSockets, Long-Polling, and Server-Sent Events (SSE)
- RPC (Remote Procedure Call) and gRPC
- Serialization Formats: Protocol Buffers (Protobuf), Apache Thrift, Apache Avro

## 5. Basic Intro to Core Components
- Introduction to CDN
- Introduction to Load balancer
- Introduction to Caching
- Introduction to API Gateway

## 6. Database Engineering Fundamentals
### ACID
- Atomicity
- Consistency
- Isolation
- Durability
- Understanding ACID properties with a live example

### Database Transactions
- What are database transactions?
- Transaction isolation levels
- Phantom Reads
- Dirty reads and non-repeatable reads
- Serialization vs. Repeatable Read

### Database Fundamentals
- OLTP vs OLAP systems
- Database normalization
- Primary keys, foreign keys, and constraints
- Designing Database Schema (principles, data types, migrations)

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
- SQL vs NoSQL - which, when, where & why?

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

## 8. Load Balancing and Traffic Management
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

### Health Checks, Failover & Traffic Management
- Health check strategies (Active vs passive)
- Failover and failback strategies
- Circuit breaker integration
- Sticky sessions and session affinity
- Rate limiting and throttling
- Traffic shaping and QoS
- Global load balancing

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

### Cache Technologies & Distributed Caching
- Redis deep dive
- Memcached vs Redis
- Application-level caching
- Database query result caching
- Distributed cache architecture
- Cache sharding and partitioning
- Cache replication strategies
- Handling cache failures

## 10. Asynchronous Communication Patterns
### Message Queue Fundamentals
- What are message queues?
- Synchronous vs asynchronous communication
- Point-to-point vs publish-subscribe
- Message ordering and delivery guarantees

### Popular Message Queue Systems
- Apache Kafka architecture and use cases
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

## 11. Database Scaling Concepts
### Database Indexing
- Indexing - data structure that powers your database
- How database indexing actually works internally?
- B-tree and B+ tree indexes
- Hash indexes and bitmap indexes
- Composite indexes and index optimization

### Database Locking
- Introduction to database locking
- Row-level vs table-level locking
- Deadlock detection and prevention

### Database Tuning & Optimizations
- What is database performance tuning?
- Query optimization techniques
- Database connection pooling
- Analyzing query execution plans

### Database Replication & Partitioning
- What is database replication?
- Master-slave replication
- Master-master replication
- Replication lag and consistency
- What is database partitioning?
- Horizontal partitioning (sharding)
- Vertical partitioning
- Sharding strategies and challenges
- Consistent hashing for sharding

## 12. Architectural Patterns and Design Principles
### Monolithic vs Microservices
- Monolithic architecture pros and cons
- Introduction to microservices
- When to choose microservices vs monolith
- Service decomposition strategies

### Event-Driven Architecture
- What is event-driven architecture?
- Event sourcing patterns
- CQRS (Command Query Responsibility Segregation)
- Pub/Sub messaging patterns

### Resilience & Migration Patterns
- Circuit breaker pattern
- Bulkhead pattern
- Retry and timeout patterns
- Saga pattern for distributed transactions
- Strangler fig pattern
- Blue-green deployment
- Canary deployment

## 13. Probabilistic & Advanced Data Structures
- Bloom Filters (Set membership, caching optimizations)
- HyperLogLog (Unique counting at scale)
- Count-Min Sketch (Frequency counting in streams)
- Geohashes & Quadtrees (Location-based services)
- Merkle Trees (Anti-entropy in Dynamo/Cassandra)
- Tries & Inverted Indexes (Search and Typeahead)

## 14. Advanced Distributed Systems
### Concurrency, Time & State
- What is Concurrency?
- Introduction to threads, deadlock & starvation
- Race conditions and synchronization
- What is idempotency and why it matters?
- Implementing idempotent operations
- Why time is hard in distributed systems
- Introduction to logical clocks and NTP
- Vector clocks and causality
- Service discovery and Heartbeats

### Consensus & Coordination
- What is consensus in distributed systems?
- Raft consensus algorithm
- Paxos algorithm explained
- Byzantine fault tolerance
- Distributed locks and leader election
- Apache Zookeeper coordination service
- etcd for distributed coordination
- Gossip protocols for information dissemination

### Distributed Transactions & Partitioning
- Two-phase commit (2PC) protocol
- Three-phase commit (3PC) protocol
- Saga pattern for long-running transactions
- Eventual consistency patterns
- Data partitioning strategies & Consistent hashing deep dive
- Quorum-based systems

## 15. Global Architecture & Multi-Data Center Design
- Multi-Data Center deployments (Active-Active vs. Active-Passive)
- Global Databases (Google Spanner, CockroachDB, TrueTime)
- Edge computing and advanced CDN architectures

## 16. Database Internals
### Storage Engine Internals
- How tables and indexes are stored on disk?
- B-tree and LSM-tree storage structures
- Page layouts and buffer pool management
- Write-ahead logging (WAL) mechanisms

### Query Processing & Specific DB Internals
- Query parsing and optimization
- Execution plan generation
- Join algorithms and optimization
- Cost-based optimization
- InnoDB storage engine architecture
- Sorting algorithm behind ORDER BY query in MySQL
- MySQL replication internals
- Transaction isolation in InnoDB
- MongoDB document storage and indexing
- Cassandra ring architecture and partitioning
- Redis data structures and persistence
- Elasticsearch inverted index structure

## 17. Search & AI System Design
- Search Architecture (Full-text search, TF-IDF, Ranking algorithms)
- Vector Databases & Embeddings (Semantic search, AI integration)
- ML Model Serving Architectures

## 18. Performance Optimization
### Performance Fundamentals
- Performance metrics and KPIs
- Latency vs throughput trade-offs
- Performance testing strategies
- Capacity planning and forecasting

### Component Optimization
- Application Performance (Code-level, GC, Async patterns, Connection pooling)
- Database Performance (Query tuning, Read replicas, Partitioning)
- System Performance (CPU, memory, I/O, Network optimization)

## 19. Modern Infrastructure and DevOps
### Containerization & Orchestration
- Docker fundamentals for system design
- Container orchestration with Kubernetes
- Microservices deployment patterns
- Service mesh architecture (Istio, Linkerd)

### Cloud Architecture & Deployment
- Cloud-native application design
- Serverless architecture patterns
- Multi-cloud and hybrid cloud strategies
- CI/CD pipeline design
- Rolling deployment and rollback

### Infrastructure as Code
- Infrastructure automation principles
- Configuration management
- Auto-scaling and resource management
- Disaster recovery and backup strategies

## 20. Security
### Authentication & Authorization
- Authentication vs authorization
- OAuth 2.0 and OpenID Connect
- JWT tokens and session management
- Single Sign-On (SSO) systems

### Security Patterns & Threats
- API authentication strategies (Keys vs tokens)
- Defense in depth & Zero trust architecture
- Principle of least privilege & Security by design
- DDoS attacks and mitigation
- SQL injection & XSS prevention
- Data encryption at rest and in transit

## 21. Monitoring and Observability
### Fundamentals
- What is observability?
- Metrics, logs, and traces (three pillars)
- SLIs, SLOs, and error budgets

### Metrics, Alerting & Logging
- Application & Infrastructure metrics
- Alerting strategies and alert fatigue
- Dashboards and visualization
- Structured logging best practices
- Centralized logging architecture
- Log aggregation and analysis

## 22. Specific System Design Case Studies (Practice)
- Designing a Rate Limiter
- Designing a URL Shortener (e.g., TinyURL)
- Designing a Real-time Chat Application (e.g., WhatsApp, Discord)
- Designing a Video Streaming Service (e.g., Netflix, YouTube)
- Designing a Ride-Hailing App (e.g., Uber, Lyft)
- Designing a Location-Based Service (e.g., Yelp, Proximity Search)
- Designing a Distributed Web Crawler
- Designing a Typeahead / Autocomplete System
- Designing a Ticket Booking System
