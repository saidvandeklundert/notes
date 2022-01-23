import tempfile

with tempfile.TemporaryFile() as temp:
    temp.write(b"This is a temporary file")
    temp.seek(0)
    print(dir(temp))
    print(f"Name of the temp file: {temp.name}")
    print(temp.read())