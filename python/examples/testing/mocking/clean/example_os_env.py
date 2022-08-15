import os
from unittest import mock


@mock.patch.dict(os.environ, {"SOME_VAR": "111"})
def test_os_mock():
    """
    We can patch a variety of things, in this case we
    patch a dict.
    """
    print(os.environ["SOME_VAR"])
    import pdb

    pdb.set_trace()

    assert os.environ["SOME_VAR"] == "111"
