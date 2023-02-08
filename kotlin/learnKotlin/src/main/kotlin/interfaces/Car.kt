package interfaces

interface Car {
    val speed:Int
    fun drive()
    fun stop()
}

class BMW: Car {
    override val speed: Int = 250
    override fun drive() {
        println("BMW driving at $speed kph")
    }
    override fun stop() {
        println("Stopping")
    }
}

class VolksWagen: Car {
    override val speed: Int = 220
    override fun drive() {
        println("VW driving at $speed kph")
    }
    override fun stop() {
        println("Stopping")
    }
}

class CarFactory {
    // The companion object is used to make a method callable without
    // the need to create an instance of the class
    companion object {
        fun makeCar(carType:String):Car {
            return when(carType) {
                "BMW" -> BMW()
                "VW" -> VolksWagen()
                else -> throw Exception("Unknown car type")
            }
        }
    }
}


fun mainCar(){

    val bmw = CarFactory.makeCar("BMW")
    val vw= CarFactory.makeCar("VW")
    bmw.drive()
    vw.drive()
}