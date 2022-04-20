"""
python -m pytest example.py
"""
import os
from unittest import TestCase, mock
import unittest


def some_func():
    if os.getenv("ENV_A") == "AAAAA":
        return "run microservice a"
    elif os.getenv("ENV_B") == "BBBBB":
        return "run microservice b"
    else:
        return "no env var"


@mock.patch.dict(os.environ, {"ENV_A": "AAAAA"})
def test_env_a_set():
    """
    Here we test some_func with os.environ "ENV_A" returning "AAAAA"
    """
    ret = some_func()
    assert isinstance(ret, str)
    assert "run microservice a" == ret


@mock.patch.dict(os.environ, {"ENV_B": "BBBBB"})
def test_env_b_set():
    """
    Here we test some_func with os.environ "ENV_B" returning "BBBBB"
    """
    ret = some_func()
    assert isinstance(ret, str)
    assert "run microservice b" == ret


@mock.patch.dict(os.environ, {})
def test_absent_env():
    """
    Here we test some_func with no env variables
    """
    ret = some_func()
    assert isinstance(ret, str)
    assert "no env var" == ret
