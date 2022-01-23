class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        """ez constructor"""
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def add_first(self, node):
        """add to the start of the linked list"""
        # set next of the node that is passed in to the linked list:
        # then re-assign head to the node that is passed in
        node.next = self.head
        self.head = node

    def add_last(self, node):
        """add to the end of the linked list"""
        if not self.head:
            self.head = node
            return
        for cur_node in self:
            pass
        cur_node.next = node

    def add_after(self, target_node_data, new_node):
        """add new_node to the list after target_node_data if it is found"""
        if not self.head:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception("Target node not in list")

    def add_before(self, target_node_data, new_node):
        """add new_node to the list before target_node_data if it is found"""
        if not self.head:
            raise Exception("List is empty")
        if self.head.data == target_node_data:
            return self.add_first(new_node)
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Target node not in list")

    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                return
            prev_node = node

        raise Exception("Target node not in list")

    def get_index(self, index):
        if not self.head:
            raise Exception("List is empty")
        i = 0
        for node in self:
            if i == index:
                return node.data
            i += 1

        raise Exception("Index not in linked list")

    # challenge: make the linked list indexable through the use of brackets

    def reverse(self):
        pass

    def enque(self):
        pass

    def deque(self):
        pass

    def __iter__(self):
        """make the linked list iterable in a Pythonic way"""
        node = self.head
        while node is not None:
            # yield is similar to return
            #  except it does not stop execution
            yield node
            node = node.next

    def __repr__(self):
        """method so we can print the data structure"""
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


if __name__ == "__main__":
    # create a linked list and manually assign the nodes:
    a_llist = LinkedList()
    first_node = Node("a")
    second_node = Node("b")
    third_node = Node("c")
    a_llist.head = first_node
    first_node.next = second_node
    second_node.next = third_node
    # >>> a_llist
    # a -> b -> c -> None

    strings = ["first", "second", "third", "fourth"]
    b_llist = LinkedList(strings)
    # >>> b_llist
    # first -> second -> third -> fourth -> None
    # >>> for i in b_llist:
    # ...     print(i)
    # ...
    # first
    # second
    # third
    # fourth
    #
    # Add new first to the linked list:
    # >>> b_llist.add_first(Node(data="zero"))
    # >>> b_llist
    #
    # Add new last to the linked list:
    # >>> b_llist.add_last(Node(data="fifth"))
    # >>> b_llist
    # zero -> first -> second -> third -> fourth -> fifth -> None
