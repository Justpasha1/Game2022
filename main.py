import pygame
import os
from Image2 import Image
from character import Character
from graphic_elements import Graphic_elements*

pygame.init()

screen = pygame.display.set_mode((1080, 720))

background = Graphic_elements(0,0,1080,720,"\\image\\phone.png")
buttonplay = Graphic_elements(700, 50, 180, 86, "\\image\\buttonplay1.png")
buttonhelp = Graphic_elements(700, 302, 180, 86, "\\image\\buttonhelp1.png")
buttonexit = Graphic_elements(700, 506, 180, 86, "\\image\\buttonexit1.png")
mainchar = Character(300, 604, 21, 48, "\\image\\char.png")

mainchar.load_image()

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
            mainchar.show_image(screen)

    
    
    
    
    pygame.display.flip()
    
