import copy

tests = [
    {
        "linkedList": {
            "head": "1",
            "nodes": [
                {"id": "1", "next": "1-2", "value": 1},
                {"id": "1-2", "next": "1-3", "value": 1},
                {"id": "1-3", "next": "2", "value": 1},
                {"id": "2", "next": "3", "value": 3},
                {"id": "3", "next": "3-2", "value": 4},
                {"id": "3-2", "next": "3-3", "value": 4},
                {"id": "3-3", "next": "4", "value": 4},
                {"id": "4", "next": "5", "value": 5},
                {"id": "5", "next": "5-2", "value": 6},
                {"id": "5-2", "next": None, "value": 6},
            ],
        }
    },
]
# from biglists import tests


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
    while currentNode is not None:
        nextDistinctNode = currentNode.next

        while (
            nextDistinctNode is not None and nextDistinctNode.value == currentNode.value
        ):
            nextDistinctNode = nextDistinctNode.next

        currentNode.next = nextDistinctNode
        currentNode = nextDistinctNode

    return linkedList


if __name__ == "__main__":
    print("num1")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        # print(removeDuplicatesFromLinkedList(test))
