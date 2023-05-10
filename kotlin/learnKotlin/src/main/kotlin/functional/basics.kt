package functional

typealias IntBinOp = (Int) -> (Int) -> Int

fun Currying(){
    // curried form of the equivalent functions of tuples:

    val add: IntBinOp = { a -> { b -> a + b } }
    val multiply:IntBinOp = {a -> {b -> a * b} }
    println(add(3)(5))
    multiply(3)(5)
}

fun valueFunctions(){
    println("value functions")
    // normal function:
    fun normalDouble(x: Int): Int = x * 2
    // same function as a value function:
    val double: (Int) -> Int = {x -> x *2}
    println(double(3))

    // value functions can cross multiple lines:
    val doubleThenAddOne: (Int) -> Int = {
        x ->
        val doubled = x * 2
        doubled + 1
    }
    println(doubleThenAddOne(3))
}


fun funtionReference(){
    println("function reference")
    fun normalDouble(x:Int):Int = x * 2
    // function reference:
    val double: (Int) -> Int = ::normalDouble
    println(double(3))
}


