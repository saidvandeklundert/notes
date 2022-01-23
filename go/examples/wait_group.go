package main

import (
	"fmt"
	"runtime"
	"sync"
	"time"
)

func main() {
	fmt.Println(runtime.GOMAXPROCS(0))
	ConcurrentExample(0)

	ConcurrentExample(1)
}

// Start 8 threads and report the thread number
func ConcurrentExample(Id int) {
	var wg sync.WaitGroup
	fmt.Printf("\nConcurrentExample %d ", Id)
	go ConcurrentFunc(1, Id, &wg)
	go ConcurrentFunc(2, Id, &wg)
	go ConcurrentFunc(3, Id, &wg)
	go ConcurrentFunc(4, Id, &wg)
	go ConcurrentFunc(5, Id, &wg)
	go ConcurrentFunc(6, Id, &wg)
	go ConcurrentFuncMoarThreads(7, Id, &wg)
	go ConcurrentFuncMoarThreads(8, Id, &wg)
	wg.Add(8)
	wg.Wait()
}

func ConcurrentFunc(Nr int, Id int, wg *sync.WaitGroup) {
	// Ensure we wrap up saying done even if we crash
	defer wg.Done()
	time.Sleep(5 * time.Second)
	fmt.Printf("\nConcurrentExample ID %d ConcurrentFunc %d", Id, Nr)
}

func ConcurrentFuncMoarThreads(Nr int, Id int, wg *sync.WaitGroup) {
	// Ensure we wrap up saying done even if we crash
	defer wg.Done()
	var nestedWG sync.WaitGroup
	fmt.Printf("\nConcurrentFuncMoarThreads ID %d ConcurrentFuncMoarThreads %d", Id, Nr)
	go NestedConcurrentFunc(1, Id, &nestedWG)
	go NestedConcurrentFunc(2, Id, &nestedWG)
	go NestedConcurrentFunc(3, Id, &nestedWG)
	go NestedConcurrentFunc(4, Id, &nestedWG)
	nestedWG.Add(4)
	nestedWG.Wait()

}

func NestedConcurrentFunc(Nr int, Id int, nestedWG *sync.WaitGroup) {
	// Ensure we wrap up saying done even if we crash
	defer nestedWG.Done()
	time.Sleep(5 * time.Second)
	fmt.Printf("\n\tNestedConcurrentFunc ID %d Number %d NumGoRoutine %d", Id, Nr, runtime.NumGoroutine())
}
