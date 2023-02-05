package patterns

interface ChessPiece {
    var file:Char
    var rank:Char
}

data class Pawn(
    override var file:Char,
    override var rank:Char
):ChessPiece

data class Queen(
    override var file:Char,
    override var rank:Char
):ChessPiece

data class King(
    override var file:Char,
    override var rank:Char
):ChessPiece

fun createPiece(notation:String):ChessPiece{
    val (type, file, rank) = notation.toCharArray()
    return when (type){
        'q' ->Queen(file, rank)
        'p'-> Pawn(file, rank)
        'k' -> King(file,rank)
        else -> throw RuntimeException("Unkown piece: $type")
    }
}

fun factoryMethodExample(){
    val king = createPiece("ka6")
    val queen = createPiece("qa5")
    println(king)
    println(queen)

}
