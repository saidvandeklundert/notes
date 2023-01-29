package basics

// 
fun talkAboutNull(){
    // following MUST always be of the type String, it cannot be null:
    var name:String = "Said"
    println(name)
    var name_or_null:String? = null
    println(name_or_null)

    // elvis operator (?:) can be used to substitute possible null:
    printStringExample(name_or_null)
    name_or_null = "Jan"
    printStringExample(name_or_null)
}

fun printStringExample(s:String?){
    println("printStringExample for ${s}")
    // 
    println(s?.uppercase())
    // use ?: to indicate the value in case s is null
    val toPrint = s ?: "unkown"
    println(toPrint)
    
    // or in one go:
    println(s?.uppercase() ?: "unknown")    

}

