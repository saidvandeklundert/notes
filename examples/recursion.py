def recurse(i: int):
    if i >= 10:  # base case
        print("done recursing")
        return i
    else:  # recursive case
        i += 1
        print(f"recursing, {i} still smaller then 10")
        recurse(i)


if __name__ == "__main__":
    import sys

    i = int(sys.argv[1])
    recurse(i)
