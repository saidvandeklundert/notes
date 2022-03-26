from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        array = list(range(n))

        print(array)
        array = [x + 1 for x in array]
        for i, v in enumerate(array):

            if array[i] / 3 == int(i / 3):
                if i / 5 == int(i / 5):
                    array[i] = "FizzBuzz"
                else:
                    array[i] = "Fizz"
            elif array[i] / 5 == int(i / 5):
                array[i] = "Buzz"
            else:
                array[i] = str(i)
        return array


def fizzBuzz(n: int) -> List[str]:
    array = []
    for number in range(n):
        number += 1
        if number / 3 == int(number / 3):
            if number / 5 == int(number / 5):
                array.append("FizzBuzz")
            else:
                array.append("Fizz")
        elif number / 5 == int(number / 5):
            array.append("Buzz")
        else:
            array.append(str(number))

    return array


if __name__ == "__main__":
    x = Solution()
    print(fizzBuzz(16))
