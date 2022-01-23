

### Contains:

Used to check for presence of substrings:
```go
import "strings"
exampleString := "Some words uttered by someone."
strings.Contains(exampleString, "words")                    // true
strings.Contains(exampleString, "giant massive robot")      // false
```


### Joining strings

```go
Slice := []string{"a", "b", "c", "d", "e", "f"}
Joined := strings.Join(Slice, ", ")         // a, b, c, d, e, f
```