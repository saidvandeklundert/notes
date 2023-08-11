import ast, inspect, pprint


def some_function(a: int, b: int) -> int:
    return a * b


pprint.pprint(ast.dump(ast.parse(inspect.getsource(some_function))))


import dis

dis.dis(some_function)


source_code = """
def some_function(a: int, b: int) -> int:
    return a * b

x = 1
y = 2
z = some_function(x, y)
"""
dis.dis(source_code)

pprint.pprint(ast.dump(ast.parse(source_code)))


code_object = compile("a, b = 1000, 1000", filename="whatever.py", mode="single")
code_object.co_consts
