import pygame
from random import randint

class Palline:
    def __init__(self, screen, image, raggio, x, y) -> None:
        self.screen = screen
        self.image = image
        self.image = pygame.transform.scale(self.image, (raggio*2, raggio*2))
        # x_min = 50
        # x_max = 600
        # y_min = 50
        # y_max = 400

        # self.x = randint(x_min, x_max)
        # self.y = randint(y_min, y_max)
        
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center = (x,y))
        
        
    def draw(self): 
        self.screen.blit(self.image, self.rect)