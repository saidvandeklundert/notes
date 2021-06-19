# function that shifts a number by shifting a codepoint, wrapping around the aplpabet.
# func("a", 1) should become "b"
# func("xyz", 2) should become "zab"
tests = [
    ["xyz", 2],
    ["abc", 122],
]


def caesarCipherEncryptor(string: str, key: int):
    new_string = []
    for c in string:
        a = key % 26 + ord(c)
        if a > 122:
            a = a - 122 + 96
        new_char = chr(a)
        new_string.append(new_char)
    return "".join(new_string)


def caesarCipherEncryptor2(string: str, key: int):
    new_string = []
    key = key % 26
    for c in string:
        nlc = ord(c) + key
        if nlc <= 122:
            new_char = chr(nlc)
            new_string.append(new_char)
        else:
            print("nlc", nlc)
            nlc = nlc + 96 - 122

            new_char = chr(nlc)
            new_string.append(new_char)

    return "".join(new_string)


def caesarCipherEncryptor3(string: str, key: int):
    byPc = {n + 1: x for n, x in enumerate("abcdefghijklmnopqrstuvwxyz")}
    byCh = {x: n + 1 for n, x in enumerate("abcdefghijklmnopqrstuvwxyz")}
    key = key % 26

    ret = []
    for c in string:
        pc = byCh[c]
        pc = pc + key
        pc = pc if pc < 27 else pc - 26

        nc = byPc[pc]
        ret.append(nc)
    return "".join(ret)


if __name__ == "__main__":
    print("num1")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(caesarCipherEncryptor(test[0], test[1]))
    print("num2")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(caesarCipherEncryptor2(test[0], test[1]))
    print("num3")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(caesarCipherEncryptor3(test[0], test[1]))
    # testing(tests[0])
