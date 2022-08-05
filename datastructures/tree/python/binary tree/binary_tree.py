"""
pre-order:
- value
- left
- right

post-order:
- left
- right
- value

in-order:
- left
- value
- right






"""
from __future__ import annotations


class Node:
    def __init__(self, value: int, left: Node | None = None, right: Node | None = None):
        self.value = value
        self.left = left
        self.right = right


def pre_order(
    node: Node,
) -> list[int]:
    if node is None:
        return

    print(node.value)
    pre_order(node.left)
    pre_order(node.right)


if __name__ == "__main__":
    root = Node(value=1)
    two = Node(value=2)
    three = Node(value=3)
    four = Node(value=4)
    five = Node(value=5)
    six = Node(value=6)
    ten = Node(value=10)
    eleven = Node(value=11)
    twenty_one = Node(value=21)

    """
     1
    / \
   /   \
  2     \
 / \     4
3   21   / \
       5   \
            6
           / \
          10  11
    """
    root.left = two
    root.right = four
    two.left = three
    two.right = twenty_one

    four.left = five
    four.right = six
    six.left = ten
    six.right = eleven
    pre_order(root)
