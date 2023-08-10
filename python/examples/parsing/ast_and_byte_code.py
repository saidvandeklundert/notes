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
