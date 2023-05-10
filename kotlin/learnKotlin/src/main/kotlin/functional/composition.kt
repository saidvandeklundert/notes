package functional

fun composition(){
    println("composition")


    fun composed(f: (Int)->Int, g: (Int)->Int):(Int)->Int = { x -> f(g(x)) }

    // composed takes 2 functions as arguments:
    // - f: (Int)->Int: this function takes an Int and returns an Int
    // - g: (Int)->Int: this function takes an Int and returns an Int
    //
    // The composed function body is written like so: { x -> f(g(x)) }
    //
    // This is taking an input int called x,
    // and passing it to the function g
    // and then passing the result of that to the function f
    // and then returning the result of that.

    fun square(n:Int):Int = n * n
    fun triple(n:Int):Int = n * 3

    val squareThenTriple = composed(::square, ::triple)
    println(squareThenTriple(3))
}