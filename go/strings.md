`string`: a read-only slice of immutable bytes. 

Strings are utf-8 encoded by default. The zero value is an empty string

In the context of strings, a `rune` is a unicode code point. The `rune` is a alias for `int32`, which can represent a unicode code point. When referrring to characters, use `rune` to clarify intent.

```go
var s string = "Example string"
var b byte = s[1]               // 120 ( utf-8 decimal codepoint for x is 120)
var sliceOfSting s[2:4]         // am

// Runes and bytes can be converted to strings:
var r rune = "a"
var s string = string(r)
fmt.Println("Rune: ", r, " string: ", s)        // Rune:  97  string:  a


var b byte = "y"
var s string = string(b)
fmt.Println("Byte: ", b, " string: ", s)        // Byte:  121  string:  y
```

Most data in Go is read and written as a series of bytes, so most common string conversions are with byte slices instead of with rune slices.



It is possible that text contains characters that are more then 1 byte. This can be characters from languages other then English or emoticons. In those cases, the length of the byte-slice will not equal the number of characters. In Go, you should only slice strings from texts that are made using one byte characters.


### UTF-8

UTF-8 is the most common encoding for Unicode. Check the utf8 table [here](https://www.utf8-chartable.de/unicode-utf8-table.pl?utf8=dec).

Unicode uses 4 bytes, or 32 bites, to represent each code point (character). The simples way to store this would be to use 4 bytes for each code point, which is done in UTF-32. Because this wastes so much space, it is mostly unused.

Another common encoding is UTF-16, which uses 1 or 2 16 bit sequences. Also wastefull since most of the content in the world uses code points that fit in a byte.

UTF-8 can use a single byte for characters with a value below 128 (includes all English letters, numbers and puctuations) but it can expand to 4 bytes to represent all the other codepoints. You can look at any byte in a sequence and understand if you are at the start or in the middle of a character. However, if you want to count the number of characters in a string, you have to start counting at the beginning.

Instead of using slice and index operations, extract substrings and code points from strings with `strings` and `unicode/utf8` from the standard library.