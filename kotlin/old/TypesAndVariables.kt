
fun main() {
    // var means the value is allowed to change
    var age:Int = 0
    // val means that value is NOT allowed to change
    val immutable_age:Int = 1

    // Strings
    var name:String="Said"
    var last_name = "van de Klundert" // types can also be inferred
    var escape_char = "A new line\n"
    var concatenatedString:String = "some words " + "concatenated " +
            "together"
    val multiLineSting:String = """
This is a string
that covers
multiple lines
    """.trimIndent()

    // Kotlin offers string interpolation:
    var message:String = "My name is $name, lenght of my name is ${name.length}"
    println(message)
    var character:Char = 's' // mind the single '

    // some types
    var number_0: Short = 1
    var number_1: Int = 1
    var number_2: Long=12292323
    var number_3: Float = 1.1f
    var number_4: Double = 254.2
    var number_5: Byte = 2

    // types can be inferred, but conversion is ALWAYS explicit:
    var MyInt = 2
    var MyLong = MyInt.toLong()


    println("yolo")



}
