"""Some functions used in other examples to illustrate mock/patch"""
import os
import requests
from datetime import datetime
import random

def dice_roll():
    return random.randint(1,6)
    

def is_weekday():
    today = datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return (0 <= today.weekday() < 5)

def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def talk_about_holiday(self)->str:
        result = requests.get('http://localhost/api/holidays')

        return f"{self.name} went to {result}"


def remove(path:str):
    os.remove(path)