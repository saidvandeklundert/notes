package basics

/*
Interfaces in Kotlin can contain declarations of abstract methods, as well as method implementations.

What makes them different from abstract classes is that interfaces cannot store state.

They can have properties, but these need to be abstract or provide accessor implementations.
 */

interface Person{

    fun introduce():String
    fun work():String
}

class Baker(val name:String):Person{

    override fun introduce():String {
        return "Hello, I am a Baker called $name"
    }
    override fun work():String {
        return "I bake bread"
    }
}


class Programmer(val name:String, val language:String):Person{

    override fun introduce():String {
        return "Hello, I am a programmer called $name"
    }
    override fun work():String {
        return "I program in $language"
    }
}

fun interfaces_main(){
    val bill = Baker(name = "Bill")
    println(bill.introduce())
    println(bill.work())
    val bob = Programmer(name="Bob", language = "Kotlin")
    println(bob.introduce())
    println(bob.work())
}