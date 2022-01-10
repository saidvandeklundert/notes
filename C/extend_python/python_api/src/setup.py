from distutils.core import setup, Extension

module = Extension("helloworld", sources=["helloworld.c"])
setup(
    name="packagename",
    version="1.0",
    description="a test package",
    ext_modules=[module],
)
