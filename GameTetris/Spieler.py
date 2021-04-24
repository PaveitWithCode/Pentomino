'''
Created on 07.01.2021

@author: metko_kerstin
'''
import pygame
from pygame.locals import *
import random
from pygame._sprite import pygame

#######################################Konstanten - Setting################################
WIDTH = 1000
HEIGHT = 1000
WINDOW_SIZE = (WIDTH, HEIGHT)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 30
TITLE = "Titel"
GESCHWINDIGKEIT = 5
SIZE = 100
IMAGES = {}
FBREITE, FHOEHE = 1920, 1080


class Tetris_teile():
    '''
    classdocs
    Hier werden die Eigenschaften und Verhaltensweisen
    eines Spielers festgelegt.
    '''

    def __init__(self, size, anzahl):
        '''
        Constructor
        Konstruieren Sie Ihre Klassen
        Wie sieht soll das Objekt zu Beginn aussehen?
        '''

        self.pos_x = 0

        self.pos_y = 0

        self.rotation = 54546873521
        self.img1r = pygame.Rect(size * anzahl + size * 10, 0, size * 1, size * 4)
        self.img2r = pygame.Rect(size * anzahl + size * 4, 0, size * 2, size * 3)
        self.img3r = pygame.Rect(size * anzahl + size * 7, 0, size * 2, size * 3)
        self.img4r = pygame.Rect(size * anzahl + size, 0, size * 2, size * 2)
        self.img5r = pygame.Rect(size * anzahl + size, size * 3, size * 2, size * 2)
        self.img6r = pygame.Rect(size * anzahl + size * 4, size * 4, size * 3, size * 2)
        self.img7r = pygame.Rect(size * anzahl + size, size * 6, size * 3, size * 2)
        self.img8r = pygame.Rect(size * anzahl + size * 4, size * 7, size * 3, size * 2)
        self.img9r = pygame.Rect(size * anzahl + size * 7, size * 6, size * 3, size * 2)
        # TODO:
        WEISS = (255, 255, 255)



        self.img1 = pygame.image.load('Images/1.png')
        self.img1.set_colorkey(WEISS)
        self.img2 = pygame.image.load('Images/2.png')
        self.img2.set_colorkey(WEISS)
        self.img3 = pygame.image.load('Images/3.png')
        self.img3.set_colorkey(WEISS)
        self.img4 = pygame.image.load('Images/4.png')
        self.img4.set_colorkey(WEISS)
        self.img5 = pygame.image.load('Images/5.png')
        self.img5.set_colorkey(WEISS)
        self.img6 = pygame.image.load('Images/6.png')
        self.img6.set_colorkey(WEISS)
        self.img7 = pygame.image.load('Images/7.png')
        self.img7.set_colorkey(WEISS)
        self.img8 = pygame.image.load('Images/8.png')
        self.img8.set_colorkey(WEISS)
        self.img9 = pygame.image.load('Images/9.png')
        self.img9.set_colorkey(WEISS)


        self.imgStretch1 = pygame.transform.scale(self.img1, (SIZE, SIZE // 2))
        self.imgStretch2 = pygame.transform.scale(self.img2, (SIZE, SIZE // 2))
        self.imgStretch3 = pygame.transform.scale(self.img3, (SIZE, SIZE // 2))
        self.imgStretch4 = pygame.transform.scale(self.img4, (SIZE, SIZE // 2))
        self.imgStretch5 = pygame.transform.scale(self.img5, (SIZE, SIZE // 2))
        self.imgStretch6 = pygame.transform.scale(self.img6, (SIZE, SIZE // 2))
        self.imgStretch7 = pygame.transform.scale(self.img7, (SIZE, SIZE // 2))
        self.imgStretch8 = pygame.transform.scale(self.img8, (SIZE, SIZE // 2))
        self.imgStretch9 = pygame.transform.scale(self.img9, (SIZE, SIZE // 2))

        self.colors = [
            (0, 0, 0),
            (120, 37, 179),
            (100, 179, 179),
            (80, 34, 22),
            (80, 134, 22),
            (180, 34, 22),
            (180, 34, 122),
        ]

        # self.type = random.randint(0, len(self.figures) - 1)
        self.color = (128, 128, 128)  # random.randint(1, len(self.colors) - 1)

    def image(self):
        return self.figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])

    #####################################################################Bewegungen als Methoden festlegen
    # mit Defaultwert (optionalen Parameter) GESCHWINDIGKEITE
    def bewegungNachUnten(self, step=GESCHWINDIGKEIT):
        self.rect.y += step  # bewegt sich nach unten

    def bewegungNachOben(self, step=GESCHWINDIGKEIT):
        self.rect.y -= step

    def bewegungNachLinks(self, step=GESCHWINDIGKEIT):
        self.rect.x -= step

    def bewegungNachRechts(self, step=GESCHWINDIGKEIT):
        self.rect.x += step

    def istKollisionMit(self, otherRect):  # TODO:
        self.setPunkte(1)
        return self.rect.colliderect(otherRect)  # True, wenn Kollision

    #####################################################################Datenkapselung mit Zugriffsmethoden
    def getPunkte(self):  # Abfragemethode
        return self.punkte

    def setPunkte(self, anzahlPunkte=1):  # Ã„nderungsmethode
        self.punkte += anzahlPunkte

    ####################################################################Update und Events
    def update(self):
        pass  # Hier erfolgt das Zustandsupdate des Spielers werden

    def handle_event(self, event):  # TODO                                #Event-Handlung der Bewegungstasten
        if event.type == pygame.KEYUP:
            if event.key == K_LEFT or event.key == K_a:
                self.bewegungNachLinks()
            if event.key == K_RIGHT or event.key == K_d:
                self.bewegungNachRechts()
            if event.key == K_UP or event.key == K_w:
                self.bewegungNachOben()
            if event.key == K_DOWN or event.key == K_s:
                self.bewegungNachUnten()

#####################################################################################Instanzen der Klasse testen
# myPlay1 = Spieler(0,0, 10, 10)
# myPlay2 = Spieler(10, 10, 10, 10)
# print("Get:" + str(myPlay1.getPunkte()))
# myPlay1.setPunkte(1)
# print("GetNach+1:" + str(myPlay1.getPunkte()))
# mehrere Spieler verwenden
# listeSpieler = []
# listeSpieler.append(myPlay1)
# listeSpieler.append(myPlay2)


######################################################################################Main-Methode
# if __name__ == '__main__':
# myPlay1 = Tetris_teile(0,0, 10, 10)
# myPlay2 = Spieler(10, 10, 10, 10)
# listeSpieler = []
# listeSpieler.append(myPlay1)
# listeSpieler.append(myPlay2)