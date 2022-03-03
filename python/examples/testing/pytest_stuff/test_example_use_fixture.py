"""
python -m pytest
"""


def test_example(api_call_return):
    assert isinstance(api_call_return, str)
