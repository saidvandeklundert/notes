import inspect


def __line__():
    return inspect.currentframe().f_back.f_lineno


print(f"I am {__file__} on line {__line__()}.")


def main():
    print("running main.")
    print(f"I am {__file__} on line {__line__()}.")


if __name__ == "__main__":
    main()
