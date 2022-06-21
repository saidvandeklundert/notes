from typing import Any
from __future__ import annotations


class TreeNode:
    def __init__(self, val: Any = 0, left: TreeNode = None, right: TreeNode = None):
        self.val = val
        self.left = left
        self.right = right


if __name__ =="__main__":
    #x = TreeNode({val: 1, left: TreeNode({val: 2, left: None, right: None}), right: TreeNode({val: 3, left: None, right: None}))