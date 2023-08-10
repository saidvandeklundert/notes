"""
python .\ze_bouncing_heads.py
"""

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
from me import Papa, Jan, Henk

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 960
FRAMES_PER_SECOND = 40
N_BALLS = 2

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sounds, etc.

# 5 - Initialize variables
me_list = []
for _ in range(0, N_BALLS):
    # Each time through the loop, create a Ball object
    papa = Papa(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    jan = Jan(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    henk = Henk(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    me_list.append(papa)
    me_list.append(jan)
    me_list.append(henk)
# 6 - Loop forever
while True:
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Do any "per frame" actions
    for me in me_list:
        me.update()  # tell each Ball to update itself

    # 9 - Clear the window before drawing it again
    window.fill(BLACK)

    # 10 - Draw the window elements
    for me in me_list:
        me.draw()  # tell each Ball to draw itself

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
