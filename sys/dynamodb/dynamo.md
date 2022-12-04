Dynamo has a simple key/value interface, is highly available with a clearly defined consistency window, is efficient in its resource usage, and has a simple scale out scheme to address growth in data set size or request rates. Each service that uses
Dynamo runs its own Dynamo instances.

Dynamo uses a synthesis of well known techniques to achieve scalability and availability. Data is partitioned and replicated using consistent hashing, and consistency is facilitated by object versioning.
The consistency among replicas during updates is maintained by a quorum-like technique and a decentralized replica synchronization protocol. Dynamo maintains a gossip based distribution failure detection and membership protocol. Dynamo is a completely decentralized system with minimal need for manual administration. Storage nodes can be added and removed from Dynamo without requiring any manual partitioning or redistribution.

### System assumptions and requirements

Query model: simple read and write operations to a data item that is uniquely identified by a key. State is stored as binary objects (blobs) identified by unique keys. No operations span multiple data items and there is no need for relational schema. Dynamo targets applications that need to store objects that are relatively small (usually less than 1 MB).

ACID properties: Atomicity, Consistency, Isolation, Durability) is a set of properties that guarantee that database transactions are processed reliably. These guarnatees tend to have poor availability. Dynamo targets applications that operate with weaker consistency (the C in ACID) if this results in high availability. Dynamo does not provide any isolation guarantees and permits only single key updates.

Efficiency: Dynamo functions on commodity hardware.

Dynamo is used by AWS interal services. The operational environment is non-hostile. Each service uses its distinct instance of Dynamo.

### Design considerations

Dynamo is designed to be an eventually consistent data store; that is all updates reach all replicas eventually.

Other keywords:
- incremental scalability: Dynamo should be able to scale out one store host (node) at a time with minimal impact.
- symmetry: every node should have the same set of responsibilities as its peers. There are no nodes with special roles.
- decentralization: the design favors decentralized peer-to-peer techniques over centralized control. Centralized control has resulted in outages and the goal is to avoid it as much as possible.
- heterogenity: the system needs to be able to exploit heterogeneity in the infrastructure it runs on. E.g., the work distribution needs to be proportional to the capabilities of the individual servers. This is essential in adding new nodes with higher capacity without having to upgrade all hosts at once.


Dynamo allows read and write operations to continue even during network partitions and resolves updated conflicts using different conflixt resolution mechanisms.


### Dynamo concepts:


Dynamo targets applications that require only key/value access with primary focus on high availability where updates are not rejected even in the wake of network partitions or server failures.

Dynamo is built for an infrastructure with a single administrative domain where all nodes are assumed to be trusted.

Applications that use Dynamo do not require support for hierarchical namespaces or complext relational schema.

Dynamo is built for latency sensitive applications that require at least 99.9% of read and write operations to be performed within a few hundred milliseconds. To meet the stringesnt latency requirements, it was imperitive to avoid routing requests through multiple nodes. Dynamo is characterized as a zero-hop distributed hash table, where each node maintains enough routing information locally to route a request to the appropriate node directly.

### Techniques used in Dynamo


![Dynamo techniques](/img/dynamo_techniques.png)

#### System interface

Dynamo stores objects associated with a key through a simple interface; it exposes two operations: `get()` and `put()`.

The `get(key)` operation locates the object replicas associated with the `key` in the storage system and returns a single object or a list of objects with conflicting versions along with a _context_.
The `put(key, context)` operation determines where the erplicas of the object should be placed based on the associated _key_,and writes the replicas to disk. 

The _context_ encodes system metadata about the object that is opaque to the caller and includes information such as the version of the object. The context information is stored along with the object so that the system can verify the validity of the context object supplied in the put request.

Dynamo treats both the key and the object supplied by the caller as an opaque array of bytes. It applies a MD5 hash on the key to generate a 128-bit identifier, which is used to determine the storage nodes that are responsible for serving the key.

#### Partitioning algorithm

Dynamo must scale incrementally. This requires a mechanism to dynamically partition the data over the set of nodes (storage hosts) in the system. Dynamo's partitioning scheme relies on consistent hashing to distribute the load acoss multiple storage hosts.

The output range of a hash function is treated as a fixed circular space or ring. Each node gets assigned multiple points in the ring for which it is responsible. So a node can act as multiple virtual nodes. This has some advantages:
- if a node becomes unavailable, other nodes can handle the load
- new nodes added can take over load from others
- number of virtual nodes that a node is responsible for can be decided based on its capacity, accounting for the heterogeneity in the physical infrastructure

#### Replication

Dynamo replicates it's data on multiple hosts. Each data item is replicated on N hosts. Each key is assigned a co-ordinator node. The coordinator node is in charge of the replication of the data items that fall within its range. In addition to locally storing each key within its range, the coordinator replicates these keys at the N-1 clockwise successor nodes in the ring.


#### Data versioning

Dynamo provides eventual consistency, which allows for updates to be propagated to all replicas asynchronously. Dynamo treats the result of each modification as a new and immutable version of the data. A complicated scheme is put in place to handle cases where an item is updated at different times during times of isolation or network partitions.

#### Execution of get and put operations

Any node in Dynamo is eligable to recieve client get and put operations for any key.


#### Handling failure: hinted handoff.

Instead of strict quorum, Dynamo uses "sloppy quorum": all read and write operations are performed on the first N healthy nodes from the preference list, which may not always be the first N nodes encountered while walking the consistent hashing ring.

Each object is replicated across multiple datacenters.

#### Handling permanent failues: replica synchronization

To detect the inconsistencies be tween replicas faster and to
minimize the amount of transferred data, Dynamo uses Merkle
trees. 

A Merkle tree is a hash tree where leaves are hashes of the values of individual keys. Pare nt nodes higher in the tree are hashes of their respective children. The principal advantage of Merkle tree is that each branch of the tree can be checked independently without requiring nodes to download the entire tree or the entire data set. Moreover, Merkle trees help in reducing the amount of data that needs to be transferred while checking for inconsistencies among replicas. For in stance, if the hash values of the root of two trees are equal, then the values of the leaf nodes in the tree are equal and the nodes require no synchronization. If not, it implies that the values of some replicas are different. In such cases, the nodes may exchange the hash values of children and the process continues until it reaches the leaves of the trees, at which point the hosts can identify the keys that are “out of sync”. Merkle trees minimize the amount of data that needs to be transferred for synchronization and reduce the num ber of disk reads performed during the anti-entropy process.

Dynamo uses Merkle trees for an ti-entropy as follows: Each node maintains a separate Merkle tree for each key range (the set of keys covered by a virtual node) it hosts. This allows nodes to compare whether the keys within a key range are up-to-date. In this scheme, two nodes exchange the root of the Merkle tree corresponding to the key ranges that they host in common.

Subsequently, using the tree traversal scheme described above the nodes determine if they have any differences and perform the appropriate synchronization action. The disadvantage with this scheme is that many key ranges change when a node joins or leaves the system thereby requiring the tree(s) to be recalculated.

This issue is addressed, however , by the refined partitioning scheme described in Section 6.2



### Implementation

In Dynamo, each storage node has three main software components: request coordinati on, membership and failure detection, and a local persistenc e engine. All these components are implemented in Java.

Dynamo’s local persistence co mponent allows for different storage engines to be plugged in. Engines that are in use are Berkeley Database (BDB) Transactional Data Store 2, BDB Java Edition, MySQL, and an in-memory buffer with persistent backing store. 
The majority of Dynamo's production instances use BDB Transactional Data Store.



### Experience and lessons learned


Excerpt from [this](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf).
