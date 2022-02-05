# from realpython:
"""
python -m pytest .\mock_side_effect.py

python .\mock_side_effect.py
"""
import unittest
from requests.exceptions import Timeout
from unittest.mock import Mock

# Mock requests to control its behavior
requests = Mock()

# the function under test:
def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None

# the test class where we verify what happens during timeout:
class TestCalendar(unittest.TestCase):

    def test_get_holidays_timeout(self):
        # Test a connection timeout by setting a side effect:
        requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()

if __name__ == '__main__':
    unittest.main()
