import ctypes
from pydantic import BaseModel
from typing import List

rust = ctypes.CDLL("target/release/librust_lib2.so")


class PythonModel(BaseModel):
    timeout: int
    retries: int
    host_list: List[str]
    action: str


class RustResult(BaseModel):
    result: str
    message: str
    failed_hosts: List[str]


if __name__ == "__main__":

    i = 1_000
    while i > 0:
        hosts = [f"server-{x}" for x in range(1, 5000)]
        model = PythonModel(
            timeout=10,
            retries=3,
            action="reboot",
            host_list=hosts,
        )
        some_bytes = model.json().encode("utf-8")

        ptr = rust.start_procedure(some_bytes)

        returned_bytes = ctypes.c_char_p(ptr).value

        if returned_bytes:
            returned_model = RustResult.parse_raw(returned_bytes)

        # rust.free_string(ptr)
