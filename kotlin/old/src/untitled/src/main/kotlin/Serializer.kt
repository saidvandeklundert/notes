import kotlinx.serialization.Serializable
import kotlinx.serialization.json.Json
import kotlinx.serialization.decodeFromString

@Serializable
data class Data(val a: Int, val b: String)

fun main() {
    val obj = Json.decodeFromString<Data>("""{"a":42, "b": "str"}""")
}