package classes
// This refers to the class instance attributes, like when you use 'self' in Python
fun mainThis(){
    val jan = ThisPerson("an", 7)
    jan.updateName("Marie")
    println(jan.name)
}
class ThisPerson(var name:String, var age:Int){
    fun updateName(name:String){
        this.name = name
    }
}