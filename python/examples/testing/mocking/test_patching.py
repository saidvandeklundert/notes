"""
https://realpython.com/python-mock-library/#patch
"""
import unittest
from patch_source import get_holidays
from requests.exceptions import Timeout
from unittest.mock import patch

class TestCalendar(unittest.TestCase):
    # the patch decorator passes the mock_requests argument into the method
    #  this argument is of type https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock
    @patch('patch_source.requests') 
    def test_get_holidays_timeout(self, mock_requests):
            #import pdb; pdb.set_trace()
            print(f"mock_requests is of type {type(mock_requests)} and has the following methods:")
            for method in dir(mock_requests):
                print(f"    {method}")
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()

    # instead of using the patch decorator, we use the context manager here:
    def test_get_holidays_timeout_context_manager(self):
        with patch('patch_source.requests') as mock_requests:
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()   
    """
    Next example is where we patch Human and set the return value for a method of that class.
    """
    @patch('patch_source.Human') 
    def test_human_on_holiday(self, mock_human):            
            print(f"mock_requests is of type {type(mock_human)} and has the following methods:")
            for method in dir(mock_human):
                print(f"    {method}")
            mock_human.talk_about_holiday.return_value = "Jan went to Spain"
            print(mock_human.talk_about_holiday())
            assert "Spain" in mock_human.talk_about_holiday()                              

if __name__ == '__main__':
    unittest.main()
