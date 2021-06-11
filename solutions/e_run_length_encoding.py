tests = [
    "AAAAAAAAAAAAABBCCCCDD",
    "AAAAAAAAAAAAABBCCCCDDEEEEEE",
    "........______=========AAAA   AAABBBB   BBB",
]


def runLengthEncoding2(string):
    s = ""
    cur = []
    for c in string:
        if len(cur) == 0:
            cur.append(c)
        elif c in cur and len(cur) < 9:
            cur.append(c)

        elif c in cur and len(cur) >= 9:
            s = s + str(len(cur)) + c
            cur = [c]

        elif c not in cur:
            s = s + str(len(cur)) + cur[0]
            cur = [c]
    else:
        s = s + str(len(cur)) + cur[0]
    return s


def runLengthEncoding(string):
    encoded = []
    currLength = 1

    for i in range(1, len(string)):
        currentCharacter = string[i]
        previousCharacter = string[i - 1]

        if currentCharacter != previousCharacter or currLength == 9:
            encoded.append(str(currLength))
            encoded.append(previousCharacter)
            currLength = 0

        currLength += 1

    encoded.append(str(currLength))
    encoded.append(string[len(string) - 1])

    return "".join(encoded)


if __name__ == "__main__":
    print("num1")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(runLengthEncoding(test))
