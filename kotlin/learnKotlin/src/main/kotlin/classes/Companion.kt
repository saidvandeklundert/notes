package classes

/*
 When a class has a Companion object defined, you can use the methods on the companion object
  without instantiating the class. The companion object is a singleton.
 */

class SomeClass{
    companion object {
        fun someMethod(){
            println("calling 'someMethod' on the companion object of SomeClass")
        }
    }
}

fun classesCompanion(){
    SomeClass.someMethod()
}