package generics

fun <T> printMessage(message:T){

    println("message $message")
}

fun <T> createListOf(item:T):List<T>{
    var exampleList:List<T> = mutableListOf(item, item, item)

    println(exampleList)
    return exampleList
}

interface Generico<T> {
    fun double():T

    fun triple():T
}

class Point(val x:Int, val y:Int):Generico<Int>{

    override fun double():Int{
        return (this.x + this.y) * 2
    }
    override fun triple():Int{
        return (this.x + this.y) * 3
    }
}

class Human(val name:String):Generico<String>{
    override fun double():String{
        return " " + this.name + this.name
    }

    override fun triple():String{
        return " " + this.name + this.name + this.name
    }
}

fun functionExamples(){
    printMessage(1)
    printMessage("A string value")
    createListOf("1")
    createListOf(true)
    createListOf(arrayListOf(1,2,3))
    var myPoint = Point(2,3)
    println("${myPoint.double()} ${myPoint.triple()}")
    var myMan= Human("Mr T")
    println(" ${myMan.double()} ${myMan.triple()}")
}