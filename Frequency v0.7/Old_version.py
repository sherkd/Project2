import pygame, time, random, os
from Node import *

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Soundtrack/crash.wav")
pygame.mixer.music.play(-1)

#############
crash_sound = pygame.mixer.Sound('Soundtrack/song.wav')
#############

display_width = 1280
display_height = 720

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
silver = (191,191,191)
darksilver = (230,230,230)
bright_red = (255,255,255)
bright_green = (255,255,255)
block_color = (53,115,255)

clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Frequency')

gameIcon = pygame.image.load('Content/Frequency.png')
pygame.display.set_icon(gameIcon)

pause = False
#crash = True

#laod the image for the background
bg = pygame.image.load("Content/map.png")
background = pygame.image.load("Pawns/map.jpg")

##########################################################
#laod the image for the pawns
##########################################################
tg = pygame.image.load("Pawns/tank geel.png")
tankgeel = Unit(240, -5)
sg = pygame.image.load("Pawns/soldier geel.png")
soldiergeel = Unit(190,40)
rg = pygame.image.load("Pawns/robot geel.png")

playergeel = pygame.image.load("Pawns/player_red_resize.png")


tgr = pygame.image.load("Pawns/tank groen.png")
tankgroen = Unit(990, 675)
sgr = pygame.image.load("Pawns/soldier groen.png")
soldiergroen = Unit(1045,640)
rgr = pygame.image.load("Pawns/robot groen.png")

playergroen = pygame.image.load("Pawns/player groen.png")


tr = pygame.image.load("Pawns/tank rood.png")
tankrood = Unit(990, -5)
sr = pygame.image.load("Pawns/soldier rood.png")
soldierrood = Unit(1040,40)
rr = pygame.image.load("Pawns/robot rood.png")

playerrood = pygame.image.load("Pawns/player rood.png")


tb = pygame.image.load("Pawns/tank blauw.png")
tankblauw = Unit(240, 675)
sb = pygame.image.load("Pawns/soldier blauw.png")
soldierblauw = Unit(190,640)
rb = pygame.image.load("Pawns/robot blauw.png")

playerblauw = pygame.image.load("Pawns/player blauw.png")
##########################################################

player1 = Player(190,-5,500,240,750,150,500,1000)
player1tank = Empty
player1robot = Empty
player1soldaat = Empty
player1basis = Node(Basis(playergeel,190,-5),Empty)
player1barak = Empty


player2 = Player(190,-5,500,240,750,150,500,1000)
player2tank = Empty
player2robot = Empty
player2soldaat = Empty
player2basis = Node(Basis(playergroen,190,-5),Empty)
player2barak = Empty


player3 = Player(190,-5,500,240,750,150,500,1000)
player3tank = Empty
player3robot = Empty
player3soldaat = Empty
player3basis = Node(Basis(playerrood,190,-5),Empty)
player3barak = Empty


player4 = Player(190,-5,500,240,750,150,500,1000)
player4tank = Empty
player4robot = Empty
player4soldaat = Empty
player4basis = Node(Basis(playerblauw,190,-5),Empty)
player4barak = Empty

##########################################################

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def crash():
    ####################################
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    ####################################
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()



        button("Play Again",150,450,100,50,silver,white,two_players)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(60)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def quitgame():
    pygame.quit()
    quit()


def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False


def paused():
    ############
    pygame.mixer.music.pause()
    #############
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)


    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        button("Continue",440,480,100,40,silver,white,unpause)
        button("Main Menu",590,480,100,40,silver,white,game_intro)
        button("Quit",745,480,100,40,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(60)


def Draw(sl):
    if sl.IsEmpty == True:
        return
    else:
        tempS = sl.Value
        if tempS != Empty:
            gameDisplay.blit(tempS.Texture,(tempS.PositionX,tempS.PositionY))
            Draw(sl.Tail)


##def draw(a,b,c):
##
##    gameDisplay.blit(a,(b,c))

##def draw_tank():
##
##    while draw_tank:
##        draw(tg,tankgeel.PosX,tankgeel.PosY)
##(player1robot,player1tank,player1,player1soldaat,player1barak)

def game_intro():

    pygame.mixer.music.unpause()

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        bg = pygame.image.load("Content/bg2.png")
        gameDisplay.blit(bg, (0, 0))

        button("Two Players",570,100,150,40,silver,white,two_players(player1robot,player1tank,player1,player1soldaat,player1barak))
        button("Four Players",570,160,150,40,silver,white,four_players)
        button("Rules",570,220,150,40,silver,white,rules)
        button("Quit",570,550,150,40,red,bright_red,quitgame)

        pygame.display.update()

        clock.tick(60)
        text = "Frequency | FPS: {0:.2f} ".format(clock.get_fps())
        pygame.display.set_caption(text)


def two_players(plr,plt,player1,pls,plb):
    #Call pause function, without this the pause function doesn't work. Must be called in every function needed.
    global pause

    #Player's turn text
    smallText = pygame.font.SysFont("comicsansms",18)
    p1Turn, TextRect = text_objects("Player 1's Turn", smallText)

##    two_players_player_1 = True

    #moves counter
    counter = 4

    #MainLoop
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            #Constantly print mouse position in the console
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
            #Unit 1 Controls (tank)
                if event.key == pygame.K_w and counter > 0:
                    tankgeel.PosY -= 40
                    counter -= 1
                    print (tankgeel.PosX,tankgeel.PosY)
                if event.key == pygame.K_a and counter > 0:
                    tankgeel.PosX -= 50
                    counter -= 1
                    print (tankgeel.PosX,tankgeel.PosY)
                if event.key == pygame.K_s and counter > 0:
                    tankgeel.PosY += 40
                    counter -= 1
                    print (tankgeel.PosX,tankgeel.PosY)
                if event.key == pygame.K_d and counter > 0:
                    tankgeel.PosX += 50
                    counter -= 1
                    print (tankgeel.PosX,tankgeel.PosY)
            #Unit 2 Controls (soldier)
                if event.key == pygame.K_i and counter > 0:
                    soldiergeel.PosY -= 40
                    counter -= 1
                if event.key == pygame.K_j and counter > 0:
                    soldiergeel.PosX -= 50
                    counter -= 1
                if event.key == pygame.K_k and counter > 0:
                    soldiergeel.PosY += 40
                    counter -= 1
                if event.key == pygame.K_l and counter > 0:
                    soldiergeel.PosX += 50
                    counter -= 1
            #Unit 3 Controls (robot)
                if event.key == pygame.K_LEFT:
                    .PosX -= 50
                    counter -= 1
                if event.key == pygame.K_UP:
                    .PosY -= 40
                    counter -= 1
                if event.key == pygame.K_DOWN:
                    .PosY += 40
                    counter -= 1
                if event.key == pygame.K_RIGHT:
                    .PosX += 50
                    counter -= 1
##            #Unit 4 Controls (boat (nevergonnahappen))
##                if event.key == pygame.K_KP8:
##                    .PosY -= 40
##                if event.key == pygame.K_KP4:
##                    .PosX -= 50
##                if event.key == pygame.K_KP5:
##                    .PosY += 40
##                if event.key == pygame.K_KP6:
##                    .PosX += 50

            #pause the game by clicking either 'escape' or 'p'
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                    pause = True
                    paused()

            #get position by clicking left mouse button
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                print (mouseX, mouseY)

            #borders/boundaries Yellow Tank
            if tankgeel.PosX >= 1040:
                tankgeel.PosX = 1040

            if tankgeel.PosX <= 190:
                tankgeel.PosX = 190

            if tankgeel.PosY >= 675:
                tankgeel.PosY = 675

            if tankgeel.PosY <= -5:
                tankgeel.PosY = -5

            #borders/boundaries Yellow Soldier
            if soldiergeel.PosX >= 1040:
                soldiergeel.PosX = 1040

            if soldiergeel.PosX <= 190:
                soldiergeel.PosX = 190

            if soldiergeel.PosY >= 675:
                soldiergeel.PosY = 675

            if soldiergeel.PosY <= -5:
                soldiergeel.PosY = -5



        #Draw the background on position x,y
        gameDisplay.blit(background, (0, 0))

        #Draw the amount of moves
        livecounter, TextRect = text_objects("Moves Left:" + str(counter), smallText)
        gameDisplay.blit(livecounter, (45,20))

        #Draw the players turn
        gameDisplay.blit(p1Turn, (40,0))

##        Draw(plr1tank)
##        Draw(plr1soldier)
##        Draw(plr1robot)
##        Draw(player1basis)

        Draw(plt)
        Draw(pls)
        Draw(plr)
        Draw(player1basis)

        #Draw the tanks
##        draw(tg,tankgeel.PosX,tankgeel.PosY)
##        draw(tgr,tankgroen.PosX,tankgroen.PosY)

##        button("Buy Tank",25,80,150,40,silver,white,draw_tank)

        #Draw the soldiers
##        draw(sg,soldiergeel.PosX,soldiergeel.PosY)
##        draw(sgr,soldiergroen.PosX,soldiergroen.PosY)

        if counter == 0:
            #Button to switch turns: button("textonbutton",x,y,length,width,colour,function)
            button("End Turn",25,50,150,40,silver,white,turn_switch_2_player)

        pygame.display.update()
        clock.tick(60)
        text = "Frequency | FPS: {0:.2f} ".format(clock.get_fps())
        pygame.display.set_caption(text)


def turn_switch_2_player():
    #Call pause function, without this the pause function doesn't work. Must be called in every function needed.
    global pause

    #Player's turn text
    smallText = pygame.font.SysFont("comicsansms",18)
    p2Turn, TextRect = text_objects("Player 2's Turn", smallText)

    #moves counter
    counter = 4

    #MainLoop
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            #constantly print mouse position in the console
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
            #Unit 1 Controls (tank)
                if event.key == pygame.K_w and counter > 0:
                    tankgroen.PosY -= 40
                    counter -= 1
                if event.key == pygame.K_a and counter > 0:
                    tankgroen.PosX -= 50
                    counter -= 1
                if event.key == pygame.K_s and counter > 0:
                    tankgroen.PosY += 40
                    counter -= 1
                if event.key == pygame.K_d and counter > 0:
                    tankgroen.PosX += 50
                    counter -= 1
            #Unit 2 Controls (soldier)
                if event.key == pygame.K_i and counter > 0:
                    soldiergroen.PosY -= 40
                    counter -= 1
                if event.key == pygame.K_j and counter > 0:
                    soldiergroen.PosX -= 50
                    counter -= 1
                if event.key == pygame.K_k and counter > 0:
                    soldiergroen.PosY += 40
                    counter -= 1
                if event.key == pygame.K_l and counter > 0:
                    soldiergroen.PosX += 50
                    counter -= 1
##            #Unit 3 Controls (robot)
##                if event.key == pygame.K_LEFT:
##                    tankgroen.PosX -= 50
##                if event.key == pygame.K_UP:
##                    tankgroen.PosY -= 40
##                if event.key == pygame.K_DOWN:
##                    tankgroen.PosY += 40
##                if event.key == pygame.K_RIGHT:
##                    tankgroen.PosX += 50
##            #Unit 4 Controls (boat)
##                if event.key == pygame.K_KP8:
##                    soldiergroen.PosY -= 40
##                if event.key == pygame.K_KP4:
##                    soldiergroen.PosX -= 50
##                if event.key == pygame.K_KP5:
##                    soldiergroen.PosY += 40
##                if event.key == pygame.K_KP6:
##                    soldiergroen.PosX += 50

            #pause the game by clicking either 'escape' or 'p'
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                    pause = True
                    paused()

            #get position by clicking left mouse button
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                print (mouseX, mouseY)


            #borders/boundaries Green Tank
            if tankgroen.PosX >= 1040:
                tankgroen.PosX = 1040

            if tankgroen.PosX <= 190:
                tankgroen.PosX = 190

            if tankgroen.PosY >= 675:
                tankgroen.PosY = 675

            if tankgroen.PosY <= -5:
                tankgroen.PosY = -5

            #borders/boundaries Green Soldier
            if soldiergroen.PosX >= 1040:
                soldiergroen.PosX = 1040

            if soldiergroen.PosX <= 190:
                soldiergroen.PosX = 190

            if soldiergroen.PosY >= 675:
                soldiergroen.PosY = 675

            if soldiergroen.PosY <= -5:
                soldiergroen.PosY = -5


        #Draw the background on position x,y
        gameDisplay.blit(bg, (0, 0))

        #Draw the amount of moves
        livecounter, TextRect = text_objects("Moves Left:" + str(counter), smallText)
        gameDisplay.blit(livecounter, (45,20))

        #Draw the players turn
        gameDisplay.blit(p2Turn, (40,0))

        #Draw the tank
        draw(tg,tankgeel.PosX,tankgeel.PosY)
        draw(tgr,tankgroen.PosX,tankgroen.PosY)

        #Draw the soldier
        draw(sg,soldiergeel.PosX,soldiergeel.PosY)
        draw(sgr,soldiergroen.PosX,soldiergroen.PosY)

        if counter == 0:
            #Button to switch turns: button("textonbutton",x,y,length,width,colour,function)
            button("End Turn",25,50,150,40,silver,white,two_players)

        clock.tick(60)
        text = "Frequency | FPS: {0:.2f} ".format(clock.get_fps())
        pygame.display.set_caption(text)

        pygame.display.update()


def four_players():
    #Call pause function, without this the pause function doesn't work. Must be called in every function needed.
    global pause

    #player's turn text
    smallText = pygame.font.SysFont("comicsansms",18)
    p1Turn, TextRect = text_objects("Player 1's Turn", smallText)

    #moves counter
    counter = 4

    #main loop
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            #constantly print mouse position in the console
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
            #Unit 1 Controls
                if event.key == pygame.K_w and counter > 0:
                    tankgeel.PosY -= 40
                    counter -= 1
                if event.key == pygame.K_a and counter > 0:
                    tankgeel.PosX -= 50
                    counter -= 1
                if event.key == pygame.K_s and counter > 0:
                    tankgeel.PosY += 40
                    counter -= 1
                if event.key == pygame.K_d and counter > 0:
                    tankgeel.PosX += 50
                    counter -= 1
            #Unit 2 Controls
                if event.key == pygame.K_i and counter > 0:
                    soldiergeel.PosY -= 40
                    counter -= 1
                if event.key == pygame.K_j and counter > 0:
                    soldiergeel.PosX -= 50
                    counter -= 1
                if event.key == pygame.K_k and counter > 0:
                    soldiergeel.PosY += 40
                    counter -= 1
                if event.key == pygame.K_l and counter > 0:
                    soldiergeel.PosX += 50
                    counter -= 1
##            #Unit 3 Controls
##                if event.key == pygame.K_LEFT:
##                    tankgroen.PosX -= 50
##                if event.key == pygame.K_UP:
##                    tankgroen.PosY -= 40
##                if event.key == pygame.K_DOWN:
##                    tankgroen.PosY += 40
##                if event.key == pygame.K_RIGHT:
##                    tankgroen.PosX += 50
##            #Unit 4 Controls
##                if event.key == pygame.K_KP8:
##                    soldiergroen.PosY -= 40
##                if event.key == pygame.K_KP4:
##                    soldiergroen.PosX -= 50
##                if event.key == pygame.K_KP5:
##                    soldiergroen.PosY += 40
##                if event.key == pygame.K_KP6:
##                    soldiergroen.PosX += 50

            #pause the game by clicking either 'escape' or 'p'
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                    pause = True
                    paused()

            #get position by clicking left mouse button
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                print (mouseX, mouseY)

            #borders/boundaries Yellow Tank
            if tankgeel.PosX >= 1040:
                tankgeel.PosX = 1040

            if tankgeel.PosX <= 190:
                tankgeel.PosX = 190

            if tankgeel.PosY >= 675:
                tankgeel.PosY = 675

            if tankgeel.PosY <= -5:
                tankgeel.PosY = -5

            #borders/boundaries Yellow Soldier
            if soldiergeel.PosX >= 1040:
                soldiergeel.PosX = 1040

            if soldiergeel.PosX <= 190:
                soldiergeel.PosX = 190

            if soldiergeel.PosY >= 675:
                soldiergeel.PosY = 675

            if soldiergeel.PosY <= -5:
                soldiergeel.PosY = -5



        #laod the image for the background
        bg = pygame.image.load("Content/map.png")

        #Draw the background on position x,y
        gameDisplay.blit(bg, (0, 0))

        #Draw the amount of moves
        livecounter, TextRect = text_objects("Moves Left:" + str(counter), smallText)
        gameDisplay.blit(livecounter, (45,20))

        #Draw the players turn
        gameDisplay.blit(p1Turn, (40,0))

        #Draw the tank
        draw(tg,tankgeel.PosX,tankgeel.PosY)
        draw(tgr,tankgroen.PosX,tankgroen.PosY)
        draw(tr,tankrood.PosX,tankrood.PosY)
        draw(tb,tankblauw.PosX,tankblauw.PosY)

        #Draw the soldier
        draw(sg,soldiergeel.PosX,soldiergeel.PosY)
        draw(sgr,soldiergroen.PosX,soldiergroen.PosY)
        draw(sr,soldierrood.PosX,soldierrood.PosY)
        draw(sb,soldierblauw.PosX,soldierblauw.PosY)

        if counter == 0:
            #Button to switch turns: button("textonbutton",x,y,length,width,colour,function)
            button("End Turn",25,50,150,40,silver,white,turn_switch_four_player)

        pygame.display.update()
        clock.tick(60)
        text = "Frequency | FPS: {0:.2f} ".format(clock.get_fps())
        pygame.display.set_caption(text)


def turn_switch_four_player():
    #Call pause function, without this the pause function doesn't work. Must be called in every function needed.
    global pause

    #Player's turn text
    smallText = pygame.font.SysFont("comicsansms",18)
    p2Turn, TextRect = text_objects("Player 2's Turn", smallText)

    #moves counter
    counter = 4

    #MainLoop
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            #constantly print mouse position in the console
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
            #Unit 1 Controls (tank)
                if event.key == pygame.K_w and counter > 0:
                    tankgroen.PosY -= 40
                    counter -= 1
                if event.key == pygame.K_a and counter > 0:
                    tankgroen.PosX -= 50
                    counter -= 1
                if event.key == pygame.K_s and counter > 0:
                    tankgroen.PosY += 40
                    counter -= 1
                if event.key == pygame.K_d and counter > 0:
                    tankgroen.PosX += 50
                    counter -= 1
            #Unit 2 Controls (soldier)
                if event.key == pygame.K_i and counter > 0:
                    soldiergroen.PosY -= 40
                    counter -= 1
                if event.key == pygame.K_j and counter > 0:
                    soldiergroen.PosX -= 50
                    counter -= 1
                if event.key == pygame.K_k and counter > 0:
                    soldiergroen.PosY += 40
                    counter -= 1
                if event.key == pygame.K_l and counter > 0:
                    soldiergroen.PosX += 50
                    counter -= 1
##            #Unit 3 Controls (robot)
##                if event.key == pygame.K_LEFT:
##                    tankgroen.PosX -= 50
##                if event.key == pygame.K_UP:
##                    tankgroen.PosY -= 40
##                if event.key == pygame.K_DOWN:
##                    tankgroen.PosY += 40
##                if event.key == pygame.K_RIGHT:
##                    tankgroen.PosX += 50
##            #Unit 4 Controls (boat)
##                if event.key == pygame.K_KP8:
##                    soldiergroen.PosY -= 40
##                if event.key == pygame.K_KP4:
##                    soldiergroen.PosX -= 50
##                if event.key == pygame.K_KP5:
##                    soldiergroen.PosY += 40
##                if event.key == pygame.K_KP6:
##                    soldiergroen.PosX += 50

            #pause the game by clicking either 'escape' or 'p'
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                    pause = True
                    paused()

            #get position by clicking left mouse button
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                print (mouseX, mouseY)

            #borders/boundaries Green Tank
            if tankgroen.PosX >= 1040:
                tankgroen.PosX = 1040

            if tankgroen.PosX <= 190:
                tankgroen.PosX = 190

            if tankgroen.PosY >= 675:
                tankgroen.PosY = 675

            if tankgroen.PosY <= -5:
                tankgroen.PosY = -5

            #borders/boundaries Green Soldier
            if soldiergroen.PosX >= 1040:
                soldiergroen.PosX = 1040

            if soldiergroen.PosX <= 190:
                soldiergroen.PosX = 190

            if soldiergroen.PosY >= 675:
                soldiergroen.PosY = 675

            if soldiergroen.PosY <= -5:
                soldiergroen.PosY = -5

        #laod the image for the background
        bg = pygame.image.load("Content/map.png")

        #Draw the background on position x,y
        gameDisplay.blit(bg, (0, 0))

        #Draw the amount of moves
        livecounter, TextRect = text_objects("Moves Left:" + str(counter), smallText)
        gameDisplay.blit(livecounter, (45,20))

        #Draw the players turn
        gameDisplay.blit(p2Turn, (40,0))

        #Draw the tank
        draw(tg,tankgeel.PosX,tankgeel.PosY)
        draw(tgr,tankgroen.PosX,tankgroen.PosY)
        draw(tr,tankrood.PosX,tankrood.PosY)
        draw(tb,tankblauw.PosX,tankblauw.PosY)

        #Draw the soldier
        draw(sg,soldiergeel.PosX,soldiergeel.PosY)
        draw(sgr,soldiergroen.PosX,soldiergroen.PosY)
        draw(sr,soldierrood.PosX,soldierrood.PosY)
        draw(sb,soldierblauw.PosX,soldierblauw.PosY)

        if counter == 0:
            #Button to switch turns: button("textonbutton",x,y,length,width,colour,function)
            button("End Turn",25,50,150,40,silver,white,turn_switch_four_player_2)

        clock.tick(60)
        text = "Frequency | FPS: {0:.2f} ".format(clock.get_fps())
        pygame.display.set_caption(text)

        pygame.display.update()



def turn_switch_four_player_2():
    #Call pause function, without this the pause function doesn't work. Must be called in every function needed.
    global pause

    #Player's turn text
    smallText = pygame.font.SysFont("comicsansms",18)
    p3Turn, TextRect = text_objects("Player 3's Turn", smallText)

    #moves counter
    counter = 4

    #MainLoop
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            #constantly print mouse position in the console
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
            #Unit 1 Controls (tank)
                if event.key == pygame.K_w:
                    tankrood.PosY -= 40
                    counter -= 1
                if event.key == pygame.K_a:
                    tankrood.PosX -= 50
                    counter -= 1
                if event.key == pygame.K_s:
                    tankrood.PosY += 40
                    counter -= 1
                if event.key == pygame.K_d:
                    tankrood.PosX += 50
                    counter -= 1
            #Unit 2 Controls (soldier)
                if event.key == pygame.K_i:
                    soldierrood.PosY -= 40
                    counter -= 1
                if event.key == pygame.K_j:
                    soldierrood.PosX -= 50
                    counter -= 1
                if event.key == pygame.K_k:
                    soldierrood.PosY += 40
                    counter -= 1
                if event.key == pygame.K_l:
                    soldierrood.PosX += 50
                    counter -= 1
##            #Unit 3 Controls (robot)
##                if event.key == pygame.K_LEFT:
##                    tankgroen.PosX -= 50
##                if event.key == pygame.K_UP:
##                    tankgroen.PosY -= 40
##                if event.key == pygame.K_DOWN:
##                    tankgroen.PosY += 40
##                if event.key == pygame.K_RIGHT:
##                    tankgroen.PosX += 50
##            #Unit 4 Controls (boat)
##                if event.key == pygame.K_KP8:
##                    soldiergroen.PosY -= 40
##                if event.key == pygame.K_KP4:
##                    soldiergroen.PosX -= 50
##                if event.key == pygame.K_KP5:
##                    soldiergroen.PosY += 40
##                if event.key == pygame.K_KP6:
##                    soldiergroen.PosX += 50

            #pause the game by clicking either 'escape' or 'p'
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                    pause = True
                    paused()

            #get position by clicking left mouse button
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                print (mouseX, mouseY)

            #borders/boundaries Red Tank
            if tankrood.PosX >= 1040:
                tankrood.PosX = 1040

            if tankrood.PosX <= 190:
                tankrood.PosX = 190

            if tankrood.PosY >= 675:
                tankrood.PosY = 675

            if tankrood.PosY <= -5:
                tankrood.PosY = -5

            #borders/boundaries Red Soldier
            if soldierrood.PosX >= 1040:
                soldierrood.PosX = 1040

            if soldierrood.PosX <= 190:
                soldierrood.PosX = 190

            if soldierrood.PosY >= 675:
                soldierrood.PosY = 675

            if soldierrood.PosY <= -5:
                soldierrood.PosY = -5

        #laod the image for the background
        bg = pygame.image.load("Content/map.png")

        #Draw the background on position x,y
        gameDisplay.blit(bg, (0, 0))

        #Draw the amount of moves
        livecounter, TextRect = text_objects("Moves Left:" + str(counter), smallText)
        gameDisplay.blit(livecounter, (45,20))

        #Draw the players turn
        gameDisplay.blit(p3Turn, (40,0))

        #Draw the tank
        draw(tg,tankgeel.PosX,tankgeel.PosY)
        draw(tgr,tankgroen.PosX,tankgroen.PosY)
        draw(tr,tankrood.PosX,tankrood.PosY)
        draw(tb,tankblauw.PosX,tankblauw.PosY)

        #Draw the soldier
        draw(sg,soldiergeel.PosX,soldiergeel.PosY)
        draw(sgr,soldiergroen.PosX,soldiergroen.PosY)
        draw(sr,soldierrood.PosX,soldierrood.PosY)
        draw(sb,soldierblauw.PosX,soldierblauw.PosY)

        if counter == 0:
            #Button to switch turns: button("textonbutton",x,y,length,width,colour,function)
            button("End Turn",25,50,150,40,silver,white,turn_switch_four_player_3)

        clock.tick(60)
        text = "Frequency | FPS: {0:.2f} ".format(clock.get_fps())
        pygame.display.set_caption(text)

        pygame.display.update()



def turn_switch_four_player_3():
    #Call pause function, without this the pause function doesn't work. Must be called in every function needed.
    global pause

    #Player's turn text
    smallText = pygame.font.SysFont("comicsansms",18)
    p4Turn, TextRect = text_objects("Player 4's Turn", smallText)

    #moves counter
    counter = 4

    #MainLoop
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            #constantly print mouse position in the console
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
            #Unit 1 Controls (tank)
                if event.key == pygame.K_w:
                    tankblauw.PosY -= 40
                    counter -= 1
                if event.key == pygame.K_a:
                    tankblauw.PosX -= 50
                    counter -= 1
                if event.key == pygame.K_s:
                    tankblauw.PosY += 40
                    counter -= 1
                if event.key == pygame.K_d:
                    tankblauw.PosX += 50
                    counter -= 1
            #Unit 2 Controls (soldier)
                if event.key == pygame.K_i:
                    soldierblauw.PosY -= 40
                    counter -= 1
                if event.key == pygame.K_j:
                    soldierblauw.PosX -= 50
                    counter -= 1
                if event.key == pygame.K_k:
                    soldierblauw.PosY += 40
                    counter -= 1
                if event.key == pygame.K_l:
                    soldierblauw.PosX += 50
                    counter -= 1
##            #Unit 3 Controls (robot)
##                if event.key == pygame.K_LEFT:
##                    tankgroen.PosX -= 50
##                if event.key == pygame.K_UP:
##                    tankgroen.PosY -= 40
##                if event.key == pygame.K_DOWN:
##                    tankgroen.PosY += 40
##                if event.key == pygame.K_RIGHT:
##                    tankgroen.PosX += 50
##            #Unit 4 Controls (boat)
##                if event.key == pygame.K_KP8:
##                    soldiergroen.PosY -= 40
##                if event.key == pygame.K_KP4:
##                    soldiergroen.PosX -= 50
##                if event.key == pygame.K_KP5:
##                    soldiergroen.PosY += 40
##                if event.key == pygame.K_KP6:
##                    soldiergroen.PosX += 50

            #pause the game by clicking either 'escape' or 'p'
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                    pause = True
                    paused()

            #get position by clicking left mouse button
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                print (mouseX, mouseY)

            #borders/boundaries Blue Tank
            if tankblauw.PosX >= 1040:
                tankblauw.PosX = 1040

            if tankblauw.PosX <= 190:
                tankblauw.PosX = 190

            if tankblauw.PosY >= 675:
                tankblauw.PosY = 675

            if tankblauw.PosY <= -5:
                tankblauw.PosY = -5

            #borders/boundaries Blue Soldier
            if soldierblauw.PosX >= 1040:
                soldierblauw.PosX = 1040

            if soldierblauw.PosX <= 190:
                soldierblauw.PosX = 190

            if soldierblauw.PosY >= 675:
                soldierblauw.PosY = 675

            if soldierblauw.PosY <= -5:
                soldierblauw.PosY = -5

        #laod the image for the background
        bg = pygame.image.load("Content/map.png")

        #Draw the background on position x,y
        gameDisplay.blit(bg, (0, 0))

        #Draw the amount of moves
        livecounter, TextRect = text_objects("Moves Left:" + str(counter), smallText)
        gameDisplay.blit(livecounter, (45,20))

        #Draw the players turn
        gameDisplay.blit(p4Turn, (40,0))

        #Draw the tank
        draw(tg,tankgeel.PosX,tankgeel.PosY)
        draw(tgr,tankgroen.PosX,tankgroen.PosY)
        draw(tr,tankrood.PosX,tankrood.PosY)
        draw(tb,tankblauw.PosX,tankblauw.PosY)

        #Draw the soldier
        draw(sg,soldiergeel.PosX,soldiergeel.PosY)
        draw(sgr,soldiergroen.PosX,soldiergroen.PosY)
        draw(sr,soldierrood.PosX,soldierrood.PosY)
        draw(sb,soldierblauw.PosX,soldierblauw.PosY)

        if counter == 0:
            #Button to switch turns: button("textonbutton",x,y,length,width,colour,function)
            button("End Turn",25,50,150,40,silver,white,four_players)

        clock.tick(60)
        text = "Frequency | FPS: {0:.2f} ".format(clock.get_fps())
        pygame.display.set_caption(text)

        pygame.display.update()



def rules():

    gameExit = False
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        bg = pygame.image.load("Rules/rules.png")
        gameDisplay.blit(bg, (0, 0))

        button("Main Menu",25,30,150,40,silver,white,game_intro)
        button("Next",300,650,100,40,silver,white,rules2)

        pygame.display.update()
        clock.tick(60)
        text = "Frequency | FPS: {0:.2f} ".format(clock.get_fps())
        pygame.display.set_caption(text)


def rules2():

    gameExit = False
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        bg = pygame.image.load("Rules/rules2.png")
        gameDisplay.blit(bg, (0, 0))

        button("Main Menu",25,30,150,40,silver,white,game_intro)
        button("Back",200,650,100,40,silver,white,rules)
        button("Next",300,650,100,40,silver,white,rules3)


        pygame.display.update()
        clock.tick(60)
        text = "Frequency | FPS: {0:.2f} ".format(clock.get_fps())
        pygame.display.set_caption(text)


def rules3():

    gameExit = False
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        bg = pygame.image.load("Rules/rules3.png")
        gameDisplay.blit(bg, (0, 0))

        button("Main Menu",25,30,150,40,silver,white,game_intro)
        button("Back",200,650,100,40,silver,white,rules2)
##        button("Next",300,650,100,40,silver,white,rules4)


        pygame.display.update()
        clock.tick(60)
        text = "Frequency | FPS: {0:.2f} ".format(clock.get_fps())
        pygame.display.set_caption(text)



game_intro()
##two_players(player1robot,player1tank,player1,player1soldaat,player1barak)
##rules()
pygame.quit()
quit()