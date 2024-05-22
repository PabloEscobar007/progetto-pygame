import pygame

class Palla():
   
    def __init__(self, screen, pos, size, color):
        self.screen = screen
        self.image = pygame.Surface(size)
        # disegno un cerchio nella superficie
        pygame.draw.circle(self.image, color, [size[0]/2, size[1]/2], size[0]/2)

        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        
        self.velocity = 2
        
    def muovi(self):
        # spostamento normale
        self.rect.x += self.velocity
        self.rect.y += self.velocity

        # collisione bordo a sinistra
        if self.rect.x <= 0:
            self.velocity = -self.velocity
        # collisione bordo a destra
        if self.rect.right >= self.screen.get_width():
            self.velocity = -self.velocity
        # collisione bordo sopra
        if self.rect.y < 0:
            self.velocity = -self.velocity
        # collisione bordo sotto
        if self.rect.bottom > self.screen.get_height():
            self.velocity = -self.velocity
          
        # collisione con le palline
        # if self.rect.colliderect(self screen.paddles[0]) or self.rect.colliderect(self screen.paddles[1]):
        #     self.velocity[0] = -self.velocity[0]
        #     self.velocity[1] = randint(-8,8)

    def draw(self):
        self.screen.blit(self.image, self.rect)