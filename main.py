import pygame, sys
from pygame.locals import *
import math

pygame.init()

# settaggi base finestra, clock e colori
lunghezza_schermo = 700
altezza_schermo = 750
window_size = (lunghezza_schermo, altezza_schermo)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('peggle')
clock = pygame.time.Clock()  
fps = 60
black = (0, 0, 0)
white = (255, 255, 255)

# carico le immagini
cannone_immagine = pygame.image.load('immagini/cannone.png')
palla_blu = pygame.image.load('immagini/palla_blu.png')
palla_verde = pygame.image.load('immagini/palla_verde.png')
palla_rossa = pygame.image.load('immagini/palla_rossa.png')
palla_gialla = pygame.image.load('immagini/palla_gialla.png')

# proporziono il cannone in base allo schermo
cannone_proporzionato = pygame.transform.scale_by(cannone_immagine, 0.5)

# informazioni su dove voglio posizionare il mio cannone
x = lunghezza_schermo/2
y = altezza_schermo - 50


# carattere e grandezza delle varie cose che vogliamo scrivere
font = pygame.font.SysFont('comicsans', 50)

# schermata iniziale (titolo)
def draw_text(text, title):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center = (lunghezza_schermo/2, altezza_schermo/2))
    title_surface = font.render(title, True, (255, 255, 255))
    title_rect = title_surface.get_rect(center = (lunghezza_schermo/2, altezza_schermo/4))
    screen.fill((0, 0, 0))
    screen.blit(text_surface, text_rect)
    screen.blit(title_surface, title_rect)
    pygame.display.flip()

# funzione per far partire il gioco 
def wait_for_input():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False

draw_text("Premi invio per cominciare", "PEGGLE")
wait_for_input()

# ciclo fondamentale
while True:
    
    # inputs
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(black)
    
    pos = pygame.mouse.get_pos()
    # calcolare l'angolo del cannone
    x_distanza = pos[0] - x
    y_distanza = -(pos[1] - y)
    angle = math.degrees(math.atan2(y_distanza, x_distanza))

    # faccio ruotare il cannone
    cannone_finale = pygame.transform.rotate(cannone_proporzionato, angle - 90)
    cannone_rect = cannone_finale.get_rect(center = (x, y))
    
    # stampo il cannone
    screen.blit(cannone_finale, cannone_rect)

    pygame.display.update()
    clock.tick(fps)

