import pygame
import os
from Image2 import Image
from character import Character
from level import *
from text import Text
from ores import Ores

pygame.init()
pygame.font.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1080, 720))
font = pygame.font.SysFont('Comic Sans MS', 27)

background = Image(0,0,1080,720,"\\image\\phone.png")
buttonplay = Image(690, 53, 180, 86, "\\image\\buttonplay1.png")
buttonhelp = Image(690, 282, 180, 86, "\\image\\buttonhelp1.png")
buttonexit = Image(690, 509, 180, 86, "\\image\\buttonexit1.png")
mainchar = Character(400, 550, 17, 27, 4, 5, 27*2+7, "\\image\\char1.png")
oressilver1 = Ores(200,600,38,16,"/image/ores/silver.png",'silver')
oresemeralds1 = Ores(200,600,25,16,"/image/ores/emeralds.png",'emerald')
oresgold1 = Ores(200,600,37,30,"/image/ores/gold.png",'gold')
oresiron1 = Ores(200,600,35,23,"/image/ores/iron.png",'iron')
oresdiamond1 = Ores(200,600,32,18,"/image/ores/diamond.png",'diamond')
bgstart = Image(0,0,1080,720,'\\image\\bg\\bgstart.png')
taverna = Image(400,523,204,152,'\\image\\taverna1.png')
tavernabg = Image(0,0,1080,720,'\\image\\bg\\tavernabg.png')
X = Image(taverna.X + taverna.WIDTH/2-25, taverna.Y - 42,40,40,'\\image\\X.png')
Esc = Image(10,10,40,40,'\\image\\Esc.png')
buttonsell = Image(560, 400, 47*3,18*3,'\\image\\taverna\\sell1.png')
buttonbuy = Image(560+47*3+20,400,47*3,18*3,'\\image\\taverna\\buy1.png')
buttonselldiamond = Image(500, 60, 40*3,40*3,'\\image\\taverna\\diamondsell.png')
buttonsellemeralds = Image(700, 60, 40*3,40*3,'\\image\\taverna\\emeraldssell.png')
buttonsellgold = Image(900, 60, 40*3,40*3,'\\image\\taverna\\goldsell.png')
buttonselliron = Image(600, 230, 40*3,40*3,'\\image\\taverna\\ironsell.png')
buttonsellsilver = Image(800, 230, 40*3,40*3,'\\image\\taverna\\silversell.png')
coin1 = Image(buttonselldiamond.X,buttonselldiamond.Y+buttonselldiamond.HEIGHT,27,27,'\\image\\taverna\\coin.png')
coin2 = Image(buttonsellemeralds.X,buttonsellemeralds.Y+buttonsellemeralds.HEIGHT,27,27,'\\image\\taverna\\coin.png')
coin3 = Image(buttonsellgold.X,buttonsellgold.Y+buttonsellgold.HEIGHT,27,27,'\\image\\taverna\\coin.png')
coin4 = Image(buttonselliron.X,buttonselliron.Y+buttonselliron.HEIGHT,27,27,'\\image\\taverna\\coin.png')
coin5 = Image(buttonsellsilver.X,buttonsellsilver.Y+buttonsellsilver.HEIGHT,27,27,'\\image\\taverna\\coin.png')
coin6 = Image(buttonbuy.X + buttonbuy.WIDTH + 10, buttonbuy.Y + 12,27, 27,'\\image\\taverna\\coin.png')
sellall = Image(buttonsellemeralds.X,0,40*3,20*3,'\\image\\taverna\\sellall.png')
caveentertop = Image(1018,549,62,127,'\\image\\caveentertop.png')
caveenterbottom = Image(1018,608,25,68,'\\image\\caveenterbottom.png')
cavebg = Image(0,0,1080,720,'\\image\\bg\\cavebg.png')
list_coin = [coin1,coin2,coin3,coin4,coin5]
list_ores = [oresdiamond1]

buttonsound = pygame.mixer.Sound(os.path.abspath(__file__ + "/..") +'\\sounds\\buttonpressed.wav')
walk_sound = pygame.mixer.Sound(os.path.abspath(__file__ + "/..") +'\\sounds\\step.wav')

diamondprice = Text(coin2.X+coin2.WIDTH+5,coin2.Y,27,'arial','5',(0,0,0))
emeraldsprice = Text(coin1.X+coin1.WIDTH+5,coin1.Y,27,'arial','4',(0,0,0))
goldprice = Text(coin3.X+coin3.WIDTH+5,coin3.Y,27,'arial','3',(0,0,0))
silverprice = Text(coin5.X+coin5.WIDTH+5,coin5.Y,27,'arial','2',(0,0,0))
ironprice = Text(coin4.X+coin4.WIDTH+5,coin4.Y,27,'arial','1',(0,0,0))

diamondcount = Text(buttonselldiamond.X+buttonselldiamond.WIDTH//2-10,buttonselldiamond.Y,27,'arial',str(mainchar.diamond),(0,0,0))
emeraldscount = Text(buttonsellemeralds.X+buttonsellemeralds.WIDTH//2-10,buttonsellemeralds.Y,27,'arial',str(mainchar.emeralds),(0,0,0))
goldcount = Text(buttonsellgold.X+buttonsellgold.WIDTH//2-10,buttonsellgold.Y,27,'arial',str(mainchar.gold),(0,0,0))
silvercount = Text(buttonsellsilver.X+buttonsellsilver.WIDTH//2-10,buttonsellsilver.Y,27,'arial',str(mainchar.silver),(0,0,0))
ironcount = Text(buttonselliron.X+buttonselliron.WIDTH//2-10,buttonselliron.Y,27,'arial',str(mainchar.iron),(0,0,0))
monyewehave = Text(coin6.X+coin6.WIDTH + 5,coin6.Y,27,'arial',str(mainchar.coin),(0,0,0))

# 

for i in list_ores:
    i.load_image()
for i in list_coin:
    i.load_image()
coin6.load_image()
cavebg.load_image()
caveenterbottom.load_image()
caveentertop.load_image()
diamondprice.load_text()
emeraldsprice.load_text()
goldprice.load_text()
silverprice.load_text()
ironprice.load_text()
sellall.load_image()
buttonsellemeralds.load_image()
buttonselldiamond.load_image()
buttonsellgold.load_image()
buttonselliron.load_image()
buttonsellsilver.load_image()
buttonbuy.load_image()
buttonsell.load_image()
tavernabg.load_image()
bgstart.load_image()
taverna.load_image()
Esc.load_image()

menu = None
clock = pygame.time.Clock()
mouse_position = 1
scene = 9
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
            mainchar.leave_taverna()
            if mainchar.can_entern_taverna != True:
                scene = 2
    
    if scene == 2:
        bgstart.show_image(screen)
        for i in list_ores:
            i.show_image(screen)
        for i in list_levelstart:
            i.show_image(screen)
        taverna.show_image(screen)
        caveenterbottom.show_image(screen)
        mainchar.move_character(list_levelstart,walk_sound)
        mainchar.ores_collision(list_ores)
        mainchar.taverna(X,taverna,screen)

        if mainchar.can_entern_taverna:
            scene = 3
        mainchar.show_image(screen)
        caveentertop.show_image(screen)
        if mainchar.X_sprite >= 1050:
            mainchar.X_sprite = 20
            mainchar.Y_sprite = 27*2
            scene = 4
            
    if scene == 4:
        cavebg.show_image(screen)
        for i in list_level_1:
            i.show_image(screen)
        mainchar.move_character(list_level_1,walk_sound)
        mainchar.show_hp(screen)
        mainchar.show_image(screen)
        # print(mainchar.X_sprite,mainchar.Y_sprite)
        Mouse_x, Mouse_y = pygame.mouse.get_pos()
        print(Mouse_x,Mouse_y)
        if mainchar.X_sprite >= 1050:
            mainchar.Y_sprite = 432
            mainchar.X_sprite = 20
            scene= 5
            
    if scene == 5:
        cavebg.show_image(screen)
        for i in list_level_2:
            i.show_image(screen)
        mainchar.move_character(list_level_2,walk_sound)
        mainchar.show_hp(screen)
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
    if scene == 6:
        cavebg.show_image(screen)
        for i in list_level_3:
            i.show_image(screen)
        mainchar.move_character(list_level_3,walk_sound)
        mainchar.show_hp(screen)
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
    if scene == 7:
        cavebg.show_image(screen)
        for i in list_level_4:
            i.show_image(screen)
        mainchar.move_character(list_level_4,walk_sound)
        mainchar.show_hp(screen)
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
    if scene == 8:
        cavebg.show_image(screen)
        for i in list_level_5:
            i.show_image(screen)
        mainchar.move_character(list_level_5,walk_sound)
        mainchar.show_hp(screen)
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
    if scene == 9:
        cavebg.show_image(screen)
        for i in list_level_6:
            i.show_image(screen)
        mainchar.move_character(list_level_6,walk_sound)
        mainchar.show_hp(screen)
        mainchar.show_image(screen)
        Mouse_x, Mouse_y = pygame.mouse.get_pos()
        print(Mouse_x,Mouse_y)
        if mainchar.X_sprite >= 1074:
            mainchar.X_sprite = 42
            mainchar.Y_sprite = 144
            scene = 6
    clock.tick(60)
    pygame.display.flip()