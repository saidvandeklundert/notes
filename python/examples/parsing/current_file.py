import os
import ast
from pprint import pprint

print("Current File Name : ", os.path.realpath(__file__))

with open(os.path.realpath(__file__), "r") as f:
    source = f.read()
tree = ast.parse(source=source)

pprint(ast.dump(tree))
