## Reader interface


```go
type Reader interface {
    Read(p []byte) (n int, err error)
}
```