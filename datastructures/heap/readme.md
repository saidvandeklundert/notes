The Heap datastructure.

The simplest way to put it:
- The heap is a binary tree where every child and grand child is smaller (maxHeap) or later (minHeap) than the current node.
- Whenever we add a node, we must adjust the tree. 
- Whenever we remove a node, we must adjust the tree.

Heaps are commonly used to implement priority queues.



The heap is a complete binary tree. A Complete Binary Tree is always balanced
There is no traversing the tree.

Max heap: the top is the biggest value.
Min heap: the top is the lowest value.

In computer memory, the heap is usually represented as an array of numbers. We can map the node to an index quite easily.

The root node sits at index 0. The formula for the other nodes:
- left-child index: 2 * i + 1
- right-child index: 2 * i + 2

Example:
```
      0
    /   \
   /     \
  1       2
 / \    /   \
3   4  5     6   

```
The bottom 5 and 6 explained:
2 * 2 + 1 = 5
2 * 2 + 2 = 6


Insertion into a heap is log(n).
Deletion of an element is log(n).




https://realpython.com/python-heapq-module/