package patterns

/*
 - can explicitly name different object constructures
 - exceptions more accepted from methods
 */

/*

Companion object: methods that do not belong to an instance of a class
 */

class Router private constructor(hostname:String){
    val hostname = hostname
    init{
        println("Initializing router $hostname")
    }
    companion object{
        fun createRouter(hostname:String):Router{
            return Router(hostname)
        }
    }
}

fun staticFactoryMethod(){
    var r1 = Router.createRouter("Router1")
    println(r1.hostname)


}