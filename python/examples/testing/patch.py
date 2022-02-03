"""
python -m pytest .\patch.py

Lisa Roach - Demystifying the Patch Function - PyCon 2018
https://www.youtube.com/watch?v=ww1UsGZV8fQ


https://speakerdeck.com/pycon2018


"""
from unittest import mock

# this patches the 'mock_dice_roll' object from 'mocking'
@mock.patch("mocking.mock_dice_roll")
def test_dice_roller_patched(mock_dice_roll):
    mock_dice_roll.return_value = 5
    assert mock_dice_roll() == 5


"""
Confusing things about patch:
1. Identifying the target
2. Multiple ways to call

1. Identifying the target

The target must be importable from the test file.

2. Multiple ways to call

Patch where the object is used.

For patch, scope matters.
"""