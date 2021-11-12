import itertools as it

inputs = [
    {"intervals": [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]},
    {"intervals": [[1, 3], [2, 8], [9, 10]]},
    {
        "intervals": [
            [1, 10],
            [10, 20],
            [20, 30],
            [30, 40],
            [40, 50],
            [50, 60],
            [60, 70],
            [70, 80],
            [80, 90],
            [90, 100],
        ]
    },
    {
        "intervals": [
            [1, 10],
            [11, 20],
            [21, 30],
            [31, 40],
            [41, 50],
            [51, 60],
            [61, 70],
            [71, 80],
            [81, 90],
            [91, 100],
        ]
    },
    {"intervals": [[100, 105], [1, 104]]},
    {"intervals": [[89, 90], [-10, 20], [-50, 0], [70, 90], [90, 91], [90, 95]]},
    {"intervals": [[-5, -4], [-4, -3], [-3, -2], [-2, -1], [-1, 0]]},
    {"intervals": [[43, 49], [9, 12], [12, 54], [45, 90], [91, 93]]},
    {"intervals": [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]},
    {"intervals": [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1]]},
    {"intervals": [[1, 22], [-20, 30]]},
    {
        "intervals": [
            [20, 21],
            [22, 23],
            [0, 1],
            [3, 4],
            [23, 24],
            [25, 27],
            [5, 6],
            [7, 19],
        ]
    },
    {"intervals": [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]},
    {"intervals": [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]},
    {"intervals": [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]},
]


def mergeOverlappingIntervals(intervals):
    intervals_sorted = sorted(intervals, key=lambda x: x[0])
    merged_intervals = []
    currentInterval = intervals_sorted[0]
    merged_intervals.append(currentInterval)

    for nextInterval in intervals_sorted:
        _, currentIntervalEnd = currentInterval
        nextIntervalStart, nextIntervalEnd = nextInterval

        if currentIntervalEnd >= nextIntervalStart:
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
        else:
            currentInterval = nextInterval
            merged_intervals.append(currentInterval)
    return merged_intervals


if __name__ == "__main__":
    for test in inputs:
        print(mergeOverlappingIntervals(**test))

        print(50 * "_")
