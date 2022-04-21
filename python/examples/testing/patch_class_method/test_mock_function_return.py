"""
Run the following to see the test result:
    python -m pytest test_mock_function_return.py


2 ways to patch the private method of a class.

1: using moch.patch.object:

@mock.patch.object(ReportGenerator, "_get_information_from_database")

2: using mock.patch:

@mock.patch("report_generator.ReportGenerator._get_information_from_database")

The difference is that 'mock.patch' takes a string which is resolved to an object when 
applying the patch whereas mock.patch.object() takes a direct reference.

https://stackoverflow.com/questions/29152170/what-is-the-difference-between-mock-patch-object-and-mock-patch

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


@mock.patch("report_generator.ReportGenerator._get_information_from_database")
def test_calculator_alternative_patch(_get_information_from_database_mock):
    """This patches the same method, just using a different approach"""
    _get_information_from_database_mock.return_value = [10, 10]
    report_generator = ReportGenerator()
    report = report_generator.generate_report()

    assert report == 20


@mock.patch("report_generator.ReportGenerator._get_information_from_database")
def test_calculator_alternative_patch_test_private_method(
    _get_information_from_database_mock,
):
    """Testing the private method directly, showcasing the effect of the patch."""
    _get_information_from_database_mock.return_value = [10, 10]
    assert ReportGenerator()._get_information_from_database() == [10, 10]


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
