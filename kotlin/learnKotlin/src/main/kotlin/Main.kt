import kotlinx.serialization.Serializable
import kotlinx.serialization.json.Json
import kotlinx.serialization.decodeFromString
import java.io.File
fun readFileAsLinesUsingBufferedReader(fileName: String): String
        = File(fileName).bufferedReader().readLines().toString()

fun main() {
    println("hello world")
    val fileContent = readFileAsLinesUsingBufferedReader("src/main/kotlin/some_data.yaml")
    println(fileContent)
}