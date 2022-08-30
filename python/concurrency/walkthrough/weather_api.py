import requests
from typing import Union
from concurrent.futures import ThreadPoolExecutor
from concurrent import futures
from datetime import datetime


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


def example_process_pool(api_key, cities):
    fut: list[futures.Future] = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        for city in cities:
            fut.append(executor.submit(open_weather, api_key, city))
    print("All threads are done.")

    # focus on the requests that succeeded:
    for future in fut:
        resp = future.result()
        print("multi", resp)


if __name__ == "__main__":
    cities = [
        "dublin",
        "rome",
        "paris",
        "amsterdam",
        "london",
        "sydney",
        "berlin",
        "rotterdam",
        "madrid",
        "brussels",
        "antwerp",
        "tokyo",
        "kyoto",
    ] * 5
    api_key = "2d9ec7886d0ac683aba79852f269ce5d"

    startTime = datetime.now()
    for city in cities:
        print("single", open_weather(api_key, city))
    single_thread_duration = datetime.now() - startTime

    print("multithreaded:")
    startTime = datetime.now()
    example_process_pool(api_key, cities)
    multi_thread_duration = datetime.now() - startTime
    print(f"single threaded took {single_thread_duration}")
    print(f"multi threaded took {multi_thread_duration}")
    print("fin.")
