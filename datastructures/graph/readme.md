## Graphs

### Terms

cycle: when you start at `Node(x)`, follow the links, and end back at `Node(x)`.

acyclic: a graph that does not contain any cycles

connected: when every node has a path to another node

directed: when there is a direction to the connections. 

    node < -- > node <--- node : has directions

undirected: not directed

    node --- node --- node : does not have directions

weighted: the edges have weights (or costs) associated with them (like with OSPF).

dag: Directed, acyclical graph.

### Terms related to the implementation of graps

node: a point or vertex on the graph

edge: the connection between two nodes

Graps can be represented with adjacencies in a list or in a matrix.

### Big O

BigO is commonly stated in terms of V and E where V stands for vertices and E stands for edges

So O(V * E) means that we will check every vertex, and on every vertex we check every edge


