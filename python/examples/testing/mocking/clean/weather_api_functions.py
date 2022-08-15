import requests
from typing import Union


def sunny(location: str) -> bool:
    """Returns a boolean, indicating whether or not it is sunny
    at target location."""
    url = f"https://weatherdbi.herokuapp.com/data/weather/{location}"
    api_response_str = requests.get(url)
    api_response_d = api_response_str.json()

    if "sunny" in api_response_d["currentConditions"]["comment"].lower():
        return True
    else:
        return False


def open_weather(api_key, city_name) -> Union[dict, bool]:
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        current_temperature = data["main"]["temp"]
        current_pressure = data["main"]["pressure"]
        current_humidity = data["main"]["humidity"]
        weather_description = data["weather"][0]["description"]
        return {
            "temperature": current_temperature,
            "atmospheric pressure": current_pressure,
            "humidity": current_humidity,
            "description": weather_description,
        }

    else:
        return False


if __name__ == "__main__":
    print(open_weather("2d9ec7886d0ac683aba79852f269ce5d", "dublin"))
