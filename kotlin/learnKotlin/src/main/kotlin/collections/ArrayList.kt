package collections

fun arrayListOperations(){
    var list:ArrayList<String> = arrayListOf()

    list.add("1")
    list.add("2")
    list.add("3")
    list.add("4")
    for ((index, element) in list.withIndex()){
        println("$index $element")
    }
    println(list[0])
    println(list)
    list

}