package basics
class Human(val name:String, var age:Int){
    fun displayAge():Int{
        return age
    }

    override fun toString():String{
        return "$name is $age years old"
    }
}


// Enums can have methods
enum class Color(
    val r:Int, val g:Int, val b:Int
){
    RED(255,0,0), ORANGE(255,165,0),YELLOW(255,255,0),GREEN(0,255,0),BLUE(0,0,255),
    INDIGO(255,255,0),VIOLET(238,130,238);

    fun rgb() = (r* 256 +g) * 256 + b
}
