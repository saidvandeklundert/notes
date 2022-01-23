bufio is a package that provides you with buffered io, this is what the pacakge has to say about itself:

```
Package bufio implements buffered I/O. It wraps an io.Reader or io.Writer object, creating another object (Reader or Writer) that also implements the interface but provides buffering and some help for textual I/O.
```

The source is found [here](https://github.com/golang/go/tree/master/src/bufio).

## Reader

Typically, a reader is created using either of the following methods:

```go
// NewReader returns a new Reader whose buffer has the default size.
func NewReader(rd io.Reader) *Reader {
	return NewReaderSize(rd, defaultBufSize)
}

// NewReaderSize returns a new Reader whose buffer has at least the specified
// size. If the argument io.Reader is already a Reader with large enough
// size, it returns the underlying Reader.
func NewReaderSize(rd io.Reader, size int) *Reader {
	// Is it already a Reader?
	b, ok := rd.(*Reader)
	if ok && len(b.buf) >= size {
		return b
	}
	if size < minReadBufferSize {
		size = minReadBufferSize
	}
	r := new(Reader)
	r.reset(make([]byte, size), rd)
	return r
}
```

Use the `NewReaderSize` in case the default buffersize of `4096` is not appropriate.

The functions take in an type of `io.Reader`. This is 'something' that satisfies the `Reader` interface that is defined in the io-package:
```go
// Reader interface from the IO package
//  https://github.com/golang/go/blob/master/src/io/io.go
type Reader interface {
	Read(p []byte) (n int, err error)
}
```


The function returns a `Reader` struct that is defined as follows:

```go
// Reader implements buffering for an io.Reader object.
type Reader struct {
	buf          []byte
	rd           io.Reader // reader provided by the client
	r, w         int       // buf read and write positions
	err          error
	lastByte     int // last byte read for UnreadByte; -1 means invalid
	lastRuneSize int // size of last rune read for UnreadRune; -1 means invalid
}
```

Some examples:
```go
f, _ := os.Open("show_version_short.txt")
r := bufio.NewReader(f)

fmt.Printf("\n%#v\n %v\n", r, r)
// Use ReadSlice to read the file line by line:
for {
	line, err := r.ReadSlice('\n')
	if err == io.EOF {
		fmt.Println(err)
		break
	}
	fmt.Println("The bytes: ", line)
	fmt.Println("The string: ", string(line))
}
// Use Readline to read the file line by line:
f, _ = os.Open("show_version_short.txt")
r = bufio.NewReader(f)
for {
	line, isPrefix, err := r.ReadLine()
	if err == io.EOF {
		fmt.Println(err)
		break
	}
	fmt.Println("The bytes: ", line)
	fmt.Println("The string: ", string(line))
	fmt.Println("isPrefix: ", isPrefix)
}
// Use Read:
f, _ = os.Open("show_version_short.txt")
r = bufio.NewReader(f)
// Create a buffer for n bytes
b := make([]byte, 5)
for {
	// Call read, pass in the buffer.
	//  Read will put content in the buffer!
	//   n is the number of bytes in the buffer
	n, err := r.Read(b)
		// check for errors:
	if err == io.EOF {
		fmt.Println(err)
		break
	}
	// Print the buffer.
	//  The [:n] makes sure that we only read the n-number of
	//   bytes that were written to the buffer
	fmt.Println(b[:n])
	fmt.Println(string(b[:n]))
}
```

