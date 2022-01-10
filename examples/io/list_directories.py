from pprint import pprint
import pathlib
import os

pprint(os.listdir())
# change dir:
os.chdir("..")
# print current dir:
print(os.getcwd())
# print files and dirs:
pprint(os.listdir())

# us pathlib to print only certain type of files in the current working directory:
print("using pathlib:")
for file in pathlib.Path().iterdir():
    if file.is_file():
        print(file)

# us pathlib to print only certain type of files in the subdirectories of the current working directory:
for file in pathlib.Path(os.getcwd()).glob("*.py"):  # glob is used to filter files
    print(file, "the entire filename")
    print(file.parent, "just the path")
    print(file.name, "just the name")
    print(file.stem, "the name without the extension")
    print(file.parts, "convient list of parts")


for file in pathlib.Path(os.getcwd()).glob("*.txt"):  # glob is used to filter files
    print(file, "the entire filename")
    print(file.parent, "just the path")
    print(file.name, "just the name")
    print(file.stem, "the name without the extension")
    print(file.parts, "convient list of parts")