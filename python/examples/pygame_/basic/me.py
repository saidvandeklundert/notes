import pygame
from pygame.locals import *
import random


class Me:
    def __init__(self, window, windowWidth, windowHeight):
        self.window = window  # remember the window, so we can draw later
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.image = pygame.image.load("images/me.jpg")
        # A rect is made up of [x, y, width, height]
        ballRect = self.image.get_rect()

        self.width = ballRect.width
        self.height = ballRect.height
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height
        start_x = self.maxWidth if self.maxWidth > 0 else 100
        start_y = self.maxHeight if self.maxHeight > 0 else 100
        # Pick a random starting position
        self.x = random.randrange(0, start_x)
        self.y = random.randrange(0, start_y)

        # Choose a random speed between -4 and 4, but not zero
        # in both the x and y directions
        speedsList = [5]
        self.xSpeed = random.choice(speedsList)
        self.ySpeed = random.choice(speedsList)

    def update(self):
        # Check for hitting a wall.  If so, change that direction.
        if (self.x < 0) or (self.x >= self.maxWidth):
            self.xSpeed = -self.xSpeed

        if (self.y < 0) or (self.y >= self.maxHeight):
            self.ySpeed = -self.ySpeed

        # Update the Ball's x and y, using the speed in two directions
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))


class Jan:
    def __init__(self, window, windowWidth, windowHeight):
        self.window = window  # remember the window, so we can draw later
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.image = pygame.image.load("images/jan.jpg")
        # A rect is made up of [x, y, width, height]
        ballRect = self.image.get_rect()

        self.width = ballRect.width
        self.height = ballRect.height
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height
        start_x = self.maxWidth if self.maxWidth > 0 else 100
        start_y = self.maxHeight if self.maxHeight > 0 else 100
        # Pick a random starting position
        self.x = random.randrange(0, start_x)
        self.y = random.randrange(0, start_y)

        # Choose a random speed between -4 and 4, but not zero
        # in both the x and y directions
        speedsList = [50]
        self.xSpeed = random.choice(speedsList)
        self.ySpeed = random.choice(speedsList)

    def update(self):
        # Check for hitting a wall.  If so, change that direction.
        if (self.x < 0) or (self.x >= self.maxWidth):
            self.xSpeed = -self.xSpeed

        if (self.y < 0) or (self.y >= self.maxHeight):
            self.ySpeed = -self.ySpeed

        # Update the Ball's x and y, using the speed in two directions
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))


class Henk:
    def __init__(self, window, windowWidth, windowHeight):
        self.window = window  # remember the window, so we can draw later
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.image = pygame.image.load("images/henk.jpg")
        # A rect is made up of [x, y, width, height]
        ballRect = self.image.get_rect()

        self.width = ballRect.width
        self.height = ballRect.height
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height
        start_x = self.maxWidth if self.maxWidth > 0 else 100
        start_y = self.maxHeight if self.maxHeight > 0 else 100
        # Pick a random starting position
        self.x = random.randrange(0, start_x)
        self.y = random.randrange(0, start_y)

        # Choose a random speed between -4 and 4, but not zero
        # in both the x and y directions
        speedsList = [19]
        self.xSpeed = random.choice(speedsList)
        self.ySpeed = random.choice(speedsList)

    def update(self):
        # Check for hitting a wall.  If so, change that direction.
        if (self.x < 0) or (self.x >= self.maxWidth):
            self.xSpeed = -self.xSpeed

        if (self.y < 0) or (self.y >= self.maxHeight):
            self.ySpeed = -self.ySpeed

        # Update the Ball's x and y, using the speed in two directions
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))
