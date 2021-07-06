`-buildmode=c-shared` will output two file:
- a shared object binary file (.so) exposing Go functions as a C-style APIs
- a C header file, defines C types mapped to Go compatible types


In Python, we use [ctypes](https://docs.python.org/3/library/ctypes.html) to call the exported functions.

```python
from ctypes import cdll
go_lib = cdll.LoadLibrary("./main.so")
```

When the Python code is executed, it calls the Go functions in the shared object.

An easy way of going about things is reading/writing JSON between Python and Go.

A faster way is 

| Go      |  C       | Python  |
|---------|----------|---------|
| string  | *C.char  | string  |
|         |          |         |
|         |          |         |
|         |          |         |
|         |          |         |



## C Types in Go


### char

```go
type C.char
type C.schar (signed char)
type C.uchar (unsigned char)
```

### short

```go
type C.short
type C.ushort (unsigned short)
```

### int

```go
type C.int
type C.uint (unsigned int)
```

### long

```go
type C.long
type C.ulong (unsigned long)
```

### longlong

```go
type C.longlong (long long)
type C.ulonglong (unsigned long long)
```

### float

```go
type C.float  
```

### double

```go
type C.double
```

## Access to C structs


As in `C.struct_stat`

### struct

```go
type C.struct_***
```
### union

```go
type C.union_***
```

### enum

```go
type C.enum_***
```

### void*

```go
func unsafe.Pointer() *ArbitraryType
```
https://golang.org/pkg/unsafe/