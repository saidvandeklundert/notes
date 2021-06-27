class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

    def __repr__(self):
        return self.data


class CircularLinkedList:
    def __init__(self, nodes):
        self.head = None
        if nodes is not None:
            self.head = Node(nodes.pop(0))

        node = self.head
        for data in nodes:
            node.next = Node(data=data)
            node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


if __name__ == "__main__":
    first_node = Node("a")
    print(first_node)

    cll = CircularLinkedList(["a", "b", "c"])

    print(cll)
