# root
root = {"data": "A", "children": []}
# childe nodes
node2 = {"data": "B", "children": []}
node3 = {"data": "C", "children": []}
node4 = {"data": "D", "children": []}
node5 = {"data": "E", "children": []}
node6 = {"data": "F", "children": []}
node7 = {"data": "G", "children": []}
node8 = {"data": "H", "children": []}

# creating the tree
root["children"] = [node2, node3]
node2["children"] = [node4]
node3["children"] = [node5, node6]
node5["children"] = [node7, node8]

# print node from tree:
print(root["children"][1]["data"])

# traverse the tree using recursion:
# - base case: a leaf node without children
# - argument: node
# - how to reach the base case? Simply follow the edges
#   untill you reach a leaf.


def pre_order_traversal(node):
    # print node data
    print(node["data"], end=" ")
    if len(node["children"]) > 0:
        # recursive case:
        for child in node["children"]:
            pre_order_traversal(child)  # traverse child nodes
    # Base case
    return


pre_order_traversal(root)

print()


def post_order_traversal(node):
    for child in node["children"]:
        # recursive case:
        post_order_traversal(child)  # traverse child nodes
    print(node["data"], end=" ")  # access this node's data
    # BASE CASE
    return


post_order_traversal(root)

print()


def in_order(node):
    if len(node["children"]) >= 1:
        # recursive case:
        in_order(node["children"][0])  # traverse left child
    # access node data
    print(node["data"], end=" ")

    if len(node["children"]) >= 2:
        # recursive case:
        in_order(node["children"][1])  # traverse right child
    # BASE CASE
    return


in_order(root)
print()


def find_letters(node, to_find: str, debug: bool):
    if debug:
        print(f"Visiting node {node['data']}")

    # Preorder depth first:
    if debug:
        print("Checking if ", node["data"], f"is {to_find}")
    if node["data"] == to_find:
        return node["data"]
    if node["data"] != to_find:
        # recursive case:
        for child in node["children"]:
            ret = find_letters(child, to_find, debug)
            if ret is not None:
                if debug:
                    print(f"{to_find} is found!!!")
                return ret
    if debug:
        print(f"{to_find} is not found!!")
    return None


print(find_letters(root, "Z", False))
print(find_letters(root, "G", False))
print(find_letters(root, "G", True))
