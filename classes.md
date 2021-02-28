# Classes


### Intro:

Classes are defined using the `class` statement. By convention, classes are named using camel case.

Every class has an __init__(), which is short for initializer. 

The `init` can be made to take arguments, which can be forwarded to be assigned to the object's attributes.

`Attributes` are variables that are associated with an object. Every object has it's own set of attributes. You can set and access these attributes just like any variable.

A class may have functions defined. These functions are called `methods`.

In Python, there are no private attributes or private methods. There is a convention though, to signify to others that some attributes and methods are to be treated as private. This is done by prefixing the attribute or method name with a `_`.

Creating objects from classes is done by calling their constructors. This is done by calling the class name as a function. This, in turn, calls the class's `__init__()` method.


### Terms and terminology:


#### Class methods:

Associated with a class instead of an individual object.

Class methods can be recognized by 2 things:
- the `classmethod` decorator is called before the method
- the first argument for the classmethod is not `self` but `cls`. The `cls` argument refers to the object's class

```python
    @classmethod
    def example(cls):
        return 'yolo'
```

Class methods are not commonly used. One use-case is to provide an alternative constructor method apart from the `init()`.

#### Class attributes

Class attributes are variables that belong to the class instead of to the object.

Class attributes are defined inside the class, but outside any method:
```python
class MyClass:
    class_attribute = 'example'                 # The class attribtue
    def __init__(self, attribute_1,):
        self.attribute_1 = attribute_1
```

#### Static methods

Static methods cannot access attributes or methods that belong to the class or object. 

A method in a class that is prefixed by the `@staticmethod` decorator.
```python
    @staticmethod
    def example():
        return 'yolo'
```


### Examples:

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