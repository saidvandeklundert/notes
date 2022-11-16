class MakeCallable:
    def __init__(self, x: int):
        self.x = x

    def __call__(self) -> None:
        print(vars(self))


if __name__ == "__main__":
    make_callable = MakeCallable(x=10)
    make_callable()
    make_callable.__call__()
