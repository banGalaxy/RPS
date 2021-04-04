import pygame
from game import screen_height, screen_width

class Option(pygame.sprite.Sprite, ):
        def __init__(self, name):
            pygame.sprite.Sprite.__init__(self)
            self.option = name
            self.xsize = int(screen_width / 5)
            self.ysize = int(screen_height / 5)

        def display(self):
            self.image = pygame.image.load(self.option + ".png")
            self.image = pygame.transform.scale(self.image,(self.xsize, self.ysize))
            if self.option == "rock" : 
                screen.blit(self.image, ((screen_width / 10) , (screen_height - screen_height / 10) - self.ysize))
            elif self.option == "paper" : 
                screen.blit(self.image, ((screen_width/2) - self.xsize/2 , (screen_height - screen_height / 10) - self.ysize))
            elif self.option == "scissors" : 
                screen.blit(self.image, ((screen_width - screen_width / 10) - self.xsize  , (screen_height - screen_height / 10) - self.ysize))