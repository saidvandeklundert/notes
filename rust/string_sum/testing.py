# python -m venv c:\venv
# C:\venv\Scripts\activate
# pip install maturin
# pip install maturin
import ctypes

library_name = (
    "C:\\dev-container\\python\\rust\\string_sum\\target\\release\\stringtools.dll"
)
stringtools = ctypes.CDLL(library_name)
print(stringtools.count_substrings(b"banana", b"na"))
