package classes
fun main_constructor_examples(){
    var jan = Human("Jan", 7)
    jan.greet()
    val someCar = Car("BMW", 260)
}

// If we plan on having 1 constructor, we do not use the constructor keyword.
// The input arguments are used to instantiate the class are supplied in the class declaration
class Human(val name:String, var age:Int){
    fun greet(){
        println("Hello, my name is $name and I am $age years old")
    }
}

// Example of a class with multiple constructors
// The input arguments used to instantiate the class determine what constructor is used
class Car{
    constructor(){
        model = "No model"
        topSpeed = 160
    }
    constructor(newModel:String){
        model=newModel
        topSpeed = 160
    }
    constructor(newModel:String, newTopSpeed:Int){
        model=newModel
        topSpeed=newTopSpeed
    }

    var model:String?=null
    var topSpeed:Int = 100
}