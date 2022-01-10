from memory_profiler import profile


class TestA(object):
    __slots__ = ["a", "b", "c"]

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class TestB(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


@profile
def test():
    temp = [TestA(i, i + 1, i + 2) for i in range(10000)]
    del temp
    temp = [TestB(i, i + 1, i + 2) for i in range(10000)]
    del temp


if __name__ == "__main__":
    test()