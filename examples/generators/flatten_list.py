def flatten(items):
    stack = [iter(items)]

    while stack:
        try:
            item = next(stack[-1])
            if isinstance(item, list):
                stack.append(iter(item))
            else:
                yield item
        except StopIteration:
            stack.pop()


if __name__ == "__main__":
    nested_list = [1, 2, [3, 4, [5, 6], 7], 8]
    flat = list(flatten(nested_list))
    print(nested_list)
    print(flat)