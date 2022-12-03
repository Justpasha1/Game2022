import pygame
import os

pygame.init()

from b_g import Background
from Image2 import Image

screen = pygame.display.set_mode((1080, 720))
background = Background(0,0,1080,720,"/image/phone.png")

buttonplay = Image(900, 100, 160, 72, "\\image\\buttonplay1.png")
buttonhelp = Image(900, 202, 160, 72, "\\image\\buttonhelp1.png")
buttonexit = Image(900, 306, 160, 72, "\\image\\buttonexit1.png")
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    buttonplay.show_image(screen)
    
    
    
    pygame.display.flip()
    

