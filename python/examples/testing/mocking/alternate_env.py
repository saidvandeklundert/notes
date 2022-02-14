import os
from unittest import TestCase, mock
import unittest

def some_func():
    if os.getenv("SOME_VAR"):
        return os.getenv("SOME_VAR")
    else:
        return "yolo"

class SettingsTests(TestCase):
    @mock.patch.dict(os.environ, {"SOME_VAR": "XXXXXX"})
    def test_get_actual_env_root_alternate_env(self):
        ret = some_func()
        print("test_get_actual_env_root_alternate_env", ret)
        assert isinstance(ret, str)
        assert "XXXXXX" in ret

    def test_some_func(self):
        ret = some_func()
        print("test_some_func", ret)
        assert isinstance(ret, str)
        assert "yolo" in ret


if __name__ == "__main__":
    unittest.main()
