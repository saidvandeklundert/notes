

The reader interface has 1 method:
```go
type Reader interface {
  Read(p []byte) (n int, err error)
}
```

How it is intended to be used is as follows:
- the method is implemented on a type
- when the method is called, it is passed a slice of bytes
- Read fills the slice of bytes with data
- Read returns the number of bytes that were read and an error value

Unless the Reader reaches the end of the file, the bytes read should be equal to the size of the buffer.

The error value that is returned is `nil` if there is no error. It is used to communicate errors and to indicate when the end of the thing is is reading is reached. Usually, code will include something like `if err == io.EOF` to see if this was the end of the file/thing that was being read.

The main idea is that you iterate something, reading that thing byte by byte filing the buffer. When the buffer is full, or when the end of the file/type is encountered, the number of bytes read is returned. The buffer should then be read up until this number of bytes. When an error is encountered, the Reader should stop.

Example:
```go
f, _ := os.Open("example.txt")
b := make([]byte, 120)
for {
	// Call read, pass in the buffer.
	//  Read will put content in the buffer!
	//   n is the number of bytes in the buffer
	n, err := f.Read(b)
	// check for errors:
	if err == io.EOF {
		fmt.Println(err)
		break
	}
	// Print the buffer.
	//  The [:n] makes sure that we only read the n-number of
	//   bytes that were written to the buffer	
	fmt.Println(string(b[:n]))
}
```

The comments in the standard library documentation are found [here](https://golang.org/pkg/io/#Reader)






## Example implementation OS:

The definition of `Read()` in OS:

```go
// Read reads up to len(b) bytes from the File.
// It returns the number of bytes read and any error encountered.
// At end of file, Read returns 0, io.EOF.
func (f *File) Read(b []byte) (n int, err error) {
	if err := f.checkValid("read"); err != nil {
		return 0, err
	}
	n, e := f.read(b)
	return n, f.wrapErr("read", e)
}
```

Using `Read()` on the type `File`:
```go
f, _ := os.Open("example.txt")
b := make([]byte, 120)
for {
	n, err := f.Read(b)

	if err == io.EOF {
		fmt.Println(err)
		break
	}

	fmt.Println(b[:n])
	fmt.Println(string(b[:n]))
}
```

## Example implementation strings:

The definition of `Read()` in strings [here](https://github.com/golang/go/blob/master/src/strings/reader.go):

```go
// A Reader implements the io.Reader, io.ReaderAt, io.ByteReader, io.ByteScanner,
// io.RuneReader, io.RuneScanner, io.Seeker, and io.WriterTo interfaces by reading
// from a string.
// The zero value for Reader operates like a Reader of an empty string.
type Reader struct {
	s        string
	i        int64 // current reading index
	prevRune int   // index of previous rune; or < 0
}

// NewReader returns a new Reader reading from s.
// It is similar to bytes.NewBufferString but more efficient and read-only.
func NewReader(s string) *Reader { return &Reader{s, 0, -1} }

// Read implements the io.Reader interface.
func (r *Reader) Read(b []byte) (n int, err error) {
	if r.i >= int64(len(r.s)) {
		return 0, io.EOF
	}
	r.prevRune = -1
	n = copy(b, r.s[r.i:])
	r.i += int64(n)
	return
}
```

Using `Read()` on the type `string`:
```go
var s string = "Golang."

r := strings.NewReader(s)

b := make([]byte, 2)
for {
	n, err := r.Read(b)
	if err == io.EOF {
		fmt.Println(err)
		break
	}
	fmt.Println(string(b[:n]))
}
```