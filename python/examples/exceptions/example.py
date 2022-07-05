some_dict = {"key-1": "value-1"}

# Following runs fine since the key exists:
print(some_dict["key-1"])

# When we access a key that does not exist, an exception is raised:
try:
    print(some_dict["key-2"])
except Exception as err:
    print(err)


# Exception is the base class and catches any type of exception
# better to be more specific. In the following,
# we capture the 'KeyError' and prevent from capturing
# Exceptions of a type we were not planning on capturing:

try:
    print(some_dict["key-2"])
except KeyError as err:
    print(
        f"we have a key error, key {err} does not exist!\n"
        "This is where we handle the exception."
    )

# We can also do something in the ABSENSE of an exception:
try:
    print(some_dict["key-1"])
except KeyError as err:
    print(
        f"we have a key error, key {err} does not exist!\n"
        "This is where we handle the exception."
    )
else:
    print("We run this because everything went fine.")

# notice in the following example, the else clause does not run:
try:
    print(some_dict["key-2"])
except KeyError as err:
    print(
        f"we have a key error, key {err} does not exist!\n"
        "This is where we handle the exception."
    )
else:
    print("We run this because everything went fine.")

# The last term in the try/except block is the finaly:
try:
    print(some_dict["key-2"])
except KeyError as err:
    print(
        f"we have a key error, key {err} does not exist!\n"
        "This is where we handle the exception."
    )
else:
    print("Everything went fine.")
finally:
    print("This clause will always run.")
    print("This can be usefull for cleanup actions.")

# The following is an unhandled exception, it will crash
#  the program and generate a Traceback.
print(some_dict["key-2"])
