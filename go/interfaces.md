## Interfaces 

All types are concrete types, except the interface type. The interface type is an abstract type and unlike with a concrete type, we cannot directly use an interface type to create a value.

Interfaces can be usefull in case a method does something that can be re-used for a variety of objects. Interfaces in Go are oftentimes explained as something that is used to define a behavior, like printing, writing etc.

You can create a variable that is an interface type and that has the methods that belong to the interface. This makes the method a custom type as well as a collection of methods.

Interfaces are implicit. We do not manually define the correlation between the interface custom type and the other methods and functions.

Interfaces can be seen as a contract to help manage types. The Go compiler will check all the values and the returns involved, but (obviously) will not check if the logic that is used is sound.


## Defining an interface

The following is an example on how you can define an interface that groups together several methods:

```go
type HumanBehaviors interface {
	Speak(s string)
	Greet(s string) (g string)
	Sleep()
}
```

The interface is defined as a collection of method signatures.

The methods are themed 'HumanBehaviors'. The `interface` keyword indicates this is an interface.

This interface right now does not do anything and you cannot call it. It is an abstract that merely describes a set of behaviors.

After definnig the interface, we can now implement it on types by providing the type with any of the methods mentioned in the interface.

This part was the most confusing to me initialy as this is not something that is done directly. Rather, instead of syntactically directly implementing or referring to in one way or another, a type merely has to `satisfy` the interface. This is done by implementing it's methods.

Let's make a struct and give that struct a method that is an implementation of the interface:

```go
// Defining the type:
type Person struct {
	Name string
}

type SoftSpokenPerson struct {
	Person
}

// Implementation of the interface:
func (ssp SoftSpokenPerson) Speak(s string) {
	fmt.Println("Speaks with a soft voice: ", s)
}

func (ssp SoftSpokenPerson) Greet(s string) (g string) {
	g = fmt.Sprintf("Greets with a soft voice: %s", s)
	return g
}

func (ssp SoftSpokenPerson) Sleep() {
	fmt.Println("zzzzzzzzzzzzzzzzzzzz")
}
```
We can see there was no explicit declaration of intent and no syntax involved here whatsoever. The interface was implemented imlicitly through the definition of the interface methods on the type `SoftSpokenPerson`. Through that definition, we `satisfied` the interface.

Let's use the interfaces:

```go

silentBob := SoftSpokenPerson{
	Person: Person{
		Name: "Bob",
	},
}
// using the interface:
silentBob.Speak("talk talk talk")
g := silentBob.Greet("Hello there.")
fmt.Println(g)
silentBob.Sleep()
/*
Speaks with a soft voice:  talk talk talk
Greets with a soft voice: Hello there.
zzzzzzzzzzzzzzzzzzzz
*/
```

Note that in order to implement an interface, the type has to implement `all` of the methods from the interface. To verify that this was done, you could do something like this:

```go
var h HumanBehaviors    // h is the zero value for the interface
h = silentBob   // h is assigned the value of silentBob
t, ok := h.(interface{ HumanBehaviors })    // we assert that the type of h is HumanBehaviors
fmt.Printf("t: %v ok: %v", t, ok)
/* Output:
t: {{Bob}} ok: true

To see it fail, comment out one of the methods so that the interface is no longer satisfied. 
 You will start seeing errors as soon as you do this.
*/
```

Another thing about interfaces is that you can program against the interface itself. The following function is an example function that takes in the previously defined interface:
```go
func programAgainstTheInterface(h HumanBehaviors) {
	h.Sleep()
	h.Greet("Hello.")
	h.Speak("Thus spoke the interface.")
}
// Pass in the previously defined instances of the structs that satisfy the interface:
programAgainstTheInterface(silentBob)
programAgainstTheInterface(loudLarry)
```


The interface is a type. If some type implements the ibterface, it also becomes that type. The full code for the examples we used is found [here](https://github.com/saidvandeklundert/go/tree/main/examples/interfaces).



'If you have my method you are also my type.' - the interface

'The bigger the interface, the weaker the abstraction' - Rob Pike.