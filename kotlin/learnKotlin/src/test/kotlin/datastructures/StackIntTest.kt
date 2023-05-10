package datastructures

import kotlin.test.Test
import kotlin.test.assertEquals

import kotlin.test.assertEquals

class StackIntTest {

    @Test
    fun testStackCreation(){
        var stack = datastructures.Stack()
        assertEquals(10, stack.arr.size)
        stack = datastructures.Stack(size=100)
        assertEquals(100, stack.arr.size)
    }

    @Test
    fun testPush(){
        var stack = datastructures.Stack()
        stack.push("1")
        stack.push("2")
    }
    @Test
    fun testPushAndPop(){
        var stack = datastructures.Stack()
        stack.push("1")
        stack.push("2")
        assertEquals("2", stack.pop())
        assertEquals("1", stack.pop())
    }

    @Test
    fun testIsEmpty(){
        var stack = datastructures.Stack()
        assertEquals(true, stack.isEmpty())
        stack.push("1")
        assertEquals(false, stack.isEmpty())
        stack.pop()
        assertEquals(true, stack.isEmpty())
    }

    @Test
    fun testPeek(){
        var stack = datastructures.Stack()
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
        var stack = datastructures.Stack()
        assertEquals(false, stack.contains("1"))
        stack.push("1")
        stack.push("11")
        stack.push("111")
        stack.push("1111")
        assertEquals(true, stack.contains("1"))
        assertEquals(false, stack.contains("2"))
    }

    @Test
    fun testDisplay(){
        var stack = datastructures.Stack()
        stack.push("1")
        stack.display()
    }

    @Test
    fun testPeekBottom(){
        var stack = datastructures.Stack()
        assertEquals(null, stack.peekBottom())
        stack.push("1")
        assertEquals("1", stack.peekBottom())
        stack.push("11")
        assertEquals("1", stack.peekBottom())
        stack.push("111")
        stack.push("1111")
        assertEquals("1", stack.peekBottom())
        stack.pop()
        assertEquals("1", stack.peekBottom())
    }
}