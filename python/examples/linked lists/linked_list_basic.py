# https://realpython.com/linked-lists-python/


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


if __name__ == "__main__":
    llist = LinkedList()
    first_node = Node("a")
    llist.head = first_node

    # add second node:
    second_node = Node("b")
    first_node.next = second_node

    # add third node:
    third_node = Node("c")
    second_node.next = third_node

    # add fourth node:
    fourth_node = Node("d")
    third_node.next = fourth_node

    # add fifth node:
    fith_node = Node("d")
    fourth_node.next = fith_node

    print("loop through list")
    now = llist.head
    while now is not None:
        print(now.data)
        now = now.next

    print(f"Remove duplicates, list before:")
    print("\t", llist)
    currentNode = llist.head
    while currentNode is not None:
        nextDistinctNode = currentNode.next
        while (
            nextDistinctNode is not None and nextDistinctNode.data == currentNode.data
        ):
            nextDistinctNode = nextDistinctNode.next

        currentNode.next = nextDistinctNode
        currentNode = nextDistinctNode
    print("list after:")
    print("\t", llist)
