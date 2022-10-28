
## Install kotlin

install scoop
scoop install kotlin

## Compile and run:

```
kotlinc-jvm .\hello_world.kt
kotlin Hello_worldKt
```
What happened here?
- compiled the `hello_world.kt` source file which gave the `Hello_worldKt.class` file.
- ran the file

## Run as script

Create a file with the `kts` extension and then:
```
kotlinc -script .\HelloWorldScript.kts
```

Note: you have to call a function in order for the script to run it. Even if the function is called main.

## Start the repl

```
kotlinc
Welcome to Kotlin version 1.7.20 (JRE 11.0.12+7)
Type :help for help, :quit for quit
>>> println("Hello, World!")
Hello, World!

>>> var name = "Jan"

>>> println("Hello, $name!")
Hello, Jan!

... :help

Available commands:
:help                   show this help
:quit                   exit the interpreter
:dump bytecode          dump classes to terminal
:load <file>            load script from specified file

>>> :quit
```
## Run online

Go to https://try.kotl.in/. Includes a tutorial.

## Java interoperability

You can:
- call Java functions and use Java classes / interfaces
- call Java APIs frmo Kotlin and vice versa
- have a mixed language project

There is also a Java to Kotlin converter.

## Functional programming:

- first-class functions: you can work with functions as values. Pass them around in variables and return them from other functions.
- immutability: you work with immutable objects that cannot change state after creation
- no side effects: use pure functions that return the same result given the same inputs and that do not modify the state of other objects or interact with the outside world in another way

## Mutable and immutable variables
`val`: value, an immutable reference. Cannot be re-assigned after it is initialized. Corresponds to a `final` in Java.
`var`: variable, a mutable reference.

Try to default to `val` and switch to `var` only when necessary.

A `val` can be declared and initialized later on based on a condition:
```kotlin
val message: String
if (someOperation()){
    message = "The eagle has landed"
} else{
    message = "The eagle has flown"
}
```

A `val` reference may point to a mutable object, like an `arrayListOf`.

Note that even though `var` variables can have their values changed, their type is fixed.


## Packaging and imports

Every Kotlin file can have a package statement. If so, all declarations in the file are placed in that package.
Declarations in other files can be used directly in case they are in the same package.

Declarations made in other packages need to be imported.

## Links

[awesome Kotlin](https://github.com/mcxiaoke/awesome-kotlin)