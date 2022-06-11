from __future__ import annotations
from logging import root
from tkinter.tix import Tree
from typing import Any, List


class TreeNode:
    def __init__(self, val: Any = 0, children: List[TreeNode] = []):
        self.val = val
        self.children: List[TreeNode] = children

    def add_node(self, node: TreeNode):
        self.children.append(node)


class Tree:
    def __init__(self, root: Any, children: List[TreeNode] = []):
        self.root = root
        self.children = children

    def add_node(self, node: TreeNode):
        self.children.append(node)


if __name__ == "__main__":
    tree = Tree("root")
    print(tree)
