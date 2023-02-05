package patterns

fun abstractFactory(){

    val server1 = ServerFactory.server(listOf("port: 8080", "environment: production"))
    println(server1)
    // ServerConfigurationImpl(properties=[IntProperty(name=port, value=8080), StringProperty(name=environment, value=production)])
}
class ServerFactory{
    companion object{
        fun server(propertyStrings:List<String>): ServerConfiguration{
            val parsedProperties = mutableListOf<Property>()
            for (p in propertyStrings) {
                parsedProperties += property(p)
            }

            return ServerConfigurationImpl(parsedProperties)
        }

        fun property(prop:String):Property{
            val (name, value) = prop.split(":")

            return when (name) {
                "port" -> IntProperty(name, value.trim().toInt())
                "environment" -> StringProperty(name, value.trim())
                else -> throw RuntimeException("Unknown property: $name")
            }
        }
    }
}

// Server property interface:
interface Property{
    val name:String
    val value: Any
}
// Server configuration interface:
interface ServerConfiguration{
    val properties: List<Property>
}

// Server implementation:
data class ServerConfigurationImpl(
    override val properties:List<Property>
): ServerConfiguration

// String property to be given to a server:
data class StringProperty(
    override val name:String,
    override val value: String
):Property

// Int property to be given to a server:
data class IntProperty(
    override val name:String,
    override val value:Int
): Property