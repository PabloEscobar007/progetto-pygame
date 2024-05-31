import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Bottone:
    def __init__(self, screen, pos, size, testo) -> None:
        self.screen = screen
        self.pos = pos
        self.size = size
        self.testo = testo

        self.colore_base = (200,200,200)
        self.colore_chiaro = (255,255,255)
        self.colore = self.colore_base

        self.image = pygame.Surface(size)
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

        # self.font = pygame.font.Font(None, size[1])
        self.font = pygame.font.Font(None, 50)
    
    def draw(self):
        self.image.fill(BLACK)

        self.text = self.font.render(self.testo, 1, self.colore)

        # self.image.fill((100,100,100))
        pygame.draw.rect(self.image, (self.colore), (0, 0, self.rect.width, self.rect.height), 5)
        x = self.rect.width / 2 - self.text.get_width() / 2
        y = self.rect.height / 2 - self.text.get_height() / 2
        self.image.blit(self.text, (x, y))
        # self.image.blit(self.text, (10, 10))

        # self.image.fill((100,100,100))
        self.screen.blit(self.image, self.rect)

    def chiaro(self):
        self.colore = self.colore_chiaro

    def base(self):
        self.colore = self.colore_base

    def toggle(self):
        if self.colore == self.colore_base:
            self.colore = self.colore_chiaro
        else:
            self.colore = self.colore_base

    def reset(self):
        pass