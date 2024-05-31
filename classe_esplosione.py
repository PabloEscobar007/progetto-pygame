#classe che serve per l'esplosione delle palline quando vengono colpite dalla palla princ
import pygame
import os

EXPLOSION_SPEED = 1

espl = pygame.image.load("immagini\\animazioni_esplosione1.png")
nespx = 5
nespy = 5

class Esplosione:
    def __init__(self, x, y, nscala):
        self.parts = []
        self.img = None
        self.img = espl
        rettangolo = self.img.get_rect()
        self.rect = pygame.Rect(rettangolo.x, rettangolo.y, rettangolo.width//nespx, rettangolo.height//nespy)
        for i in range(nespy):
            for j in range(nespx):
                startx = j * self.rect.width
                starty = i * self.rect.height
                img_part = self.img.subsurface((startx, starty, self.rect.width, self.rect.height))
                img_part = pygame.transform.scale(img_part, (self.rect.width/nscala, self.rect.height/nscala))
                self.parts.append(img_part)
       
        self.index = 0
        self.punto = pygame.Vector2(x - self.rect.width/nscala/2, y-self.rect.height/nscala/2)
        self.conta = 0
        self.fine = False

    def draw(self, screen):
        if self.fine == False:
            screen.blit(self.parts[self.index], (self.punto.x, self.punto.y))
            self.conta += 1
            if self.conta >= EXPLOSION_SPEED and self.index < len(self.parts) - 1:
                self.conta = 0
                self.index += 1

            if self.index >= len(self.parts) - 1 and self.conta >= EXPLOSION_SPEED:
                self.fine = True