import copy

tests = [
    ["this", "that", "did", "deed", "them!", "a"],
]
# from biglists import tests


def minimumCharactersForWords(words):

    total_char_d = {}
    for word in words:
        word_d = {}
        for c in word:
            if c in word_d:
                word_d[c] += 1
            else:
                word_d[c] = 1

        for k, v in word_d.items():
            if k in total_char_d:
                if v > total_char_d[k]:
                    total_char_d[k] = v
            else:
                total_char_d[k] = v

    answer = []
    for k, v in total_char_d.items():
        extension = [k] * v
        answer.extend(extension)

    return answer


if __name__ == "__main__":
    print("num1")
    i = 0
    for test in tests:
        i += 1
        print(f"Test number {i}")
        print(minimumCharactersForWords(test))
