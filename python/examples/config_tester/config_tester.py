from pathlib import Path
import os


for file in Path(os.getcwd()).glob("**/*.cfg"):
    print(50 * "-")
    print(file)
