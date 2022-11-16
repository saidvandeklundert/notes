package basics

import java.util.TreeMap
fun loopy(i:Int) = when{
    i % 15 ==0 -> "divisable by 15\n"
    i % 3 == 0 -> "divisable by 3\n"
    i % 5 == 0 -> "divisable by 5\n"
    else -> "$i\n"
}

fun callLoopy(){
    for (i in 1..100){
        print(loopy(i))
    }
}

fun iterateMap(){
    val binaryReps = TreeMap<Char,String>()
    for (c in 'A'..'F'){
        val binary = Integer.toBinaryString(c.code)
        binaryReps[c] = binary
    }

    for ((letter,binary) in binaryReps){
        println("$letter = $binary")
    }
}

fun iterateCollection(){
    val list = arrayListOf("10","11","12")
    for ((index, element) in list.withIndex()){
        println("$index $element")
    }
}
