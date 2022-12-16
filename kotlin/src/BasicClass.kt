class Customer(var id:Int , var name: String){
}

class AlternateCustomerSyntax1(){
    var id: Int = 0
    var name: String="String"
}
class AlternateCustomerSyntax2(){
    var id: Int = 0
    var name: String="String"
    init {
        // Optional initializer
        println("This runs when the class is initialized.")
        this.name = name.uppercase()

    }
}


fun main(args: Array<String>){
    val customer = Customer(10, "Said")
    var custer_alternative = AlternateCustomerSyntax2()
    println(custer_alternative.name)
}