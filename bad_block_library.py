# chapter 14.py
# Justin Singer
# 4/6/16

import pygame
import random

screen_width = 700
screen_height = 400

RED = (255,   0,   0)

class BadBlock(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([20, 15])
        self.image.fill(RED)
 
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

    def update(self):
    #move blocks down the screen
        self.rect.y += 1
        if self.rect.y > screen_height:
            self.rect.y = random.randrange(-100, -10)
            self.rect.x = random.randrange(0, screen_width)

    def reset_pos(self):
    #reset position to the top of the screen at a random x location.
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, screen_width)

    def update(self):
        self.rect.y += 1
        if self.rect.y > 410:
            self.reset_pos()

        
        
