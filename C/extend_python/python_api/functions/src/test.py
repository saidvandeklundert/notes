import c_functions

if __name__ == "__main__":

    c_functions.printer()
    c_functions.system("ls -l")
    greeting = c_functions.greeter("Jan")
    print(greeting)
    square = c_functions.square(5)
    print(square)