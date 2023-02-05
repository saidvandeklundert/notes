package patterns


class Printer(private val stringFormatterStrategy: (String) ->String){
    fun CreateMessage(message:String) :String{
         val result = stringFormatterStrategy(message)
        println(result)
        return result
    }
}

val lowerCase = {string:String->string.lowercase()}
val upperCase = {string:String->string.uppercase()}

fun StrategySimple(){
    val upperCasePrinter = Printer(upperCase)
    upperCasePrinter.CreateMessage("ddddd")
    val lowerCasePrinter = Printer(lowerCase)
    lowerCasePrinter.CreateMessage("DDDD")
}