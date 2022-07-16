#  pygame demo 9 - 3-button test with callbacks

# 1 - Import packages
import pygame
from pygame.locals import *
from simple_button import *
from simple_text import *
import sys

# 2 - Define constants
GRAY = (200, 200, 200)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30

# Define a function to be used as a "callback"
def myCallBackFunction():
    print("User pressed Button B, called myCallBackFunction")


# Define a class with a method to be used as a "callback"
class CallBackTest:
    def __init__(self):
        pass

    def myMethod(self):
        print("User pressed Button C, called myMethod of the CallBackTest object")


# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds, etc.

# 5 - Initialize variables

oCallBackTest = CallBackTest()
# Create instances of SimpleButton
# No call back
oButtonA = SimpleButton(
    window, (25, 30), "images/buttonAUp.png", "images/buttonADown.png"
)
# Specifying a function to call back
oButtonB = SimpleButton(
    window,
    (150, 30),
    "images/buttonBUp.png",
    "images/buttonBDown.png",
    callBack=myCallBackFunction,
)
# Specifying method to call back
oButtonC = SimpleButton(
    window,
    (275, 30),
    "images/buttonCUp.png",
    "images/buttonCDown.png",
    callBack=oCallBackTest.myMethod,
)
counter = 0
# text
oFrameCountLabel = SimpleText(
    window, (60, 20), "Program has run through this many loops: ", WHITE
)
oFrameCountDisplay = SimpleText(window, (500, 20), "", WHITE)
oRestartButton = SimpleButton(
    window, (280, 60), "images/restartUp.png", "images/restartDown.png"
)
frameCounter = 0

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oRestartButton.handleEvent(event):
            frameCounter = 0  # clicked button, reset counter

        # Pass the event to the button, see if has been clicked on
        if oButtonA.handleEvent(event):
            print("User pressed button A, handled in the main loop")

        # oButtonB and oButtonC have callbacks,
        # no need to check result of these calls
        oButtonB.handleEvent(event)

        oButtonC.handleEvent(event)

    # 8 - Do any "per frame" actions
    counter = counter + 1
    oFrameCountDisplay.setValue(str(frameCounter))

    frameCounter = frameCounter + 1  # increment each frame
    oFrameCountDisplay.setValue(str(frameCounter))

    # 9 - Clear the window
    window.fill(GRAY)

    # 10 - Draw all window elements
    oButtonA.draw()
    oButtonB.draw()
    oButtonC.draw()
    oFrameCountLabel.draw()
    oFrameCountDisplay.draw()
    oRestartButton.draw()
    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
