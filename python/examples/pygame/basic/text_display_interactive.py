#  Demo of pygwidgets capabilities
#
#  4/17  Developed by Irv Kalb

# 1 - Import libraries
import os
import sys

# The next line is here just in case you are running from the command line
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import pygame
from pygame.locals import *
import pygwidgets


# 2 - Define constants
BLACK = (0, 0, 0)
BLACKISH = (10, 10, 10)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
FRAMES_PER_SECOND = 30


# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()  # create a clock object


# 4 - Load assets: image(s), sounds,  etc.
oBackgroundImage = pygwidgets.Image(window, (0, 0), "images/background.jpg")

oInputTextA = pygwidgets.InputText(
    window,
    (20, 100),
    "Default input text",
    textColor=WHITE,
    backgroundColor=BLACK,
    fontSize=24,
    width=250,
)

oInputTextB = pygwidgets.InputText(
    window, (20, 200), initialFocus=True, textColor=(0, 0, 255), fontSize=28
)  # add: , mask='*' for passwords


oDisplayTextA = pygwidgets.DisplayText(
    window,
    (20, 300),
    "Here is some display text",
    fontSize=24,
    textColor=WHITE,
    justified="center",
)

oDisplayTextB = pygwidgets.DisplayText(
    window,
    (20, 400),
    "Here is some display text",
    fontSize=24,
    textColor=BLACK,
    backgroundColor=WHITE,
)


oCheckBoxB = pygwidgets.TextCheckBox(window, (450, 295), "Allow Radio Buttons")


oPythonIcon = pygwidgets.Image(window, (15, 500), "images/pythonIcon.png")


# 5 - Initialize variables
screen_display_text = "some text"

# 6 - Loop forever
while True:

    # 7 - Check for and handle events

    for event in pygame.event.get():
        # check if the event is the close button
        if event.type == pygame.QUIT:
            # if it is quit, the program
            pygame.quit()
            sys.exit()

        if oInputTextA.handleEvent(event):  # pressed Return or Enter
            theText = oInputTextA.getValue()
            print("The text of oInputTextA is: " + theText)
            screen_display_text = theText

        if oInputTextB.handleEvent(event):  # pressed Return or Enter
            theText = oInputTextB.getValue()
            print("The text of oInputTextB is: " + theText)
            screen_display_text = theText

    # 8  Do any "per frame" actions

    oDisplayTextB.setValue(screen_display_text)

    # 9 - Clear the window
    oBackgroundImage.draw()

    # 10 - Draw all window elements

    oInputTextA.draw()
    oInputTextB.draw()
    oDisplayTextA.draw()
    oDisplayTextB.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
