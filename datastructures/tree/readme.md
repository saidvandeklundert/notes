# Tree

A Tree is a non-linear datastructure. A tree is actually a type/form of graph.

There are many different types of trees. A few of the most common/important ones are :
- general tree (filesystem)
- binary tree 
- AVL tree (self balancing binary search tree)

## Important definitions:

Node: the nodes are what make the tree. A node can have a name, which can be referred to as 'key'. A node may also have additional information, called 'payload'.

Root: the beginning of the tree structure.

Parent: a node that has child nodes.

Child: a node that has a parent node.

Leaf node: a node without children.

Inner/internal node: a node that is not a root or a leaf.

Sibling: nodes in the tree that are children of the same parent are said to be siblings.

Edge: connects two nodes to show that there is a relationship between them. Formula: number of edges = number of nodes - 1

Levels: the tree is made up of levels:
- level 0: root node
- level 1: level below root
- level x: x levels below root

Height: ithe height of any node is the number of edges from that node to the deepest leaf.

Depth: depth of any node can be defined as the length of path from root node to that particular node.

Path: ordered list of nodes connected by edges.

Subtrees: set of nodes and edges comprised of a parent and all the descendants of that parent.




## Binary tree

- a node has at most 2 children
- exactly 1 root
- 1 path between a root and any node

Pre-order traversal:
- Process the root
- Process the nodes in the left subtree with a recursive call
- Process the nodes in the right subtree with a recursive call

In-order traversal:
- Process the nodes in the left subtree with a recursive call
- Process the root
- Process the nodes in the right subtree with a recursive call

Post-order traversal:
- Process the nodes in the left subtree with a recursive call
- Process the nodes in the right subtree with a recursive call
- Process the root



[Jacob Sorber](https://www.youtube.com/watch?v=UbhlOk7vjVY)

https://www.cpp.edu/~ftang/courses/CS241/notes/trees.htm


https://gist.github.com/aidanhs/5ac9088ca0f6bdd4a370

[Binary Tree Algorithms for Technical Interviews - Full Course](https://www.youtube.com/watch?v=fAAZixBzIAI)