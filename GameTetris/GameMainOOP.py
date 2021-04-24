'''
Created on 07.01.2021

@author: metko_kerstin

Dokumentation:
Dies ist ein Pythonmodul, mit dem man ein einfaches Spiel realisieren
und initialisiert werden kann.
Nehmen Sie dies gern als Vorlage fÃ¼r Ihr Projekt.
Themen: Farbwahl, Events, Grafik, Sound, Bewegung, Kollision und Zeitgeber.
'''
#####################################################################################Import
import pygame, sys, time  # importiere Module
from pygame.locals import *  # importiere Konstanten von Pygame
# from OOP_Game_TetrisPuzzle.Vorlage.Spieler import Spieler as Spieler
import GameTetris.Spieler as Spieler

# halllllloooooo

# import Vorlage.Hindernis                                                              #import packackage.modul

#####################################################################################SET-UP
# der Variablen
TITEL = "Tetris Puzzle"
# FBREITE = 500
# FHOEHE = FBREITE
WSIZE = (1000, 1000)

FBREITE, FHOEHE = 1800, 1000
screen = pygame.display.set_mode((FBREITE, FHOEHE))

#####################################################################################Farbwahl

SCHWARZ = (0, 0, 0)  # RGB - Rot GrÃ¼n Blau
WEISS = (255, 255, 255)
PINKTAFFY = (249, 135, 197)
PINKFANDANGO = (223, 125, 134)
PINKDARK = (144, 33, 71)
GRAU = (128, 128, 128)
PURPUR = (128, 0, 128)
BLAUGRUEN = (0, 128, 128)
GELB = (255, 255, 0)
FPS = 20

HINTERGRUND = pygame.image.load('Images/jungle.jpg')
HINTERGRUND = pygame.transform.scale(HINTERGRUND, (1800, 1000))

#####################################################################################Klasse fÃ¼r Spiel erstellen
class MyGameMain(object):
    '''
    classdocs:
    Erstellen der Klasse, als Startklasse fÃ¼r das Spiel.
    ErklÃ¤ren Sie hier, was die Klasse macht.
    '''

    #################################################################################__init__ der Klasse MyGameMain, wird automatisch aufgerufen
    def __init__(self, anzahlGegner, zeit):  # self ist Referenz auf die aktuelle Instanz

        '''
        Constructor:
        Wir weisen die Anfangsattribute zu.
        '''
        #############################################################################Attribute der Klasse MyGameMain
        # self.raeume = None
        # self.spieler = None
        self.verloren = False
        # self.anzahlGegner = anzahlGegner
        self.zeit = zeit
        self.uhr = pygame.time.Clock()  # Zeitgeber
        #self.tetris_teileL = []
        # self.musicplay = False
        # self.ercollide = pygame.Rect(0, 0, 20, 20)
        # self.imagRMouseUp = pygame.Rect(0, 0, 20, 20)
        print("Welcome")
        self.size = 100
        self.anzahl = 6  # Pygame initieren
        pygame.init()
        self.gui = pygame.display.set_mode((FBREITE, FHOEHE))  # GUI-Fenster-GrÃ¶ÃŸe festlegen
        pygame.display.set_caption(TITEL)  # Titel festlegen
        # self.backgroundImg =  pygame.image.load('Images/background1.png')           #Backgroundimages festlegen
        # pygame.mixer.music.load('Sounds/miau.mp3')                                  #Backgroundsounds
        # pygame.mixer.music.play(-1,0.0)                                             #-1 unendlich oft wiederholen, 2 wÃ¤re 2x abspielen
        # self.musicplay = True                                                       #Attribut fÃ¼r Musik an/aus

    def setup(self):  # Setup der beteiligten Objekte
        self.tetris_teile = Spieler.Tetris_teile(self.size, self.anzahl)
        # self.tetris_teileL.append(Vorlage.Spieler.Tetris_teile(0,400,20,20))
        # self.tetris_teileL.append(Vorlage.Spieler.Tetris_teile(0,600,20,20))
        # self.tetris_teileL.append(self.tetris_teile)
        self.aktivesTeil = None
        self.liesteFelder = []

    # Methoden der Klasse MyGameMain

    def feldZeichnen(self):

        screen.blit(HINTERGRUND, (0,0))



        colors = [GRAU, SCHWARZ]
        for r in range(self.anzahl):
            for c in range(self.anzahl):
                color = colors[((r + c) % 2)]
                # pygame.draw.rect(self.gui, color, pygame.Rect(c*50, r*50, 50, 50))
                # self.liesteFelder.append(pygame.Rect(c*50, r*50, 50, 50))

                rectX = pygame.Rect(c * self.size, r * self.size, self.size, self.size)
                dict = {"A1": rectX}
                self.liesteFelder.append(dict)
                pygame.draw.rect(self.gui, color, pygame.Rect(c * self.size, r * self.size, self.size, self.size))

        # pygame.draw.rect(self.gui, (0,0,0), pygame.Rect(0,0,50,50))
        # pygame.draw.rect(self.gui, (255,255,255), pygame.Rect(51,0,50,50))
        # pygame.draw.rect(self.gui, (255,255,255), pygame.Rect(0,51,50,50))
        # pygame.draw.rect(self.gui, (0,0,0), pygame.Rect(51,51,50,50))

    def hinweiseIntro(self):  # Platz fÃ¼r die SpielerklÃ¤rungen und -hinweise
        print("Hier kann die Anleitung des Spiels stehen")  # Welche Taste macht was, was ist das Ziel, etc.

    # def sounds(self):                                                               #Sound
    #   self.soundShort = pygame.mixer.Sound('Sounds/knut.mp3')                     #Kurze Sounds

    def mouse(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx = event.pos[0]
            my = event.pos[1]
            b1 = pygame.Rect(mx, my, self.size, self.size)
            self.ercollide = b1
            # b2 = pygame.Rect(mx, my, 20, -80)
            if self.tetris_teile.img1r.colliderect(b1):
                print("collision Teil 1 mouse button down")
                self.aktivesTeil = 1
            elif self.tetris_teile.img2r.colliderect(b1):
                print("collision Teil 2 mouse button down")
                self.aktivesTeil = 2
            elif self.tetris_teile.img3r.colliderect(b1):
                print("collision Teil 3 mouse button down")
                self.aktivesTeil = 3
            elif self.tetris_teile.img4r.colliderect(b1):
                print("collision Teil 4 mouse button down")
                self.aktivesTeil = 4
            elif self.tetris_teile.img5r.colliderect(b1):
                print("collision Teil 5 mouse button down")
                self.aktivesTeil = 5
            elif self.tetris_teile.img6r.colliderect(b1):
                print("collision Teil 6 mouse button down")
                self.aktivesTeil = 6
            elif self.tetris_teile.img7r.colliderect(b1):
                print("collision Teil 7 mouse button down")
                self.aktivesTeil = 7
            elif self.tetris_teile.img8r.colliderect(b1):
                print("collision Teil 8 mouse button down")
                self.aktivesTeil = 8
            elif self.tetris_teile.img9r.colliderect(b1):
                print("collision Teil 9 mouse button down")
                self.aktivesTeil = 9

        if event.type == pygame.MOUSEBUTTONUP:
            mx = event.pos[0]
            my = event.pos[1]
            b1 = pygame.Rect(mx, my, self.size, self.size)
            self.imagRMouseUp = b1
            row = my // self.size
            col = mx // self.size
            print(row)
            print(col)
            if self.aktivesTeil == 1:
                self.tetris_teile.img1r = pygame.Rect(col * self.size, row * self.size, self.size * 1, self.size * 4)
                self.aktivesTeil = None
                print("aktieves mouse button up")
            elif self.aktivesTeil == 2:
                self.tetris_teile.img2r = pygame.Rect(col * self.size, row * self.size, self.size * 2, self.size * 3)
                self.aktivesTeil = None
            elif self.aktivesTeil == 3:
                self.tetris_teile.img3r = pygame.Rect(col * self.size, row * self.size, self.size * 2, self.size * 3)
                self.aktivesTeil = None
            elif self.aktivesTeil == 4:
                self.tetris_teile.img4r = pygame.Rect(col * self.size, row * self.size, self.size * 2, self.size * 2)
                self.aktivesTeil = None
            elif self.aktivesTeil == 5:
                self.tetris_teile.img5r = pygame.Rect(col * self.size, row * self.size, self.size * 2, self.size * 2)
                self.aktivesTeil = None
            elif self.aktivesTeil == 6:
                self.tetris_teile.img6r = pygame.Rect(col * self.size, row * self.size, self.size * 3, self.size * 2)
                self.aktivesTeil = None
            elif self.aktivesTeil == 7:
                self.tetris_teile.img7r = pygame.Rect(col * self.size, row * self.size, self.size * 3, self.size * 2)
                self.aktivesTeil = None
            elif self.aktivesTeil == 8:
                self.tetris_teile.img8r = pygame.Rect(col * self.size, row * self.size, self.size * 3, self.size * 2)
                self.aktivesTeil = None
            elif self.aktivesTeil == 9:
                self.tetris_teile.img9r = pygame.Rect(col * self.size, row * self.size, self.size * 3, self.size * 2)
                self.aktivesTeil = None

            # if self.tetris_teile.img2r.colliderect(b1):

    def run(self):

        while not self.verloren:  #####################################################Main-Loop, Hauptschleife
            #########################################################################Zeichnen des Screens, der Elemente
            self.gui.fill((255, 255, 255))  # WEISS fuellen
            self.feldZeichnen()
            #########################################################################Eventschleife
            for event in pygame.event.get():
                if event.type == QUIT:  # Beendenbutton X
                    pygame.quit()  # Beenden der Anwendung
                    sys.exit()
                if self.tetris_teile is not None:  # TODO:                                 #Events fÃ¼r Spieler-Klasse
                    self.tetris_teile.handle_event(event)
                    self.mouse(event)
                if event.type == KEYUP:
                    if event.key == K_m:  # Taste m fÃ¼r Ton ein/aus
                        if self.musicplay:  # Hintergrundmusik
                            pygame.mixer.stop()  # stoppt Musik
                        else:
                            pygame.mixer.music.play(-1, 0.0)
                            self.musicplay = not self.musicplay

                # if event.type == MOUSEBUTTONUP:                                     #Mausevents verwenden
                # b1 = {'rect':pygame.Rect(event.pos[0], event.pos[1],10,10), 'color':PURPUR}
                # pygame.draw.rect(self.gui, b1['color'], b1['rect']) #Zeichne Box auf GUI
                # self.gui.blit(self.imgStretch, pygame.Rect(215,75,80,80))
                # pygame.draw.circle(self.gui, BLAUGRUEN, (event.pos[1], event.pos[0]), 52, 10)

                # self.gui.blit(self.tetris_teileL[1].imgStretch2, self.tetris_teileL[1].img2r)

            else:
                hindernisse = []

            # if self.tetris_teileL is not None:
            # self.gui.blit()
            # self.Spieler.update() #TODO:
            # self.gui.blit(self.spieler.imgStretch, self.spieler.rect)           #Zeichnet den Spieler
            # for tetris in self.tetris_teileL:
            # pygame.Rect(tetris.pos_x, tetris.pos_y, tetris.groesse[0], tetris.groesse[1])

            self.gui.blit(self.tetris_teile.img1, self.tetris_teile.img1r)
            self.gui.blit(self.tetris_teile.img2, self.tetris_teile.img2r)
            self.gui.blit(self.tetris_teile.img3, self.tetris_teile.img3r)
            self.gui.blit(self.tetris_teile.img4, self.tetris_teile.img4r)
            self.gui.blit(self.tetris_teile.img5, self.tetris_teile.img5r)
            self.gui.blit(self.tetris_teile.img6, self.tetris_teile.img6r)
            self.gui.blit(self.tetris_teile.img7, self.tetris_teile.img7r)
            self.gui.blit(self.tetris_teile.img8, self.tetris_teile.img8r)
            self.gui.blit(self.tetris_teile.img9, self.tetris_teile.img9r)
            # pygame.draw.rect(self.gui, PURPUR, self.ercollide)
            # pygame.draw.rect(self.gui, GELB, self.imagRMouseUp)
            # pygame.draw.rect(self.gui, BLAUGRUEN, pygame.Rect(self.tetris_teile.img1r.x, self.tetris_teile.img1r.y , self.size*1 +10, self.size*4+10))

            # pygame.draw.rect(self.gui, tetris.color, (tetris.pos_x, tetris.pos_y, tetris.groesse[0], tetris.groesse[1]))
            #########################################################################Display update und Bewegungen zeigen
            pygame.display.flip()
            self.uhr.tick(FPS)  # FPS-Frames per Second, Zeitgeber
        #############################################################################wenn Spiel beendet, pygame beenden
        pygame.quit()

    #####################################################################################Instanzen der Klasse testen


obj1MyGameMain = MyGameMain(2, 60)  # Instanz von der MyGameMain erstellt
obj1MyGameMain.setup()  # Setup ausfÃ¼hren
obj1MyGameMain.run()  # Hauptschleife starten

if __name__ == '__main__':
    obj1MyGameMain = MyGameMain(2, 60)  # Instanz von der MyGameMain erstellt
    obj1MyGameMain.methode1()
    print(obj1MyGameMain.anzahlGegner)