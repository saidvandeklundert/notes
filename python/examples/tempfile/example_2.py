import tempfile

fp = tempfile.TemporaryFile()
fp.write(b"Hello world!")
# read data from file
fp.seek(0)
fp.read()
# as the script ends, the file is garbage collected.

# closing the file earlier will have Python clean it up earlier.
