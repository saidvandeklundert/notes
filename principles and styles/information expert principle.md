## Information expert principle:

How data is passed around in the application is often a big part of how a program works. One trademark of applications where data is not handled properly is when function signatures demand a plethora of input coming from different places.

The information expert principle (part of the GRASP principles) is about putting behavior as close as possible to the data it needs. This reduces the amount of data that you have to pass around in the application.