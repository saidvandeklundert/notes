package excercisms

fun twofer(name: String?=null): String {
    if (name == null)
        return "One for you, one for me."
    else {
        return "One for $name, one for me."
    }

}
