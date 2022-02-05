from patch_source import remove
from unittest import mock
import unittest

class RmTestCase(unittest.TestCase):
    
    # the following decorator will replace the 'os' module with a unittest.mock.MagicMock:
    @mock.patch('patch_source.os')
    def test_rm(self, mock_os):        
        remove("any path")
        # Instead of writing a unit test that actually removes a file,
        #  we verify we assert os.remove was called with the proper argument
        #   thus skipping the IO-heavy function and only testing the logic of our code.
        mock_os.remove.assert_called_with("any path")


if __name__ == '__main__':
    unittest.main()
