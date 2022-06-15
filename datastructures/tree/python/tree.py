from __future__ import annotations
from typing import Any, List, Union


class TreeNode:
    def __init__(self, val: Any, nodes: Union[List[TreeNode], None] = None):
        self.val = val
        if nodes:
            self._nodes: List[TreeNode] = nodes
        else:
            self._nodes: List[TreeNode] = list()

    def add_node(self, node: TreeNode) -> None:
        self._nodes.append(node)

    def remove_node(self, node: TreeNode) -> None:
        self._nodes.remove(node)

    def __repr__(self):
        return f"TreeNode({str(self.val)})"

    def __contains__(self, identifier):
        return [node.val for node in self._nodes if node.val is identifier]

    def __len__(self):
        return len(self._nodes)


class Tree:
    def __init__(self, root: Any, nodes: Union[List[TreeNode], None] = None):
        self.root = root
        if nodes:
            self._nodes: List[TreeNode] = nodes
        else:
            self._nodes: List[TreeNode] = list()

    def add_node(self, node: TreeNode) -> None:
        self._nodes.append(node)

    def remove_node(self, node: TreeNode) -> None:
        self._nodes.remove(node)

    def __contains__(self, identifier):
        return [node.val for node in self._nodes if node.val is identifier]

    def __len__(self):
        return len(self._nodes)


if __name__ == "__main__":
    tree = Tree("root")

    tree.add_node(TreeNode(1))
    tree.add_node(TreeNode(2))
    three = TreeNode(3)
    three.add_node(TreeNode(3.1))
    three.add_node(TreeNode(3.2))
    three.add_node(TreeNode(3.3))
    tree.add_node(three)
    print(tree._nodes)
    print(tree._nodes[2])

    treenode = TreeNode("king")
    treenode.add_node(TreeNode("prince"))
    treenode.add_node(TreeNode("princess"))
