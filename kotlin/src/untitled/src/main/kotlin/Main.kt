import com.google.gson.Gson
data class TestModel(
    val id: Int,
    val description: String
)

fun main(args: Array<String>) {
    println("Hello World!")

    // Try adding program arguments via Run/Debug configuration.
    // Learn more about running applications: https://www.jetbrains.com/help/idea/running-applications.html.
    println("Program arguments: ${args.joinToString()}")
    var gson = Gson()
    var jsonString = gson.toJson(TestModel(1,"Test"))
    //Assert.assertEquals(jsonString, """{"id":1,"description":"Test"}""")
    //println(jsonString)
}