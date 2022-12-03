# python -m mypy .\00_basic.py
from typing import List, Dict, Tuple, Union


# basics:
string: str = "string value"
integer: int = 1
floating_point: float = 1.2
boolean: bool = False


# sequences:
list_of_strings: List[str] = ["string 1", "string 2"]
list_of_integers: List[int] = [1, 2]

tuple_of_str_int: Tuple[str, int, bool] = ("string", 0, False)


# mappings:
dictionary: Dict = {}
dict_str_str: Dict[str, str] = {"string-key": "string-value"}
dict_int_bool: Dict[int, bool] = {1: False}
dict_str_list: Dict[str, List[str]] = {"key": ["string 1", "string 2"]}


# either this or that:
str_or_int_1: Union[str, int] = 1
str_or_int_2: Union[str, int] = "2"

list_of_stuff: List[Union[str, bool]] = [False, True, "string"]

dict_of_stuff: Dict[str, Union[str, int]] = {"key1": 1, "key2": "2"}
