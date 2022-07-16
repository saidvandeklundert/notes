# OOP

Object oriented programming gives programmers a way to combine code and data together in cohesive units. In turn, this can avoid certain complications inherent in procedural programming.

Object state: the attributes of a class
Object bahaviors: the methods that can operate on the state of a class

Instantiating is the process of creating an object from a class.

Method: function defined inside a class.

In Python, create a class with a method like so:

```python
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hi(self):
        print(f"Hi, I am {self.name}.")

jan = Human("jan", 6)
```

You can call the method like so:
```python
jan.say_hi()
```
When you call the method, Python takes the object you specify and rearranges it to become the first argument.

Kind of like so:

```python
say_hi(jan)
```


Every class:
- is a type
- can have class attributes
- can have class methods and/or class attributes
- has it's own scope


In Python, even though classes can contain hundreds or even thousands of lines of code, no object gets a copy of the class’s code.

When you instantiate an object, Python allocates enough memory for the required instance variables. You can look at these variables using `vars()`.


`composition`: a logical structure in which one object manages one or more other objects




`interface`: the collection of methods a class provides (and the parameters that each method expects). The interface shows what an object created from the class can do.

`implementation`: the actual code of the class, which shows how an object does what it does. 

`callback`: a function/method of an object that is called when a particular action, event, or condition happens. 

Button object example: when clicked, a callback follows. When the user clicks a button, a button (usually) calls a callback function/method. That function or method is the callback.