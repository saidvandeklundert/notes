// kotlinc-jvm .\Day3RuckSack.kt
// kotlin Day3RuckSackKt

import java.io.File
import java.io.InputStream

fun read_input(file_name:String):String{
    val inputStream: InputStream = File(file_name).inputStream()
    val inputString = inputStream.bufferedReader().use { it.readText() }
    return inputString
}

fun main() {
    val second_input = read_input("input_3.txt")
    println(second_input)
}