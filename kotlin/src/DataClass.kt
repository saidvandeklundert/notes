package basics

data class Person(val name: String) {
    var age: Int = 0
}
enum class Gender {
    MALE, FEMALE
}

data class Employee(val name:String, val age:Int, val function:String, val gender:Gender)
fun main(){
    var person:Person = Person(name="Said van de Klundert")
    println(person)
    var employee = Employee(name="Bertrand", age=23, function="Noodle", gender=Gender.MALE)
    println(employee)
}