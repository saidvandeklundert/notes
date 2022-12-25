import com.fasterxml.jackson.module.kotlin.jacksonObjectMapper
import com.fasterxml.jackson.module.kotlin.readValue

import java.io.File

data class User (
    val id: Int,
    val username: String,
    val password: String,
    val fullName: String
)
// Registering the Kotlin module with the ObjectMpper instance
val mapper = jacksonObjectMapper()

// JSON String
val jsonString = """{
"id":101,
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


fun main(args: Array<String>) {
    println(userFromJson)
    println(userJson)
    userList.add(User(102, "jsmith", "P@ss", "John Smith"))
    userList.add(User(301, "ai3000","123rT", "Ian relWofer"))
    println(userList)



}