[Great preso](https://docs.google.com/presentation/d/1UMDZtvgYUksip_Jx1nzAuDYAPeaoB4heYZr6gbyjvb8/edit#slide=id.g865b75ec1e_0_103)



OLTP: Online Transaction Processing database.
- mySQL, Oracle

OLAP: Online Analytical Processing database
- Hbase, Hive, Spark

Row-store:
+ easy to add/modify record
- might read unnecessary data

Column-store:
+ only read relevant data
- tuples writes requires multiple access


# Datbase types:

Key value:
  - data partitioning
  - simple data model  
  - high write and query performance
  
  * Examples:
    - Redis
    - DynamoDB
    - Apache HBase

Newsql:
  - transactions and ACID
  - SQL support

  * Examples:
    - CockraochDB
    - SingleStore

Graph:
  - Relationship focus
  - Deep insight

  * Examples:
    - Neo4j
    - AWS neptune
    - Janus Graph

Time-series:
  - efficient query performance
  - document versioning
  - flexible schema
  
  * Examples:
    - influxDB
    - Kafka

Spatial:
  - Special types and indexing
  - columnwise indexing
  - topology and network analysis
  - integeration with GI
  
  * Examples:
    - Snowflake
    - msft SQL server


Ledger:
  - transparency and immutability
  - auditability and traceability
  - consensus mechanism

  * Examples:
    - Amazon QLDB

SQL (RDBMS):
  - indexing and optimization
  - security features
  - SQL support
  - transactions and ACID
  - relational and referential integrety
  - structured data

  * Examples:
    - mySQL
    - PostgresSQL
    - Msft SQL server

Clumnar:
  - Column oriented storage
  - Column level compression
  - Column wise indexing
  - scheme evolution  
  - analytical query performance

  * Examples:
    - Apache
    - Cassandra
    - Datastax

Object-oriented:
  - Object Persistence
  - Inheritance & Polymorphism
  - Object versioning
  - Complex Data models
  - Encapsulation and data abstraction
  - complext querying and navigation

  * Examples:
    - ObjectDB
    - ZODB

Document:
  - efficient query performance
  - document versioning
  - flexible schema

  * Examples: