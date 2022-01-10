from pathlib import Path
import os
import pathlib

# make a Path instance (pi):
pi = Path("current.txt")

# name of the file:
print(pi.name)

# path of the file:
print(pi.parent)

# parts of the file:
print(pi.parts)

# print metadata of a file:
print(pi.stat())
print(pi.stat().st_size)  # file size in bytes

# Check if it is a file:
print(pi.is_file())


# look through the current directory and print things about the files that are found:
for file in Path(os.getcwd()).glob("*.txt"):  # glob is used to filter files
    print(50 * "-")
    print(file, "the entire filename")
    print(file.parent, "just the path")
    print(file.name, "just the name")
    print(file.stem, "the name without the extension")
    print(file.parts, "convient list of parts")

# from the current directory, all the way down, print things about the files that are found:
for file in Path(os.getcwd()).glob("**/*.txt"):
    print(50 * "-")
    print(file, "the entire filename")
    print(file.parent, "just the path")
    print(file.name, "just the name")
    print(file.stem, "the name without the extension")
    print(file.parts, "convient list of parts")


# same using os.walk:
for path, directories, files in os.walk(os.getcwd()):
    print(f"path: {path}")
    print(f"    directories: {directories}")
    print(f"    files: {files}")


# create a file:
with open("new_file.txt", "w") as f:
    f.write("hello world")

# remove a file:
to_remove = Path("new_file.txt")
print("removing file", to_remove.unlink())
print("Is the file still there?", to_remove.exists())

# remove directory:
# Path.rmdir()