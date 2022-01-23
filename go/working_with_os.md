


```go
import "os"
OS_ENV := os.Getenv("OS_ENV")
```



```go
// create a dir in case it does not exist:
if _, err := os.Stat(dir); os.IsNotExist(err) {
	os.MkdirAll(dir, 0700)
}
```    