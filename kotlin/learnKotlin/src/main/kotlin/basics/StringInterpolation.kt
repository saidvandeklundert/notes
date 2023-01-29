package stringinterpolation

fun exampleInterpolations(){
    example()
}

fun example(){
    val someNumber:Int=100
    val someString:String="Twinkle"
    println("interpolate a variable: $someNumber")

    println("Interpolate a function ${add(4,4)}")
    println("""
    Twinkle, $someString Little Bat
    How I wonder what you're at!
    """.trimIndent())
}

fun add(a:Int, b:Int):Int{
    return a+b
}