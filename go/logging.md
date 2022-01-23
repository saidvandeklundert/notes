### Logging example:


```go
package nameofthepackage

import (
	"io"
	"log"
	"os"
)

// Runs before main, sets up the logger:
func init() {
	file, err := os.OpenFile("/var/log/nameofthepackage.log", os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0666)
	if err != nil {
		log.Fatalln("Failed to open log file: ", err)
	}
    // log to os.Stdout:
	Info = log.New(os.Stdout, "INFO: ", log.Ldate|log.Ltime|log.Lshortfile)
    // log to os.Stout and a file:
	Warning = log.New(io.MultiWriter(file, os.Stdout), "WARNING: ", log.Ldate|log.Ltime|log.Lshortfile)
	// log to os.Stderr and a file:
    Error = log.New(io.MultiWriter(file, os.Stderr), "ERROR: ", log.Ldate|log.Ltime|log.Lshortfile)

	Info.Println("ssot logger initialized.")
}

var (
	Info    *log.Logger
	Warning *log.Logger
	Error   *log.Logger
)
```

After it is setup like this, you can use the logger like so:
```go
Info.Printf("Lost connection to device ", device)
Warning.Println("high watermark: ", value)
Error.Println("serious error")
```
