from distutils.core import setup, Extension

module = Extension("cModPyDem", sources=["cModPyDem.c"])
setup(
    name="packagename",
    version="1.0",
    description="a test package",
    ext_modules=[module],
)
