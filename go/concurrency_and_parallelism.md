## Introduction to concurrency in Go

Go's main concurrency model is based on CSP, Communication Seqeuntial Processes.
Concurrency is not parallelism:
- concurrency: multiple threads executing code.
- parallelism: multiple threads executed at the exact same time (requires multiple CPUs).

In the context of Go, the following terms are important:
- `Goroutines`: User-space thread managed by the Go runtime. The thread is not managed by the OS. Goroutines are used to execute tasks independently.
- `Channels`: reference type that is used for communication and synchronization between Goroutines.
- `Go scheduler`: multiplexes Goroutines onto OS threads.

*Channels*:
- are Goroutine-safe
- store and pass values between Goroutines
- provide FIFO semantics (when they are buffered)
- can cause Goroutines to block and unblock

The zero value for a channel is `nil`.


### Goroutines

A Goroutine can be seen as a lightweight process managed by the Go runtime. Scheduling of goroutines onto OS threads is handled by the Go runtime scheduler. The runtime scheduler multiplexes Go routines into OS threads. 

The Go runtime scheduler manages go routines. Go does not rely on the OS to manage threads. Go using it's own scheduler has some advantages:
- Goroutines can be created faster then an OS can create threads
- Goroutines require less memory. They have a very small initial stack size that can grow as needed.
- switching between Goroutines is faster then swtiching between threads
- the Goroutine scheduler is able to optimize its decisions because it is part of the Go process


A goroutine has a simple model: it is a function executing concurrently with other goroutines in the same address space. It is lightweight, costing little more than the allocation of stack space. Additionally, context switching between go routines is also a lot more lightweight versus having the OS context switch threads. More [here](https://golang.org/doc/effective_go#goroutines).

The `go` statement starts the execution of a function call as an independant concurrent thread of control, or `goroutine`, within the same address space.

`W. Kennedy`: Go has turned IO-bound work into CPU-bound work because by running multiple Go routines in a single thread (from an OS pov), Go can keep the CPU busy all the time.

`Goroutine vs OS threads`:

| Go routine  | OS thread  |
|---|---|
| Managed by the Go runtime   | Managed by kernal  |
| Not hardware dependant   | hardware dependant  |
| Easy communication through channels  | No easy communication between threads  |
| Low latency communication between channels | Latency involved in inter-thread communication  |
| Go routine does not have an ID as it does not have thread local storage  | unique ID because they have thread local storage  |
| Cheap | Expensive (less then processes, but still)  |
| fast startup  | slow startup  |
| growable segmented stacks | no growable segmented stacks |
| cooperatively scheduled  | preemptively scheduled |


Look into Mutex or Atomic to avoid race conditions in case the Go routines share variables. 

Channels enable safe communication between Go routines. 

Go also offers mutex (mutual exclusion). Use a mutex when multiple Go routines read/write to a shared value (struct field for instance). Using mutexes, when a Go routine needs to access a value shared between Go routines, it needs to call `Lock` on it. The Goroutine aquires the lock immediately or after waiting for other Goroutines to release it. Once it lock is aquired, the Go routine can safely access and work with the value. When the Go routine is done, it can call `Unlock` the value.

When to use channels and when to use mutexes:
- when sharing a field in a struct, use mutexes
- when channels stand in the way of fixing a critical performance issue, use mutexes
- if you are coordinating goroutines or tracking a value that is transformed by a series of Goroutines, use channels

In addition to mutexes and channels, there is also atomics. According to 'Learning Go', skipp this unless you are a concurrency expert solving a problem where every bit of performance matters.
## Channels

Channels in go facilitate communication between different Go routines. In a sense, channels offer a way to manage concurrent code. They allow us to safely pass values between Goroutines. 

The channel is a reference type. And in addition to that, it is defined for a specific type. The zero value for a channel is `nil`.

Channels are blocking. This means that after you push a message onto a channel, the operation is blocking until the value is read from the channel.

After a channel is created, and a go routine is started, you can use the channel to:
- send data into the channel
- recieve values in the channel


**Receive channel**:
- can receive values from the channel
- cannot close a recieve channel

**Send channel**:
- push values to the channel
- cannot receive/pull or read from the channel


You can use the comma idiom to check if a channel is empty:
**v, ok := <-ch**

`ok` is `false` if there are no more values to receive and the channel is closed.

Sending on a closed channel will cause a panic so only the sender should close a channel. Closing is generally only necessary when the receiver must be told there are no more values coming, such as to terminate a range loop. 

Context can be used to ensure spawned Go routines are halted. This to prevent leaking of Go routines and to prevent wasting of resources.

## The scheduler

The Go scheduler is the 'behind-the-scenes' orechestrator of your Go programs. The design of the scheduler and the scheduling decisions of the Go scheduler impact the performance of the Go programs.

The Go scheduler:
- ensures created Goroutines are run/scheduled
- pauses and resumes Goroutines (blocking channel operations, mutex operations)
- coordinates: blocking system calls, network I/O, runtime tasks like garbage collection

`Why` does Go need a scheduler?

Instead of having kernel threads managed and scheduled by the OS, Go has Goroutines. These are user-space thread managed by the Go runtime. The Goroutines were implemented because they are cheaper when compared to kernel threads:
- smaller memory footprint ( initial Goroutine stack 2KB)
- faster creation, destruction and context switches (measured in ns instead of microseconds)

In short, Go needs a scheduler because Go has Goroutines. 

Goroutines are user-space threads and the Go scheduler multiplexes them onto Kernel threads.

`What` the Go scheduler aims to achieve:
- use a small number of kernal threads (because they are so expensive)
- support high concurrency (run many many many Goroutines)
- leverage parallelism and make use of available cores


The `how` behind the `what`:
- use a small number of kernal threads (because they are so expensive)
  - re-use threads and limit the number of Goroutine-running threads
- support high concurrency (run many many many Goroutines)
  - threads use independant runqueues and keep them balanced
- leverage parallelism and make use of available cores
  - use a runqueue per core and employ thread spinning


A lot of information came from:
- William Kennedy's course on O'Reilly
- Learning Go
- `GopherCon 2017: Kavya Joshi - Understanding Channels`
- `GopherCon 2018: Kavya Joshi - The Scheduler Saga`
## Examples


### Simple Goroutines example

```go
package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	var wg sync.WaitGroup
	wg.Add(2)				// add the number of Goroutines we will use to the wait group

	// Launch a Goroutine from a closure (has access to wg defined in main)
	go func() {
		example()	// Have Goroutine run example()
		wg.Done()	// Done decrements the WaitGroup counter by one 
	}()
	// Launch another Goroutine:
	go func() {
		example()
		wg.Done()
	}()

	wg.Wait()	// Wait blocks until the WaitGroup counter is zero.

	fmt.Println("Program finished.")
}

func example() {
	time.Sleep(5 * time.Second)
	fmt.Println("waited 5 seconds")
}
```
2 Go routines execute the example task that takes 5 seconds in +/- 5 seconds.


### Simple channels example:

```go
package main

import (
	"fmt"
	"time"
)

func main() {
	numbers := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
	// create the channel using make:
	c := make(chan int)

	// Launch the go routines that will execute the example function:
	for _, number := range numbers {
		go example(number, c)
	}
	
	// Range over all channels:
	for range numbers {
		// Inside the for clause we specify what we do with an individual channel:
		x := <-c				// read from the channel
		fmt.Println(x)
	}
}

// example function writes an integer to the channel:
func example(number int, c chan int) {
	time.Sleep(2 * time.Second)
	c <- number
}
/* Output:
15
5
0
9
11
12
7
3
8
6
2
4
14
13
10
1
*/
```

Notice that the Goroutines do not finish the work in the same order that they started it.


### Channels example including select and a timeout

```go
package main

import (
	"fmt"
	"time"
)

func main() {
	start := time.Now()

	// Creating channels that can transport different types of values:
	eve := make(chan int)
	odd := make(chan int)
	s_chan := make(chan string)

	// Run a func that sends values into the channels:
	go send(eve, odd, s_chan)

	// Run a func that uses 'select' to read the different values from these channels:
	receive(eve, odd, s_chan)
	elapsed := time.Since(start)
	fmt.Println("Seconds the script took to complete: ", elapsed)
}

const delaySeconds = 2

// Functions that sends different value types into the channels:
func send(e, o chan<- int, s chan<- string) {
	time.Sleep(delaySeconds * time.Second)
	for i := 0; i < 5; i++ {
		if i%2 == 0 {
			e <- i
		} else {
			o <- i
		}
	}
	time.Sleep(delaySeconds * time.Second)
	aSlice := []string{"some", "words", "were", "uttered"}
	for _, word := range aSlice {
		s <- word
	}
	time.Sleep(delaySeconds * time.Second)
	for i := 0; i < 5; i++ {
		if i%2 == 0 {
			e <- i
		}
	}
	time.Sleep(delaySeconds * time.Second)
	s <- "fin"
}

// loops over channels, using select to handle the 
func receive(e, o <-chan int, s <-chan string) {
	// for instructs the function to just keep on running select
	for {
		// select blocks until one of its cases can run, then it executes that case.
		//  It chooses one at random if multiple are ready.
		select {
		case v := <-e:
			fmt.Println("Reading even from channel: ", v)
		case v := <-o:
			fmt.Println("Reading odd from channel: ", v)
		case v := <-s:
			fmt.Println("Reading string from channel: ", v)
		// Timeout is set in this case,
		//  every iteration resets the timer.
		case <-time.After(5 * time.Second):
			fmt.Println("Time is up!!")
			return		// without this return, the program keeps hitting this case every 5 seconds.			
		}
	}
}
/* Output:
Reading even from channel:  0
Reading odd from channel:  1
Reading even from channel:  2
Reading odd from channel:  3
Reading even from channel:  4
Reading string from channel:  some
Reading string from channel:  words
Reading string from channel:  were
Reading string from channel:  uttered
Reading even from channel:  0
Reading even from channel:  2
Reading even from channel:  4
Reading string from channel:  fin
Time is up!!
Seconds the script took to complete:  13s


Note from time.After:
	After waits for the duration to elapse and then sends the current time on the returned channel. It is equivalent to NewTimer(d).C. The underlying Timer is not recovered by the garbage collector until the timer fires. If efficiency is a concern, use NewTimer instead and call Timer.Stop if the timer is no longer needed.
*/
```

### Work pattern using channels:

```go
// From Go in action
// from https://github.com/goinaction/code/blob/master/chapter7/patterns/work/work.go
//
// Notes:
// - the workers iterate the tasks one after the other
// - if one tasks takes a long time, backing up one worker, the other workers can continue iterating through the tasks
//
package main

import (
	"log"
	"sync"
	"time"
)

// Provide some tasks
var tasks = []string{
	"build a swimming pool",
	"bake a cake",
	"run up stairs",
	"climb a tree and catch wind",
	"dig a ditch",
	"lay bricks",
	"dig a hole",
	"build a house",
	"get some paper",
	"hunt a fox",
	"catch fish",
}

// workPrinter provides special support for printing work:
type workPrinter struct {
	work string
}

// In this example, Task implements the Worker interface for the workPrinter struct.
// Understanding how the interface is implemented makes it
//  possible to have other struct methods implement the interface also.
//
// Other example: https://github.com/saidvandeklundert/go/blob/main/examples/gosnmp/snmp_worker_verbose.go#L88
//
func (w *workPrinter) Task() {
	log.Println(w.work)
	time.Sleep(3 * time.Second)
}
func main() {
	// Increase the number of tasks( usefull if you want to up the workers to 200 or something):
	for i := 0; i < 2; i++ {
		tasks = append(tasks, tasks...)
	}

	// Create a work pool with x goroutines:
	p := New(3)

	// define a waitgroup and increment the counter for the amount of tasks we have
	var wg sync.WaitGroup
	wg.Add(len(tasks))

	// iterate over the slice of names
	for _, task := range tasks {
		// Create a workPrinter and provide the
		// specific task
		np := workPrinter{
			work: task,
		}
		go func() {
			p.Run(&np)
			wg.Done()
		}()
	}

	wg.Wait()

	// shutdown the work pool and wait for all existing work to be completed
	p.Shutdown()
}

// Worker must be implemented by types that want to use
// the work pool.
type Worker interface {
	Task()
}

// Pool provides a pool of goroutines that can execute any Worker
// tasks that are submitted.
type Pool struct {
	work chan Worker
	wg   sync.WaitGroup
}

// New creates a new work pool.
func New(maxGoroutines int) *Pool {
	p := Pool{
		work: make(chan Worker),
	}

	p.wg.Add(maxGoroutines)
	for i := 0; i < maxGoroutines; i++ {
		go func() {
			for w := range p.work {
				w.Task()
			}
			p.wg.Done()
		}()
	}

	return &p
}

// Run submits work to the pool.
func (p *Pool) Run(w Worker) {
	p.work <- w
}

// Shutdown waits for all the goroutines to shutdown.
func (p *Pool) Shutdown() {
	close(p.work)
	p.wg.Wait()
}
```


Go concurrency slogan:

```
Do not communicate by sharing memory; instead, share memory by communicating.
```


### to sort:

Green threads: user level threads. Scheduled as a user level process, not schedules by the Kernel. Green thread memory comes from the heap, not from the stack. In Go, these are known as Goroutines.


"Make it correct, make it clear, make it concise, make it fast. In that order" - Wes Dyer