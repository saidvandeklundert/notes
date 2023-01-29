//  ./gradlew run  
import com.fasterxml.jackson.module.kotlin.jacksonObjectMapper
import com.fasterxml.jackson.module.kotlin.readValue

import java.io.File

import serialization.*
import basics.*


fun main(args: Array<String>) {

    // serialize examples
    serialization.serializeSomethingUsingJackson()
    serialization.anotherThing()
    basics.talkAboutNull()
    basics.conversions()

}