import E05_weather_api
from unittest import mock


test_text = '{"region":"Dublin, County Dublin, Ireland","currentConditions":{"dayhour":"Tuesday 1:00 PM","temp":{"c":18,"f":65},"precip":"14%","humidity":"90%","wind":{"km":14,"mile":9},"iconURL":"https://ssl.gstatic.com/onebox/weather/64/rain.png","comment":"Rain"},"next_days":[{"day":"Tuesday","comment":"Rain","max_temp":{"c":26,"f":79},"min_temp":{"c":13,"f":55},"iconURL":"https://ssl.gstatic.com/onebox/weather/48/rain.png"},{"day":"Wednesday","comment":"Mostly cloudy","max_temp":{"c":21,"f":69},"min_temp":{"c":11,"f":52},"iconURL":"https://ssl.gstatic.com/onebox/weather/48/partly_cloudy.png"},{"day":"Thursday","comment":"Cloudy","max_temp":{"c":19,"f":66},"min_temp":{"c":12,"f":54},"iconURL":"https://ssl.gstatic.com/onebox/weather/48/cloudy.png"},{"day":"Friday","comment":"Partly cloudy","max_temp":{"c":19,"f":67},"min_temp":{"c":14,"f":57},"iconURL":"https://ssl.gstatic.com/onebox/weather/48/partly_cloudy.png"},{"day":"Saturday","comment":"Showers","max_temp":{"c":22,"f":72},"min_temp":{"c":17,"f":62},"iconURL":"https://ssl.gstatic.com/onebox/weather/48/rain_light.png"},{"day":"Sunday","comment":"Showers","max_temp":{"c":23,"f":74},"min_temp":{"c":15,"f":59},"iconURL":"https://ssl.gstatic.com/onebox/weather/48/rain_light.png"},{"day":"Monday","comment":"Showers","max_temp":{"c":21,"f":69},"min_temp":{"c":13,"f":55},"iconURL":"https://ssl.gstatic.com/onebox/weather/48/rain_light.png"},{"day":"Tuesday","comment":"Mostly cloudy","max_temp":{"c":19,"f":66},"min_temp":{"c":12,"f":53},"iconURL":"https://ssl.gstatic.com/onebox/weather/48/partly_cloudy.png"}],"contact_author":{"email":"communication.with.users@gmail.com","auth_note":"Mail me for feature requests, improvement, bug, help, ect... Please tell me if you want me to provide any other free easy-to-use API services"},"data_source":"https://www.google.com/search?lr=lang_en&q=weather+in+dublin"}'


@mock.patch.object(E05_weather_api.requests, "get")
def test_sunny_patched(request_mock):
    request_mock.get.text = test_text
    sunny_result = E05_weather_api.sunny("Dublin")
    assert sunny_result is False
