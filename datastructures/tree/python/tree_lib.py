from treelib import Node, Tree

tree = Tree()
tree.create_node("ceo", "ceo")  # root
tree.create_node("vp1", "vp1", parent="ceo")
tree.create_node("vp2", "vp2", parent="ceo")
tree.create_node("gm1", "gm1", parent="vp1")
tree.create_node("gm2", "gm2", parent="vp2")


print(tree.show())
