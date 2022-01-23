package main

import (
	"fmt"
	"time"
)

func main() {

	eve := make(chan int)
	odd := make(chan int)
	quit := make(chan int)

	go send(eve, odd, quit)

	receive(eve, odd, quit)

	fmt.Println("Done.")
}

func send(e, o, q chan<- int) {
	for i := 0; i < 100; i++ {
		if i%2 == 0 {
			e <- i
		} else {
			o <- i
		}
	}
	q <- 0
}

func receive(e, o, q <-chan int) {
	for {
		select {
		case v := <-e:
			fmt.Println("From the eve channel: ", v)
		case v := <-o:
			fmt.Println("From the odd channel: ", v)
		case v := <-q:
			fmt.Println("From the quit channel: ", v)
			time.Sleep(2 * time.Second)
			return
		}
	}
}
