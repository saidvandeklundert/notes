"""
Reverse an int and return the value. 

Return 0 if the int does not fit in an unsigned 32bit integer value.
"""


def reverse(x: int) -> int:
    if x == 0:
        return 0
    string_representation = str(x)
    string_representation_reversed = string_representation[::-1]

    if string_representation_reversed[-1] == "-":
        string_representation_reversed = "-" + string_representation_reversed[:-1]

    string_representation_reversed = string_representation_reversed.strip("0")
    int_reversed = int(string_representation_reversed)
    if int_reversed > 2147483648:
        return 0
    elif int_reversed < -2147483648:
        return 0
    else:
        return int_reversed


inputs = [123, -123, 120, 0, 2147483649]

for x in inputs:
    print(reverse(x))
