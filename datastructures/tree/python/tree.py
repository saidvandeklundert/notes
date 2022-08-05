from __future__ import annotations
from typing import Any, List, Union


class Node:
    def __init__(self, val: Any, nodes: Union[List[Node], None] = None):
        self.val = val
        if nodes:
            self._nodes: List[Node] = nodes
        else:
            self._nodes: List[Node] = list()

    def __repr__(self):
        return f"TreeNode({str(self.val)})"

    def __contains__(self, identifier):
        return [node.val for node in self._nodes if node.val is identifier]

    def __len__(self):
        return len(self._nodes)

    def add_node(self, node: Node) -> None:
        self._nodes.append(node)

    def remove_node(self, node: Node) -> None:
        self._nodes.remove(node)


class Tree:
    def __init__(self, root: Any, nodes: Union[List[Node], None] = None):
        self.root = root
        if nodes:
            self._nodes: List[Node] = nodes
        else:
            self._nodes: List[Node] = list()

    def add_node(self, node: Node) -> None:
        self._nodes.append(node)

    def remove_node(self, node: Node) -> None:
        self._nodes.remove(node)

    def __contains__(self, identifier):
        return [node.val for node in self._nodes if node.val is identifier]

    def __len__(self):
        return len(self._nodes)


if __name__ == "__main__":
    tree = Tree(Node(0))

    tree.add_node(Node(1))
    tree.add_node(Node(2))
    three = Node(3)
    three.add_node(Node(3.1))
    three.add_node(Node(3.2))
    three.add_node(Node(3.3))
    tree.add_node(three)
    print(tree._nodes)
    print(tree._nodes[2])
    print(tree.preorder_list())
