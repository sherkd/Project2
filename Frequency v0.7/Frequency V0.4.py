import pygame, time, random, os
##from Frequency import *
from Node import *
from Playerlist import *
from Playermodels import *

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

smallText = pygame.font.SysFont("comicsansms",18)

money = 5000
counter = 10


##for event in pygame.event.get():
##    if event.type == pygame.QUIT:
##        pygame.quit()
##        quit()
##    if event.type == pygame.MOUSEMOTION:
##        mousex, mousey = pygame.mouse.get_pos()
##
##mousex, mousey = pygame.mouse.get_pos()

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

##Main(True,False,False,player1robot,player1tank,player1,player1soldaat,player1barak)

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
            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP and mousex > 590 and mousex < 690 and mousey > 480 and mousey < 520:
                    Main(True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat,player1barak,player2robot,player2tank,player2,player2soldaat,player2barak)

        button("Continue",440,480,100,40,silver,white,unpause)
        button("Main Menu",590,480,100,40,silver,white)
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


def CheckUp(l,x,y):
    while l.IsEmpty == False:
        tempL = l.Value
        if x > tempL.PositionX and x < (tempL.PositionX + 42) and y > tempL.PositionY and y < (tempL.PositionY + 42):
            tempL.PositionY = tempL.PositionY - 40
            l.Value.PositionX = tempL.PositionX
            Main(False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat,player1barak,player2robot,player2tank,player2,player2soldaat,player2barak)
        else: CheckUp(l.Tail,x,y)
    Main(False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat,player1barak,player2robot,player2tank,player2,player2soldaat,player2barak)

def CheckDown(l,x,y):
    while l.IsEmpty == False:
        tempL = l.Value
        if x > tempL.PositionX and x < (tempL.PositionX + 42) and y > tempL.PositionY and y < (tempL.PositionY + 42):
            tempL.PositionY = tempL.PositionY + 40
            l.Value.PositionX = tempL.PositionX
            Main(False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat,player1barak,player2robot,player2tank,player2,player2soldaat,player2barak)
        else: CheckDown(l.Tail,x,y)
    Main(False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat,player1barak,player2robot,player2tank,player2,player2soldaat,player2barak)

def CheckLeft(l,x,y):
    while l.IsEmpty == False:
        tempL = l.Value
        if x > tempL.PositionX and x < (tempL.PositionX + 42) and y > tempL.PositionY and y < (tempL.PositionY + 42):
            tempL.PositionX = tempL.PositionX - 50
            l.Value.PositionX = tempL.PositionX
            Main(False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat,player1barak,player2robot,player2tank,player2,player2soldaat,player2barak)
        else: CheckLeft(l.Tail,x,y)
    Main(False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat,player1barak,player2robot,player2tank,player2,player2soldaat,player2barak)

def CheckRight(l,x,y):
    while l.IsEmpty == False:
        tempL = l.Value
        if x > tempL.PositionX and x < (tempL.PositionX + 42) and y > tempL.PositionY and y < (tempL.PositionY + 42):
            tempL.PositionX = tempL.PositionX + 50
            l.Value.PositionX = tempL.PositionX
            Main(False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat,player1barak,player2robot,player2tank,player2,player2soldaat,player2barak)
        else: CheckRight(l.Tail,x,y)
    Main(False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat,player1barak,player2robot,player2tank,player2,player2soldaat,player2barak)


def Main(menu,twoplayers,rules,rules2,rules3,buytank,buysoldier,buyrobot,move,movetank,movetankright,movetankleft,movetankup,movetankdown,movesoldier,movesoldierright,movesoldierleft,movesoldierup,movesoldierdown,moverobot,moverobotright,moverobotleft,moverobotup,moverobotdown,p1robot,p1tank,player1,p1soldier,p1basis,p2robot,p2tank,player2,p2soldier,p2basis):

    while menu:
        pygame.mixer.music.unpause()

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP and mousex > 570 and mousex < 720 and mousey > 100 and mousey < 140:
                    menu = False
                    twoplayers = True
            if event.type == pygame.MOUSEBUTTONUP and mousex > 570 and mousex < 720 and mousey > 220 and mousey < 260:
                    menu = False
                    twoplayers = False
                    rules = True

        gameDisplay.blit(menubg, (0, 0))

        button("Two Players",570,100,150,40,silver,white)
        button("Four Players",570,160,150,40,silver,white)
        button("Rules",570,220,150,40,silver,white)
        button("Quit",570,550,150,40,red,bright_red,quitgame)

        pygame.display.update()

        clock.tick(60)
        text = "Frequency | FPS: {0:.2f} ".format(clock.get_fps())
        pygame.display.set_caption(text)


    while twoplayers:
        global bg, counter, money, pause

        for event in pygame.event.get():
            #Constantly print mouse position in the console
            print(event)
            #makes it possible to use quit the game on the top right
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #receives position of the mouse
            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP and mousex > 20 and mousex < 170 and mousey > 100 and mousey < 140 and counter > 0: #buy tank button
                twoplayers = False
                buytank = True
                counter -= 1
                money -= 500
            if event.type == pygame.MOUSEBUTTONUP and mousex > 20 and mousex < 170 and mousey > 160 and mousey < 200 and counter > 0: #buy soldier button
                twoplayers = False
                buysoldier = True
                counter -= 1
                money -= 150
            if event.type == pygame.MOUSEBUTTONUP and mousex > 20 and mousex < 170 and mousey > 220 and mousey < 260  and counter > 0: #buy robot button
                twoplayers = False
                buyrobot = True
                counter -= 1
                money -= 300
            if event.type == pygame.MOUSEBUTTONUP and mousex > 20 and mousex < 170 and mousey > 340 and mousey < 380 and counter > 0: #move button
                twoplayers = False
                move = True
                counter -= 1

##            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
##                CheckUp(player1tank,mousex,mousey)
##                counter -= 1
##            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
##                CheckLeft(player1tank,mousex,mousey)
##                counter -= 1
##            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
##                CheckDown(player1tank,mousex,mousey)
##                counter -= 1
##            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
##                CheckRight(player1tank,mousex,mousey)
##                counter -= 1


##            if event.type == pygame.KEYDOWN:
##            #Unit 1 Controls (tank)
##                if event.key == pygame.K_w and counter > 0:
##                    CheckRight(player1tank,mousex,mousey)
##                    counter -= 1
##
##                if event.key == pygame.K_a and counter > 0:
##                    CheckRight(player1tank,mousex,mousey)
##                    counter -= 1
##
##                if event.key == pygame.K_s and counter > 0:
##                    CheckRight(player1tank,mousex,mousey)
##                    counter -= 1
##
##                if event.key == pygame.K_d and counter > 0:
##                    CheckRight(player1tank,mousex,mousey)
##                    counter -= 1
##
##            #Unit 2 Controls (soldier)
##                if event.key == pygame.K_i and counter > 0:
##                    soldiergeel.PosY -= 40
##                    counter -= 1
##                if event.key == pygame.K_j and counter > 0:
##                    soldiergeel.PosX -= 50
##                    counter -= 1
##                if event.key == pygame.K_k and counter > 0:
##                    soldiergeel.PosY += 40
##                    counter -= 1
##                if event.key == pygame.K_l and counter > 0:
##                    soldiergeel.PosX += 50
##                    counter -= 1

##            #Unit 3 Controls (robot)
##                if event.key == pygame.K_LEFT:
##                    .PosX -= 50
##                    counter -= 1
##                if event.key == pygame.K_UP:
##                    .PosY -= 40
##                    counter -= 1
##                if event.key == pygame.K_DOWN:
##                    .PosY += 40
##                    counter -= 1
##                if event.key == pygame.K_RIGHT:
##                    .PosX += 50
##                    counter -= 1

            if event.type == pygame.KEYDOWN:
            #pause the game by clicking either 'escape' or 'p'
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                    pause = True
                    paused()

            #get position by clicking left mouse button
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                print (mouseX, mouseY)


        #Draw the background on position x,y
        gameDisplay.blit(bg, (0, 0))

        #Draw the players turn
        p1Turn, TextRect = text_objects("Player 1's Turn", smallText)
        gameDisplay.blit(p1Turn, (30,0))

        #Draw the amount of moves
        livecounter, TextRect = text_objects("Moves Left:" + str(counter), smallText)
        gameDisplay.blit(livecounter, (35,25))

        #Draw the money of the current player
        playermoney, TextRect = text_objects("Money:" + str(money), smallText)
        gameDisplay.blit(playermoney, (45,50))

        #Draw the helptext
        Pause, TextRect = text_objects("Press Esc or P", smallText)
        gameDisplay.blit(Pause, (1100,660))
        Pause2, TextRect = text_objects("to Pause the game", smallText)
        gameDisplay.blit(Pause2, (1100,680))

        if counter > 0:
            #Draw the available buttons
            button("Buy Tank",20,100,150,40,silver,white)
            button("Buy Soldier",20,160,150,40,silver,white)
            button("Buy Robot",20,220,150,40,silver,white)
            button("Build Barracks",20,280,150,40,silver,white)
            button("Move",20,340,150,40,silver,white)


        #draw the units of player
        Draw(p1tank)
        Draw(p1soldier)
        Draw(p1robot)
        Draw(player1basis)

        Draw(p2tank)
        Draw(p2soldier)
        Draw(p2robot)
        Draw(player2basis)


        if counter == 0:
            #Button to switch turns: button("textonbutton",x,y,length,width,colour,function)
            button("End Turn",20,650,150,40,silver,white)

        pygame.display.update()
        clock.tick(60)
        text = "Frequency | FPS: {0:.2f} ".format(clock.get_fps())
        pygame.display.set_caption(text)


    while rules:

        for event in pygame.event.get():
            #makes it possible to use quit the game on the top right
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #receives position of the mouse
            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP and mousex > 25 and mousex < 175 and mousey > 30 and mousey < 70:
                Main(True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat,player1barak,player2robot,player2tank,player2,player2soldaat,player2barak)
            if event.type == pygame.MOUSEBUTTONUP and mousex > 300 and mousex <400 and mousey > 650 and mousey < 690:
                rules = False
                rules2 = True

        bg = pygame.image.load("Rules/rules.png")
        gameDisplay.blit(bg, (0, 0))

        button("Main Menu",25,30,150,40,silver,white)
        button("Next",300,650,100,40,silver,white)

        pygame.display.update()
        clock.tick(60)
        text = "Frequency | FPS: {0:.2f} ".format(clock.get_fps())
        pygame.display.set_caption(text)


    while rules2:

        for event in pygame.event.get():
            #makes it possible to use quit the game on the top right
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #receives position of the mouse
            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP and mousex > 25 and mousex < 175 and mousey > 30 and mousey < 70: #main menu
                Main(True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat,player1barak,player2robot,player2tank,player2,player2soldaat,player2barak)
            if event.type == pygame.MOUSEBUTTONUP and mousex > 200 and mousex < 300 and mousey > 650 and mousey < 690: #back
                Main(False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat,player1barak,player2robot,player2tank,player2,player2soldaat,player2barak)
            if event.type == pygame.MOUSEBUTTONUP and mousex > 300 and mousex < 400 and mousey > 650 and mousey < 690: #next
                Main(False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat,player1barak,player2robot,player2tank,player2,player2soldaat,player2barak)

        bg = pygame.image.load("Rules/rules2.png")
        gameDisplay.blit(bg, (0, 0))

        button("Main Menu",25,30,150,40,silver,white)
        button("Back",200,650,100,40,silver,white)
        button("Next",300,650,100,40,silver,white)


        pygame.display.update()
        clock.tick(60)
        text = "Frequency | FPS: {0:.2f} ".format(clock.get_fps())
        pygame.display.set_caption(text)


    while rules3:

        for event in pygame.event.get():
            #makes it possible to use quit the game on the top right
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #receives position of the mouse
            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP and mousex > 25 and mousex < 175 and mousey > 30 and mousey < 70: #main menu
                Main(True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat,player1barak,player2robot,player2tank,player2,player2soldaat,player2barak)
            if event.type == pygame.MOUSEBUTTONUP and mousex > 200 and mousex < 300 and mousey > 650 and mousey < 690: #back
                Main(False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat,player1barak,player2robot,player2tank,player2,player2soldaat,player2barak)

        bg = pygame.image.load("Rules/rules3.png")
        gameDisplay.blit(bg, (0, 0))

        button("Main Menu",25,30,150,40,silver,white)
        button("Back",200,650,100,40,silver,white)

        pygame.display.update()
        clock.tick(60)
        text = "Frequency | FPS: {0:.2f} ".format(clock.get_fps())
        pygame.display.set_caption(text)

    while buytank:
        global player1soldaat, player1robot, player1tank, pause

        for event in pygame.event.get():
            #makes it possible to use quit the game on the top right
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #receives position of the mouse
            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP and mousex > player1.startPosX and mousex < (player1.startPosX + 42) and mousey > player1.startPosY and mousey < (player1.startPosY +42):
                player1tank = Node(Tank(tg,(player1.startPosX+55),player1.startPosY),player1tank)
                player1.Money = player1.Money - 300
                Main(False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat,player1barak,player2robot,player2tank,player2,player2soldaat,player2barak)
            if event.type == pygame.KEYDOWN:
            #pause the game by clicking either 'escape' or 'p'
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                    pause = True
                    paused()

        #Draw the background on position x,y
        gameDisplay.blit(bg, (0 ,0))

        #Draw the players turn
        p1Turn, TextRect = text_objects("Player 1's Turn", smallText)
        gameDisplay.blit(p1Turn, (30,0))

        #Draw the amount of moves
        livecounter, TextRect = text_objects("Moves Left:" + str(counter), smallText)
        gameDisplay.blit(livecounter, (35,25))

        #Draw the money of the current player
        playermoney, TextRect = text_objects("Money:" + str(money), smallText)
        gameDisplay.blit(playermoney, (45,50))

        #Draw the instructions
        instr, TextRect = text_objects("Click on the", smallText)
        gameDisplay.blit(instr, (0,100))
        instr2, TextRect = text_objects("Base/Barrack where", smallText)
        gameDisplay.blit(instr2, (0,120))
        instr3, TextRect = text_objects("you want to build", smallText)
        gameDisplay.blit(instr3, (0,140))
        instr4, TextRect = text_objects("this unit.", smallText)
        gameDisplay.blit(instr4, (0,160))

        #Draw the helptext
        Pause, TextRect = text_objects("Press Esc or P", smallText)
        gameDisplay.blit(Pause, (1100,660))
        Pause2, TextRect = text_objects("to Pause the game", smallText)
        gameDisplay.blit(Pause2, (1100,680))

        #draw player 1's units
        Draw(p1tank)
        Draw(p1soldier)
        Draw(p1robot)
        Draw(player1basis)

        Draw(p2tank)
        Draw(p2soldier)
        Draw(p2robot)
        Draw(player2basis)

        pygame.display.update()
        clock.tick(60)
        text = "Frequency | FPS: {0:.2f} ".format(clock.get_fps())
        pygame.display.set_caption(text)

    while buysoldier:
        global player1soldaat, player1robot, player1tank, pause

        for event in pygame.event.get():
            #makes it possible to use quit the game on the top right
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #receives position of the mouse
            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP and mousex > player1.startPosX and mousex < (player1.startPosX + 42) and mousey > player1.startPosY and mousey < (player1.startPosY +42):
                player1soldaat = Node(Soldier(sg,(player1.startPosX+50),(player1.startPosY+5)),player1soldaat)
                player1.Money = player1.Money - 300
                Main(False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat,player1barak,player2robot,player2tank,player2,player2soldaat,player2barak)
            if event.type == pygame.KEYDOWN:
            #pause the game by clicking either 'escape' or 'p'
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                    pause = True
                    paused()

        #Draw the background on position x,y
        gameDisplay.blit(bg, (0 ,0))

        #Draw the players turn
        p1Turn, TextRect = text_objects("Player 1's Turn", smallText)
        gameDisplay.blit(p1Turn, (30,0))

        #Draw the amount of moves
        livecounter, TextRect = text_objects("Moves Left:" + str(counter), smallText)
        gameDisplay.blit(livecounter, (35,25))

        #Draw the money of the current player
        playermoney, TextRect = text_objects("Money:" + str(money), smallText)
        gameDisplay.blit(playermoney, (45,50))

        #Draw the instructions
        instr, TextRect = text_objects("Click on the", smallText)
        gameDisplay.blit(instr, (0,100))
        instr2, TextRect = text_objects("Base/Barrack where", smallText)
        gameDisplay.blit(instr2, (0,120))
        instr3, TextRect = text_objects("you want to build", smallText)
        gameDisplay.blit(instr3, (0,140))
        instr4, TextRect = text_objects("this unit.", smallText)
        gameDisplay.blit(instr4, (0,160))

        #Draw the helptext
        Pause, TextRect = text_objects("Press Esc or P", smallText)
        gameDisplay.blit(Pause, (1100,660))
        Pause2, TextRect = text_objects("to Pause the game", smallText)
        gameDisplay.blit(Pause2, (1100,680))

        #draw player 1's units
        Draw(p1tank)
        Draw(p1soldier)
        Draw(p1robot)
        Draw(player1basis)

        Draw(p2tank)
        Draw(p2soldier)
        Draw(p2robot)
        Draw(player2basis)

        pygame.display.update()
        clock.tick(60)
        text = "Frequency | FPS: {0:.2f} ".format(clock.get_fps())
        pygame.display.set_caption(text)

    while buyrobot:
        global player1soldaat, player1robot, player1tank, pause

        for event in pygame.event.get():
            #makes it possible to use quit the game on the top right
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #receives position of the mouse
            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP and mousex > player1.startPosX and mousex < (player1.startPosX + 42) and mousey > player1.startPosY and mousey < (player1.startPosY +42):
                player1robot = Node(Robot(rg,(player1.startPosX+50),(player1.startPosY+5)),player1robot)
                player1.Money = player1.Money - 300
                Main(False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat,player1barak,player2robot,player2tank,player2,player2soldaat,player2barak)
            if event.type == pygame.KEYDOWN:
            #pause the game by clicking either 'escape' or 'p'
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                    pause = True
                    paused()

        #Draw the background on position x,y
        gameDisplay.blit(bg, (0 ,0))

        #Draw the players turn
        p1Turn, TextRect = text_objects("Player 1's Turn", smallText)
        gameDisplay.blit(p1Turn, (30,0))

        #Draw the amount of moves
        livecounter, TextRect = text_objects("Moves Left:" + str(counter), smallText)
        gameDisplay.blit(livecounter, (35,25))

        #Draw the money of the current player
        playermoney, TextRect = text_objects("Money:" + str(money), smallText)
        gameDisplay.blit(playermoney, (45,50))

        #Draw the instructions
        instr, TextRect = text_objects("Click on the", smallText)
        gameDisplay.blit(instr, (0,100))
        instr2, TextRect = text_objects("Base/Barrack where", smallText)
        gameDisplay.blit(instr2, (0,120))
        instr3, TextRect = text_objects("you want to build", smallText)
        gameDisplay.blit(instr3, (0,140))
        instr4, TextRect = text_objects("this unit.", smallText)
        gameDisplay.blit(instr4, (0,160))

        #Draw the helptext
        Pause, TextRect = text_objects("Press Esc or P", smallText)
        gameDisplay.blit(Pause, (1100,660))
        Pause2, TextRect = text_objects("to Pause the game", smallText)
        gameDisplay.blit(Pause2, (1100,680))

        #draw player 1's units
        Draw(p1tank)
        Draw(p1soldier)
        Draw(p1robot)
        Draw(player1basis)

        Draw(p2tank)
        Draw(p2soldier)
        Draw(p2robot)
        Draw(player2basis)

        pygame.display.update()
        clock.tick(60)
        text = "Frequency | FPS: {0:.2f} ".format(clock.get_fps())
        pygame.display.set_caption(text)

    while move:

        for event in pygame.event.get():
            #makes it possible to use quit the game on the top right
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #receives position of the mouse
            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP and mousex > 20 and mousex < 170 and mousey > 100 and mousey < 140: #move tank button
                move = False
                movetank = True
            if event.type == pygame.MOUSEBUTTONUP and mousex > 20 and mousex < 170 and mousey > 160 and mousey < 200: #move soldier button
                move = False
                movesoldier = True
            if event.type == pygame.MOUSEBUTTONUP and mousex > 20 and mousex < 170 and mousey > 220 and mousey < 260: #move robot button
                move = False
                moverobot = True
            if event.type == pygame.MOUSEBUTTONUP and mousex > 20 and mousex < 170 and mousey > 220 and mousey < 260: #move robot button
                move = False
                moverobot = True
            if event.type == pygame.KEYDOWN:
            #pause the game by clicking either 'escape' or 'p'
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                    pause = True
                    paused()

        #Draw the background on position x,y
        gameDisplay.blit(bg, (0 ,0))

        #Draw the players turn
        p1Turn, TextRect = text_objects("Player 1's Turn", smallText)
        gameDisplay.blit(p1Turn, (30,0))

        #Draw the amount of moves
        livecounter, TextRect = text_objects("Moves Left:" + str(counter), smallText)
        gameDisplay.blit(livecounter, (35,25))

        #Draw the money of the current player
        playermoney, TextRect = text_objects("Money:" + str(money), smallText)
        gameDisplay.blit(playermoney, (45,50))

        #Draw the available buttons
        button("Move Tank",20,100,150,40,silver,white)
        button("Move Soldier",20,160,150,40,silver,white)
        button("Move Robot",20,220,150,40,silver,white)

        #Draw the helptext
        Pause, TextRect = text_objects("Press Esc or P", smallText)
        gameDisplay.blit(Pause, (1100,660))
        Pause2, TextRect = text_objects("to Pause the game", smallText)
        gameDisplay.blit(Pause2, (1100,680))

        #draw player 1's units
        Draw(p1tank)
        Draw(p1soldier)
        Draw(p1robot)
        Draw(player1basis)

        Draw(p2tank)
        Draw(p2soldier)
        Draw(p2robot)
        Draw(player2basis)

        pygame.display.update()
        clock.tick(60)
        text = "Frequency | FPS: {0:.2f} ".format(clock.get_fps())
        pygame.display.set_caption(text)

    while movetank:

        for event in pygame.event.get():
            print(event)
            #makes it possible to use quit the game on the top right
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #receives position of the mouse
            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP and mousex > 60 and mousex < 125 and mousey > 260 and mousey < 320: #move up button
                movetank = False
                movetankup = True
            if event.type == pygame.MOUSEBUTTONUP and mousex > 0 and mousex < 60 and mousey > 320 and mousey < 390: #move left button
                movetank = False
                movetankleft = True
            if event.type == pygame.MOUSEBUTTONUP and mousex > 125 and mousex < 175 and mousey > 320 and mousey < 390: #move right button
                movetank = False
                movetankright = True
            if event.type == pygame.MOUSEBUTTONUP and mousex > 60 and mousex < 125 and mousey > 380 and mousey < 445: #move down button
                movetank = False
                movetankdown = True
            if event.type == pygame.KEYDOWN:
            #pause the game by clicking either 'escape' or 'p'
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                    pause = True
                    paused()

        #Draw the background on position x,y
        gameDisplay.blit(movebg, (0 ,0))

        #Draw the players turn
        p1Turn, TextRect = text_objects("Player 1's Turn", smallText)
        gameDisplay.blit(p1Turn, (30,0))

        #Draw the amount of moves
        livecounter, TextRect = text_objects("Moves Left:" + str(counter), smallText)
        gameDisplay.blit(livecounter, (35,25))

        #Draw the money of the current player
        playermoney, TextRect = text_objects("Money:" + str(money), smallText)
        gameDisplay.blit(playermoney, (45,50))

        #Draw the helptext
        Pause, TextRect = text_objects("Press Esc or P", smallText)
        gameDisplay.blit(Pause, (1100,660))
        Pause2, TextRect = text_objects("to Pause the game", smallText)
        gameDisplay.blit(Pause2, (1100,680))

        #draw player 1's units
        Draw(p1tank)
        Draw(p1soldier)
        Draw(p1robot)
        Draw(player1basis)

        Draw(p2tank)
        Draw(p2soldier)
        Draw(p2robot)
        Draw(player2basis)

        pygame.display.update()
        clock.tick(60)
        text = "Frequency | FPS: {0:.2f} ".format(clock.get_fps())
        pygame.display.set_caption(text)

    while movetankright:
        global player1soldaat, player1robot, player1tank, pause
        #Draw the background on position x,y
        gameDisplay.blit(movebg, (0 ,0))

        #Draw the players turn
        p1Turn, TextRect = text_objects("Player 1's Turn", smallText)
        gameDisplay.blit(p1Turn, (30,0))

        #Draw the amount of moves
        livecounter, TextRect = text_objects("Moves Left:" + str(counter), smallText)
        gameDisplay.blit(livecounter, (35,25))

        #Draw the money of the current player
        playermoney, TextRect = text_objects("Money:" + str(money), smallText)
        gameDisplay.blit(playermoney, (45,50))

        #Draw the instructions
        instr, TextRect = text_objects("Click on the", smallText)
        gameDisplay.blit(instr, (0,100))
        instr2, TextRect = text_objects("Tank that you", smallText)
        gameDisplay.blit(instr2, (0,120))
        instr3, TextRect = text_objects("wish to move.", smallText)
        gameDisplay.blit(instr3, (0,140))

        #Draw the helptext
        Pause, TextRect = text_objects("Press Esc or P", smallText)
        gameDisplay.blit(Pause, (1100,660))
        Pause2, TextRect = text_objects("to Pause the game", smallText)
        gameDisplay.blit(Pause2, (1100,680))

        #draw player 1's units
        Draw(p1tank)
        Draw(p1soldier)
        Draw(p1robot)
        Draw(player1basis)

        Draw(p2tank)
        Draw(p2soldier)
        Draw(p2robot)
        Draw(player2basis)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mousex,mousey = pygame.mouse.get_pos()
            if event.type == pygame.KEYUP and event.key == K_ESCAPE:
                movetankright = False
            if event.type == pygame.MOUSEBUTTONUP:
                CheckRight(player1tank,mousex,mousey)
            pygame.display.update()

    while movetankleft:
        global player1soldaat, player1robot, player1tank, pause
        #Draw the background on position x,y
        gameDisplay.blit(movebg, (0 ,0))

        #Draw the players turn
        p1Turn, TextRect = text_objects("Player 1's Turn", smallText)
        gameDisplay.blit(p1Turn, (30,0))

        #Draw the amount of moves
        livecounter, TextRect = text_objects("Moves Left:" + str(counter), smallText)
        gameDisplay.blit(livecounter, (35,25))

        #Draw the money of the current player
        playermoney, TextRect = text_objects("Money:" + str(money), smallText)
        gameDisplay.blit(playermoney, (45,50))

        #Draw the instructions
        instr, TextRect = text_objects("Click on the", smallText)
        gameDisplay.blit(instr, (0,100))
        instr2, TextRect = text_objects("Tank that you", smallText)
        gameDisplay.blit(instr2, (0,120))
        instr3, TextRect = text_objects("wish to move.", smallText)
        gameDisplay.blit(instr3, (0,140))

        #Draw the helptext
        Pause, TextRect = text_objects("Press Esc or P", smallText)
        gameDisplay.blit(Pause, (1100,660))
        Pause2, TextRect = text_objects("to Pause the game", smallText)
        gameDisplay.blit(Pause2, (1100,680))

        #draw player 1's units
        Draw(p1tank)
        Draw(p1soldier)
        Draw(p1robot)
        Draw(player1basis)

        Draw(p2tank)
        Draw(p2soldier)
        Draw(p2robot)
        Draw(player2basis)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mousex,mousey = pygame.mouse.get_pos()
            if event.type == pygame.KEYUP and event.key == K_ESCAPE:
                movetankleft = False
            if event.type == pygame.MOUSEBUTTONUP:
                CheckLeft(player1tank,mousex,mousey)
            pygame.display.update()

    while movetankup:
        global player1soldaat, player1robot, player1tank, pause
        #Draw the background on position x,y
        gameDisplay.blit(movebg, (0 ,0))

        #Draw the players turn
        p1Turn, TextRect = text_objects("Player 1's Turn", smallText)
        gameDisplay.blit(p1Turn, (30,0))

        #Draw the amount of moves
        livecounter, TextRect = text_objects("Moves Left:" + str(counter), smallText)
        gameDisplay.blit(livecounter, (35,25))

        #Draw the money of the current player
        playermoney, TextRect = text_objects("Money:" + str(money), smallText)
        gameDisplay.blit(playermoney, (45,50))

        #Draw the instructions
        instr, TextRect = text_objects("Click on the", smallText)
        gameDisplay.blit(instr, (0,100))
        instr2, TextRect = text_objects("Tank that you", smallText)
        gameDisplay.blit(instr2, (0,120))
        instr3, TextRect = text_objects("wish to move.", smallText)
        gameDisplay.blit(instr3, (0,140))

        #Draw the helptext
        Pause, TextRect = text_objects("Press Esc or P", smallText)
        gameDisplay.blit(Pause, (1100,660))
        Pause2, TextRect = text_objects("to Pause the game", smallText)
        gameDisplay.blit(Pause2, (1100,680))

        #draw player 1's units
        Draw(p1tank)
        Draw(p1soldier)
        Draw(p1robot)
        Draw(player1basis)

        Draw(p2tank)
        Draw(p2soldier)
        Draw(p2robot)
        Draw(player2basis)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mousex,mousey = pygame.mouse.get_pos()
            if event.type == pygame.KEYUP and event.key == K_ESCAPE:
                movetankup = False
            if event.type == pygame.MOUSEBUTTONUP:
                CheckUp(player1tank,mousex,mousey)
            pygame.display.update()

    while movetankdown:
        global player1soldaat, player1robot, player1tank, pause
        #Draw the background on position x,y
        gameDisplay.blit(movebg, (0 ,0))

        #Draw the players turn
        p1Turn, TextRect = text_objects("Player 1's Turn", smallText)
        gameDisplay.blit(p1Turn, (30,0))

        #Draw the amount of moves
        livecounter, TextRect = text_objects("Moves Left:" + str(counter), smallText)
        gameDisplay.blit(livecounter, (35,25))

        #Draw the money of the current player
        playermoney, TextRect = text_objects("Money:" + str(money), smallText)
        gameDisplay.blit(playermoney, (45,50))

        #Draw the instructions
        instr, TextRect = text_objects("Click on the", smallText)
        gameDisplay.blit(instr, (0,100))
        instr2, TextRect = text_objects("Tank that you", smallText)
        gameDisplay.blit(instr2, (0,120))
        instr3, TextRect = text_objects("wish to move.", smallText)
        gameDisplay.blit(instr3, (0,140))

        #Draw the helptext
        Pause, TextRect = text_objects("Press Esc or P", smallText)
        gameDisplay.blit(Pause, (1100,660))
        Pause2, TextRect = text_objects("to Pause the game", smallText)
        gameDisplay.blit(Pause2, (1100,680))

        #draw player 1's units
        Draw(p1tank)
        Draw(p1soldier)
        Draw(p1robot)
        Draw(player1basis)

        Draw(p2tank)
        Draw(p2soldier)
        Draw(p2robot)
        Draw(player2basis)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mousex,mousey = pygame.mouse.get_pos()
            if event.type == pygame.KEYUP and event.key == K_ESCAPE:
                movetankdown = False
            if event.type == pygame.MOUSEBUTTONUP:
                CheckDown(player1tank,mousex,mousey)
            pygame.display.update()

    while movesoldier:

        for event in pygame.event.get():
            print(event)
            #makes it possible to use quit the game on the top right
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #receives position of the mouse
            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP and mousex > 60 and mousex < 125 and mousey > 260 and mousey < 320: #move up button
                movesoldier = False
                movesoldierup = True
            if event.type == pygame.MOUSEBUTTONUP and mousex > 0 and mousex < 60 and mousey > 320 and mousey < 390: #move left button
                movesoldier = False
                movesoldierleft = True
            if event.type == pygame.MOUSEBUTTONUP and mousex > 125 and mousex < 175 and mousey > 320 and mousey < 390: #move right button
                movesoldier = False
                movesoldierright = True
            if event.type == pygame.MOUSEBUTTONUP and mousex > 60 and mousex < 125 and mousey > 380 and mousey < 445: #move down button
                movesoldier = False
                movesoldierdown = True
            if event.type == pygame.KEYDOWN:
            #pause the game by clicking either 'escape' or 'p'
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                    pause = True
                    paused()

        #Draw the background on position x,y
        gameDisplay.blit(movebg, (0 ,0))

        #Draw the players turn
        p1Turn, TextRect = text_objects("Player 1's Turn", smallText)
        gameDisplay.blit(p1Turn, (30,0))

        #Draw the amount of moves
        livecounter, TextRect = text_objects("Moves Left:" + str(counter), smallText)
        gameDisplay.blit(livecounter, (35,25))

        #Draw the money of the current player
        playermoney, TextRect = text_objects("Money:" + str(money), smallText)
        gameDisplay.blit(playermoney, (45,50))

        #Draw the helptext
        Pause, TextRect = text_objects("Press Esc or P", smallText)
        gameDisplay.blit(Pause, (1100,660))
        Pause2, TextRect = text_objects("to Pause the game", smallText)
        gameDisplay.blit(Pause2, (1100,680))

        #draw player 1's units
        Draw(p1tank)
        Draw(p1soldier)
        Draw(p1robot)
        Draw(player1basis)

        Draw(p2tank)
        Draw(p2soldier)
        Draw(p2robot)
        Draw(player2basis)

        pygame.display.update()
        clock.tick(60)
        text = "Frequency | FPS: {0:.2f} ".format(clock.get_fps())
        pygame.display.set_caption(text)

    while movesoldierright:
        global player1soldaat, player1robot, player1tank, pause
        #Draw the background on position x,y
        gameDisplay.blit(movebg, (0 ,0))

        #Draw the players turn
        p1Turn, TextRect = text_objects("Player 1's Turn", smallText)
        gameDisplay.blit(p1Turn, (30,0))

        #Draw the amount of moves
        livecounter, TextRect = text_objects("Moves Left:" + str(counter), smallText)
        gameDisplay.blit(livecounter, (35,25))

        #Draw the money of the current player
        playermoney, TextRect = text_objects("Money:" + str(money), smallText)
        gameDisplay.blit(playermoney, (45,50))

        #Draw the instructions
        instr, TextRect = text_objects("Click on the", smallText)
        gameDisplay.blit(instr, (0,100))
        instr2, TextRect = text_objects("Soldier that you", smallText)
        gameDisplay.blit(instr2, (0,120))
        instr3, TextRect = text_objects("wish to move.", smallText)
        gameDisplay.blit(instr3, (0,140))

        #Draw the helptext
        Pause, TextRect = text_objects("Press Esc or P", smallText)
        gameDisplay.blit(Pause, (1100,660))
        Pause2, TextRect = text_objects("to Pause the game", smallText)
        gameDisplay.blit(Pause2, (1100,680))

        #draw player 1's units
        Draw(p1tank)
        Draw(p1soldier)
        Draw(p1robot)
        Draw(player1basis)

        Draw(p2tank)
        Draw(p2soldier)
        Draw(p2robot)
        Draw(player2basis)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mousex,mousey = pygame.mouse.get_pos()
            if event.type == pygame.KEYUP and event.key == K_ESCAPE:
                movesoldierright = False
            if event.type == pygame.MOUSEBUTTONUP:
                CheckRight(player1soldaat,mousex,mousey)
            pygame.display.update()

    while movesoldierleft:
        global player1soldaat, player1robot, player1tank, pause
        #Draw the background on position x,y
        gameDisplay.blit(movebg, (0 ,0))

        #Draw the players turn
        p1Turn, TextRect = text_objects("Player 1's Turn", smallText)
        gameDisplay.blit(p1Turn, (30,0))

        #Draw the amount of moves
        livecounter, TextRect = text_objects("Moves Left:" + str(counter), smallText)
        gameDisplay.blit(livecounter, (35,25))

        #Draw the money of the current player
        playermoney, TextRect = text_objects("Money:" + str(money), smallText)
        gameDisplay.blit(playermoney, (45,50))

        #Draw the instructions
        instr, TextRect = text_objects("Click on the", smallText)
        gameDisplay.blit(instr, (0,100))
        instr2, TextRect = text_objects("Soldier that you", smallText)
        gameDisplay.blit(instr2, (0,120))
        instr3, TextRect = text_objects("wish to move.", smallText)
        gameDisplay.blit(instr3, (0,140))

        #Draw the helptext
        Pause, TextRect = text_objects("Press Esc or P", smallText)
        gameDisplay.blit(Pause, (1100,660))
        Pause2, TextRect = text_objects("to Pause the game", smallText)
        gameDisplay.blit(Pause2, (1100,680))

        #draw player 1's units
        Draw(p1tank)
        Draw(p1soldier)
        Draw(p1robot)
        Draw(player1basis)

        Draw(p2tank)
        Draw(p2soldier)
        Draw(p2robot)
        Draw(player2basis)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mousex,mousey = pygame.mouse.get_pos()
            if event.type == pygame.KEYUP and event.key == K_ESCAPE:
                movesoldierleft = False
            if event.type == pygame.MOUSEBUTTONUP:
                CheckLeft(player1soldaat,mousex,mousey)
            pygame.display.update()

    while movesoldierup:
        global player1soldaat, player1robot, player1tank, pause
        #Draw the background on position x,y
        gameDisplay.blit(movebg, (0 ,0))

        #Draw the players turn
        p1Turn, TextRect = text_objects("Player 1's Turn", smallText)
        gameDisplay.blit(p1Turn, (30,0))

        #Draw the amount of moves
        livecounter, TextRect = text_objects("Moves Left:" + str(counter), smallText)
        gameDisplay.blit(livecounter, (35,25))

        #Draw the money of the current player
        playermoney, TextRect = text_objects("Money:" + str(money), smallText)
        gameDisplay.blit(playermoney, (45,50))

        #Draw the instructions
        instr, TextRect = text_objects("Click on the", smallText)
        gameDisplay.blit(instr, (0,100))
        instr2, TextRect = text_objects("Soldier that you", smallText)
        gameDisplay.blit(instr2, (0,120))
        instr3, TextRect = text_objects("wish to move.", smallText)
        gameDisplay.blit(instr3, (0,140))

        #Draw the helptext
        Pause, TextRect = text_objects("Press Esc or P", smallText)
        gameDisplay.blit(Pause, (1100,660))
        Pause2, TextRect = text_objects("to Pause the game", smallText)
        gameDisplay.blit(Pause2, (1100,680))

        #draw player 1's units
        Draw(p1tank)
        Draw(p1soldier)
        Draw(p1robot)
        Draw(player1basis)

        Draw(p2tank)
        Draw(p2soldier)
        Draw(p2robot)
        Draw(player2basis)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mousex,mousey = pygame.mouse.get_pos()
            if event.type == pygame.KEYUP and event.key == K_ESCAPE:
                movesoldierup = False
            if event.type == pygame.MOUSEBUTTONUP:
                CheckUp(player1soldaat,mousex,mousey)
            pygame.display.update()

    while movesoldierdown:
        global player1soldaat, player1robot, player1tank, pause
        #Draw the background on position x,y
        gameDisplay.blit(movebg, (0 ,0))

        #Draw the players turn
        p1Turn, TextRect = text_objects("Player 1's Turn", smallText)
        gameDisplay.blit(p1Turn, (30,0))

        #Draw the amount of moves
        livecounter, TextRect = text_objects("Moves Left:" + str(counter), smallText)
        gameDisplay.blit(livecounter, (35,25))

        #Draw the money of the current player
        playermoney, TextRect = text_objects("Money:" + str(money), smallText)
        gameDisplay.blit(playermoney, (45,50))

        #Draw the instructions
        instr, TextRect = text_objects("Click on the", smallText)
        gameDisplay.blit(instr, (0,100))
        instr2, TextRect = text_objects("Soldier that you", smallText)
        gameDisplay.blit(instr2, (0,120))
        instr3, TextRect = text_objects("wish to move.", smallText)
        gameDisplay.blit(instr3, (0,140))

        #Draw the helptext
        Pause, TextRect = text_objects("Press Esc or P", smallText)
        gameDisplay.blit(Pause, (1100,660))
        Pause2, TextRect = text_objects("to Pause the game", smallText)
        gameDisplay.blit(Pause2, (1100,680))

        #draw player 1's units
        Draw(p1tank)
        Draw(p1soldier)
        Draw(p1robot)
        Draw(player1basis)

        Draw(p2tank)
        Draw(p2soldier)
        Draw(p2robot)
        Draw(player2basis)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mousex,mousey = pygame.mouse.get_pos()
            if event.type == pygame.KEYUP and event.key == K_ESCAPE:
                movesoldierdown = False
            if event.type == pygame.MOUSEBUTTONUP:
                CheckDown(player1soldaat,mousex,mousey)
            pygame.display.update()

    while moverobot:

        for event in pygame.event.get():
            print(event)
            #makes it possible to use quit the game on the top right
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #receives position of the mouse
            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP and mousex > 60 and mousex < 125 and mousey > 260 and mousey < 320: #move up button
                moverobot = False
                moverobotup = True
            if event.type == pygame.MOUSEBUTTONUP and mousex > 0 and mousex < 60 and mousey > 320 and mousey < 390: #move left button
                moverobot = False
                moverobotleft = True
            if event.type == pygame.MOUSEBUTTONUP and mousex > 125 and mousex < 175 and mousey > 320 and mousey < 390: #move right button
                moverobot = False
                moverobotright = True
            if event.type == pygame.MOUSEBUTTONUP and mousex > 60 and mousex < 125 and mousey > 380 and mousey < 445: #move down button
                moverobot = False
                moverobotdown = True
            if event.type == pygame.KEYDOWN:
            #pause the game by clicking either 'escape' or 'p'
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                    pause = True
                    paused()

        #Draw the background on position x,y
        gameDisplay.blit(movebg, (0 ,0))

        #Draw the players turn
        p1Turn, TextRect = text_objects("Player 1's Turn", smallText)
        gameDisplay.blit(p1Turn, (30,0))

        #Draw the amount of moves
        livecounter, TextRect = text_objects("Moves Left:" + str(counter), smallText)
        gameDisplay.blit(livecounter, (35,25))

        #Draw the money of the current player
        playermoney, TextRect = text_objects("Money:" + str(money), smallText)
        gameDisplay.blit(playermoney, (45,50))

        #Draw the helptext
        Pause, TextRect = text_objects("Press Esc or P", smallText)
        gameDisplay.blit(Pause, (1100,660))
        Pause2, TextRect = text_objects("to Pause the game", smallText)
        gameDisplay.blit(Pause2, (1100,680))

        #draw player 1's units
        Draw(p1tank)
        Draw(p1soldier)
        Draw(p1robot)
        Draw(player1basis)

        Draw(p2tank)
        Draw(p2soldier)
        Draw(p2robot)
        Draw(player2basis)

        pygame.display.update()
        clock.tick(60)
        text = "Frequency | FPS: {0:.2f} ".format(clock.get_fps())
        pygame.display.set_caption(text)

    while moverobotright:
        global player1soldaat, player1robot, player1tank, pause
        #Draw the background on position x,y
        gameDisplay.blit(movebg, (0 ,0))

        #Draw the players turn
        p1Turn, TextRect = text_objects("Player 1's Turn", smallText)
        gameDisplay.blit(p1Turn, (30,0))

        #Draw the amount of moves
        livecounter, TextRect = text_objects("Moves Left:" + str(counter), smallText)
        gameDisplay.blit(livecounter, (35,25))

        #Draw the money of the current player
        playermoney, TextRect = text_objects("Money:" + str(money), smallText)
        gameDisplay.blit(playermoney, (45,50))

        #Draw the instructions
        instr, TextRect = text_objects("Click on the", smallText)
        gameDisplay.blit(instr, (0,100))
        instr2, TextRect = text_objects("Robot that you", smallText)
        gameDisplay.blit(instr2, (0,120))
        instr3, TextRect = text_objects("wish to move.", smallText)
        gameDisplay.blit(instr3, (0,140))

        #Draw the helptext
        Pause, TextRect = text_objects("Press Esc or P", smallText)
        gameDisplay.blit(Pause, (1100,660))
        Pause2, TextRect = text_objects("to Pause the game", smallText)
        gameDisplay.blit(Pause2, (1100,680))

        #draw player 1's units
        Draw(p1tank)
        Draw(p1soldier)
        Draw(p1robot)
        Draw(player1basis)

        Draw(p2tank)
        Draw(p2soldier)
        Draw(p2robot)
        Draw(player2basis)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mousex,mousey = pygame.mouse.get_pos()
            if event.type == pygame.KEYUP and event.key == K_ESCAPE:
                moverobotright = False
            if event.type == pygame.MOUSEBUTTONUP:
                CheckRight(player1robot,mousex,mousey)
            pygame.display.update()

    while moverobotleft:
        global player1soldaat, player1robot, player1tank, pause
        #Draw the background on position x,y
        gameDisplay.blit(movebg, (0 ,0))

        #Draw the players turn
        p1Turn, TextRect = text_objects("Player 1's Turn", smallText)
        gameDisplay.blit(p1Turn, (30,0))

        #Draw the amount of moves
        livecounter, TextRect = text_objects("Moves Left:" + str(counter), smallText)
        gameDisplay.blit(livecounter, (35,25))

        #Draw the money of the current player
        playermoney, TextRect = text_objects("Money:" + str(money), smallText)
        gameDisplay.blit(playermoney, (45,50))

        #Draw the instructions
        instr, TextRect = text_objects("Click on the", smallText)
        gameDisplay.blit(instr, (0,100))
        instr2, TextRect = text_objects("Robot that you", smallText)
        gameDisplay.blit(instr2, (0,120))
        instr3, TextRect = text_objects("wish to move.", smallText)
        gameDisplay.blit(instr3, (0,140))

        #Draw the helptext
        Pause, TextRect = text_objects("Press Esc or P", smallText)
        gameDisplay.blit(Pause, (1100,660))
        Pause2, TextRect = text_objects("to Pause the game", smallText)
        gameDisplay.blit(Pause2, (1100,680))

        #draw player 1's units
        Draw(p1tank)
        Draw(p1soldier)
        Draw(p1robot)
        Draw(player1basis)

        Draw(p2tank)
        Draw(p2soldier)
        Draw(p2robot)
        Draw(player2basis)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mousex,mousey = pygame.mouse.get_pos()
            if event.type == pygame.KEYUP and event.key == K_ESCAPE:
                moverobotleft = False
            if event.type == pygame.MOUSEBUTTONUP:
                CheckLeft(player1robot,mousex,mousey)
            pygame.display.update()

    while moverobotup:
        global player1soldaat, player1robot, player1tank, pause
        #Draw the background on position x,y
        gameDisplay.blit(movebg, (0 ,0))

        #Draw the players turn
        p1Turn, TextRect = text_objects("Player 1's Turn", smallText)
        gameDisplay.blit(p1Turn, (30,0))

        #Draw the amount of moves
        livecounter, TextRect = text_objects("Moves Left:" + str(counter), smallText)
        gameDisplay.blit(livecounter, (35,25))

        #Draw the money of the current player
        playermoney, TextRect = text_objects("Money:" + str(money), smallText)
        gameDisplay.blit(playermoney, (45,50))

        #Draw the instructions
        instr, TextRect = text_objects("Click on the", smallText)
        gameDisplay.blit(instr, (0,100))
        instr2, TextRect = text_objects("Robot that you", smallText)
        gameDisplay.blit(instr2, (0,120))
        instr3, TextRect = text_objects("wish to move.", smallText)
        gameDisplay.blit(instr3, (0,140))

        #Draw the helptext
        Pause, TextRect = text_objects("Press Esc or P", smallText)
        gameDisplay.blit(Pause, (1100,660))
        Pause2, TextRect = text_objects("to Pause the game", smallText)
        gameDisplay.blit(Pause2, (1100,680))

        #draw player 1's units
        Draw(p1tank)
        Draw(p1soldier)
        Draw(p1robot)
        Draw(player1basis)

        Draw(p2tank)
        Draw(p2soldier)
        Draw(p2robot)
        Draw(player2basis)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mousex,mousey = pygame.mouse.get_pos()
            if event.type == pygame.KEYUP and event.key == K_ESCAPE:
                moverobotup = False
            if event.type == pygame.MOUSEBUTTONUP:
                CheckUp(player1soldaat,mousex,mousey)
            pygame.display.update()

    while moverobotdown:
        global player1soldaat, player1robot, player1tank, pause
        #Draw the background on position x,y
        gameDisplay.blit(movebg, (0 ,0))

        #Draw the players turn
        p1Turn, TextRect = text_objects("Player 1's Turn", smallText)
        gameDisplay.blit(p1Turn, (30,0))

        #Draw the amount of moves
        livecounter, TextRect = text_objects("Moves Left:" + str(counter), smallText)
        gameDisplay.blit(livecounter, (35,25))

        #Draw the money of the current player
        playermoney, TextRect = text_objects("Money:" + str(money), smallText)
        gameDisplay.blit(playermoney, (45,50))

        #Draw the instructions
        instr, TextRect = text_objects("Click on the", smallText)
        gameDisplay.blit(instr, (0,100))
        instr2, TextRect = text_objects("Robot that you", smallText)
        gameDisplay.blit(instr2, (0,120))
        instr3, TextRect = text_objects("wish to move.", smallText)
        gameDisplay.blit(instr3, (0,140))

        #Draw the helptext
        Pause, TextRect = text_objects("Press Esc or P", smallText)
        gameDisplay.blit(Pause, (1100,660))
        Pause2, TextRect = text_objects("to Pause the game", smallText)
        gameDisplay.blit(Pause2, (1100,680))

        #draw player 1's units
        Draw(p1tank)
        Draw(p1soldier)
        Draw(p1robot)
        Draw(player1basis)

        Draw(p2tank)
        Draw(p2soldier)
        Draw(p2robot)
        Draw(player2basis)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mousex,mousey = pygame.mouse.get_pos()
            if event.type == pygame.KEYUP and event.key == K_ESCAPE:
                moverobotdown = False
            if event.type == pygame.MOUSEBUTTONUP:
                CheckDown(player1robot,mousex,mousey)
            pygame.display.update()

Main(True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,player1robot,player1tank,player1,player1soldaat,player1barak,player2robot,player2tank,player2,player2soldaat,player2barak)
pygame.quit()
quit()