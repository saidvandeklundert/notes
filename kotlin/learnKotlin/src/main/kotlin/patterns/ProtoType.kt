package patterns

fun protoTypeExamples() {
    val originalUser = User("admin1", Role.ADMIN, setOf("READ", "WRITE", "DELETE"))
    allUsers += originalUser
    val originalUser2 = User("admin12", Role.SUPER_ADMIN, setOf("READ", "WRITE", "DELETE"))

    createUser("admin2", Role.ADMIN)
    createUser("Said", Role.SUPER_ADMIN)
    createUser("Jan", Role.REGULAR_USER)
    println(allUsers)
}

// the users database we write to
private val allUsers = mutableListOf<User>()

// enumeration of possible roles
enum class Role {
    ADMIN,
    SUPER_ADMIN,
    REGULAR_USER
}

// Dataclass representing a user:
data class User(
    val name: String,
    val role: Role,
    val permissions: Set<String>,
) {
    fun hasPermission(permission: String) = permission in permissions
}


// function that creates a user in the 'database' defined as 'private val allUsers'
fun createUser(_name: String, role: Role) {
    for (u in allUsers) {
        if (u.role == role) {
            allUsers += u.copy(name = _name)
            return
        } else{
            allUsers += u.copy(name = _name)
            return
        }
    }
    // Handle case that no other user with such a role exists
}