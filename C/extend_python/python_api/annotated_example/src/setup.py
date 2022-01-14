"""
pip install -e src/
python3 src/test.py
"""
from distutils.core import setup, Extension

module = Extension("c_extension", sources=["c_extension.c"])

setup(
    name="c_extension",
    version="0.1",
    description="An example of C extension made callable to the Python API.",
    ext_modules=[module],
)