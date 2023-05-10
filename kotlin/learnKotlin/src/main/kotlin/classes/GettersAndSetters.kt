package classes
fun mainGettersAndSetters(){
    var jan = Person()
    jan.name = "Jan"
    jan.age = 7
    println(jan.name)
    println(jan.age)

    var said = ValidatedPersonData(name="Said")
    println(said.name)
}

class Person()
{
    var name: String = ""
        get() {
            return field.uppercase()
        }
        set(value) {
            println("Setting the name to $value")
            field = value
        }
    var age:Int = 0
        get() {
            return field
        }
        set(value) {
            println("Setting the age to $value")
            field = value
        }

}

