from typing import Tuple, Union

Result = Union[Tuple[str, str, dict], Tuple[str, str]]
from pydantic import BaseModel


class Res(BaseModel):
    res: Result


def result_tuple(
    status: str, message: str, *format_parameters, **kwargs
) -> tuple[str, str, dict] | tuple[str, str]:
    print("format_paramaters", format_parameters)
    print("kwargs", kwargs)
    if "data" in kwargs:
        print("DATA IN HERE")
        data = (kwargs["data"],)
    else:
        data = ()

    if not format_parameters:
        return (status, message) + data
    print("data", data)
    return (status, message.format(*format_parameters)) + data


result_tuple("PASS", "something went well", 1, 1, {"data": 1}, name=1)
result_tuple("PASS", "something went well", {"data": 1})
result_tuple("PASS", "something went well")
