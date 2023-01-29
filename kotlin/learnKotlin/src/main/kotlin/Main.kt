//  ./gradlew run  
import com.fasterxml.jackson.module.kotlin.jacksonObjectMapper
import com.fasterxml.jackson.module.kotlin.readValue

import java.io.File
import controlflow.*
import serialization.*
import basics.*
import dataclasses.*
import types.*
import stringinterpolation.*
import kotlinclasses.*
import patterns.*
fun main(args: Array<String>) {

    // serialize examples
    serialization.serializeSomethingUsingJackson()
    serialization.anotherThing()
    basics.talkAboutNull()
    basics.conversions()
    dataclasses.makeAndPrintPersons()
    types.someKotlinTypes()

    stringinterpolation.exampleInterpolations()

    controlflow.controlFlowExamples()
    controlflow.controlFlowExamples()
    kotlinclasses.examples()
    patterns.SingletonLogger.log("logging something important")
    var theLogger = patterns.SingletonLogger
    theLogger.log("same logger")
}