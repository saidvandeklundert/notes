"""
Dict comprehension pattern:

    {key:value for (key,value) in dictonary.items()}
"""

from typing import Any


d: dict = {
    "Netherland": "Amsterdam",
    "France": "Paris",
    "Greece": "Athens",
    "Belgium": "Brussels",
    "Germany": "Berlin",
}

dict_variable = {key: value for (key, value) in d.items()}
print(dict_variable)

dict_variable_2 = {key: value for (key, value) in d.items() if key.startswith("F")}

print(dict_variable_2)
