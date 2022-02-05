"""A mock object substitutes a real object in a testing environment.

The mock object also contains information on it's usage during testing.


python -m pytest .\mocking_a_function.py

python .\mocking_a_function.py

"""
# the function to mock:
import random

def dice_roll():
    return random.randint(1,6)

print(dice_roll())
print(dice_roll())

# makin the mock:
from unittest.mock import Mock
mock_dice_roll = Mock(name="my_first_mock", return_value=3)

# call the mock:
print(mock_dice_roll())

# print the times we used the mock:
print(mock_dice_roll.called)
print("times we called the mock: " ,mock_dice_roll.call_count)

print(mock_dice_roll())
print("times we called the mock: " ,mock_dice_roll.call_count)



