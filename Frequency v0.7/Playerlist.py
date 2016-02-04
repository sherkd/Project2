from threading import Thread
import time, os, pygame, time
from random import randint
from builtins import print
from Node import *
from Playermodels import *

##########################################################

player1 = Player(190,-5,500,240,750,150,500,1000)
player1tank = Empty
player1robot = Empty
player1soldaat = Empty
player1basis = Node(Base(playergeel,190,0),Empty)
player1barak = Empty


player2 = Player(1045,680,500,240,750,150,500,1000)
player2tank = Empty
player2robot = Empty
player2soldaat = Empty
player2basis = Node(Base(playergroen,1045,680),Empty)
player2barak = Empty


player3 = Player(190,-5,500,240,750,150,500,1000)
player3tank = Empty
player3robot = Empty
player3soldaat = Empty
player3basis = Node(Base(playerrood,190,-5),Empty)
player3barak = Empty


player4 = Player(190,-5,500,240,750,150,500,1000)
player4tank = Empty
player4robot = Empty
player4soldaat = Empty
player4basis = Node(Base(playerblauw,190,-5),Empty)
player4barak = Empty

##########################################################