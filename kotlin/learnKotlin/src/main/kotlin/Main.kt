//  ./gradlew run  
//import com.fasterxml.jackson.module.kotlin.jacksonObjectMapper
//import com.fasterxml.jackson.module.kotlin.readValue

///import java.io.File
import controlflow.*
import serialization.*
import basics.*
import dataclasses.*
import basics.conversions
import basics.talkAboutNull
import classes.*
import types.*
import stringinterpolation.*
import kotlinclasses.*
import patterns.*
import io.*
import datastructures.*
import collections.*
import generics.*
import interfaces.*
import functional.*
fun main() {

    // serialize examples
    serializeSomethingUsingJackson()
    anotherThing()
    talkAboutNull()
    conversions()
    makeAndPrintPersons()
    someKotlinTypes()

    exampleInterpolations()

    controlFlowExamples()
    controlFlowExamples()
    examples()
    SingletonLogger.log("logging something important")
    val theLogger = SingletonLogger
    theLogger.log("same logger")
    factoryMethodExample()
    staticFactoryMethod()
    abstractFactory()
    builderExample()
    protoTypeExamples()
    StrategySimple()
    interfaces_main()
    restaurantExample()
    mainAnimals()
    mainCar()
    classesCompanion()
    coffeeExample()
    main_constructor_examples()
    mainGettersAndSetters()
    mainThis()
    runForm()
    classesWithValidators()
    filesAndStuff()
    arrayListOperations()
    stackExample()
    functionExamples()
    mainFunctional()

}

//  ./gradlew run