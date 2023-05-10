package controlflow

import com.fasterxml.jackson.databind.node.BooleanNode


fun controlFlowExamples(){
    val a = bigNumber(1)
    val b = bigNumber(1213)


    val c = bigNumberOneIf(1213)
    val d = bigNumberReturnExpression((1213))
    println("{$a} {$b} {$c} {$d}")
    println(usingWhen("Said"))
    println(usingWhen("Marie"))
    forEachLoop()
    forLoop()
    whileLoop()
}

fun bigNumber(someNumber:Int):Boolean{
    if (someNumber >10){
        return true
    } else{
        return false
    }
}

fun bigNumberOneIf(someNumber:Int):Boolean{
    var result = false
    if (someNumber > 10){
        result = true
    }
    return true
}

fun bigNumberReturnExpression(someNumber:Int):Boolean{
    return if (someNumber >10){
        true
    } else{
        false
    }
}

fun usingWhen(name: String) = when (name) {

    "Said" -> "work for Amazon"

    "Jan" -> "go to school"

    else -> "Unknown"

}

fun forEachLoop(){
    for (c in "Said van de Klundert"){
        println(c)
    }
}

fun forLoop(){
    for (i in 0..5){
        println(i)
    }
    for (i in 3 until 8){
        println(i) // stops after printing 7
    }
    for (i in 9 downTo 2){
        println(i)
    }
}

fun whileLoop(){
    var x = 0;
    while (x < 10) {
        x ++
        println("while $x")
    }
}