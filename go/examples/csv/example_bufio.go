package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

func main() {
	f, _ := os.Open("example.csv") // Open the csv file, ignoring the error
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
