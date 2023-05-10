package datastructures

interface StackInterface{

    fun push(item:String)

    fun pop():String?

    fun isEmpty():Boolean

    fun peek():String?

    fun contains(query:String):Boolean

    fun display()

    fun peekBottom(): String?
}


class Stack(size:Int=10):StackInterface{

    var head:Int = 0
    val arr = arrayOfNulls<String>(size)

    override fun push(item: String) {
        if (this.head+1 > this.arr.size){
            throw RuntimeException("Stack overflow")
        }
        this.arr[this.head] = item
        this.head +=1
        println("pushed $item, head is now ${this.peek()}")
    }

    override fun pop(): String? {
        if (this.isEmpty()){
            return null
        }
        else{
            val returnItem = this.arr[this.head-1]
            this.head -=1
            if (this.isEmpty()){
                println("popped $returnItem of the stack, stack is now empty")
                return returnItem
            }
            else{
                println("popped $returnItem of the stack, head is now ${this.arr[this.head-1]}")
                return returnItem
            }

        }
    }

    override fun isEmpty(): Boolean {
        return (this.head == 0)
    }

    override fun peek(): String? {
        if (this.isEmpty()){
            return null
        }
        else{
            return this.arr[this.head-1]
        }
    }

    override fun contains(query: String): Boolean {
        for (item in this.arr){
            if (item == query){
                return true
            }
        }
        return false
    }

    override fun display() {
        println(this.arr.joinToString())
    }

    override fun peekBottom(): String? {
        if (this.isEmpty()){
            return null
        }
        else{
            return this.arr[0]
        }
    }


}