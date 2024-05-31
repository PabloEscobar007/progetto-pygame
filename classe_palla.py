import pygame
from random import randint
tavolo_h = 75
spessore_bordo = 5

class Palla():
   
    def __init__(self, screen, image, raggio, x, y):
        self.screen = screen
        self.image = image
        self.image = pygame.transform.scale(self.image, (raggio*2, raggio*2))

        # disegno un cerchio nella superficie
        self.rect = self.image.get_rect(center = (x,y))
        
        self.velocity = [randint(2,4),randint(-4,-2)]

        
    def muovi(self):
        # spostamento normale
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        # collisione bordo a sinistra
        if self.rect.x <= 0 + spessore_bordo:
            self.velocity[0] = -self.velocity[0]
        # collisione bordo a destra
        if self.rect.right >= self.screen.get_width() - spessore_bordo:
            self.velocity[0] = -self.velocity[0]
        # collisione bordo sopra
        if self.rect.y < tavolo_h + spessore_bordo:
            self.velocity[1] = -self.velocity[1]
        # if self.rect.bottom > self.screen.get_height():
        #     self.screen.blit(self.image, self.rect)
          
        # collisione con le palline
        # if self.rect.colliderect(self.palline):
        #     self.velocity[0] = -self.velocity[0]
        #     self.velocity[1] = -self.velocity[1]

    def draw(self):
        self.screen.blit(self.image, self.rect)