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
	fmt.Printf("New Reader initial value:\n\n%v\n%#v\n", r, r)
	for {
		fmt.Printf("\n%v\n%#v\n", r, r)
		record, err := r.Read()
		if err == io.EOF {
			fmt.Println(err)
			break
		}
		if err != nil {
			log.Fatal(err)
		}

		fmt.Printf("\n%v\n%#v\n", record, record)
	}
	//fmt.Println(r)
}

/*
[first_name last_name username]
[Rob Pike rob]
[Ken Thompson ken]
[Robert Griesemer gri]
[Said  van de Klundert  said]
EOF
*/
