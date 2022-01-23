"""
At the lowest level, communication with the outside world (outside of Python), is
 done through bytes and text.

The built-in 'bytes' and bytearray':
- bytes: an immutable sequence of integers values, ranging from 0 - 255. The bytes literal representation is ASCII text.
- bytearray: a mutable sequence of integers in the range 0 - 255


- stdin: file object corresponding to the stream of input characters supplied to the interpreter.
- stdout: file object that is the interpreter's standard output stream in Python
- stderr: file object that is the interpreter's standard output stream for error messages

"""

# creating an empty byte:
empty_bytes = bytes()
print(empty_bytes)

# string as bytes:
string_as_bytes = bytes("hello", encoding="utf-8")
byte_literal = b"hello"
print(string_as_bytes, byte_literal)

# list of integers to bytes:
b = bytes([1, 2, 3, 4, 65, 0x65, 5])
print(b)

# creation of a bytearray:
ba = bytearray()
ba.extend(b"hello")
ba.extend(b"hello, this is not going to fit into a single byte, but that is OK.")
ba.extend([1, 2, 3, 4, 5, 6, 7])

# accessing byte values:
print(ba)
print(ba[0])
print(ba[0:5])
print(ba[-7:])

# converting from bytes to text and vice-versa:

some_text = "hello"
some_text_to_bytes_1 = bytes(some_text, encoding="utf-8")
some_text_to_bytes_2 = some_text.encode("utf-8")
print(
    some_text_to_bytes_1,
    type(some_text_to_bytes_1),
    some_text_to_bytes_2,
    type(some_text_to_bytes_2),
)

# surrogate escape data that is not valid utf-8:
some_invalid_utf8 = b"Some message\xf1o"
try:
    this_will_fail = some_invalid_utf8.decode("utf-8")
except UnicodeDecodeError as err:
    print(err)
this_will_not_fail = some_invalid_utf8.decode("utf-8", errors="surrogateescape")
back_to_normal_again = this_will_not_fail.encode("utf-8", errors="surrogateescape")
print(some_invalid_utf8, back_to_normal_again)


# Opening, reading and writing to a file:

# writing to a file:
with open("test.txt", "wt") as f:
    f.write("hello")
    print(" world", file=f)

# reading from a file:
with open("test.txt", "rt") as f:
    print(f.read())

with open("test.txt") as f:
    for line in f.readlines():
        print(line, end="")

#
import sys

sys.stderr.write("ERROR!")
print("ERROR!", file=sys.stderr)
sys.stdout.write("MESSAGE!")
print("MESSAGE!", file=sys.stdout)