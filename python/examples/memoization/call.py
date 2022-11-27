from collections import defaultdict

# keeps track of how many times something was called
class CallCount:
    def __init__(self):
        self._counts = defaultdict(int)

    def __call__(self, argument):
        self._counts[argument] += 1
        return self._counts[argument]


cc = CallCount()
cc(1)
cc(1)
cc(1)
