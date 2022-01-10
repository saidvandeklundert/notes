from distutils.core import setup, Extension

module = Extension("hello", sources=["hellomodule.c"])
setup(
    name="packagename",
    version="1.0",
    description="a test package",
    ext_modules=[module],
)
