# chapter 14.py
# Justin Singer
# 4/6/16

import pygame
import random

GREEN = (50, 205, 50)


class GoodBlock(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def __init__(self, screen, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([20, 15])
        self.image.fill(GREEN)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += random.randint(-3,3)
        self.rect.y += random.randint(-3,3)
 
    
        

        


