# Chapter13.py
# Justin Singer
# 4/4/16



"""
Use sprites to collect blocks.
 
Created by Justin Singer """

import pygame
import random

from goodblock_library import GoodBlock

from block_library import Block

from bad_block_library import BadBlock
 
# Define some colors and variables
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (50, 205, 50)

x =  350
y = 100

x_coord = 10
y_coord = 10

x_speed = 0
y_speed = 0

score = 0

 
class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(BLACK)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
 
    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        while self.rect.x < 0:
            self.rect.x += 1
            bump.play()
        while self.rect.x > 685:
            self.rect.x -= 1
            bump.play()
        while self.rect.y < 0:
            self.rect.y += 1
            bump.play()
        while self.rect.y > 385:
            self.rect.y -= 1
            bump.play()



 
# Initialize Pygame
pygame.init()

# Collision sounds
bell = pygame.mixer.Sound('bell_ding1.wav')
blip = pygame.mixer.Sound('Blip_Select.ogg')
bump = pygame.mixer.Sound('bump.ogg')
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
good_block_list = pygame.sprite.Group()

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
bad_block_list = pygame.sprite.Group()
 
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
for i in range(50):
    # This represents a good block
    good_block = GoodBlock(screen, GREEN, 20, 15)
    

    # Set a random location for the blocks
    good_block.rect.x = random.randrange(screen_width)
    good_block.rect.y = random.randrange(screen_height)
    
# Add the good block to the list of objects
    good_block_list.add(good_block)
    all_sprites_list.add(good_block)

for i in range(50):
    # This represents a bad block
    bad_block = BadBlock(RED, 20, 15)
 
    
    
    bad_block.rect.x = random.randrange(screen_width)
    bad_block.rect.y = random.randrange(screen_height)
 
    

    # Add the bad block to the list of objects
    bad_block_list.add(bad_block)
    all_sprites_list.add(bad_block)
 
# Create a BLUE player block
player = Player(50, 50)
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()



 
# -------- Main Program Loop -----------
while not done:

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)
 

       

    # Clear the screen
    screen.fill(WHITE)


    #Score board code goes here
    scoreText = "Score: " +str(score)
    
    font = pygame.font.Font(None, 25)

    text = font.render(scoreText, True, BLACK)

    screen.blit(text, [100,100] )


    


    # This calls update on all the sprites
    all_sprites_list.update()
    good_block_list.update()
    bad_block_list.update()
    
    # See if the player block has collided with anything.
    good_blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)
    bad_blocks_hit_list = pygame.sprite.spritecollide(player, bad_block_list, True)
 
    # Check the list of collisions.
    for good_block in good_blocks_hit_list:
        score += 1
        bell.play()
        print(score)
        
    for bad_block in bad_blocks_hit_list:
        score -= 1
        blip.play()
        print(score)
 
 
    # Draw all the spites
    all_sprites_list.draw(screen)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()
