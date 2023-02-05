package types
import java.util.*
// Several of the Kotlin types, this fun is also an object
// the return type is implicit, it is 'Unit'
fun someKotlinTypes(){
    var someInt:Int=0
    val someImmutableInt:Int=0
    var someInferredInt = 0

    val someString:String="hello Said"

    val someBool:Boolean=false
    val someOtherBool = true

    // comparisons
    println(someBool == someOtherBool)
    println(someBool != someOtherBool)

    // call fun
    val returned_message = amplifyMessage(someString)
    println(returned_message)
    lengthPrinter(returned_message)
    lengthPrinter(null)
    simpleList()
    simpleSet()
    simpleMap()
    treeMapExample()
    simpleArray()
}


// function that takes a string and returns it all uppercase:
fun amplifyMessage(message:String):String{
    return message.uppercase()
}

// function that takes an optional string and prints the lenght
fun lengthPrinter(someString:String?){
    println(someString?.length)
}


fun simpleList(){
    // initialize an immutabe list:
    val someList :List<String> = listOf("Said", "Anne", "Jan", "Marie")
    // loop through the list:
    for (name in someList){
        println(name)
    }
    // Same thing for the mutable version
    var mutableList = mutableListOf("Said", "Anne", "Jan", "Marie")
    mutableList.add("Henk")
    mutableList.add("Kees")
    val uppercaseName = mutableList[0].uppercase()
    mutableList[0] = uppercaseName
    for (name in someList){
        println("Mutable list name: $name")
    }
}

fun simpleSet(){
    // initialize an immutable set
    val someSet:Set<String> = setOf("Said", "Anne", "Jan", "Marie", "Henk")

    // loop through set:
    for (name in someSet){
        println("Set name: $name")
    }
}

fun simpleMap(){
    val ages= mapOf<String,Int>(
        "Henk" to 0,
        "Anne" to 38,
        "Said" to 38,
        "Marie" to 4,
        "Jan" to 7,
    )
    println(ages)
    println(ages["Henk"])
    println("January" in ages)
    for (entry in ages.entries.iterator()) {
        println("${entry.key} : ${entry.value}")
    }

    // mutable map:
    var mutableAges = mutableMapOf<String,Int>(
        "Henk" to 0,
        "Anne" to 38,
    )
    mutableAges.put("Jan",7)
    mutableAges.put("Marie", 4)
    mutableAges.put("Said", 38)

    for (entry in ages.entries.iterator()) {
        println("${entry.key} : ${entry.value}")
    }


}

// Using Treemap


// Mutable map that is sorted by its keys
fun treeMapExample(){
    val treeMap = java.util.TreeMap(

        mapOf(

            "One" to "1",

            "Two" to "2",

            "Three" to "3"

        )

    )

    println(treeMap.keys)
}


fun simpleArray(){
    val people: Array<String> = arrayOf("Dave", "David",   "Desiree")
    val arrayOfNumber = listOf(1, 2, 3, 5).toTypedArray()
    println(people.joinToString(", "))
    println(arrayOfNumber.joinToString(", "))
}

fun casts(AnyValue:Any){
    // unsafe cast:
    val port: Int = AnyValue as Int
    // When an unsafe cast fails, the program will crash
    // safe cast:
    val safePort:Int? = AnyValue as? Int

    // When a safe cast fails, the cast returns 'null'

    // smart cast is better, cast only if it is possible:
    if (AnyValue is Int){
        val inForSure :Int = AnyValue

    }
}