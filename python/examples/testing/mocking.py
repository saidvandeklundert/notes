"""
python -m pytest .\mocking.py
"""
import random

def dice_roll():
    return random.randint(1,6)
#
from unittest import mock
print(dice_roll())
print(dice_roll())

mock_dice_roll = mock.Mock(name="my_first_mock", return_value=3)
print(mock_dice_roll())
print(mock_dice_roll())

print(mock_dice_roll.called)
print("times we called the mock: " ,mock_dice_roll.call_count)

print(mock_dice_roll())
print(mock_dice_roll())
print("times we called the mock: " ,mock_dice_roll.call_count)



