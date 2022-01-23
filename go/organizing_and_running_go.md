
## Go CLI:

go run:
go build:
go fmt:
go install:
go get:
go test:



## Packages:

The first line of a file must always declare what package it belongs to.

Package 'main' indicates a package is an executable that can be compiled. The package MUST have a function called main.

Packages with oter names can be used as a de

```go
import "fmt"
import (
	"fmt"
	"sort"
)
```

## Creating your first module


The `ssot` will contain the library, the `ssotClient` will contain the `main.go`:
```
mkdir ssot
mkdir ssotClient
```

Put code in the library and use `go mod`:
```
cd ssot
go mod init example.com/ssot
vi ssot.go
```

Put the following in the file:
```go
package ssot

import "fmt"

// Start of the module
func Start(name string) string {
	message := fmt.Sprintf("Hi, %v. Welcome to using the ssot package!", name)
	return message
}
```

Move to the other directory
```
cd ..
cd ssotClient/
```

Create the `main.go` file:
```go
package main

import (
    "fmt"
    "example.com/ssot"
)

func main() {
    // Get a greeting message and print it.
    message := ssot.Start("Said")
    fmt.Println(message)
}
```

Run the following commands:
```
go mod init example.com/ssotClient
go mod edit -replace=example.com/ssot=../ssot
go mod tidy
go run .
```



## Quick install note:

Install yum, download and install Go, set the env path and go:
```
yum install wget
wget https://golang.org/dl/go1.16.3.linux-amd64.tar.gz

rm -rf /usr/local/go && tar -C /usr/local -xzf go1.16.3.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin
go version
go version go1.16.3 linux/amd64
```



## Linter:

Get the linter:
```
go get -u github.com/golang/lint/golint
```
Run the linter:
```
golint ./..
```