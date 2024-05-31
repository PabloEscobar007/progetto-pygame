import pygame
black = (0, 0, 0)
white = (255, 255, 255)

class Tavolo:
    def __init__(self, screen, pos, size, bordo_spessore, bordo_colore) -> None:
        self.screen = screen
        self.bordo_colore = bordo_colore
        self.pos = pos
        self.size = size
        self.bordo_spessore = bordo_spessore

        self.palla = None

        self.image = pygame.Surface(
            [size[0] - bordo_spessore*2, size[1] - bordo_spessore*2]
        )
        self.rect = pygame.Rect(
            pos[0] + bordo_spessore, # x
            pos[1] + bordo_spessore, # y
            size[0] - (bordo_spessore * 2), # width
            size[1] - (bordo_spessore * 2)  # height
        )
        print(self.rect)

    def ridisegna_sfondo(self):
        pygame.draw.rect(
            self.screen, 
            self.bordo_colore,
            (self.pos[0], self.pos[1], self.size[0], self.size[1]),
        )
        self.image.fill(black)
        

    def draw(self):
        # ridisegno lo sfondo
        pygame.draw.rect(
            self.screen, 
            self.bordo_colore,
            (self.pos[0], self.pos[1], self.size[0], self.size[1]),
        )
        self.image.fill(black)
        
        # disegno pallina
        if self.palla != None:
            self.palla.draw()

        self.screen.blit(self.image, self.rect)