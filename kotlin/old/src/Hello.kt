package basics
fun main(args: Array<String>) {
    println("Hello world!")
    val jan = Human("Jan",7)
    jan.age = 19
    println(jan.displayAge())
    println(jan)
    println(multiply(2,2))
    println(another_multiply(2,2))
    println(another_multiply_with_type_inference(2,2))
    callLoopy()
    iterateMap()
    iterateCollection()
    exceptor()
}


// regular function with a 'block body':
fun multiply(a:Int, b:Int):Int{
    return a * b
}

// Another way to write the function
// with an expression body:
fun another_multiply(a:Int,b:Int):Int = a * b

// The same function with the return type inferred:
fun another_multiply_with_type_inference(a:Int,b:Int) = a * b