#classe che serve per l'esplosione delle palline quando vengono colpite dalla palla princ
import pygame
import os

EXPLOSION_SPEED = 1

espl = pygame.image.load("immagini\\Explosion Medium.png")

class Esplosione:
    def __init__(self, x, y):
        self.parti = []
        self.immagine_gen = None
        self.immagine_gen = espl
        rettangolo = self.immagine_gen.get_rect()
        self.rect = pygame.Rect(rettangolo.x, rettangolo.y, rettangolo.width//6, rettangolo.height)
        for i in range(6):
            startx = i * self.rect.width
            immagine_gen_part = self.immagine_gen.subsurface((startx, 0, self.rect.width, self.rect.height))
            immagine_gen_part = pygame.transform.scale(immagine_gen_part, (self.rect.width, self.rect.height))
            self.parti.append(immagine_gen_part)
       
        self.indice = 0
        self.punto = pygame.Vector2(x - self.rect.width/2, y-self.rect.height/2)
        self.conta = 0
        self.fine = False

    def draw(self, screen):
        if self.fine == False:
            screen.blit(self.parti[self.indice], (self.punto.x, self.punto.y))
            self.conta += 1
            if self.conta >= EXPLOSION_SPEED and self.indice < len(self.parti) - 1:
                self.conta = 0
                self.indice += 1

            if self.indice >= len(self.parti) - 1 and self.conta >= EXPLOSION_SPEED:
                self.fine = True