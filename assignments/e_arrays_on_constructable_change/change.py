inputs = [
    {"coins": [5, 7, 1, 1, 2, 3, 22]},
    {"coins": [1, 1, 1, 1, 1]},
    {"coins": [1, 5, 1, 1, 1, 10, 15, 20, 100]},
    {"coins": [6, 4, 5, 1, 1, 8, 9]},
    {"coins": []},
    {"coins": [87]},
    {"coins": [5, 6, 1, 1, 2, 3, 4, 9]},
    {"coins": [5, 6, 1, 1, 2, 3, 43]},
    {"coins": [1, 1]},
    {"coins": [2]},
    {"coins": [1]},
    {"coins": [109, 2000, 8765, 19, 18, 17, 16, 8, 1, 1, 2, 4]},
    {"coins": [1, 2, 3, 4, 5, 6, 7]},
    {"coins": [5, 7, 1, 1, 2, 3, 22]},  # 20
]


def nonConstructibleChange(coins):
    coins.sort()
    made_it_work = True
    tracker = 0
    while made_it_work:
        tracker += 1
        can_create = tracker
        made_it_work = False
        for i in coins:
            can_create -= i
            if can_create == 0:
                made_it_work = True

    return tracker


def faster(coins):
    coins.sort()
    currentChangeCreated = 0

    for coin in coins:
        # if the next step is bigger then what we have so far +1,
        #  we have a gap and return out of the func:
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1
        currentChangeCreated += coin

    return currentChangeCreated + 1


if __name__ == "__main__":
    for test in inputs:

        print(nonConstructibleChange(**test))
        print(faster(**test))
        print(50 * "_")
