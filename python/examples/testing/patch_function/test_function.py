"""
python -m pytest test_function.py

python -m pytest test_function.py::test_the_function_no_patch
python -m pytest test_function.py::test_the_function_patched
"""
import the_function
from unittest import mock


def test_the_function_no_patch():
    return_value = the_function.function_to_be_tested()
    assert return_value != "this is not a test value"
    assert return_value == "this is the patched value"


@mock.patch("the_function.function_to_be_tested")
def test_the_function_patched(function_to_be_tested_mock):
    function_to_be_tested_mock.return_value = "this is the patched value"
    return_value = the_function.function_to_be_tested()
    assert return_value != "this is not a test value"
    assert return_value == "this is the patched value"


"""
python -m pytest test_function.py::test_the_function_no_patch
===== test session starts =====


test_function.py F                                                                                                                                                                                                          [100%] 

===== FAILURES ===== 
___________________________________________________________________________________________________ test_the_function_no_patch ___________________________________________________________________________________________________ 

    def test_the_function_no_patch():
        return_value = the_function.function_to_be_tested()
>       assert return_value != "this is not a test value"
E       AssertionError: assert 'this is not a test value' != 'this is not a test value'

test_function.py:10: AssertionError
===== short test summary info ===== 
FAILED test_function.py::test_the_function_no_patch - AssertionError: assert 'this is not a test value' != 'this is not a test value'
===== 1 failed in 0.20s ===== 



python -m pytest test_function.py::test_the_function_patched
===== test session starts =====

collected 1 item

test_function.py .                                                                                                                                                                                                          [100%] 

===== 1 passed in 0.08s ===== 
"""
