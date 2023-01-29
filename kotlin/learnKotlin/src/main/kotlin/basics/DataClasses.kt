// In case you want to creat a class to represent an entity
// complete with implementations of equals, hashCode, toString etc, 
// use Data Classes

// Data class warning: copy on a Dataclass is implemented as a shallow copy.
package dataclasses

data class Person(
    val name:String,
    var age: Int,
)

fun makeAndPrintPersons(){
    val jan = Person(name="Jan", age=7)
    val marie  = Person("Marie",4)
    println("Data Classes created ${jan} ${marie}")
    // destructure the Data class:
    val (name,age) = jan
    println("${name} ${age}")
}