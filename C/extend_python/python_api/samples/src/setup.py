"""
pip install src/
python3 src/test.py
"""
from distutils.core import setup, Extension

module = Extension("samples", sources=["samples.c"])

setup(
    name="samples",
    version="0.1",
    description="An example of C extension made callable to the Python API.",
    ext_modules=[module],
)