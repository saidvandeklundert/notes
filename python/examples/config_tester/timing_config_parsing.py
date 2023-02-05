import timeit


def read_into_lines():
    with open("configs/den4-fc-agg-t1-a-4.cfg", "rt") as f:
        lines = [line.rstrip() for line in f]
    return lines


starttime = timeit.default_timer()
print("The start time is :", starttime)
for _ in range(0, 1000):
    lines = read_into_lines()
print("Turning config into lines :", timeit.default_timer() - starttime)

starttime = timeit.default_timer()
print("The start time is :", starttime)
for _ in range(0, 1000):
    lines = read_into_lines()
    for line in lines:
        if "vlan" in line.lower():
            line = line.upper()
print("Do something for every line :", timeit.default_timer() - starttime)
