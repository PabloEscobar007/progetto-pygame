import pygame, sys
from pygame.locals import *
import math
import random
from classe_palline import *
from classe_palla import *
from classe_tavolo import *
from classe_bottone import *
from classe_esplosione import *

pygame.init()

# settaggi base finestra, clock e colori
lunghezza_schermo =  700
altezza_schermo = 750
window_size = (lunghezza_schermo, altezza_schermo)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('peggle 2.0')
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
palla_principale = pygame.image.load('immagini/palla_princ.png')
sfondo = pygame.transform.scale((pygame.image.load("immagini/sfondo.jpg")), (lunghezza_schermo, altezza_schermo))

# proporziono il cannone in base allo schermo
cannone_proporzionato = pygame.transform.scale_by(cannone_immagine, 0.5)

# informazioni su dove voglio posizionare il mio cannone
cannone_x = lunghezza_schermo/2
cannone_y = altezza_schermo - 50

# inserisco le misure nelle quali le palle comparirano e creo le liste che mi serviranno in seguito per stampare la tipoliga di palla e la pos
tavolo_h = 75
tavolo_altezza = altezza_schermo - tavolo_h
palle_immagini = [palla_blu, palla_verde, palla_rossa, palla_gialla]
raggio = 15
x_min = raggio + 5
x_max = lunghezza_schermo - raggio - 5
y_min = raggio + 90
y_max = altezza_schermo // 2
numero_palla = 6
punti = 0

# creo il tavolo di gioco
tavolo = Tavolo(
    screen,
    [0, tavolo_h],
    [lunghezza_schermo, tavolo_altezza],
    5,
    white
)

# creazione bottone restart
bottone_restart_width = 200
bottone_restart = Bottone(screen,
                        [500, 30], # pos
                        [bottone_restart_width , 40], # size
                        "Reset"
)

#creo palline dando la distanza tra loro e dallo schermo
def distanza(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(0.5)

palline = []
for _ in range(30):
    ok = False
    while not ok:
        x = randint(x_min, x_max)
        y = randint(y_min, y_max)
        ok = True
        for pallina in palline:
            if distanza(pallina.rect.center, (x,y)) < 2*raggio:
                ok = False
    immagine = random.choice(palle_immagini)
    palline.append(Palline(screen, immagine, raggio, x, y))

#creo la palla principale
palla = Palla(screen, palla_principale, 10, cannone_x, cannone_y)

# carattere e grandezza delle varie cose che vogliamo scrivere
font = pygame.font.SysFont('comicsans', 50)
font_2 = pygame.font.SysFont('comicsans', 20)

# schermata iniziale (titolo)
def draw_text(text, title, consiglio, consiglio2):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center = (lunghezza_schermo/2, altezza_schermo/2))

    consiglio_surface = font_2.render(consiglio, True, (255, 255, 255))
    consiglio_rect = consiglio_surface.get_rect(center = (lunghezza_schermo/2, altezza_schermo/2 + 50))

    consiglio2_surface = font_2.render(consiglio2, True, (255, 255, 255))
    consiglio2_rect = consiglio2_surface.get_rect(center = (lunghezza_schermo/2, altezza_schermo/2 + 70))

    title_surface = font.render(title, True, (255, 255, 255))
    title_rect = title_surface.get_rect(center = (lunghezza_schermo/2, altezza_schermo/4))
    screen.blit(sfondo, (0,0))
    screen.blit(text_surface, text_rect)
    screen.blit(title_surface, title_rect)
    screen.blit(consiglio_surface, consiglio_rect)
    screen.blit(consiglio2_surface, consiglio2_rect)
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

# carico audio 
intro = pygame.mixer.Sound("musiche e effetti sonori/canzone_intro.mp3")
gioco = pygame.mixer.Sound("musiche e effetti sonori/canzone_gioco.mp3")

# faccio partire l'audio intro finchè non starto e ne faccio partire un'altro
pygame.mixer.Sound.play(intro, -1)
draw_text("Premere INVIO per iniziare", "PEGGLE 2.0", "CONSIGLIO: posizionare il cursore per mirare più vicino", "al cannone possibile per una precisione migliore")
wait_for_input()
pygame.mixer.Sound.stop(intro)
pygame.mixer.Sound.play(gioco, -1)
sfondo = pygame.transform.scale(sfondo, (lunghezza_schermo-10, altezza_schermo))

minuti = 0
secondi = 0
tick = 0
movimento_palla = False
cannone_giu = False
esplosioni = []
# ciclo fondamentale
while True:
    
    # inputs
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN and numero_palla > 0 and cannone_giu == False and not bottone_restart.rect.collidepoint(pos):
            if movimento_palla == False:
                numero_palla -= 1
            movimento_palla = True
        
        if event.type == MOUSEBUTTONUP and event.button == 1:
            pos = pygame.mouse.get_pos()

            if bottone_restart.rect.collidepoint(pos):
                tavolo = Tavolo(
                    screen,
                    [0, tavolo_h],
                    [lunghezza_schermo, tavolo_altezza],
                    5,
                    white
                )
                palline = []
                for _ in range(30):
                    ok = False
                    while not ok:
                        x = randint(x_min, x_max)
                        y = randint(y_min, y_max)
                        ok = True
                        for pallina in palline:
                            if distanza(pallina.rect.center, (x,y)) < 2*raggio:
                                ok = False
                    immagine = random.choice(palle_immagini)
                    palline.append(Palline(screen, immagine, raggio, x, y))
                palla = Palla(screen, palla_principale, 10, cannone_x, cannone_y)
                numero_palla = 6
                

    keys = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()
    if keys[0] and bottone_restart.rect.collidepoint(pos): # 0: tasto sinistro, 1: rotella, 2: tasto destro
        bottone_restart.chiaro()
        secondi = 0
        minuti = 0
        tick = 0
        pygame.mixer.Sound.stop(gioco)
        pygame.mixer.Sound.play(gioco, -1)
    else:
        bottone_restart.base()

    screen.fill(black)

    pos = pygame.mouse.get_pos()
    # calcolare l'angolo del cannone
    x_distanza = pos[0] - cannone_x
    y_distanza = -(pos[1] - cannone_y)
    angle = math.degrees(math.atan2(y_distanza, x_distanza))
    
    # calcolare le distanze di dove parte la pallina 
    if x_distanza == 0 and y_distanza > 0: 
        palla.velocity[0] = 0
        palla.velocity[1] = -2
        cannone_giu = False
    elif y_distanza > 0:
        m = y_distanza / x_distanza
        if movimento_palla == False:
            palla.velocity[0] = 2 / m
            palla.velocity[1] = -2
            cannone_giu = False
    elif y_distanza <= 0:
        movimento_palla = False
        cannone_giu = True

    # faccio muiovere la palla principale nello schermo
    if movimento_palla == True:
        palla.muovi(palline)

    # cronometro
    tick += 1

    if tick == 60:
        secondi += 1
        tick = 0
        font = pygame.font.SysFont(None, 50)
        if secondi < 10:
            tempo = font.render(f"0{minuti}:0{secondi}", True, (255, 255, 255))
            screen.blit(tempo, (50, 35))
        elif secondi >= 10:
            tempo = font.render(f"0{minuti}:{secondi}", True, (255, 255, 255))
            screen.blit(tempo, (50, 35))
        if secondi == 60:
            minuti += 1
            secondi = 0
    else:
        font = pygame.font.SysFont(None, 50)
        if secondi < 10:
            tempo = font.render(f"0{minuti}:0{secondi}", True, (255, 255, 255))
            screen.blit(tempo, (50, 35))
        elif secondi >= 10:
            tempo = font.render(f"0{minuti}:{secondi}", True, (255, 255, 255))
            screen.blit(tempo, (50, 35))

    # faccio ruotare il cannone
    cannone_finale = pygame.transform.rotate(cannone_proporzionato, angle - 90)
    cannone_rect = cannone_finale.get_rect(center = (cannone_x, cannone_y))

    # collisione con le palline + animazione esplosioni
    for i in range(len(palline) - 1):
        if palla.rect.colliderect(palline[i].rect):
            esplosione = Esplosione(palline[i].x, palline[i].y)
            esplosioni.append(esplosione)
            palline.pop(i)

    
    # stampo cannone, tavolo, palla e bottone restart, animazione, sfondo
    tavolo.draw()
    screen.blit(sfondo, (5, tavolo_h+5))
    palla.draw()
    screen.blit(cannone_finale, cannone_rect)
    bottone_restart.draw()
    for esp in esplosioni:
        esp.draw(screen)

    # stampo le palline
    for i in range(len(palline) - 1):
        palline[i].draw()


    # scrivere vittoria nel caso rompi tutte le palline
    if len(palline) == 0:
        win = font.render("You won!", True, (0, 255, 0))
        screen.blit(win, (lunghezza_schermo / 2 - 100, altezza_schermo / 2))

    # scrivere game over nel caso perdi e stampare di nuovo la palla quando cade giù
    if palla.rect.y > altezza_schermo:
        if numero_palla > 0:
            palla = Palla(screen, palla_principale, 10, cannone_x, cannone_y)
        elif len(palline) > 0:
            game_over = font.render("Game over!", True, (255, 0, 0))
            screen.blit(game_over, (lunghezza_schermo / 2 - 100, altezza_schermo / 2))
        movimento_palla = False
    
    # stampare il numero di palle rimanenti 
    font2 = pygame.font.SysFont(None, 35)
    palle_rimaste = font2.render(f"palle rimaste: {numero_palla}", True, (255, 255, 255))
    screen.blit(palle_rimaste, (250, 40))

    pygame.display.update()
    clock.tick(fps)