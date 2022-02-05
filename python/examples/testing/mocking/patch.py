"""
python -m pytest .\patch.py

"""
from unittest import mock

# this patches the 'mock_dice_roll' object from 'mocking'
@mock.patch("patch_source.dice_roll")
def test_dice_roller_patched(mock_dice_roll):
    #import pdb; pdb.set_trace()
    #print(type(mock_dice_roll))
    
    # the mock_dice_roll is of the type unittest.mock.MagicMock
    # we specify the return value when we call the function:    
    mock_dice_roll.return_value = 5
    
    # we assert the function returns 5:
    assert mock_dice_roll() == 5


