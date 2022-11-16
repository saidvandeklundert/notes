package basics

import java.io.BufferedReader
import java.io.StringReader
import java.lang.NumberFormatException

fun readNumber(reader:BufferedReader):Int?{
    try{
        val line = reader.readLine()
        return Integer.parseInt(line)
    }
    catch (e:NumberFormatException){
        return null
    }
    finally{
        reader.close()
    }
}

fun exceptor(){
    val reader = BufferedReader(StringReader("2"))
    println(readNumber(reader))
}