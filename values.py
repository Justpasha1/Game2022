from Image2 import Image
from character import Character
from text import Text
from ores import Ores
import pygame
import os



# Створення всіх об'єктів та гравця в грі
    # Фони гри
background = Image(0,0,1080,720,"\\image\\phonee.png")
mainchar = Character(400, 550, 20, 27, 4, 5, 27*2+7, "\\image\\char1.png")
tavernabg = Image(0,0,1080,720,'\\image\\bg\\tavernabg.png')
bgstart = Image(0,0,1080,720,'\\image\\bg\\bgstart.png')
cavebg = Image(0,0,1080,720,'\\image\\bg\\cavebg.png')
grassbg = Image(0,0,1080,720,'\\image\\bg\\grassbg.png')
deathbg = Image(0,0,1080,720,'\\image\\bg\\dethbg.png')

    # Кнопки гри
        # Кнопки меню
buttonplay = Image(690, 53, 180, 86, "\\image\\buttonplay1.png")
buttonhelp = Image(690, 282, 180, 86, "\\image\\buttonhelp1.png")
buttonexit = Image(690, 509, 180, 86, "\\image\\buttonexit1.png")
        # Кнопки таверни
buttonsell = Image(560, 400, 47*3,18*3,'\\image\\taverna\\sell1.png')
buttonbuy = Image(560+47*3+20,400,47*3,18*3,'\\image\\taverna\\buy1.png')
buttonselldiamond = Image(500, 60, 40*3,40*3,'\\image\\taverna\\diamondsell.png')
buttonsellemeralds = Image(700, 60, 40*3,40*3,'\\image\\taverna\\emeraldssell.png')
buttonsellgold = Image(900, 60, 40*3,40*3,'\\image\\taverna\\goldsell.png')
buttonselliron = Image(600, 230, 40*3,40*3,'\\image\\taverna\\ironsell.png')
buttonsellsilver = Image(800, 230, 40*3,40*3,'\\image\\taverna\\silversell.png')
heartupgrade = Image(620, 60,39*5,45*5,'\\image\\hearts\\heartupgrade.png')
sellall = Image(buttonsellemeralds.X,0,40*3,20*3,'\\image\\taverna\\sellall.png')

# Текстури для переходів

heart = Image(359,27,588,675,'\\image\\heart.png')
taverna = Image(400,523,204,152,'\\image\\taverna1.png')
caveentertop = Image(1018,549,62,127,'\\image\\caveentertop.png')
caveenterbottom = Image(1018,608,25,68,'\\image\\caveenterbottom.png')

# Текстури кнопок

X = Image(taverna.X + taverna.WIDTH/2-25, taverna.Y - 42,40,40,'\\image\\X.png')
Esc = Image(10,10,40,40,'\\image\\Esc.png')

# Всі монети

coin1 = Image(buttonselldiamond.X,buttonselldiamond.Y+buttonselldiamond.HEIGHT,27,27,'\\image\\taverna\\coin.png')
coin2 = Image(buttonsellemeralds.X,buttonsellemeralds.Y+buttonsellemeralds.HEIGHT,27,27,'\\image\\taverna\\coin.png')
coin3 = Image(buttonsellgold.X,buttonsellgold.Y+buttonsellgold.HEIGHT,27,27,'\\image\\taverna\\coin.png')
coin4 = Image(buttonselliron.X,buttonselliron.Y+buttonselliron.HEIGHT,27,27,'\\image\\taverna\\coin.png')
coin5 = Image(buttonsellsilver.X,buttonsellsilver.Y+buttonsellsilver.HEIGHT,27,27,'\\image\\taverna\\coin.png')
coin6 = Image(buttonbuy.X + buttonbuy.WIDTH + 10, buttonbuy.Y + 12,27, 27,'\\image\\taverna\\coin.png')
coin7 = Image(heartupgrade.X +20,heartupgrade.Y+heartupgrade.HEIGHT+20,27*2,27*2,'\\image\\taverna\\coin.png')
list_coin = [coin1,coin2,coin3,coin4,coin5]
heartupgradeprice = Text(coin7.X + coin7.WIDTH + 5,coin7.Y -3,27*2,'arial','15',(0,0,0))

# Текстури для рівнів

rope = Image(50, 2,50,50,'\\image\\rope.png')

# Всі руди

oresiron1 = Ores(348,139,35,23,"/image/ores/iron.png",'iron')
oresiron2 = Ores(899,193,35,23,"/image/ores/iron.png",'iron')
oresiron3 = Ores(613,382,35,23,"/image/ores/iron.png",'iron')
oresiron4 = Ores(106,490,35,23,"/image/ores/iron.png",'iron')
oressilver1 = Ores(891,687,38,16,"/image/ores/silver.png",'silver')
oressilver2 = Ores(180,227,38,16,"/image/ores/silver.png",'silver')
oresgold1 = Ores(341,402,37,30,"/image/ores/gold.png",'gold')
oresgold2 = Ores(597,565,37,30,"/image/ores/gold.png",'gold')
list_ores1 = [oresiron1,oresiron2,oresiron3,oresiron4,oressilver1,oressilver2,oresgold1,oresgold2]

oresiron5 = Ores(570,680,35,23,"/image/ores/iron.png",'iron')
oresiron6 = Ores(468,436,35,23,"/image/ores/iron.png",'iron')
oresiron7 = Ores(825,112,35,23,"/image/ores/iron.png",'iron')
oressilver3 = Ores(293,92,38,16,"/image/ores/silver.png",'silver')
oressilver4 = Ores(840,254,38,16,"/image/ores/silver.png",'silver')
oressilver5 = Ores(193,524,38,16,"/image/ores/silver.png",'silver')
oresgold3 = Ores(460,240,37,30,"/image/ores/gold.png",'gold')
oresgold4 = Ores(880,510,37,30,"/image/ores/gold.png",'gold')
oresgold5 = Ores(798,673,37,30,"/image/ores/gold.png",'gold')
oresdiamond1 = Ores(53,225,32,18,"/image/ores/diamond.png",'diamond')
oresdiamond2 = Ores(102,685,32,18,"/image/ores/diamond.png",'diamond')
list_ores2 = [oresiron5,oresiron6,oresiron7,oressilver3,oressilver4,oressilver5,oresgold3,oresgold4,oresgold5,oresdiamond1,oresdiamond2]

oresiron8 = Ores(549,140,35,23,"/image/ores/iron.png",'iron')
oresiron9 = Ores(275,599,35,23,"/image/ores/iron.png",'iron')
oressilver6 = Ores(889,254,38,16,"/image/ores/silver.png",'silver')
oressilver7 = Ores(289,281,38,16,"/image/ores/silver.png",'silver')
oressilver8 = Ores(542,497,38,16,"/image/ores/silver.png",'silver')
oresgold6 = Ores(502,294,37,30,"/image/ores/gold.png",'gold')
oresdiamond3 = Ores(1016,441,32,18,"/image/ores/diamond.png",'diamond')
list_ores3 = [oresiron8,oresiron9,oressilver6,oressilver7,oressilver8,oresgold6,oresdiamond3]

oresiron10 = Ores(635,436,35,23,"/image/ores/iron.png",'iron')
oressilver9 = Ores(587,687,38,16,"/image/ores/silver.png",'silver')
oressilver10 = Ores(198,227,38,16,"/image/ores/silver.png",'silver')
oresgold7 = Ores(706,240,37,30,"/image/ores/gold.png",'gold')
oresgold8 = Ores(1003,78,37,30,"/image/ores/gold.png",'gold')
oresdiamond4 = Ores(102,415,32,18,"/image/ores/diamond.png",'diamond')
oresemeralds1 = Ores(53,92,25,16,"/image/ores/emeralds.png",'emerald')
list_ores4 = [oresiron10,oressilver9,oressilver10,oresgold7,oresgold8,oresdiamond4,oresemeralds1]

oresiron11 = Ores(316,436,35,23,"/image/ores/iron.png",'iron')
oresiron12 = Ores(1013,328,35,23,"/image/ores/iron.png",'iron')
oressilver11 = Ores(617,497,38,16,"/image/ores/silver.png",'silver')
oressilver12 = Ores(654,119,38,16,"/image/ores/silver.png",'silver')
oressilver13 = Ores(231,280,38,16,"/image/ores/silver.png",'silver')
oresgold9 = Ores(1002,429,37,30,"/image/ores/gold.png",'gold')
oresgold10 = Ores(441,105,37,30,"/image/ores/gold.png",'gold')
oresdiamond5 = Ores(784,252,32,18,"/image/ores/diamond.png",'diamond')
list_ores5 = [oresiron11,oresiron12,oressilver11,oressilver12,oressilver13,oresgold9,oresgold10,oresdiamond5]

oresiron13 = Ores(741,166,35,23,"/image/ores/iron.png",'iron')
oresiron14 = Ores(558,409,35,23,"/image/ores/iron.png",'iron')
oressilver14 = Ores(389,227,38,16,"/image/ores/silver.png",'silver')
oresgold11 = Ores(98,321,37,30,"/image/ores/gold.png",'gold')
oresgold12 = Ores(780,375,37,30,"/image/ores/gold.png",'gold')
oresdiamond6 = Ores(54,252,32,18,"/image/ores/diamond.png",'diamond')
oresemeralds2 = Ores(612,579,25,16,"/image/ores/emeralds.png",'emerald')
oresemeralds3 = Ores(990,551,25,16,"/image/ores/emeralds.png",'emerald')
list_ores6 = [oresiron13,oresiron14,oressilver14,oresgold11,oresgold12,oresdiamond6,oresemeralds2,oresemeralds3]

oresiron15 = Ores(397,383,35,23,"/image/ores/iron.png",'iron')
oresiron16 = Ores(739,220,35,23,"/image/ores/iron.png",'iron')
oresgold13 = Ores(568,538,37,30,"/image/ores/gold.png",'gold')
oresgold14 = Ores(224,78,37,30,"/image/ores/gold.png",'gold')
oresdiamond7 = Ores(191,577,32,18,"/image/ores/diamond.png",'diamond')
oresdiamond8 = Ores(869,468,32,18,"/image/ores/diamond.png",'diamond')
oresdiamond9 = Ores(989,685,32,18,"/image/ores/diamond.png",'diamond')
oresemeralds4 = Ores(52,416,25,16,"/image/ores/emeralds.png",'emerald')
oresemeralds5 = Ores(98,687,25,16,"/image/ores/emeralds.png",'emerald')
oresemeralds6 = Ores(937,687,25,16,"/image/ores/emeralds.png",'emerald')
list_ores7 = [oresiron15,oresiron16,oresgold13,oresgold14,oresdiamond7,oresdiamond8,oresdiamond9,oresemeralds4,oresemeralds5,oresemeralds6]

# Всі звуки

buttonsound = pygame.mixer.Sound(os.path.abspath(__file__ + "/..") +'\\sounds\\buttonpressed.wav')
walk_sound = pygame.mixer.Sound(os.path.abspath(__file__ + "/..") +'\\sounds\\step.wav')

# Весь текст
    # Таверна
        # Ціни
diamondprice = Text(coin2.X+coin2.WIDTH+5,coin2.Y,27,'arial','5',(0,0,0))
emeraldsprice = Text(coin1.X+coin1.WIDTH+5,coin1.Y,27,'arial','4',(0,0,0))
goldprice = Text(coin3.X+coin3.WIDTH+5,coin3.Y,27,'arial','3',(0,0,0))
silverprice = Text(coin5.X+coin5.WIDTH+5,coin5.Y,27,'arial','2',(0,0,0))
ironprice = Text(coin4.X+coin4.WIDTH+5,coin4.Y,27,'arial','1',(0,0,0))
        # Для показу що ми маємо в таверні
diamondcount = Text(buttonselldiamond.X+buttonselldiamond.WIDTH//2-10,buttonselldiamond.Y,27,'arial',str(mainchar.diamond),(0,0,0))
emeraldscount = Text(buttonsellemeralds.X+buttonsellemeralds.WIDTH//2-10,buttonsellemeralds.Y,27,'arial',str(mainchar.emeralds),(0,0,0))
goldcount = Text(buttonsellgold.X+buttonsellgold.WIDTH//2-10,buttonsellgold.Y,27,'arial',str(mainchar.gold),(0,0,0))
silvercount = Text(buttonsellsilver.X+buttonsellsilver.WIDTH//2-10,buttonsellsilver.Y,27,'arial',str(mainchar.silver),(0,0,0))
ironcount = Text(buttonselliron.X+buttonselliron.WIDTH//2-10,buttonselliron.Y,27,'arial',str(mainchar.iron),(0,0,0))
monyewehave = Text(coin6.X+coin6.WIDTH + 5,coin6.Y,27,'arial',str(mainchar.coin),(0,0,0))

# Загружаємо всі текстури

for i in list_ores1:
    i.load_image()
for i in list_coin:
    i.load_image()
for i in list_ores2:
    i.load_image()
for i in list_ores3:
    i.load_image()
for i in list_ores4:
    i.load_image()
for i in list_ores5:
    i.load_image()
for i in list_ores6:
    i.load_image()
rope.load_image()
heart.load_image()
heartupgradeprice.load_text()
deathbg.load_image()
heartupgrade.load_image()
coin6.load_image()
cavebg.load_image()
grassbg.load_image()
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
