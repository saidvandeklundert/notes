import requests


def test_room_1():
    api_url = "http://127.0.0.1:8000/room/1"
    response = requests.get(api_url)
    print(response.json())
    print(type(response.json()))
    assert response.json() == {"price": 15000, "id": 1, "number": "101", "size": 10}


def test_rooms():
    api_url = "http://127.0.0.1:8000/rooms"
    response = requests.get(api_url)
    print(response.json())
    print(type(response.json()))
    assert response.json() == [
        {"price": 15000, "id": 1, "number": "101", "size": 10},
        {"price": 15000, "id": 2, "number": "102", "size": 10},
        {"price": 25000, "id": 3, "number": "103", "size": 20},
        {"price": 25000, "id": 4, "number": "104", "size": 20},
        {"price": 35000, "id": 5, "number": "105", "size": 30},
    ]


def test_customer_1():
    api_url = "http://127.0.0.1:8000/customer/1"
    response = requests.get(api_url)
    print(response.json())
    print(type(response.json()))
    assert response.json() == {
        "last_name": "Smith",
        "first_name": "John",
        "id": 1,
        "email_address": "email@email.com",
    }


def test_customers():
    api_url = "http://127.0.0.1:8000/customers"
    response = requests.get(api_url)
    print(response.json())
    print(type(response.json()))
    assert response.json() == [
        {
            "last_name": "Smith",
            "first_name": "John",
            "id": 1,
            "email_address": "email@email.com",
        },
        {
            "last_name": "Doe",
            "first_name": "Jane",
            "id": 2,
            "email_address": "jane@hotmail.com",
        },
        {
            "last_name": "Black",
            "first_name": "Jack",
            "id": 3,
            "email_address": "jack@black.com",
        },
        {
            "last_name": "White",
            "first_name": "Jill",
            "id": 4,
            "email_address": "jill@gmail.com",
        },
        {
            "last_name": "Codes",
            "first_name": "Arjan",
            "id": 5,
            "email_address": "hi@arjancodes.com",
        },
    ]
