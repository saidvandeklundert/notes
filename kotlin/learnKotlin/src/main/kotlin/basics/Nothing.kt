package nothing
/*
    The private constructor means the class cannot be instantiated outside the class.
    Also, it isn’t instantiated inside the class either. 
    
    Therefore, there are no instances of Nothing.
 */
public class Nothing private constructor()


// function that does not return and just throws an exception:
fun doNothing(): Nothing = throw Exception("Nothing")