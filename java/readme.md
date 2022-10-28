## Java


Compile and run a program called `HelloWorld.java`:
```
javac HelloWorld.java
java HelloWorld
```



## Types:

Primitive types (start with lower-case):

```
boolean
long
int
char
short
byte
double
float
```

Non-primitive types (start with Capital):

```
String
```

Reference types:

```
class: defines a new data type
interface
enum
array
annotation types
```

Reference types:
- are aggregate types
- can be user defined

## Method modifiers

`abstract`: specification without implementation
`final`: may not be changed once initialized
`native`: methid is implemented in some *native* (other) language (like C)
`public, protected, private`: access modifiers
`static`: method is associated with the class and does not need an instance.
`syncrhonized`: makes a method threadsafe. Can also be done in ways other then using this keyword.
`transient`: specifies that a field is not part of the persistent state of an object and that it need not be serialized along with the rest of the object
`volatile`: indicates the field has extra semantices for concurrent use by two or more threads.

### Class field: does not need an instance:

```java
public static final double PI = 3.14159;
```

Because of the use of `final`, the above is also referred to as a constant.

### Instance field: does need an instance:

Declared without the static keyword:
```java
public double r;
```

### Constructor:

- always the name of the class
- declared without a return type
- does not return 'this' or any other value

```java
public class Circle{
    // instance field:
    protected double r;
    // constructor:
    public Circle(double r){ this.r = r};
}
```

You can overload constructors.