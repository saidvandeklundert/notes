from requests.exceptions import Timeout
from unittest.mock import Mock
import side_effect
import pytest

# python -m pytest .\test_side_effects.py::test_api_call


def test_api_call():
    """
    Test to ensure that the function under test will
    let a Timeout bubble up and return the proper result.

    This can be usefull in case we have other code in place
    that is triggered by a specific exception
    or other side effect.
    """
    side_effect.requests = Mock()
    side_effect.requests.get.side_effect = Timeout
    with pytest.raises(Timeout):

        response = side_effect.api_call()
        assert response is None


# python -m pytest .\test_side_effects.py::test_api_call_paginated


def test_api_call_paginated():
    """
    Test the assembly of a paginated response from an API.
    """
    expected = {
        "even_more_data": 3,
        "next_token": None,
        "some_additional_data": 2,
        "some_data": 1,
    }
    api_response_list = [
        Mock(**{"json.return_value": {"next_token": 1, "some_data": 1}}),
        Mock(**{"json.return_value": {"next_token": 2, "some_additional_data": 2}}),
        Mock(**{"json.return_value": {"next_token": None, "even_more_data": 3}}),
    ]
    side_effect.requests = Mock()
    side_effect.requests.get.side_effect = api_response_list

    response = side_effect.api_call_paginated()

    assert response == expected
