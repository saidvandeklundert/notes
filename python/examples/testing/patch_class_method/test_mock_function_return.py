"""
python -m pytest test_mock_function_return.py
"""
from report_generator import ReportGenerator
from unittest import mock


def test_calculator_no_mock():
    """This function does not mock the private method that
    generate_report() depends on.

    Because of this, the test is taking quite some time."""
    report_generator = ReportGenerator()
    report = report_generator.generate_report()
    assert report == 20


@mock.patch.object(ReportGenerator, "_get_information_from_database")
def test_calculator(mock_my_method):
    """Here. we patch the time-consuming private method.
    Because of this, the test is run instantly."""
    mock_my_method.return_value = [10, 10]
    report_generator = ReportGenerator()
    report = report_generator.generate_report()
    assert report == 20


"""
The slow test that depends on the database:

    python -m pytest .\test_mock_function_return.py::test_calculator_no_mock

    test_mock_function_return.py::test_calculator_no_mock PASSED                        [100%] 

    ================ 1 passed in 5.14s ================ 

The patched test that has no dependancy on the database:

    python -m pytest .\test_mock_function_return.py::test_calculator_no_mock

    test_mock_function_return.py .                                                      [100%]

    ================ 1 passed in 5.15s ================
"""
