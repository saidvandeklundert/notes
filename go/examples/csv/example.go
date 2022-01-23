package main

import (
	"encoding/csv"
	"fmt"
	"io"
	"log"
	"os"
)

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

/*
[first_name last_name username]
[Rob Pike rob]
[Ken Thompson ken]
[Robert Griesemer gri]
[Said  van de Klundert  said]
EOF
*/
