"""
python -m pytest test_linked_list.py
python -m mypy linked_list.py
"""
from linked_list import LinkedList, Node


def test_create_ll():
    ll = LinkedList()
    assert isinstance(ll, LinkedList)


def test_create_ll_3_nodes():
    ll = LinkedList()
    ll.head = Node("node-1")
    ll.head.next = Node("node-2")
    ll.head.next.next = Node("node-3")
    assert "node-3" in ll


def test_reverse_ll():
    ll = LinkedList()
    ll.head = Node("node-1")
    ll.head.next = Node("node-2")
    ll.head.next.next = Node("node-3")
    ll.reverse()
    assert ll.get_index(0) == "node-3"


def test_subscribtable():
    ll = LinkedList()
    ll.head = Node("node-1")
    ll.head.next = Node("node-2")
    ll.head.next.next = Node("node-3")
    assert ll[0] == "node-1"
    assert ll[1] == "node-2"
    assert ll[2] == "node-3"


def test_add_after():
    ll = LinkedList()
    ll.head = Node("node-1")
    ll.add_after(target_node_data="node-1", new_node=Node("node-2"))
    ll.add_after(target_node_data="node-2", new_node=Node("node-3"))

    assert ll[0] == "node-1"
    assert ll[1] == "node-2"
    assert ll[2] == "node-3"
