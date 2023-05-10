package classes

fun nameValidator(name:String):String{
    println("name validator runs")
    if (name.length <2 ){
        throw IllegalArgumentException("Name too short")
    } else if (name.length > 45){
        throw IllegalArgumentException("Name too long")
    }
    return name
}

class ValidatedPersonData(name:String){

    val name:String

    init {
        println("running the constructor that is defined in the init block")

        println("running name validator")
        this.name = nameValidator(name)


    }


}

fun classesWithValidators(){
    println("\nRunning classesWithValidators")
    val said = ValidatedPersonData(name="Said")
    println(said.name)

    try {
        val o = ValidatedPersonData(name="o")
    } catch (e:Exception){
        println(e)
    }
    try {
        val toolong = ValidatedPersonData(name="ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
    } catch (e:Exception){
        println(e)
    }

}