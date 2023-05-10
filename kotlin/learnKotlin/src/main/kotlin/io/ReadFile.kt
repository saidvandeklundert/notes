package io

import java.io.File

fun printDataToFile(fileName: String, data: String) =
    File(fileName).printWriter().use { writer ->
        writer.println(data)
    }


fun filesAndStuff(){
    printDataToFile("C:\\dev\\notes\\kotlin\\learnKotlin\\src\\main\\kotlin\\io\\rubbish.txt", "rubbish")
}