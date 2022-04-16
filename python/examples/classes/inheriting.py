"""
Instantiate a child and call the constructors of all the ancestors.
"""


class GrandFather:
    def __init__(self):
        print("GrandFather")
        self.grand_father = "GrandFather"

    def method_of_the_grand_father(self):
        print(self.grand_father)


class Father(GrandFather):
    def __init__(self):
        print("Father")
        self.father = "Father"
        super(Father, self).__init__()

    def method_of_the_father(self):
        print(self.grand_father)


class Child(Father):
    def __init__(self):
        print("Child")
        self.child = "Child"
        super(Child, self).__init__()

    def method_of_the_child(self):
        print(self.grand_father)


if __name__ == "__main__":
    child = Child()
