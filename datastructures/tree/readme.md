# Tree

A Tree is a non-linear datastructure. A tree is actually a type/form of graph.

There are many different types of trees. A few of the most common/important ones are :
- general tree (filesystem)
- binary tree 
- AVL tree (self balancing binary search tree)

Others:
- Red Black Tree (self balancing tree)
- DAG tree (directed acyclic graph)

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

Acyclic: a graph is said to be acyclic in case thee are not loops ('cycles') from child nodes to their own ancestors.

## Binary tree

- a node has at most 2 children
- exactly 1 root
- 1 path between a root and any node

The nodes in a binary tree have three values:
- data value
- pointer to the left child
- pointer to the right child


Example:
```
     1
    / \
   /   \
  2     \
 / \     3
4   5   / \
       9   \
            8
           / \
          6   7
```


Binary tree types:
- `full binary tree`: every node has either 0 childs or 2 childs. There are no nodes with 1 child.
```
     1
    /  \
   /    \
  2      3
 / \    / \
4   5  9   8
          / \
        10   12
```
- `complete binary tree`: all levels are completely filled except the last level. The last level is filled starting from the left.
```
     1
    /  \
   /    \
  2      3
 / \    / 
4   5  9 
```
- `perfect binary tree`: all internal nodes have 2 children and all leaf nodes are at the same depth or same level.
```
     1
    /  \
   /    \
  2      3
 / \    / \
4   5  9   8
```
- `balanced binary tree`: the height of the left and right sub-trees of every node may differ by at most 1
- `degenerate binary tree`: binary tree where every parent node has only one child


There are different ways in which you can traverse the tree.

Pre-order traversal:
- Process the root
- Process the nodes in the left subtree with a recursive call
- Process the nodes in the right subtree with a recursive call
- to access data in the parent nodes before the data in the child nodes

In-order traversal:
- Process the nodes in the left subtree with a recursive call
- Process the root
- Process the nodes in the right subtree with a recursive call
- traverse the keft child node, then access the node data and then traverse the right child

Post-order traversal:
- Process the nodes in the left subtree with a recursive call
- Process the nodes in the right subtree with a recursive call
- Process the root
- traverse tree before accessing data
- left nodes before right nodes and bottom nodes before top nodes



[Jacob Sorber](https://www.youtube.com/watch?v=UbhlOk7vjVY)

https://www.cpp.edu/~ftang/courses/CS241/notes/trees.htm


https://gist.github.com/aidanhs/5ac9088ca0f6bdd4a370

[Binary Tree Algorithms for Technical Interviews - Full Course](https://www.youtube.com/watch?v=fAAZixBzIAI)


Visualize the tree: https://visualgo.net/en/bst
