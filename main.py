import pygame
import os
from Image2 import Image
from character import Character
from graphic_elements import Graphic_elements
from matrix import create_blocks
import time

pygame.init()

screen = pygame.display.set_mode((1080, 720))

background = Image(0,0,1080,720,"\\image\\phone.png")
buttonplay = Image(700, 50, 180, 86, "\\image\\buttonplay1.png")
buttonhelp = Image(700, 302, 180, 86, "\\image\\buttonhelp1.png")
buttonexit = Image(700, 506, 180, 86, "\\image\\buttonexit1.png")
mainchar = Character(300, 604, 21, 48, 3, 5, 20, "\\image\\char.png")



list_block = [
               "0000000000000000000000000000000000000000",
               "0000000000000000000000000000000000000000",
               "0000000000000000000000000000000000000000",
               "0000000000000000000000000000000000000000",
               "0000000000000000000000000000000000000000",
               "0000000000000000000000000000000000000000",
               "0000000000000000000000000000000000000000",
               "0000000000000000000000000000000000000000",
               "0000000000000000000000000000000000000000",
               "0000000000000000000000000000000000000000",
               "0000000000000000000000000000000000000000",
               "0000000000000000000000000000000000000000",
               "0000000000000000000000000000000000000000",
               "0000000000000000000000000000000000000000",
               "0000000000000000000000000000000000000000",
               "0000000000000000000000000000000000000000",
               "0000000000000000000000000000000000000000",
               "0000000000000000000000000000000000000000",
               "0000000000000000000000000000000000000000",
               "0000000000000000000000000000000000000000",
               "0000011111000000000000000000000000000000",
               "0000000000000000000000000000000000000000",
               "0000000000000000011100000000000000000000",
               "1100000000000000011110000000000000000000",
               "0100000000000000000000000000000000000000",
               "0000000000000000000000000000000000000000",
               "3111111111111111111111111111111111111111",
               "3000000000000011000000000000000000000004",
               "3110111011111101000001000000000000000004",
               "3000000100000000100010000000000000001114",
               "3000000000000000011100000000000000010004",
               "3000000000000000000000000000000001000004",
               "3000000000000000000000000000010111100004",
               "3000000000000000000000001111000000000004",
               "3111111100001000000000100000000000000004",
               "3000000000011010000010100000000000000004",
               "3000000000111010101010100000000000000004",
               "3000000001111010101010100000000000000004",
               "3000000111111010101010100000000000000004",
               "5111111111111111111111111111111111111117",
]
list_level = list()
create_blocks(list_block, list_level)
for i in list_level:
    i.load_image()

clock = pygame.time.Clock()
mouse_position = 1
scene = 1
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
        screen.fill((255,255,255))
        for i in list_level:
            i.show_image(screen)
        mainchar.move_character()
        mainchar.gravity()
        mainchar.show_image(screen)
        # mainchar.jump()
        for i in list_level:
            if mainchar.Y_sprite <= i.Y:
                if mainchar.X_sprite + mainchar.Width_sprite >= i.X:
                    if   mainchar.X_sprite <= i.X + i.WIDTH:
                        if mainchar.Y_sprite + mainchar.Height_sprite >= i.Y:
                            mainchar.fall = False
            if mainchar.X_sprite <= i.X + i.WIDTH:
                if mainchar.X_sprite + mainchar.Width_sprite >= i.X:
                    mainchar.move_left = False  
            if mainchar.X_sprite >= i.X + i.WIDTH:
                if mainchar.X_sprite + mainchar.Width_sprite <= i.X:
                    mainchar.move_left = True 
            

    
    
    
    clock.tick(60)
    pygame.display.flip()
    

