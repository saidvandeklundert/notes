from binarytree import tree, bst

# Generate a random binary tree and return its root node.
my_tree = tree(height=3, is_perfect=False)

# Generate a random BST and return its root node.
my_bst = bst(height=3, is_perfect=True)


# Pretty-print the trees in stdout.
print(my_tree)
#
#        _______1_____
#       /             \
#      4__          ___3
#     /   \        /    \
#    0     9      13     14
#         / \       \
#        7   10      2
#
print(my_bst)
#
#            ______7_______
#           /              \
#        __3__           ___11___
#       /     \         /        \
#      1       5       9         _13
#     / \     / \     / \       /   \
#    0   2   4   6   8   10    12    14
#
