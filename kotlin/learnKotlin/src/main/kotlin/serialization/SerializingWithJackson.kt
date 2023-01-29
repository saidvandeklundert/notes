package serialization

import com.fasterxml.jackson.module.kotlin.jacksonObjectMapper
import com.fasterxml.jackson.module.kotlin.readValue

fun serializeSomethingUsingJackson(){
    // Read data from a JSON string





    // Load JSON String using objectmapper:
    data class Person (
        val id: Int,
        val name: String,
        val email: String,
        val age: Int
    )

    val objectmapper = jacksonObjectMapper()

    val jsonPersons = """
    [
        {
        "id":1012,
        "name":"jan",
        "email":"jan@yolo.com",
        "age":7    
        }
    ]
    """

    val personsFromJson: Array<Person> = objectmapper.readValue(jsonPersons)    
    for (item in personsFromJson)
        println(item)    
}


fun anotherThing(){
    data class User (
        val id: Int,
        val username: String,
        val password: String,
        val fullName: String
    )
    // Registering the Kotlin module with the jacksonObjectMapper instance
    val mapper = jacksonObjectMapper()

    // JSON String
    val jsonString = """{
    "id":1012,
    "username":"admin",
    "password":"Admin123",
    "fullName":"Best Admin"
    }"""

    // Read data from a JSON string
    //val jsonFile: String = File("assets/jsonObject.json").readText(Charsets.UTF_8)
    val userFromJson: User = mapper.readValue(jsonString)

    val user = User(102, "test", "pass12", "Test User")

    val userJson = mapper.writeValueAsString(user)

    val userList = mutableListOf<User>()    
        println(userFromJson)
        println(userJson)
        userList.add(User(102, "jsmith", "P@ss", "John Smith"))
        userList.add(User(301, "ai3000","123rT", "Ian relWofer"))
        println(userList)
}