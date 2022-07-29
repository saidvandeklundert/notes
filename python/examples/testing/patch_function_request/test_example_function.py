"""
python -m pytest test_example_function.py


python -m pytest test_example_function.py::test_the_function_no_patch
python -m pytest test_example_function.py::test_the_function_patched
python -m pytest test_example_function.py::sunny

"""
import example_functions
from unittest import mock

##
# 1: examle with a function:
#
# python -m pytest test_example_function.py::test_the_function_no_patch
# python -m pytest test_example_function.py::test_the_function_patched
##


def test_the_function_no_patch():
    return_value = example_functions.get_item_from_database()
    assert return_value == "100"


@mock.patch("example_functions.get_item_from_database")
def test_the_function_patched(patched_function):
    patched_function.return_value = "this is the patched value"
    return_value = example_functions.get_item_from_database()
    assert return_value == "this is the patched value"


##
# 2: examle with a class:
#
# python -m pytest test_example_function.py::test_calculator_no_mock
# python -m pytest test_example_function.py::test_calculator_patched
##


def test_calculator_no_mock():
    """This function does not mock the private method that
    generate_report() depends on.

    Because of this, the test is taking quite some time."""
    report_generator = example_functions.ReportGenerator()
    report = report_generator.generate_report()
    assert report == 20


@mock.patch.object(example_functions.ReportGenerator, "_get_information_from_database")
def test_calculator_patched(mock_my_method):
    """Here. we patch the time-consuming private method.
    Because of this, the test is run instantly."""
    mock_my_method.return_value = [10, 10]
    report_generator = example_functions.ReportGenerator()
    report = report_generator.generate_report()
    assert report == 20


##
# 2: examle with a fnction calling an API:
#
# python -m pytest test_example_function.py::test_sunny_no_mock
# python -m pytest test_example_function.py::test_sunny_patched
##


def test_sunny_no_mock():
    """
    Makes an actual API call. Several problems here:
    - service can be down
    - we do not know the weater when it is run
    - it is (relatively) slow
    """
    sunny_result = example_functions.sunny("Dublin")
    assert sunny_result is False


test_text = '{"region":"Dublin, County Dublin, Ireland","currentConditions":{"dayhour":"Tuesday 1:00 PM","temp":{"c":18,"f":65},"precip":"14%","humidity":"90%","wind":{"km":14,"mile":9},"iconURL":"https://ssl.gstatic.com/onebox/weather/64/rain.png","comment":"Rain"},"next_days":[{"day":"Tuesday","comment":"Rain","max_temp":{"c":26,"f":79},"min_temp":{"c":13,"f":55},"iconURL":"https://ssl.gstatic.com/onebox/weather/48/rain.png"},{"day":"Wednesday","comment":"Mostly cloudy","max_temp":{"c":21,"f":69},"min_temp":{"c":11,"f":52},"iconURL":"https://ssl.gstatic.com/onebox/weather/48/partly_cloudy.png"},{"day":"Thursday","comment":"Cloudy","max_temp":{"c":19,"f":66},"min_temp":{"c":12,"f":54},"iconURL":"https://ssl.gstatic.com/onebox/weather/48/cloudy.png"},{"day":"Friday","comment":"Partly cloudy","max_temp":{"c":19,"f":67},"min_temp":{"c":14,"f":57},"iconURL":"https://ssl.gstatic.com/onebox/weather/48/partly_cloudy.png"},{"day":"Saturday","comment":"Showers","max_temp":{"c":22,"f":72},"min_temp":{"c":17,"f":62},"iconURL":"https://ssl.gstatic.com/onebox/weather/48/rain_light.png"},{"day":"Sunday","comment":"Showers","max_temp":{"c":23,"f":74},"min_temp":{"c":15,"f":59},"iconURL":"https://ssl.gstatic.com/onebox/weather/48/rain_light.png"},{"day":"Monday","comment":"Showers","max_temp":{"c":21,"f":69},"min_temp":{"c":13,"f":55},"iconURL":"https://ssl.gstatic.com/onebox/weather/48/rain_light.png"},{"day":"Tuesday","comment":"Mostly cloudy","max_temp":{"c":19,"f":66},"min_temp":{"c":12,"f":53},"iconURL":"https://ssl.gstatic.com/onebox/weather/48/partly_cloudy.png"}],"contact_author":{"email":"communication.with.users@gmail.com","auth_note":"Mail me for feature requests, improvement, bug, help, ect... Please tell me if you want me to provide any other free easy-to-use API services"},"data_source":"https://www.google.com/search?lr=lang_en&q=weather+in+dublin"}'


@mock.patch.object(example_functions.requests, "get")
def test_sunny_patched(request_mock):
    """
    The patched version has some benefits:
    - always has the same results
    - runs very quickly
    - we focus on testing our code instead of the request module

    Downsides are that we do not take into consideration all
    sorts of failure scenarios.
    """
    request_mock.get.text = test_text
    sunny_result = example_functions.sunny("Dublin")
    assert sunny_result is False
