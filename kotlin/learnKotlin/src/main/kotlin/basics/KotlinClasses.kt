package kotlinclasses

fun examples(){
    println("some example classes")
    var simpleJan = SimpleHuman("Jan", -2)
    var jan = Human("Jan")
    println(simpleJan.name)
    println(simpleJan.age)
    println(jan.name)
    println(jan.age)
    var janWithAnInterface = HumanWithInterface("Jan")
    janWithAnInterface.age = 7
    janWithAnInterface.greet(janWithAnInterface.name)
    println(janWithAnInterface.abstractGreeting())
    var janDataClass = HumanDataClass("Jan", 7)
    println(janDataClass)
    val passWord = "Admin123"
    println(passWord.hidePassword())
    val d = SysDev("Zeus")
    d.walk()
    d.speak()
    d.doSomething()

    val c = SoftwareDeveloper("Rusty")
    c.walk()
    c.speak()
    c.doSomething()

}

class SimpleHuman(val name:String, var age:Int){
    // just a class with some fields
}

class Human(name: String) {
    val name = name
        // custom getter
        get() = field.uppercase()
    var age: Int = 0
        // custom setter prevents age from being a negative
        set(value) {

            field = if (value >= 0) {

                value

            } else {

                0

            }

        }

}

// Interface specification and implementation
interface Greeter {
    // abstract interface
    fun abstractGreeting():String

    fun greet(name:String){
        println("Hello, I am $name!")
    }

}

class HumanWithInterface(val name:String):Greeter{
    var age: Int = 0
    override fun abstractGreeting(): String {
        return "Hello, I am $name! This is the implementation of the abstract interface"
    }
}


/*

Abstract class:
- similar to interfaces
- cannot be initialized
- can contain state

* */
abstract class Employee (name: String) {
    abstract fun doSomething(): Unit          //abstract, open by default
    fun walk(): Unit = println("I’m walking")  //concrete, closed (final)
    open fun speak(): Unit = println("Default")     //concrete, open
}


class SysDev(name: String) : Employee(name) {
    override fun doSomething() = println("Setting up pipelines, tending to the containers")
}

class SoftwareDeveloper(name: String) : Employee(name) {
    override fun speak() = println("I write software")
    override fun doSomething() = println("Refactoring and writing code")
}

// dataclass
data class HumanDataClass(val name:String, var age:Int)

// Extension function
fun String.hidePassword() = "*".repeat(this.length)