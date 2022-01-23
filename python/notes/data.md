
# Python data structures


## Python built-in objects

| Object type        | Example                                           |
| ------------------ |:-------------------------------------------------:|
| Numbers            | 1, 234, 34135                                     |
| Strings            | "python", "word"                                  |
| Lists              | [], [1, 2, "string", [2],]                        |
| Dictionaries       | {"key" : "value" }, dict(monts=12)                |
| Tuples             | (1, 'spam', 4, 'U'), tuple('spam'), namedtuple    |
| Files              | open('config.txt'), open('/srv/data.json')        |
| Sets               | set('123'), {'dog', 'bone', 'cat'}                |
| Booleans           | True, False                                       |
| NoneType           | None                                              |
| Program unit types | Functions, Modules, Classes                       |


## Major types:

### Numbers 
Support addition, multiplication, etc.

Examples:
- integer
- floating-point
- decimal
- fraction

### Sequences 
Sequences support indexing, slicing, concatenation and more.

Examples:
- strings
- lists
- tuples


### Mappings 
Mappings support indexing by key.

Example:
 - dictionaries



## Mutable and immutable:

### Immutable:

The state of an immutable object cannot be changed after it is instantiated. In some cases, you might run an expression against an immutable object to create a new object with altered values.

Immutable object examples:
- numbers
- strings
- tuples
- frozensets.


### Mutable:

The state of mutable objects can be changed after they are instantiated. Mutable objects support in-place operations.

Mutable object examples:
- lists
- dictionaries
- sets

### Object flexibility:
- Lists, dictionaries and tuples can hold any object
- Sets can contain immutable objects
- Lists, dictionaries, and tuples can be nested
- Lists, dictionaries and sets can grow and shrink

### Object categories

| Object type        | Category  | Mutable yes/no|
| ------------------ |:---------:|:-------------:|
| Numbers            | numeric   | no            |
| Strings            | sequence  | no            |
| Lists              | sequence  | yes           |
| Dictionaries       | mapping   | yes           |
| Tuples             | sequence  | no            |
| Files              | extension | n/a           |
| Sets               | set       | yes           |
| Frozenset          | set       | no            |
| bytearray          | sequence  | yes           |

### Assigning values

```python
a = 'a'
b = a
```
In the above, both variables now reference the same object. The variable 'b' does nto reference variable 'a'. Variables cannot be linked together in Python.


### Callable types:

- user defined functions
- built-in functions (example is `len()`)
- built-in methods (`dict.get()`)
- methods defined in a class
- classes
- class instances
- generator functions; functions or methods that use the yield keyword. 