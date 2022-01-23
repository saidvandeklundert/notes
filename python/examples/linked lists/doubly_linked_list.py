class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(1) time | O(1) space
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    # O(1) time | O(1) space
    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    # O(1) time | O(1) space
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    # O(1) time | O(1) space
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    # O(p) time | O(1) space
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        # if we hit the position:
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        # if we hit the tail:
        else:
            self.setTail(nodeToInsert)

    # O(n) time | O(n) space
    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    # O(1) time | O(1) space
    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    # O(n) tiome | O(1) space
    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None

    def removeNodeBindings(self, node):
        """remove a node by having the pointers of adjacent nodes point to each other"""
        if node.prev is not None:
            node.prev.next = node.next

        if node.next is not None:
            node.next.prev = node.prev

        node.prev = None
        node.next = None

    def __repr__(self):
        """method so we can print the data structure"""
        node = self.head
        nodes_front_to_back = []

        while node is not None:
            nodes_front_to_back.append(node.value)

            node = node.next
        nodes_front_to_back.append("None")
        ret = " <-> ".join(nodes_front_to_back)

        return ret


if __name__ == "__main__":

    dll = DoublyLinkedList()

    node_a = Node("a")
    dll.setHead(node_a)

    node_b = Node("b")
    node_c = Node("c")
    node_d = Node("d")
    dll.setHead(node_b)
    dll.setHead(node_c)
    dll.setHead(node_d)
    print(f"afer setting heads\n {dll}")
    dll.removeNodesWithValue("c")
    print(f"afer removing c\n {dll}")
    node_e = Node("e")
    dll.insertAfter(node_a, node_e)
    print(f"afer inserting e\n {dll}")
    dll.removeNodeBindings(node_b)
    print(f"afer removeNodeBindings for node_b\n {dll}")
