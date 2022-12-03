inputs = [
    {"string": "AlgoExpert is the best!"},
    {"string": "Reverse These Words"},
    {"string": "..H,, hello 678"},
    {"string": "this this words this this this words this"},
    {"string": "1 12 23 34 56"},
    {"string": "APPLE PEAR PLUM ORANGE"},
    {"string": "this-is-one-word"},
    {"string": "a"},
    {"string": "ab"},
    {"string": ""},
    {
        "string": "algoexpert is the best platform to use to prepare for coding interviews!"
    },
    {"string": "words, separated, by, commas"},
    {"string": "this      string     has a     lot of   whitespace"},
    {"string": "a ab a"},
    {"string": "test        "},
    {"string": " "},
    {"string": "AlgoExpert is the best!"},
    {"string": "test        "},
    {"string": " "},
]


def reverseWordsInString(string: str):
    words = []
    start_of_word = 0

    for idx in range(len(string)):
        char = string[idx]

        # this marks the end of a word, so we slice up untill the previous index:
        if char == " ":
            # this is a slice up to, but not including idx:
            #   l = [0,1,2]
            #   l[0:2]
            #   >>> [0,1] < the 2 here is missing!
            word = string[start_of_word:idx]
            print(f"appending word -{word}-")
            print("words now", words)
            words.append(word)
            start_of_word = idx
        # adding a space to the words list
        elif string[start_of_word] == " ":
            words.append(" ")
            start_of_word = idx
    words.append(string[start_of_word:])

    reverse_list(words)
    return "".join(words)


def reverse_list(a_list):
    start, end = 0, len(a_list) - 1
    while start < end:
        a_list[start], a_list[end] = a_list[end], a_list[start]
        start += 1
        end -= 1


def reverseWordsInString_slow(string):
    # print(string)

    string_in_reverse = " ".join([x for x in reversed(string.split())])
    spaces = []
    to_add = ""
    for i in string:
        # print(f"-{i}-")
        if i == " ":
            to_add += " "
        else:
            if len(to_add) > 0:
                spaces.append(to_add)
                to_add = ""
    if to_add:
        spaces.append(to_add)
    # print(f"to_add: {to_add}-")
    words = []
    word = ""
    for i in string:
        if i != " ":
            word += i
        else:
            if len(word) > 0:
                words.append(word)
                word = ""
    else:
        words.append(word)

    # print("spaces", spaces)
    # print("words", words)
    counter = len(words) - 1
    new_string = []
    if len(spaces) > 0:
        if string[-1] == " ":
            new_string.append(spaces.pop())
    while counter >= 0:

        word_to_add: str = words[counter]
        new_string.append(word_to_add)
        # print(new_string)
        if len(spaces) > 0:
            new_string.append(spaces.pop())
        counter -= 1
    new_str = "".join(new_string)
    # print(f"new_str: {new_str}-")
    return new_str


if __name__ == "__main__":
    for test in inputs:
        print(reverseWordsInString(**test))
        print(reverseWordsInString_slow(**test))
        print(50 * "_")
