package interfaces

interface AnimalBehavior{
    fun makeSound():String
    fun move():String
}

class Dog:AnimalBehavior{
    override fun makeSound(): String {
        return "Woof woof"
    }

    override fun move(): String {
        return "runs on 4 legs"
    }

}

class Pigeon:AnimalBehavior{
    override fun makeSound(): String {
        return "rookoo roo rookoo"
    }

    override fun move(): String {
        return "flies off"
    }

}

fun mainAnimals(){
    val yeller = Dog()
    val joe = Pigeon()
    println(yeller.makeSound())
    println(joe.makeSound())
}