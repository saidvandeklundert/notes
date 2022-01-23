## Walkthrough of a CSV example

Walkthrough the CSV package, following along a script that reads a CSV file and prints all the records from the file. The example script can be found [here](https://github.com/saidvandeklundert/go/tree/main/examples/csv/example.go)

The example script starts with `r := csv.NewReader(f)`. Here we use the `csv.NewReader`:

```go
// NewReader returns a new Reader that reads from r.
func NewReader(r io.Reader) *Reader {
	return &Reader{
		Comma: ',',
		r:     bufio.NewReader(r),
	}
}
```
This `NewReader` returns the pointer to a `Reader` struct from the csv package. 2 fields are mentioned. These are the following:

```go
type Reader struct {
	// Comma is the field delimiter.
	// It is set to comma (',') by NewReader.
	// Comma must be a valid rune and must not be \r, \n,
	// or the Unicode replacement character (0xFFFD).
	Comma rune
	
    // content skipped

	r *bufio.Reader

    // content skipped
}
```

The `bufio.NewReader()`, defined [here](https://github.com/golang/go/blob/master/src/bufio/bufio.go), is the following:

```go
// NewReader returns a new Reader whose buffer has the default size.
func NewReader(rd io.Reader) *Reader {
	return NewReaderSize(rd, defaultBufSize)
}
```
The bufio provides us with a buffered reader that is efficient and practical to use since the implementers of the CSV package do not have to come up with their own reader.

The previous was in fact a call to `NewReaderSize()` in bufio, which is defined as follows:

```go
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

Either way, this func will return a reader:

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

This `Reader` struct in bufio will, as we shall see later on, be used to call `ReadSlice()`, so that we can read the file line by line.

Back to the script:
```go
	r := csv.NewReader(f)

	for {
		record, err := r.Read()
		if err == io.EOF {
            fmt.Println(err)
			break
		}
		if err != nil {
			log.Fatal(err)
		}

		fmt.Println(record)
	}
```

After instantiating `csv.NewReader`, we continously call `r.Read()` until we hit `io.EOF`.

The `Read()` method is defined as follows:

```go
// Read reads one record (a slice of fields) from r.
// If the record has an unexpected number of fields,
// Read returns the record along with the error ErrFieldCount.
// Except for that case, Read always returns either a non-nil
// record or a non-nil error, but not both.
// If there is no data left to be read, Read returns nil, io.EOF.
// If ReuseRecord is true, the returned slice may be shared
// between multiple calls to Read.
func (r *Reader) Read() (record []string, err error) {
	if r.ReuseRecord {
		record, err = r.readRecord(r.lastRecord)
		r.lastRecord = record
	} else {
		record, err = r.readRecord(nil)
	}
	return record, err
}
```

This is a method and the reciever is a pointer to `Reader`, so the method can (and does) update the Reader struct.

The method checks `r.ReuseRecord`. This field in `Reader` has the following comment:
```go
// ReuseRecord controls whether calls to Read may return a slice sharing
// the backing array of the previous call's returned slice for performance.
// By default, each call to Read returns newly allocated memory owned by the caller.
```


If the backing array of the previous call can be used, that last record is fed to `r.readRecord`. 

If this is not the case, the `else` ensures that the same method is called with the argument `nil` (which The makes sense as that is the zero value for a slice.)

### readRecord

The `readRecord` signature is as follows:

```go
func (r *Reader) readRecord(dst []string) ([]string, error)
```

The following code in the `readRecord` function reads a line of code:
```go
	// Read line (automatically skipping past empty lines and any comments).
	var line []byte
	var errRead error
	for errRead == nil {
		line, errRead = r.readLine()
		if r.Comment != 0 && nextRune(line) == r.Comment {
			line = nil
			continue // Skip comment lines
		}
		if errRead == nil && len(line) == lengthNL(line) {
			line = nil
			continue // Skip empty lines
		}
		break
	}
	if errRead == io.EOF {
		return nil, errRead
	}
```

Part of the action happens in `readLine`:
```go
// readLine reads the next line (with the trailing endline).
// If EOF is hit without a trailing endline, it will be omitted.
// If some bytes were read, then the error is never io.EOF.
// The result is only valid until the next call to readLine.
func (r *Reader) readLine() ([]byte, error) {
	line, err := r.r.ReadSlice('\n')				// <- here bufio's ReadSlice is used
	if err == bufio.ErrBufferFull {
		r.rawBuffer = append(r.rawBuffer[:0], line...)
		for err == bufio.ErrBufferFull {
			line, err = r.r.ReadSlice('\n')
			r.rawBuffer = append(r.rawBuffer, line...)
		}
		line = r.rawBuffer
	}
	if len(line) > 0 && err == io.EOF {
		err = nil
		// For backwards compatibility, drop trailing \r before EOF.
		if line[len(line)-1] == '\r' {
			line = line[:len(line)-1]
		}
	}
	r.numLine++
	// Normalize \r\n to \n on all input lines.
	if n := len(line); n >= 2 && line[n-2] == '\r' && line[n-1] == '\n' {
		line[n-2] = '\n'
		line = line[:n-1]
	}
	return line, err
}
```

We can see at the top of the function that `ReadSlice` from the bufio package was used to read a slice. The `ReadSlice` method is defined [here](https://github.com/golang/go/blob/master/src/bufio/bufio.go).

ReadSlice reads until the first occurrence of delim in the input, returning a slice pointing at the bytes in the buffer. Our delimiter is a newline, so we get a slice returned up untill the point where `ReadSlice` encounters the newline. 

If ReadSlice encounters an error before finding a delimiter, it returns all the data in the buffer and the error itself (often io.EOF).

We can play with `ReadSlice` and create the following script:
```go
f, _ := os.Open("example.csv")
r := bufio.NewReader(f)
for {
	line, err := r.ReadSlice('\n')
	if err == io.EOF {
		fmt.Println(err)
		break
	}
	fmt.Println("The bytes: ", line)
	fmt.Println("The string: ", string(line))
}
/*
	The bytes:  [102 105 114 115 116 95 110 97 109 101 44 108 97 115 116 95 110 97 109 101 44 117 115 101 114 110 97 109 101 13 10]
	The string:  first_name,last_name,username

	The bytes:  [34 82 111 98 34 44 34 80 105 107 101 34 44 114 111 98 13 10]
	The string:  "Rob","Pike",rob

	The bytes:  [75 101 110 44 84 104 111 109 112 115 111 110 44 107 101 110 13 10]
	The string:  Ken,Thompson,ken

	The bytes:  [34 82 111 98 101 114 116 34 44 34 71 114 105 101 115 101 109 101 114 34 44 34 103 114 105 
	34 13 10]
	The string:  "Robert","Griesemer","gri"
*/
```

In addition to returning the line and an error value, the `readLine()` function also updates the `Read` struct with `r.numLine++`, which is the field described as `the current line being read in the CSV file`.

Now that we have a line, it's back to `readRecord` where the line is analyzed, parsed and returned as a record, which is a slice of strings.

This is then passed to `Read()` which will also return it.

The way the line is read will happen again and again untill we run into `io.EOF`, which buff will propagate up all the way up to `Read()`. This stops the function and the result is that the entire CSV file was read and that all the records were returned.


## Summary

We walked through an example script:
```go
func main() {
	f, _ := os.Open("example.csv") // Open the csv file, ignoring the error

	r := csv.NewReader(f)
	for {
		record, err := r.Read()
		if err == io.EOF {
			fmt.Println(err)
			break
		}
		if err != nil {
			log.Fatal(err)
		}

		fmt.Println(record)
	}
}
```

The script:
- opens a file
- passed the content to `csv.NewReader`
- `NewReader` returns the pointer to a `Reader` struct from the csv package
- we start calling `Read()` to extract the record from every line in the CSV
- `Read()` was implemented using the `ReadSlice` method that is implemented on the `bufio.Reader()`
- in normal operations, we `break` out of the `for` when `ReadSlice` runs into `io.EOF`


The link to the file that contains `csv.NewReader()`, `csv.Reader`, `cvs.Read()` and more:
https://github.com/golang/go/blob/master/src/encoding/csv/reader.go

The bufio package:
https://github.com/golang/go/blob/master/src/bufio/bufio.go
