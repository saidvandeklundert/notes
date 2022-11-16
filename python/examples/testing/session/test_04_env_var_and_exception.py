import os
from unittest import mock
import pytest
from E04_ENV_VAR_EXCEPTION import operations


@mock.patch("E04_ENV_VAR_EXCEPTION.ENVIRONMENT")
def test_prod_return(patched_object):
    patched_object.stage = "PROD"
    resulting_operation = operations()
    assert resulting_operation == "Doing the things prod"


@mock.patch("E04_ENV_VAR_EXCEPTION.ENVIRONMENT")
def test_beta_return(patched_object):
    patched_object.stage = "BETA"
    resulting_operation = operations()
    assert resulting_operation == "Doing the things beta"


@mock.patch("E04_ENV_VAR_EXCEPTION.ENVIRONMENT")
def test_exception_return(patched_object):
    patched_object.stage = "UNKNOWN"
    with pytest.raises(RuntimeError):
        operations()
