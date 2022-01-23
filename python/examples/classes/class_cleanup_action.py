class Human:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        # some cleanup code
        print(f"Cleaning up {self.name}")


def example():
    jan = Human("Jan")


# Notice how, as soon as the function is completed, the created instance is deleted and the
#  __del__ method is run
example()