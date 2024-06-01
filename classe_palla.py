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
        
        self.velocity = [randint(-4, 4),randint(-4, -2)]

        
    def muovi(self, palline):
        # spostamento normale
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        # collisione bordo a sinistra
        if self.rect.x <= 0 + spessore_bordo:
            self.velocity[0] = -self.velocity[0]
            if self.velocity[1] == 0:
                self.velocity[1] = randint(-1, 1)
        # collisione bordo a destra
        if self.rect.right >= self.screen.get_width() - spessore_bordo:
            self.velocity[0] = -self.velocity[0]
            if self.velocity[1] == 0:
                self.velocity[1] = randint(-1, 1)
        # collisione bordo sopra
        if self.rect.y < tavolo_h + spessore_bordo:
            self.velocity[1] = -self.velocity[1]
          
        # collisione con le palline
        for i in range(len(palline) - 1):
            if self.rect.colliderect(palline[i].rect):
                self.velocity = [randint(-4 ,4),randint(-4, 4)]
            while self.velocity == [0, 0]:
                self.velocity = [randint(-4 ,4),randint(-4, 4)]



    def draw(self):
        self.screen.blit(self.image, self.rect)