import time
from threading import Thread
import os, pygame
import time
from random import randint
from builtins import print

class Node:
    def __init__(self, value, tail):
        self.Tail = tail
        self.Value = value
        self.IsEmpty = False

class Empty:
    def __init__(self):
        self.IsEmpty = True

Empty = Empty()


class Unit():
    def __init__(self,x,y):
        self.PosX = x
        self.PosY = y

class Player:
    def __init__(self,startposx,startposy,money,robot,tank,soldaat,barak,boot):
        self.startPosX = startposx
        self.startPosY = startposy
        self.Money = money
        self.Robot = robot
        self.Tank = tank
        self.Soldaat = soldaat
        self.Barak = barak
        self.Boot = boot
        self.bRobot = False
        self.bTank = False
        self.bSoldaat = False
        self.bBarak = False
        self.bBoot = False

##Bos = 1
##Moeras = 2
##IJsvlakte = 3
##Woestijn = 4

##    def Price(self):
##        if self.startPos == 1:
##            self.Robot = 240
##            self.Tank = 750
##            self.Soldaat = 150
##            self.Barak = 500
##            self.Boot = 1000
##        if self.startPos == 2:
##            self.Robot = 300
##            self.Tank = 750
##            self.Soldaat = 150
##            self.Barak = 500
##            self.Boot = 800
##        if self.startPos == 3:
##            self.Robot = 300
##            self.Tank = 750
##            self.Soldaat = 120
##            self.Barak = 500
##            self.Boot = 1000
##        if self.startPos == 4:
##            self.Robot = 300
##            self.Tank = 600
##            self.Soldaat = 150
##            self.Barak = 500
##            self.Boot = 1000
##
##    def Train(self):
##        if self.bRobot == True and player1.startPos == 1:
##            self.Money = self.Money - self.Robot
##        if player1train.bTank == True and player1.startPos == 1:
##            self.Money = self.Money - self.Tank
##        if player1train.bSoldaat == True and player1.startPos == 1:
##            self.Money = self.Money - self.Soldaat
##        if player1train.bBarak == True and player1.startPos == 1:
##            self.Money = self.Money - self.Barak
##        if player1train.bBoot == True and player1.startPos == 1:
##            self.Money = self.Money - self.Boot
##        if player1train.bRobot == True and player1.startPos == 2:
##            self.Money = self.Money - self.Robot
##        if player1train.bTank == True and player1.startPos == 2:
##            self.Money = self.Money - self.Tank
##        if player1train.bSoldaat == True and player1.startPos == 2:
##            self.Money = self.Money - self.Soldaat
##        if player1train.bBarak == True and player1.startPos == 2:
##            self.Money = self.Money - self.Barak
##        if player1train.bBoot == True and player1.startPos == 2:
##            self.Money = self.Money - self.Boot
##        if player1train.bRobot == True and player1.startPos == 3:
##            self.Money = self.Money - self.Robot
##        if player1train.bTank == True and player1.startPos == 3:
##            self.Money = self.Money - self.Tank
##        if player1train.bSoldaat == True and player1.startPos == 3:
##            self.Money = self.Money - self.Soldaat
##        if player1train.bBarak == True and player1.startPos == 3:
##            self.Money = self.Money - self.Barak
##        if player1train.bBoot == True and player1.startPos == 3:
##            self.Money = self.Money - self.Boot
##        if player1train.bRobot == True and player1.startPos == 4:
##            self.Money = self.Money - self.Robot
##        if player1train.bTank == True and player1.startPos == 4:
##            self.Money = self.Money - self.Tank
##        if player1train.bSoldaat == True and player1.startPos == 4:
##            self.Money = self.Money - self.Soldaat
##        if player1train.bBarak == True and player1.startPos == 4:
##            self.Money = self.Money - self.Barak
##        if player1train.bBoot == True and player1.startPos == 4:
##            self.Money = self.Money - self.Boot


class Barrack:

    def __init__(self,texture,posx,posy):
         self.Texture = texture
         self.PositionX = posx
         self.PositionY = posy
##         self.HP = healthpoints

class Base:

    def __init__(self,texture,posx,posy):
         self.Texture = texture
         self.PositionX = posx
         self.PositionY = posy
##         self.HP = healthpoints


class Boat:

    def __init__(self,texture,posx,posy):
         self.Texture = texture
         self.PositionX = posx
         self.PositionY = posy
##         self.HP = healthpoints

class Robot:

   def __init__(self,texture,posx,posy):
         self.Texture = texture
         self.PositionX = posx
         self.PositionY = posy
##         self.HP = healthpoints
##         self.AP = attackpoints

class Soldier:

    def __init__(self,texture,posx,posy):
         self.Texture = texture
         self.PositionX = posx
         self.PositionY = posy
##         self.HP = healthpoints
##         self.AP = attackpoints

class Tank:

    def __init__(self,texture,posx,posy):
         self.Texture = texture
         self.PositionX = posx
         self.PositionY = posy
##         self.HP = healthpoints
##         self.AP = attackpoints