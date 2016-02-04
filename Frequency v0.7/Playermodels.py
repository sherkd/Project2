from threading import Thread
import time, os, pygame, time
from random import randint
from builtins import print
from Node import *


##########################################################
#load the image for the background
##########################################################
bg = pygame.image.load("Content/mainmap.png")
menubg = pygame.image.load("Content/bg2.png")
movebg = pygame.image.load("Content/mapmove.png")
##########################################################


##########################################################
#load the image for the pawns
##########################################################
tg = pygame.image.load("Pawns/tank geel.png")
tankgeel = Unit(240, -5)
sg = pygame.image.load("Pawns/soldier geel.png")
soldiergeel = Unit(190,40)
rg = pygame.image.load("Pawns/robot geel.png")

playergeel = pygame.image.load("Pawns/player_yellow_resize.png")


tgr = pygame.image.load("Pawns/tank groen.png")
tankgroen = Unit(990, 675)
sgr = pygame.image.load("Pawns/soldier groen.png")
soldiergroen = Unit(1045,640)
rgr = pygame.image.load("Pawns/robot groen.png")

playergroen = pygame.image.load("Pawns/player_green_resize.png")


tr = pygame.image.load("Pawns/tank rood.png")
tankrood = Unit(990, -5)
sr = pygame.image.load("Pawns/soldier rood.png")
soldierrood = Unit(1040,40)
rr = pygame.image.load("Pawns/robot rood.png")

playerrood = pygame.image.load("Pawns/player_red_resize.png")


tb = pygame.image.load("Pawns/tank blauw.png")
tankblauw = Unit(240, 675)
sb = pygame.image.load("Pawns/soldier blauw.png")
soldierblauw = Unit(190,640)
rb = pygame.image.load("Pawns/robot blauw.png")

playerblauw = pygame.image.load("Pawns/player_blue_resize.png")
##########################################################
