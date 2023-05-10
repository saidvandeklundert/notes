package datastructures


import kotlin.test.Test
import kotlin.test.assertEquals

internal class StackAbstractTest {

    @Test
    fun testPeek(){
        var stack = datastructures.ArrayStack()
        assertEquals(null, stack.peek())
        stack.push("1")
        assertEquals("1", stack.peek())
        stack.push("11")
        assertEquals("11", stack.peek())
        stack.push("111")
        stack.push("1111")
        assertEquals("1111", stack.peek())
        stack.pop()
        assertEquals("111", stack.peek())
    }
    @Test
    fun testContains(){
        var stack = datastructures.ArrayStack()
        assertEquals(false, stack.contains("1"))
        stack.push("1")
        stack.push("11")
        stack.push("111")
        stack.push("1111")
        assertEquals(true, stack.contains("1"))
        assertEquals(false, stack.contains("2"))
    }
    @Test
    fun testPushAndPopAndEmpty() {
        var stack = datastructures.ArrayStack()
        assertEquals(true, stack.isEmpty())
        stack.push("1")
        stack.push("2")
        stack.push("3")
        stack.push("4")
        assertEquals(false, stack.isEmpty())
        assertEquals("4", stack.pop())
        assertEquals("3", stack.pop())
        assertEquals("2", stack.pop())
        assertEquals("1", stack.pop())
        assertEquals(null, stack.pop())


    }
    @Test
    fun testPushAndSize() {
        var stack = datastructures.ArrayStack()
        assertEquals(0, stack.size())
        stack.push("1")
        assertEquals(1, stack.size())
        stack.push("2")
        assertEquals(2, stack.size())
        stack.push("2")
        stack.push("2")
        assertEquals(4, stack.size())

    }
}