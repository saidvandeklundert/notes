//  ./gradlew run  
import com.fasterxml.jackson.module.kotlin.jacksonObjectMapper
import com.fasterxml.jackson.module.kotlin.readValue

import java.io.File
import controlflow.*
import serialization.*
import basics.*
import dataclasses.*
import basics.conversions
import basics.talkAboutNull
import types.*
import stringinterpolation.*
import kotlinclasses.*
import patterns.*
fun main(args: Array<String>) {

    // serialize examples
    serialization.serializeSomethingUsingJackson()
    serialization.anotherThing()
    talkAboutNull()
    conversions()
    dataclasses.makeAndPrintPersons()
    types.someKotlinTypes()

    stringinterpolation.exampleInterpolations()

    controlflow.controlFlowExamples()
    controlflow.controlFlowExamples()
    kotlinclasses.examples()
    patterns.SingletonLogger.log("logging something important")
    var theLogger = patterns.SingletonLogger
    theLogger.log("same logger")
    patterns.factoryMethodExample()
    patterns.staticFactoryMethod()
    patterns.abstractFactory()
    patterns.builderExample()
    patterns.protoTypeExamples()
    patterns.StrategySimple()
    basics.interfaces_main()
    interfaces.restaurantExample()
    interfaces.mainAnimals()
    interfaces.mainCar()
    classes.classesCompanion()
    interfaces.coffeeExample()
    classes.main_constructor_examples()
    classes.mainGettersAndSetters()
    classes.mainThis()
}