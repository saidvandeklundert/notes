# Classes


Classes are defined using the `class` statement. By convention, classes are named using camel case.

Every class has an __init__(), which is short for initializer. 

The init can be made to take arguments, which can be forwarded to be assigned to the object's attributes.

Attributes are variables that are associated with an object. Every object has it's own set of attributes. You can set and access these attributes just like any variable.

A class may have functions defined. These functions are called `methods`.

In Python, there are no private attributes or private methods. There is a convention though, to signify to others that some attributes and methods are to be treated as private. This is done by prefixing the attribute or method name with a `_`.

Creating objects from classes is done by calling their constructors. This is done by calling the class name as a function. This, in turn, calls the class's `__init__()` method.

```python

class MyClass:
    
    def __init__(self, attribute_1, attribute_2,):
        self.attribute_1 = attribute_1
        self.attribute_2 = attribute_2
    
    def multiples(self):
        return self.attribute_1 * self.attribute_2


x = MyClass(1, 2)
```

```python
# Get the type of the object:
type(x)
# Get the 'pretty' class name:
type(x).__qualname__
```



## Attributes