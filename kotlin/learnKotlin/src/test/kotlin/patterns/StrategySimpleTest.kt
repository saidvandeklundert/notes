package patterns

import kotlin.test.Test
import kotlin.test.assertEquals

class StrategyTest{
    @Test
    fun testStrategyUpperCase(){
        val input:String = "SOME input VaLuE"
        val expected:String ="SOME INPUT VALUE"
        val upperCasePrinter = patterns.Printer(upperCase)

        assertEquals(expected,upperCasePrinter.CreateMessage(input) )

    }
    @Test
    fun testStrategyLowerCase(){
        val input:String = "SOME input VaLuE"
        val expected:String ="some input value"
        val lowerCasePrinter = patterns.Printer(lowerCase)

        assertEquals(expected,lowerCasePrinter.CreateMessage(input) )

    }
}