from distutils.core import setup, Extension

module = Extension("c_functions", sources=["c_functions.c"])
setup(
    name="c_functions",
    version="0.1",
    description="Several examples of C functions made callable to the Python API.",
    ext_modules=[module],
)
