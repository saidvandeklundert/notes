"""
python -m pytest .\doubly_linked_list_basic.py
ipython -i .\doubly_linked_list_basic.py
"""
from linked_list_interface import LinkedList
from typing import TypeVar

T = TypeVar("T")


class Node:
    def __init__(self, item: T):
        self.item = item
        self.prev: Node | None = None
        self.next: Node | None = None

    def __repr__(self):
        return str(self.item)


class DoublyLinkedList(LinkedList):
    def __init__(self):
        self.length = 0
        self.head: Node | None = None
        self.tail: Node | None = None

    def len(
        self,
    ):
        pass

    def insert_at(self, item: T, index: int) -> None:
        if index > self.length:
            raise IndexError(f"Index out of range, linked list lenght is {self.length}")

        if index == 0:
            return self.prepend(item=item)
        self.length += 1
        node_to_insert = Node(item=item)

        current = self.head
        idx = 0
        while True:
            idx += 1
            if idx == index:
                break
            current = current.next

        node_to_insert.next = current.next
        node_to_insert.prev = current
        current.next = node_to_insert
        if node_to_insert.next:
            node_to_insert.next.prev = node_to_insert
        if node_to_insert.next is None:
            self.tail = node_to_insert

        return None

    def remove(self, item: T) -> T | None:
        current = self.head
        while current is not None:
            if current.item == item:
                break
            current = current.next

        if current is None:
            return None
        self.length -= 1

        if current == self.tail:
            self.tail = current.prev
            self.tail.next = None
            return None
        elif current == self.head:
            self.head = current.next
            return
        else:
            print("hitit", current)
            print("current.prev ", current.prev)
            print("current.next.prev ", current.next.prev)
            current.prev.next = current.next
            current.next.prev = current.prev

        return None

    def remove_at(self, index: int) -> T | None:
        pass

    def append(self, item: T) -> None:
        node_to_insert = Node(item=item)
        self.length += 1
        self.tail.next = node_to_insert
        node_to_insert.prev = self.tail
        self.tail = node_to_insert
        return None

    def prepend(self, item: T) -> None:
        self.length += 1
        node = Node(item=item)
        if self.head is None:
            self.head = node
            self.tail = node
            return None
        node.next = self.head
        self.head.prev = node
        self.head = node
        return None

    def get(self, item: T) -> T | None:
        pass

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.item))
            node = node.next
        nodes.append("None")

        return " -> ".join(nodes)


###
# Testing
###
def test_node():
    n = Node(item=1)
    assert n.item == 1


def test_insert_at():
    ll = DoublyLinkedList()
    ll.prepend(1)
    ll.prepend(3)
    ll.prepend(4)

    ll.insert_at(2, 1)
    assert ll.length == 4
    assert ll.head.next.item == 2


def test_append():
    ll = DoublyLinkedList()
    ll.prepend(1)
    ll.prepend(2)
    assert ll.tail.item == 1
    ll.append(3)
    assert ll.length == 3

    current = ll.head
    while current.next is not None:
        current = current.next
    assert current.item == 3
    assert ll.tail.item == 3


def test_remove():
    ll = DoublyLinkedList()
    ll.prepend(1)
    ll.prepend(2)
    ll.prepend(3)
    ll.remove(2)
    print(ll)
    assert ll.length == 2
    assert ll.head.next.item == 1
    assert ll.head.item == 3
    assert ll.tail.item == 1
    ll.remove(1)
    assert ll.length == 1
    assert ll.head == ll.tail


if __name__ == "__main__":
    ll = DoublyLinkedList()

    ll.prepend(5)
    ll.prepend(4)
    ll.prepend(3)
    ll.prepend(2)
    ll.prepend(1)
    print("BEFORE")
    print(ll)
    ll.insert_at(99, 1)
    print("AFTER")
    print(ll)
    print("AFTER REMOVAL of 5:")
    ll.remove(5)
    print(ll)
    print(ll.tail)
    print("AFTER REMOVAL of 99:")
    ll.remove(99)
    print(ll)
    print(ll.tail)
