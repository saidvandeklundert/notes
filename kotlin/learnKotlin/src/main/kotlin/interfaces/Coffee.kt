package interfaces

interface Coffee {
    val name: String
    val price: Int
    fun prepare()
    fun drink()
}

class Cappuccino: Coffee {
    override val name: String = "Cappuccino"
    override val price: Int = 3
    override fun prepare() {
        println("Preparing $name")
    }
    override fun drink() {
        println("Drinking $name")
    }
}

class Americano: Coffee {
    override val name: String = "Americano"
    override val price: Int = 2
    override fun prepare() {
        println("Preparing $name")
    }
    override fun drink() {
        println("Drinking $name")
    }
}


fun prepareCoffee(coffee: Coffee){
    coffee.prepare()
}

fun drinkCoffee(coffee: Coffee){
    coffee.drink()
}

fun coffeeExample(){
    val cappuccino = Cappuccino()
    val americano = Americano()
    prepareCoffee(cappuccino)
    drinkCoffee(cappuccino)
    prepareCoffee(americano)
    drinkCoffee(americano)
}