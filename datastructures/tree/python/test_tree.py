"""
python -m pytest test_tree.py
python -m mypy hash_tree.py
https://web.archive.org/web/20120723175438/www.quesucede.com/page/show/id/python_3_tree_implementation
"""
from tree import Tree, Node


def test_create_tree():
    tree = Tree("root")
    assert isinstance(tree, Tree)


def test_tree_add_node():
    tree = Tree("root")
    tree.add_node(Node(1))
    tree.add_node(Node(2))
    tree.add_node(Node(3))

    assert len(tree._nodes) == 3


def test_tree_contains():
    tree = Tree("root")
    tree.add_node(Node(1))
    tree.add_node(Node(2))
    tree.add_node(Node(3))

    assert 1 in tree
    assert 2 in tree
    assert 3 in tree


def test_tree_len():
    tree = Tree(1)
    tree.add_node(Node(3.1))
    tree.add_node(Node(3.2))
    tree.add_node(Node(3.3))
    assert len(tree) == 3


def test_create_treenode():
    tree_node = Node(1)
    assert isinstance(tree_node, Node)


def test_add_node_treenode():
    tree_node = Tree(1)
    tree_node.add_node(Node(3.1))
    tree_node.add_node(Node(3.2))
    tree_node.add_node(Node(3.3))
    assert 3.1 in tree_node
    assert 3.2 in tree_node
    assert 3.3 in tree_node


def test_treenode_len():
    treenode = Tree(1)
    treenode.add_node(Node(3.1))
    treenode.add_node(Node(3.2))
    treenode.add_node(Node(3.3))
    assert len(treenode) == 3
