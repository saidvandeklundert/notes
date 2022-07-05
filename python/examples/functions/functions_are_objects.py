def f1(x: int):
    print(f"f1 {x}")


def f2(x: int):
    print(f"f2 {x}")


def f3(x: int):
    print(f"f3 {x}")


def f4(x: int):
    print(f"f4 {x}")


func_list = [f1, f2, f3, f4]

for f in func_list:
    f(1)
