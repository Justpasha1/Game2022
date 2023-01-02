import pygame
import os
from Image2 import Image
from character import Character
from level import *

pygame.init()

screen = pygame.display.set_mode((1080, 720))
scene = 1
background = Image(0,0,1080,720,"\\image\\phone.png")
buttonplay = Image(690, 53, 180, 86, "\\image\\buttonplay1.png")
buttonhelp = Image(690, 282, 180, 86, "\\image\\buttonhelp1.png")
buttonexit = Image(690, 509, 180, 86, "\\image\\buttonexit1.png")
mainchar = Character(400, 550, 17, 27, 2, 3, 100, "\\image\\char1.png")
oressilver1 = Image(200,600,38,16,"/image/ores/silver.png")
oresemeralds1 = Image(200,600,25,16,"/image/ores/emeralds.png")
oresgold1 = Image(200,600,37,30,"/image/ores/gold.png")
oresiron1 = Image(200,600,35,23,"/image/ores/iron.png")
oresdiamond1 = Image(200,600,32,18,"/image/ores/diamond.png")
bgstart = Image(0,0,1080,720,'\\image\\bg\\bgstart.png')
taverna = Image(400,523,204,152,'\\image\\taverna1.png')
X = Image(taverna.X + taverna.WIDTH/2-25, taverna.Y - 42,40,40,'\\image\\X.png')
list_ores = [oresdiamond1]

for i in list_ores:
    i.load_image()

bgstart.load_image()
taverna.load_image()
clock = pygame.time.Clock()
mouse_position = 1

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if scene == 1:
    #кнопки
            #кнопка play
            if  event.type == pygame.MOUSEMOTION:
                if event.pos[0] > buttonplay.X and event.pos[0] < buttonplay.X + buttonplay.WIDTH and event.pos[1] > buttonplay.Y and event.pos[1] < buttonplay.Y + buttonplay.HEIGHT:
                    buttonplay.PATH = "\\image\\buttonplay2.png"
                    buttonplay.load_image()
                else:
                    buttonplay.PATH = "\\image\\buttonplay1.png"
                    buttonplay.load_image()
                

            #кнопка help
            if  event.type == pygame.MOUSEMOTION:
                if event.pos[0] > buttonhelp.X and event.pos[0] < buttonhelp.X + buttonhelp.WIDTH and event.pos[1] > buttonhelp.Y and event.pos[1] < buttonhelp.Y + buttonhelp.HEIGHT:
                    buttonhelp.PATH = "\\image\\buttonhelp2.png"
                    buttonhelp.load_image()
                else:
                    buttonhelp.PATH = "\\image\\buttonhelp1.png"
                    buttonhelp.load_image()
            
            #кнопка exit
            if  event.type == pygame.MOUSEMOTION:
                if event.pos[0] > buttonexit.X and event.pos[0] < buttonexit.X + buttonexit.WIDTH and event.pos[1] > buttonexit.Y and event.pos[1] < buttonexit.Y + buttonexit.HEIGHT:
                    buttonexit.PATH = "\\image\\buttonexit2.png"
                    buttonexit.load_image()
                else:
                    buttonexit.PATH = "\\image\\buttonexit1.png"
                    buttonexit.load_image()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.pos[0] > buttonplay.X and event.pos[0] < buttonplay.X + buttonplay.WIDTH and event.pos[1] > buttonplay.Y and event.pos[1] < buttonplay.Y + buttonplay.HEIGHT:
                    scene = 2
                if event.pos[0] > buttonhelp.X and event.pos[0] < buttonhelp.X + buttonhelp.WIDTH and event.pos[1] > buttonhelp.Y and event.pos[1] < buttonhelp.Y + buttonhelp.HEIGHT:
                    scene = 3
                if event.pos[0] > buttonexit.X and event.pos[0] < buttonexit.X + buttonexit.WIDTH and event.pos[1] > buttonexit.Y and event.pos[1] < buttonexit.Y + buttonexit.HEIGHT:
                    game = False
            background.show_image(screen)
            buttonplay.show_image(screen)
            buttonhelp.show_image(screen)
            buttonexit.show_image(screen)
    if scene == 2:
        bgstart.show_image(screen)
        for i in list_ores:
            i.show_image(screen)
        for i in list_levelstart:
            i.show_image(screen)
        taverna.show_image(screen)
        mainchar.move_character(list_levelstart)
        mainchar.ores_collision(list_ores)
        mainchar.taverna(X,taverna,screen,scen=scene)
        mainchar.show_image(screen)
    if scene == 3:
        screen.fill((0,0,0))
        
    
    clock.tick(60)
    pygame.display.flip()