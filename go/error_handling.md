### Error handling in Go

Convention in Go is to return an error as the last return value for a function. When a function executes as expected, the error parameter is returned with a `nil` value. If an error occurs, the error value is returned instead. The other parameters of the function should, by convention, return their zero value.

The `error` in Go is defined as follows:

```go
type error interface {
	Error() string
}
```

The `error` interface method, `Error()`, specifies a `string` is returned. Since the error is an interface, returning `nil` is a valid value for one and it explains the convention as to why it is used to indicate 'no error'. Namely, `nil` is the zero value for an interface.



The following is an example where an error is raised inside a function:

```go
func exampleError(s string) (string, error) {
	if len(s) <= 6 {
		return "", errors.New("s was to short")
	} else {
		return s, nil
	}

}
```

We can also raise and format errors using the convenient `fmt.Errorf()` function, which returns a function:

```go
func exampleError(s string) (string, error) {
	if len(s) <= 6 {
		return "", fmt.Errorf("length of s should be > 6, it was %d", len(s))
	} else {
		return s, nil
	}
}
```


The above examples can be found [here](https://github.com/saidvandeklundert/go/tree/main/examples/errors).



Go does not have exceptions, as stated [here](https://golang.org/doc/faq#exceptions):

```
We believe that coupling exceptions to a control structure, as in the try-catch-finally idiom, results in convoluted code. It also tends to encourage programmers to label too many ordinary errors, such as failing to open a file, as exceptional.
```

Error is a type in Go, it is decribed [here](https://pkg.go.dev/builtin#error):

`type error`:

```go
type error interface {
	Error() string
}
```

This can be used to create your own custom errors. 

The `errors` packages is part of the standard library and the documentation is found [here](https://pkg.go.dev/errors).

The example listed in the package is something like this:

```go
import "errors"

err := errors.New("emit macho dwarf: elf header corrupted")
```

A nice thing to know is what is happening 'under the hood'. The following is the source code:
```go
// New returns an error that formats as the given text.
// Each call to New returns a distinct error value even if the text is identical.
func New(text string) error {
	return &errorString{text}
}
// errorString is a trivial implementation of error.
type errorString struct {
	s string
}

func (e *errorString) Error() string {
	return e.s
}
```
We can see that the `type errorString` struct satisfies the error interface.


## Checking for an error an logging fatal:


```go
import "log"
if err != nil {
	log.Fatal(err)
	log.Printf("%v", err)
}
```

Note that `Fatal` is equivalent to `Print()` followed by a call to `os.Exit(1)`. You can also consider `Fatalf`, which is equivalent to `Printf()` followed by a call to `os.Exit(1)`.

## Check for an error and perform followup action:

```go
if err != nil {
	if strings.Contains(err.Error(), "404") {
		Error.Println(err)
```

## Storing an error as a var and emitting it where applicable

Sometimes, errors are defined grouped together at the top of a package. The code in the rest of the package then refers to those variables in case an errors needs to be returned.

Example:

```go
// Defining an error and storing it as a variable.
// Example taken from gzip, hence the reference to that package.
var (
	// ErrChecksum is returned when reading GZIP data that has an invalid checksum.
	ErrChecksum = errors.New("gzip: invalid checksum")
)

func CheckSum() (string, error) {
	if "checksum" != "CHECKSUM" {
		err := ErrChecksum
		return "", err
	}
	return "s", nil
}
CheckSum()	//  gzip: invalid checksum
```
