#import and initialize pygame
import pygame
from pygame.locals import *
from Options import *


pygame.init()
#game variables
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])

rock = Option("rock")
paper = Option("paper")
scissors = Option("scissors")
outcome_list = [rock, paper, scissors]




def summoning():
    
    for outcome in outcome_list:
        outcome.display()
    
#loading images

            

            



#setting up the start
running = True
while running:
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #set up window


    screen.fill((30,30,30))
    #creating the options
    
    summoning()

    pygame.display.update()
    
        

    
    
    