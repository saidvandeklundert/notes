package excercisms

import kotlin.test.Test
import kotlin.test.assertEquals

internal class HelloWorldKtTest {

    @Test
    fun testSum() {
        val expected = "Hello, World!"
        assertEquals(expected, excercisms.hello())
    }
}