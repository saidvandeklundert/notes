package datastructures
// abstrack Stack and implementation
abstract class StackAbstract {

    abstract var stack:Array<String>

    abstract fun push(item:String)

    abstract fun pop():String?

    abstract fun isEmpty():Boolean

    abstract fun peek():String?

    abstract fun peekBottom():String?

    abstract fun contains(query:String):Boolean

    abstract fun display()

    abstract fun size():Int
}

class ArrayStack():StackAbstract(){
    var head:Int = 0
    var stackLimit:Int = 10
    override var stack:Array<String> = arrayOf("0","0","0","0","0","0","0","0","0","0",)

    override fun push(item:String){
        if (this.head+1 > this.stackLimit){
            throw RuntimeException("Stack overflow")
        }
        this.stack[this.head] = item
        this.head +=1
        println("pushed $item, head is now ${this.peek()}")
    }

    override fun pop():String?{
        if (this.isEmpty()){
            return null
        } else{
            val returnItem = this.stack[this.head-1]
            this.head -=1
            if (this.isEmpty()){
                println("popped $returnItem of the stack, stack is now empty")
                return returnItem
            } else{
                println("popped $returnItem of the stack, head is now ${this.stack[this.head-1]}")
                return returnItem
            }

        }

    }

    override fun isEmpty(): Boolean {
        return (this.head == 0)
    }

    override fun peek():String?{
        println("peek")
        if (this.isEmpty()){
            return null
        } else{
            return this.stack[this.head-1]
        }
    }

    override fun contains(query: String): Boolean {
        for (item in this.stack){
            if (item == query){
                return true
            }
        }
    return false
    }

    override fun display() {
        println("display the stack")
        if (this.isEmpty()){
            println("")
        } else{
            var x = 0;
            print("[ ")
            while (x < this.head) {
                print("${this.stack[x]} ")
                x +=1
            }
            println("]")
        }


    }

    override fun peekBottom(): String? {
        println("bottom")
        if (this.isEmpty() == true){
            println("stack is empty")
            return null
        }

        return this.stack[0]
    }

    override fun size(): Int {
        return this.head
    }

}

fun stackExample(){
    var stack = ArrayStack()
    stack.display()
    stack.push("4")
    stack.push("3")
    stack.push("2")
    stack.push("1")
    //for ((index, element) in stack.stack.withIndex()){
    //    println("$index $element")
    //}
    stack.display()
    //var peeked = stack.peek()
    //println("peeked $peeked")
    println("contains 190: ${stack.contains("190")}")
    //println("contains 1: ${stack.contains("1")}")

    stack.display()
    println(stack.pop())
    println(stack.pop())
    stack.display()
    stack.push("1")
    stack.push("1")

    var s2 = ArrayStack()
    s2.display()
    s2.push("4")
    s2.pop()
    s2.push("4")
    s2.push("3")
    s2.push("2")
    s2.pop()
    s2.display()
    println(s2.peek())
    println(s2.peekBottom())
    println(s2.size())
}