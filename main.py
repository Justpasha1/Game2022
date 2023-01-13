# Налаштування гри та підгрузка класів
    # Підлкючення бібліотек
import pygame
import os
from Image2 import Image
from character import Character
from level import *
from text import Text
from ores import Ores
from values import *
    # Ініціалізуємо pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()
    # Налаштування вікна
screen = pygame.display.set_mode((1080, 720))
font = pygame.font.SysFont('Comic Sans MS', 27)
pygame.display.set_caption('Unknown Depths')
    #Налаштування гри
menu = None
clock = pygame.time.Clock()
mouse_position = 1
scene = 1
game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        # Меню
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
                    mainchar.X_sprite = 20
                    mainchar.Y_sprite = 720 - 27 * 3
                    buttonsound.play(1)
                if event.pos[0] > buttonhelp.X and event.pos[0] < buttonhelp.X + buttonhelp.WIDTH and event.pos[1] > buttonhelp.Y and event.pos[1] < buttonhelp.Y + buttonhelp.HEIGHT:
                    scene = 3
                    buttonsound.play(1)
                if event.pos[0] > buttonexit.X and event.pos[0] < buttonexit.X + buttonexit.WIDTH and event.pos[1] > buttonexit.Y and event.pos[1] < buttonexit.Y + buttonexit.HEIGHT:
                    buttonsound.play(1)
                    game = False
            background.show_image(screen)
            buttonplay.show_image(screen)
            buttonhelp.show_image(screen)
            buttonexit.show_image(screen)
        # Таверна
        if scene == 3:
            if event.type == pygame.MOUSEBUTTONUP:
                if event.pos[0] > buttonsell.X and event.pos[0] < buttonsell.X + buttonsell.WIDTH and event.pos[1] > buttonsell.Y and event.pos[1] < buttonsell.Y + buttonsell.HEIGHT:
                    menu = 'sell'
                    buttonsound.play(1)
                if event.pos[0] > buttonbuy.X and event.pos[0] < buttonbuy.X + buttonbuy.WIDTH and event.pos[1] > buttonbuy.Y and event.pos[1] < buttonbuy.Y + buttonbuy.HEIGHT:
                    menu = 'buy'
                    buttonsound.play(1)
            

            keys = pygame.key.get_pressed()
            # screen.fill((0,0,0))
            tavernabg.show_image(screen)
            Esc.show_image(screen)
            buttonsell.show_image(screen)
            buttonbuy.show_image(screen)
            coin6.show_image(screen)
            
            monyewehave.TEXT = str(mainchar.coin)
            monyewehave.load_text()
            monyewehave.show_text(screen)
            if menu == 'sell':
                sellall.show_image(screen)
                diamondcount.TEXT = str(mainchar.diamond)
                emeraldscount.TEXT = str(mainchar.emeralds)
                goldcount.TEXT = str(mainchar.gold)
                silvercount.TEXT = str(mainchar.silver)
                ironcount.TEXT = str(mainchar.iron)
                buttonsell.PATH = '\\image\\taverna\\sell2.png'
                buttonbuy.PATH = '\\image\\taverna\\buy1.png'
                buttonbuy.load_image()
                buttonsell.load_image()
                buttonsellemeralds.show_image(screen)
                buttonselldiamond.show_image(screen)
                buttonsellgold.show_image(screen)
                buttonselliron.show_image(screen)
                buttonsellsilver.show_image(screen)
                diamondprice.show_text(screen)
                emeraldsprice.show_text(screen)
                goldprice.show_text(screen)
                ironprice.show_text(screen)
                silverprice.show_text(screen)
                diamondcount.load_text()
                diamondcount.show_text(screen)
                emeraldscount.load_text()
                emeraldscount.show_text(screen)
                goldcount.load_text()
                goldcount.show_text(screen)
                silvercount.load_text()
                silvercount.show_text(screen)
                ironcount.load_text()
                ironcount.show_text(screen)
                for i in list_coin:
                    i.show_image(screen)
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.pos[0] > buttonselldiamond.X and event.pos[0] < buttonselldiamond.X + buttonselldiamond.WIDTH and event.pos[1] > buttonselldiamond.Y and event.pos[1] < buttonselldiamond.Y + buttonselldiamond.HEIGHT:
                        if mainchar.diamond > 0:
                            mainchar.diamond -= 1
                            mainchar.coin += 4
                            buttonsound.play(1)
                    if event.pos[0] > buttonsellemeralds.X and event.pos[0] < buttonsellemeralds.X + buttonsellemeralds.WIDTH and event.pos[1] > buttonsellemeralds.Y and event.pos[1] < buttonsellemeralds.Y + buttonsellemeralds.HEIGHT:
                        if mainchar.emeralds > 0:
                            mainchar.emeralds -= 1
                            mainchar.coin += 5
                            buttonsound.play(1)
                    if event.pos[0] > buttonsellgold.X and event.pos[0] < buttonsellgold.X + buttonsellgold.WIDTH and event.pos[1] > buttonsellgold.Y and event.pos[1] < buttonsellgold.Y + buttonsellgold.HEIGHT:
                        if mainchar.gold > 0:
                            mainchar.gold -= 1
                            mainchar.coin += 3
                            buttonsound.play(1)
                    if event.pos[0] > buttonsellsilver.X and event.pos[0] < buttonsellsilver.X + buttonsellsilver.WIDTH and event.pos[1] > buttonsellsilver.Y and event.pos[1] < buttonsellsilver.Y + buttonsellsilver.HEIGHT:
                        if mainchar.silver > 0:
                            mainchar.silver -= 1
                            mainchar.coin += 2
                            buttonsound.play(1)
                    if event.pos[0] > buttonselliron.X and event.pos[0] < buttonselliron.X + buttonselliron.WIDTH and event.pos[1] > buttonselliron.Y and event.pos[1] < buttonselliron.Y + buttonselliron.HEIGHT:
                        if mainchar.iron > 0:
                            mainchar.iron -= 1
                            mainchar.coin += 1
                            buttonsound.play(1)
                    if event.pos[0] > sellall.X and event.pos[0] < sellall.X + sellall.WIDTH and event.pos[1] > sellall.Y and event.pos[1] < sellall.Y + sellall.HEIGHT:
                        if mainchar.iron > 0:
                            mainchar.coin += 1 * mainchar.iron
                            mainchar.iron = 0
                        if mainchar.silver > 0:
                            mainchar.coin += 2 * mainchar.silver
                            mainchar.silver = 0
                        if mainchar.gold > 0:
                            mainchar.coin += 3 * mainchar.gold
                            mainchar.gold = 0
                        if mainchar.diamond > 0:
                            mainchar.coin += 4 * mainchar.diamond
                            mainchar.diamond = 0
                        if mainchar.emeralds > 0:
                            mainchar.coin += 5 * mainchar.emeralds
                            mainchar.emeralds = 0
                        buttonsound.play(1)
            if menu == 'buy':
                buttonsell.PATH = '\\image\\taverna\\sell1.png'
                buttonbuy.PATH = '\\image\\taverna\\buy2.png'
                buttonbuy.load_image()
                buttonsell.load_image()
                heartupgrade.show_image(screen)
                coin7.show_image(screen)
                if mainchar.hp_max == 3:
                    heartupgradeprice.TEXT = '40'
                    heartupgradeprice.load_text()
                if mainchar.hp_max == 4:
                    heartupgradeprice.TEXT = '70'
                    heartupgradeprice.load_text()
                heartupgradeprice.show_text(screen)
            mainchar.leave_taverna()
            if mainchar.can_entern_taverna != True:
                scene = 2
    keys = pygame.key.get_pressed()
    # Місто
    if scene == 2:
        bgstart.show_image(screen)
        for i in list_levelstart:
            i.show_image(screen)
        taverna.show_image(screen)
        caveenterbottom.show_image(screen)
        mainchar.move_character(list_levelstart,walk_sound)
        mainchar.taverna(X,taverna,screen)

        if mainchar.can_entern_taverna:
            scene = 3
        mainchar.show_image(screen)
        caveentertop.show_image(screen)
        if mainchar.X_sprite >= 1050:
            mainchar.X_sprite = 25
            mainchar.Y_sprite = 27*2
            scene = 4
    # Печера
        # 1 рівень
    if scene == 4:
        cavebg.show_image(screen)
        for i in list_level_1:
            i.show_image(screen)
        for i in list_ores1:
            if i.X > -100:
                i.show_image(screen)
        mainchar.move_character(list_level_1,walk_sound)
        mainchar.ores_collision(list_ores1)
        mainchar.show_hp(screen)
        rope.show_image(screen)
        mainchar.show_image(screen)
        # print(mainchar.X_sprite,mainchar.Y_sprite)
        if mainchar.X_sprite >= 1050:
            mainchar.Y_sprite = 432
            mainchar.X_sprite = 20
            scene= 5
        if mainchar.X_sprite <= 20 and mainchar.Y_sprite <= 200:
            mainchar.X_sprite = 900
            mainchar.Y_sprite = 720 - 27*3
            scene = 2
        if mainchar.hp == 0:
            scene = 11
        if keys[pygame.K_x] and mainchar.hp > 0:
            mainchar.X_sprite = 900
            mainchar.Y_sprite = 720 - 27*3
            scene = 2
        # 2 рівень   
    if scene == 5:
        cavebg.show_image(screen)
        for i in list_level_2:
            i.show_image(screen)
        for i in list_ores2:
            if i.X > -100:
                i.show_image(screen)
        mainchar.move_character(list_level_2,walk_sound)
        mainchar.ores_collision(list_ores2)
        mainchar.show_hp(screen)
        rope.show_image(screen)
        mainchar.show_image(screen)
        Mouse_x, Mouse_y = pygame.mouse.get_pos()
        print(Mouse_x,Mouse_y)

        # print(mainchar.X_sprite,mainchar.Y_sprite)
        if mainchar.X_sprite <= 15:
            mainchar.X_sprite = 1041
            mainchar.Y_sprite = 420
            scene = 4

        if mainchar.Y_sprite >= 720:
            scene = 6
            mainchar.X_sprite = 951
            mainchar.Y_sprite = 20
        if mainchar.X_sprite >= 1079:
            mainchar.X_sprite = 48
            mainchar.Y_sprite = 39
            scene = 8
        if mainchar.hp == 0:
            scene = 11
        if keys[pygame.K_x] and mainchar.hp > 0:
            mainchar.X_sprite = 900
            mainchar.Y_sprite = 720 - 27*3
            scene = 2
        # 3 рівень
    if scene == 6:
        cavebg.show_image(screen)
        for i in list_level_3:
            i.show_image(screen)
        for i in list_ores3:
            if i.X > -100:
                i.show_image(screen)
        mainchar.move_character(list_level_3,walk_sound)
        mainchar.ores_collision(list_ores3)
        mainchar.show_hp(screen)
        rope.show_image(screen)
        mainchar.show_image(screen)
        Mouse_x, Mouse_y = pygame.mouse.get_pos()
        print(Mouse_x,Mouse_y)
        if mainchar.Y_sprite <= 14:
            mainchar.X_sprite = 930
            mainchar.Y_sprite = 663
            scene = 5
        if mainchar.X_sprite >= 1074:
            mainchar.X_sprite = 42
            mainchar.Y_sprite = 660
            scene = 7
        if mainchar.X_sprite <= 20:
            mainchar.X_sprite = 1047
            mainchar.Y_sprite = 150
            scene = 9
        if mainchar.hp == 0:
            scene = 11
        if keys[pygame.K_x] and mainchar.hp > 0:
            mainchar.X_sprite = 900
            mainchar.Y_sprite = 720 - 27*3
            scene = 2
        # 4 рівень
    if scene == 7:
        cavebg.show_image(screen)
        for i in list_level_4:
            i.show_image(screen)
        for i in list_ores4:
            if i.X > -100:
                i.show_image(screen)
        mainchar.move_character(list_level_4,walk_sound)
        mainchar.ores_collision(list_ores4)
        mainchar.show_hp(screen)
        rope.show_image(screen)
        mainchar.show_image(screen)
        Mouse_x, Mouse_y = pygame.mouse.get_pos()
        print(Mouse_x,Mouse_y)
        if mainchar.X_sprite <= 12:
            mainchar.X_sprite = 1044
            mainchar.Y_sprite = 663
            scene = 6
        if mainchar.Y_sprite <= 14:
            mainchar.X_sprite = 405
            mainchar.Y_sprite = 666
            scene = 8
        if mainchar.hp == 0:
            scene = 11
        if keys[pygame.K_x] and mainchar.hp > 0:
            mainchar.X_sprite = 900
            mainchar.Y_sprite = 720 - 27*3
            scene = 2
        # 5 рівень
    if scene == 8:
        cavebg.show_image(screen)
        for i in list_level_5:
            i.show_image(screen)
        for i in list_ores5:
            if i.X > -100:
                i.show_image(screen)
        mainchar.move_character(list_level_5,walk_sound)
        mainchar.ores_collision(list_ores5)
        mainchar.show_hp(screen)
        rope.show_image(screen)
        mainchar.show_image(screen)
        Mouse_x, Mouse_y = pygame.mouse.get_pos()
        print(Mouse_x,Mouse_y)
        if mainchar.X_sprite <=15:
            mainchar.X_sprite = 1059
            mainchar.Y_sprite = 30
            scene = 5
        if mainchar.Y_sprite >= 720:
            mainchar.X_sprite = 302
            mainchar.Y_sprite = 21
            scene = 7
        if mainchar.hp == 0:
            scene = 11
        if keys[pygame.K_x] and mainchar.hp > 0:
            mainchar.X_sprite = 900
            mainchar.Y_sprite = 720 - 27*3
            scene = 2
        # 6 рівень 
    if scene == 9:
        grassbg.show_image(screen)
        for i in list_level_6:
            i.show_image(screen)
        for i in list_ores6:
            if i.X > -100:
                i.show_image(screen)
        mainchar.move_character(list_level_6,walk_sound)
        mainchar.ores_collision(list_ores6)
        mainchar.show_hp(screen)
        rope.show_image(screen)
        mainchar.show_image(screen)
        Mouse_x, Mouse_y = pygame.mouse.get_pos()
        print(Mouse_x,Mouse_y)
        if mainchar.X_sprite >= 1074:
            mainchar.X_sprite = 42
            mainchar.Y_sprite = 144
            scene = 6
        if mainchar.Y_sprite >= 720:
            mainchar.X_sprite = 828
            mainchar.Y_sprite = 61
            scene = 10
        if mainchar.hp == 0:
            scene = 11
        if keys[pygame.K_x] and mainchar.hp > 0:
            mainchar.X_sprite = 900
            mainchar.Y_sprite = 720 - 27*3
            scene = 2
        # 7 рівень
    if scene == 10:
        grassbg.show_image(screen)
        for i in list_level_7:
            i.show_image(screen)
        for i in list_ores7:
            if i.X > -100:
                i.show_image(screen)
        mainchar.move_character(list_level_7,walk_sound)
        mainchar.ores_collision(list_ores7)
        mainchar.show_hp(screen)
        rope.show_image(screen)
        mainchar.show_image(screen)
        if mainchar.Y_sprite <= 6:
            mainchar.X_sprite = 792
            mainchar.Y_sprite = 663
            scene = 9
        if mainchar.hp == 0:
            scene = 11
        if mainchar.X_sprite>= 1075:
            mainchar.X_sprite = 50
            mainchar.Y_sprite = 30
            scene = 12
        if keys[pygame.K_x] and mainchar.hp > 0:
            mainchar.X_sprite = 900
            mainchar.Y_sprite = 720 - 27*3
            scene = 2
        # кінцівка з сердцем
    if scene == 12:
        grassbg.show_image(screen)
        for i in list_level_final:
            i.show_image(screen)
        heart.show_image(screen)
        
        mainchar.move_character(list_level_final,walk_sound)
        mainchar.show_image(screen)
    # меню смерті
    if scene == 11:
        buttonplay.X = 860
        buttonexit.X = 860
        buttonplay.Y = 230
        buttonexit.Y = 430
        deathbg.show_image(screen)
        for event in pygame.event.get():
            if  event.type == pygame.MOUSEMOTION:
                if event.pos[0] > buttonplay.X and event.pos[0] < buttonplay.X + buttonplay.WIDTH and event.pos[1] > buttonplay.Y and event.pos[1] < buttonplay.Y + buttonplay.HEIGHT:
                    buttonplay.PATH = "\\image\\buttonplay2.png"
                    buttonplay.load_image()
                else:
                    buttonplay.PATH = "\\image\\buttonplay1.png"
                    buttonplay.load_image()
                if event.pos[0] > buttonexit.X and event.pos[0] < buttonexit.X + buttonexit.WIDTH and event.pos[1] > buttonexit.Y and event.pos[1] < buttonexit.Y + buttonexit.HEIGHT:
                    buttonexit.PATH = "\\image\\buttonexit2.png"
                    buttonexit.load_image()
                else:
                    buttonexit.PATH = "\\image\\buttonexit1.png"
                    buttonexit.load_image()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.pos[0] > buttonplay.X and event.pos[0] < buttonplay.X + buttonplay.WIDTH and event.pos[1] > buttonplay.Y and event.pos[1] < buttonplay.Y + buttonplay.HEIGHT:
                    scene = 2
                    mainchar.X_sprite = 20
                    mainchar.Y_sprite = 720 - 27 * 3
                    mainchar.coin = 0
                    mainchar.diamond = 0
                    mainchar.emeralds = 0
                    mainchar.gold = 0
                    mainchar.silver = 0 
                    mainchar.iron = 0
                    buttonsound.play(1)
                if event.pos[0] > buttonexit.X and event.pos[0] < buttonexit.X + buttonexit.WIDTH and event.pos[1] > buttonexit.Y and event.pos[1] < buttonexit.Y + buttonexit.HEIGHT:
                    buttonsound.play(1)
                    game = False
        buttonplay.show_image(screen)
        buttonexit.show_image(screen)
    
    clock.tick(60)
    pygame.display.flip()