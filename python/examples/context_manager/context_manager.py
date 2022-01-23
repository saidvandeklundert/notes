# from python distilled


class ListTransaction:
    def __init__(self, thelist):
        self.thelist = thelist

    def __enter__(self):
        self.workingcopy = list(self.thelist)
        return self.workingcopy

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            self.thelist[:] = self.workingcopy
        return False


items = [1, 2, 3]
with ListTransaction(items) as working:
    working.append(4)
    working.append(5)

print(items)  # [1, 2, 3, 4, 5]

try:
    with ListTransaction(items) as working:
        working.append(6)
        working.append(7)
        raise RuntimeError("We are hosed!")
except RuntimeError as e:
    print(e)

print(items)
