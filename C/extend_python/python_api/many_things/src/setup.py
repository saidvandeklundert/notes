"""
pip install -e src/
python3 src/test.py
"""
from distutils.core import setup, Extension

module = Extension("many", sources=["many.c"])

setup(
    name="many",
    version="0.1",
    description="An example of C extension made callable to the Python API.",
    ext_modules=[module],
)
