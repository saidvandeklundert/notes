## Installing Go

```
yum install wget
wget https://golang.org/dl/go1.16.3.linux-amd64.tar.gz
rm -rf /usr/local/go && tar -C /usr/local -xzf go1.16.3.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin
go version
yum install gcc
go build -buildmode=c-shared -o main.so main.go
```

go_python.py will asume these files are in the same directory.
git clone https://github.com/saidvandeklundert/python.git

## Compiling Go

Instead of 
`-buildmode=c-shared` will output two file:
- a shared object binary file (.so) exposing Go functions as a C-style APIs
- a C header file, defines C types mapped to Go compatible types


In Python, we use [ctypes](https://docs.python.org/3/library/ctypes.html) to call the exported functions.

```python
from ctypes import cdll
go_lib = cdll.LoadLibrary("./main.so")
```

## Useful resources

Learning Go by Jon Bodner
https://fluhus.github.io/snopher/
https://www.ardanlabs.com/blog/2020/06/python-go-grpc.html
https://www.ardanlabs.com/blog/2020/07/extending-python-with-go.html
https://www.ardanlabs.com/blog/2020/08/packaging-python-code.html
https://www.ardanlabs.com/blog/2020/09/using-python-memory.html
https://blog.golang.org/cgo
