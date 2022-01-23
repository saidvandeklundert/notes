package main

import "fmt"

func main() {
	hosts := []string{"1.1.1.1", "2.2.2.2", "3.3.3.3"}
	for i := 0; i < len(hosts); i++ {
		fmt.Printf("%v\n", hosts[i])
	}
}
