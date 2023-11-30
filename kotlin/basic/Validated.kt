// kotlinc .\Validated.kt -include-runtime -d Validated.jar
// java -jar Validated.jar argument0 argument1
package classes

fun nameValidator(name:String):String{    
    if (name.length <2 ){
        throw IllegalArgumentException("Name too short")
    } else if (name.length > 45){
        throw IllegalArgumentException("Name too long")
    }
    return name
}

class Person(name:String){

    val name:String

    init {        
        this.name = nameValidator(name)
    }
}

fun classesWithValidators(){
    
    val said = Person(name="Said")
    println(said.name)

    try {
        val too_short = Person(name="o")
    } catch (e:Exception){
        println(e)
    }
    try {
        val toolong = Person(name="Olong Odor Bataar Balimy")
    } catch (e:Exception){
        println(e)
    }

}



fun main(args: Array<String>) {    
    classesWithValidators()
}