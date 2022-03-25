from functools import cached_property

"""
Notice how in the following, the propery is calculated only once:
"""


class Monopoly(object):
    def __init__(self):
        self.boardwalk_price = 500

    @cached_property
    def boardwalk(self):
        # Again, this is a silly example. Don't worry about it, this is
        #   just an example for clarity.
        self.boardwalk_price += 50
        return self.boardwalk_price


monopoly = Monopoly()
print(monopoly.boardwalk)
print(monopoly.boardwalk)
print(monopoly.boardwalk)


"""
Next is almost the same class, except for it being a regular property. 

In this case, it is calculated again and again.
"""


class Monopoly(object):
    def __init__(self):
        self.boardwalk_price = 500

    @property
    def boardwalk(self):
        # Again, this is a silly example. Don't worry about it, this is
        #   just an example for clarity.
        self.boardwalk_price += 50
        return self.boardwalk_price


monopoly = Monopoly()
print(monopoly.boardwalk)
print(monopoly.boardwalk)
print(monopoly.boardwalk)
