# See if string1 contains all we need to generate string2
# Select the array using the Selection Sort algorithm
tests = [
    ["Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"],
    ["     ", "     "],
    [
        "&*&you^a%^&8766 _=-09     docanCMakemthisdocument",
        "Can you make this document &",
    ],
    ["aehaolabbhb", "hello"],
    [" ", "hello"],
    ["A", "a"],
]


def generateDocument(characters, document):
    char_d = char_dict(characters)
    doc_d = char_dict(document)
    print(char_d)
    print(doc_d)
    for docd_c, docd_v in doc_d.items():
        chard_v = char_d.get(docd_c, 0)
        if docd_v > chard_v:
            return False

    return True


def char_dict(s):
    d = {}
    for c in s:

        if c in d:
            d[c] += 1
        else:

            d[c] = 1
    return d


if __name__ == "__main__":
    print("num1")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(generateDocument(test[0], test[1]))
