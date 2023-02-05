package excercisms
import kotlin.test.Test
import kotlin.test.assertEquals

class TwoFerTest {


    @Test
    fun aNameGiven() {
        assertEquals("One for Alice, one for me.", excercisms.twofer("Alice"))
    }
    @Test
    fun noNameGiven() {
        assertEquals("One for you, one for me.", excercisms.twofer())
    }

    @Test
    fun anotherNameGiven() {
        assertEquals("One for Bob, one for me.", excercisms.twofer("Bob"))
    }

    @Test
    fun emptyStringGiven() {
        assertEquals("One for , one for me.", excercisms.twofer(""))
    }

}
