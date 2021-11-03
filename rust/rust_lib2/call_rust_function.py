import ctypes
from pydantic import BaseModel
from typing import List

rust = ctypes.CDLL("target/release/librust_lib2.so")


class PythonModel(BaseModel):
    timeout: int
    retries: int
    host_list: List[str]
    action: str


if __name__ == "__main__":
    model = PythonModel(
        timeout=10, retries=3, action="reboot", host_list=["server1", "server2"]
    )
    some_bytes = model.json().encode("utf-8")
    print(rust.start_procedure(some_bytes))
