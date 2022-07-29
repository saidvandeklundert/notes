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


`encapsulation`: hiding internal details of state and behavior from any external code and having all code in one place.

`client` : any software that creates an object from a class and makes calls to the methods of that object. 

`getter`: a method that retrieves data from an object instantiated from a class.

`setter`: a method that assigns data into an object instantiated from a class.

`property`: an attribute of a class that appears to client code to be an instance variable, but instead causes a method to be called when it is accessed.


`abstraction`: handling complexity by hiding unnecessary details. 

`polymorphism`: In programming languages and type theory, polymorphism is the provision of a single interface to entities of different types, or the use of a single symbol to represent multiple different types.

There are different types of polymorphism:
- Subtype polymorphism (Runtime):
  * animal subclasses that all provide a `grab()` method
- Parametric polymorphism (Overloading): functions that work with different types
- Ad hoc polymorphism (Compile-time): functions with the same name act differently for different types.
  * Python example would be `1 + 1` and `"hello " + "world"` 
- Coercion polymorphism (Casting): transform a type into another:
  * Python example would be `int(34.1)`

In simple terms, polymorphism is the ability for multiple classes to implement methods with the same names.

'This technique of having multiple meanings for an operator is commonly known as operator overloading.'
`inheritance`:

`operator overloading`: compile-time polymorphism. Example in Python where we show that the `+` can have different uses:
```python
1 + 1
"Hello" + " world"
```



`abstract class`: a class that is not intended to be instantiated directly, but only to be used as a base class by one or more subclasses. In other languages , this is sometimes referred to as a virtual class.

`abstract method`: a method that must be overridden in every subclass. 


`lifetime`: all objects have a lifetime. In Python, there is a ref count associated with all objects. Everytime a var refers to an object, the ref count goes up. When the a variable that refers to an object is no longer in use, the refcount is decremented.

When the refcount reaches 0, the object is marked as garbage. The garbage collector periodically runs and reclaims the blocks of memory that have been marked as garbage. Use `getrefcount()` to check the refcount.

When an object is garbage collected, Python calls the magic method `__del__()` on it.


`class variable`:A variable that is defined in and owned by a class. Only one of each class variable exists, independent of how many instances of that class are created.