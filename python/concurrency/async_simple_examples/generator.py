def gen():
    counter = 0
    while counter < 10:
        yield counter
        counter += 1


g = gen()
print(type(g))

g.gi_running
g.gi_frame
# next print the function locals, there are not now:
g.gi_frame.f_locals

next(g)
g.gi_running
g.gi_frame
# next print the function locals, there are some now:
g.gi_frame.f_locals

g.gi_running


def gen_2():
    counter = 0
    while counter < 10:
        new_value = yield counter
        if new_value is not None:
            counter = new_value
        else:
            counter += 1


g2 = gen_2()

g2.gi_frame.f_locals
next(g2)
g2.send(2)