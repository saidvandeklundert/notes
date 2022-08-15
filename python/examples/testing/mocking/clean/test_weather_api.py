import weather_api_functions
from unittest import mock

# python -m pytest test_weather_api.py::test_open_weather


def test_open_weather():
    api_key = "2d9ec7886d0ac683aba79852f269ce5d"
    response = weather_api_functions.open_weather(api_key, "dublin")
    assert isinstance(response, dict)


# python -m pytest test_weather_api.py::test_sunny_no_mock


def test_sunny_no_mock():
    """
    Makes an actual API call. Several problems here:
    - the service might be down, stalling our CICD
    - we do not know the weather when we run the function
    - we cannot test all conditions
    - it is relatively slow
    """
    sunny_result = weather_api_functions.sunny("Dublin")
    assert sunny_result is False


test_text = '{"region":"Dublin, County Dublin, Ireland","currentConditions":{"dayhour":"Tuesday 1:00 PM","temp":{"c":18,"f":65},"precip":"14%","humidity":"90%","wind":{"km":14,"mile":9},"iconURL":"https://ssl.gstatic.com/onebox/weather/64/rain.png","comment":"Rain"},"next_days":[{"day":"Tuesday","comment":"Rain","max_temp":{"c":26,"f":79},"min_temp":{"c":13,"f":55},"iconURL":"https://ssl.gstatic.com/onebox/weather/48/rain.png"},{"day":"Wednesday","comment":"Mostly cloudy","max_temp":{"c":21,"f":69},"min_temp":{"c":11,"f":52},"iconURL":"https://ssl.gstatic.com/onebox/weather/48/partly_cloudy.png"},{"day":"Thursday","comment":"Cloudy","max_temp":{"c":19,"f":66},"min_temp":{"c":12,"f":54},"iconURL":"https://ssl.gstatic.com/onebox/weather/48/cloudy.png"},{"day":"Friday","comment":"Partly cloudy","max_temp":{"c":19,"f":67},"min_temp":{"c":14,"f":57},"iconURL":"https://ssl.gstatic.com/onebox/weather/48/partly_cloudy.png"},{"day":"Saturday","comment":"Showers","max_temp":{"c":22,"f":72},"min_temp":{"c":17,"f":62},"iconURL":"https://ssl.gstatic.com/onebox/weather/48/rain_light.png"},{"day":"Sunday","comment":"Showers","max_temp":{"c":23,"f":74},"min_temp":{"c":15,"f":59},"iconURL":"https://ssl.gstatic.com/onebox/weather/48/rain_light.png"},{"day":"Monday","comment":"Showers","max_temp":{"c":21,"f":69},"min_temp":{"c":13,"f":55},"iconURL":"https://ssl.gstatic.com/onebox/weather/48/rain_light.png"},{"day":"Tuesday","comment":"Mostly cloudy","max_temp":{"c":19,"f":66},"min_temp":{"c":12,"f":53},"iconURL":"https://ssl.gstatic.com/onebox/weather/48/partly_cloudy.png"}],"contact_author":{"email":"communication.with.users@gmail.com","auth_note":"Mail me for feature requests, improvement, bug, help, ect... Please tell me if you want me to provide any other free easy-to-use API services"},"data_source":"https://www.google.com/search?lr=lang_en&q=weather+in+dublin"}'

# python -m pytest test_weather_api.py::test_sunny_patched


@mock.patch.object(weather_api_functions.requests, "get")
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
    sunny_result = weather_api_functions.sunny("Dublin")
    assert sunny_result is False
