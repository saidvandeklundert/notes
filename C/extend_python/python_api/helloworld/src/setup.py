from distutils.core import setup, Extension

module = Extension("helloworld", sources=["helloworld.c"])
setup(
    name="helloworld",
    version="0.1",
    description="First steps calling C from Python",
    ext_modules=[module],
)
