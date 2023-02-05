package interfaces

interface Restaurant{
    fun provideFood():List<String>
}


class Chinese(): Restaurant {

    override fun provideFood():List<String> {
        return listOf("Babi Pangang", "Nasi", "Koe Lo Yuk")
    }

}

class Italian(): Restaurant {

    override fun provideFood():List<String> {
        return listOf("Pizza", "Pasta")
    }

}

class Indian(): Restaurant {

    override fun provideFood():List<String> {
        return listOf("Curry", "Dahl", "Naan")
    }

}

fun visitRestaurant(restaurant: Restaurant){
    val food = restaurant.provideFood()
    for ( plate in food){
        println(plate)
    }
}

fun restaurantExample(){
    val indian = Indian()
    val italian = Italian()
    val chinese = Chinese()
    visitRestaurant(indian)
    visitRestaurant(italian)
    visitRestaurant(chinese)


}