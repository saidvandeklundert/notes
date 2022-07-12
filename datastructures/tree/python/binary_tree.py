"""
     1
    / \
   /   \
  2     \
 / \     4
3   21   / \
       5   \
            6
           / \
          10  11


"""
from __future__ import annotations
from typing import Any, Union, List, Optional
from dataclasses import dataclass


class Node:
    def __init__(
        self,
        val: Any = 0,
        left: Union[None, Node] = None,
        right: Union[None, Node] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Queue:
    def __init__(self):
        self.nodes: List[Node] = []

    def enqueu(self, item: Node) -> None:
        self.nodes.append(item)

    def dequeue(self) -> Optional[Node]:
        if len(self.nodes):
            return self.nodes.pop(0)

    def peek(self) -> Optional[Node]:
        if len(self.nodes):
            return self.nodes[0].val

    def __len__(self):
        return len(self.nodes)


class BinaryTree:
    def __init__(self, root: Union[Node, None]):
        self.root = root

    def in_order_print(self):
        in_order_traversal(self.root)

    def preorder_list(self, traversal: List[int]) -> List[int]:
        return self.__preorder_list(self.root, traversal)

    def __preorder_list(self, start: Node, traversal: List[int]) -> List[int]:
        """Helper to preorder_list."""
        if start is None:
            return traversal

        traversal.append(start.val)
        self.__preorder_list(start=start.left, traversal=traversal)
        self.__preorder_list(start=start.right, traversal=traversal)
        return traversal

    def postorder_list(self, traversal: List[int]) -> List[int]:
        return self.__postorder_list(self.root, traversal)

    def __postorder_list(self, start: Node, traversal: List[int]) -> List[int]:
        """Helper to postorder_list."""
        if start is None:
            return traversal

        self.__postorder_list(start=start.left, traversal=traversal)
        self.__postorder_list(start=start.right, traversal=traversal)
        traversal.append(start.val)
        return traversal

    def inorder_list(self, traversal: List[int]) -> List[int]:
        return self.__inorder_list(self.root, traversal)

    def __inorder_list(self, start: Node, traversal: List[int]) -> List[int]:
        """Helper to postorder_list."""
        if start is None:
            return traversal

        self.__inorder_list(start=start.left, traversal=traversal)
        traversal.append(start.val)
        self.__inorder_list(start=start.right, traversal=traversal)

        return traversal

    def level_order(self, start: Node):
        """
        Level order search, aka Breadth-first search.
        """
        if start is None:
            return
        queue = Queue()
        queue.enqueu(start)
        traversal = []
        while len(queue.nodes) > 0:
            traversal.append(queue.peek())
            node = queue.dequeue()
            if node.left:
                queue.enqueu(node.left)
            if node.right:
                queue.enqueu(node.right)

        return traversal


def in_order_traversal(node: Node, depth: int = 0) -> None:
    if node.left:
        in_order_traversal(node.left, depth=depth + 1)
    print(f"{depth * ' '}{node.val}")
    if node.right:
        in_order_traversal(node.right, depth=depth + 1)
    return None


if __name__ == "__main__":
    tree = BinaryTree(root=Node(val=1))
    node_2 = Node(val=2)
    node_4 = Node(val=4)
    node_5 = Node(val=5)
    node_6 = Node(val=6)
    node_10 = Node(val=10)
    node_11 = Node(val=11)
    tree.root.left = node_2
    tree.root.right = node_4
    node_4.left = node_5
    node_4.right = node_6
    node_6.left = node_10
    node_6.right = node_11
    node_3 = Node(val=3)
    node_21 = Node(val=21)
    node_2.left = node_3
    node_2.right = node_21
    print(tree)
    tree.in_order_print()
    pre_order_list = tree.preorder_list([])
    print(pre_order_list)
    pre_order_list = tree.postorder_list([])
    print(pre_order_list)
    pre_order_list = tree.inorder_list([])
    print(pre_order_list)

    breadth_first_search = tree.level_order(tree.root)
    print(breadth_first_search)
