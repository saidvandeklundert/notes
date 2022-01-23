```go
// the '*' (indirection operator) returns the value of the pointer
// the '&' (address operator) returns the pointer to a value


// Declare integer-type pointer:
var PointerInteger *int

// Declare integer, integer-pointer and then print the values:
var integer int = 100
integerPointer := &integer		// & is used to assign the address of the integer to the pointer
fmt.Printf(`
Pointer memory addres:         %v
Address of the pointer itself: %v
Pointer value:                 %v
`, integerPointer, &integerPointer, *integerPointer)
}
/* ^ gives the following:
Pointer memory addres:         0xc0000ac058
Address of the pointer itself: 0xc0000d8020
Pointer value:                 100
*/


/*
- change someString by changing the pointer value
- assign value to 'value' and 'new_value' by referencing the pointer
*/  
var someString string = "word"		// declare string-literal
pointer := &someString				// declare string-pointer
fmt.Printf("%v\n", pointer) 		// print var value:		 	0xc000088230
fmt.Printf("%T\n", pointer) 		// print variable type:		*string
value := *pointer					//
fmt.Printf("%v\n", value) 			// print var value:			word
fmt.Printf("%T\n", value) 			// print var type:			string  
*pointer = "WORD"					// assign the value to memory address the pointer points to
new_value := *pointer				// short-declare new_value to pointer value 
fmt.Printf("%v\n", pointer)			// print var value:			0xc000088230
fmt.Printf("%v\n", new_value)		// print var value:			WORD  
fmt.Printf("%v\n", someString)		// print var value:			WORD   

```