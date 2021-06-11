# Step through the coins and increment a value, currValue, with the value of every coin encountered.
# If the coin encountered is bigger then currValue +1, we cannot make the change and return currValue +1.
# If we can create all values, we cannot make a value bigger then the max of all coins combined,
# and we return currValue + 1.
tests = [
    [1, 2, 5],
    [5, 7, 1, 1, 2, 3, 22],
]


def nonConstructibleChange(coins: list[int]):
    coins.sort()
    currValue = 0
    for coin in coins:

        if coin > currValue + 1:
            return currValue + 1
        currValue += coin

    return currValue + 1


if __name__ == "__main__":
    print("num1")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(nonConstructibleChange(test))
