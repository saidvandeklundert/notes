import database_example
from unittest import mock


# 1: examle with a function:
# python -m pytest test_database_example.py::test_get_report


def test_get_report():
    """
    When unpatched:
    - the function takes a long time. With hundreds of tests,
     this becomes a drag.
    - we do not know the actual return value, as live database
     data varies from time to time.
    - part of the test might be redundant. Tests that store andc
     fetch data from the database might already be in place elsewhere.

    """
    return_value = database_example.get_report()
    assert return_value == "100"


# python -m pytest test_database_example.py::test_get_report_patched
@mock.patch("database_example.get_database_data")
def test_get_report_patched(patched_function):
    """
    This patched version:
    - tests the logic in place for the calcucations
    - runs in a few milliseconds

    Even though we are using a patch instead of the real database,
    we still cover all our business logic and we can confidently
    make changes to the calculations in our report.
    """
    patched_function.return_value = [4324, 2341, 2324, 2424]
    return_value = database_example.get_report()
    assert return_value == 2853


# 2: examle with a class:
# python -m pytest test_database_example.py::test_report_generator_no_mock


def test_report_generator_no_mock():
    """
    Same issues as with 'test_get_report'.

    Only in this case, the report is not a function, it is a method
    in a class.

    """
    report_generator = database_example.ReportGenerator()
    report = report_generator.generate_report()
    assert report == 20


# python -m pytest test_database_example.py::test_report_generator_patched


@mock.patch.object(database_example.ReportGenerator, "_get_database_data")
def test_report_generator_patched(mock_my_method):
    """

    Now, we patch the time-consuming private method.
    Because of this, the test is run instantly.

    Notice we use 'patch.object' instead of just 'patch'.
    """
    mock_my_method.return_value = [4324, 2341, 2324, 2424]
    report_generator = database_example.ReportGenerator()
    report = report_generator.generate_report()
    assert report == 2853


# python -m pytest test_database_example.py::test_and_see


@mock.patch.object(database_example.ReportGenerator, "_get_database_data")
def test_and_see(mock_my_method):
    """Here. we patch the time-consuming private method.

    But instead of running the test, we drop to REPL.

    This way, we can check and see what is going on.
    """
    mock_my_method.return_value = [4324, 2341, 2324, 2424]

    report_generator = database_example.ReportGenerator()
    report = report_generator.generate_report()

    import pdb

    pdb.set_trace()
    assert report == 2853


"""
Check the report_generator:
>>> dir(report_generator)
[
    "_get_database_data",
    "generate_report",
]

>>> type(report_generator.generate_report)      
<class 'method'>

>>> type(report_generator._get_database_data) 
<class 'unittest.mock.MagicMock'>


Check the patched method:
>>> dir(report_generator._get_database_data)
[
    "assert_any_call",
    "assert_called",
    "assert_called_once",
    "assert_called_once_with",
    "assert_called_with",
    "assert_has_calls",
    "assert_not_called",
    "attach_mock",
    "call_args",
    "call_args_list",
    "call_count",
    "called",
    "configure_mock",
    "method_calls",
    "mock_add_spec",
    "mock_calls",
    "reset_mock",
    "return_value",
    "side_effect",
]
"""
