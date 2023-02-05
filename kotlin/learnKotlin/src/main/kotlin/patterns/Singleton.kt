package patterns
// Singleton

// Ensuring there is only 1 instance of a certain type.


// We use the keyword object to implement the singleton patter
object SingletonLogger{
    init{
        println("""
        All the code that is required for Logger setup.
        Singleton is lazy initialized.
        """.trimIndent())
    }

    fun log(message:String) {
        println("Logging $message")
    }
}