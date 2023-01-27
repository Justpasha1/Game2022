from Image2 import Image
from character import Character
from text import Text
from ores import Ores
import pygame
import os
from enemies import Enemie, Static_Enemie, Chonky_enemie
from pygame import mixer

# лого гри
logo = Image(100, 250, 95*5, 23*5,'\\image\\logo.png')


# Створення всіх об'єктів та гравця в грі
    # Фони гри
background = Image(0,0,1080,720,"\\image\\phonee.png")
mainchar = Character(400, 550, 20, 27, 4, 5, 27*2+14, "\\image\\char1.png")
tavernabg = Image(0,0,1080,720,'\\image\\bg\\tavernabg.png')
bgstart = Image(0,0,1080,720,'\\image\\bg\\bgstart.png')
cavebg = Image(0,0,1080,720,'\\image\\bg\\cavebg.png')
grassbg = Image(0,0,1080,720,'\\image\\bg\\grassbg.png')
deathbg = Image(0,0,1080,720,'\\image\\bg\\dethbg.png')
history1 = Image(0,0,1080,720,'\\image\\story\\history1.png')
history2 = Image(0,0,1080,720,'\\image\\story\\history2.png')
history3 = Image(0,0,1080,720,'\\image\\story\\history3.png')
history4 = Image(0,0,1080,720,'\\image\\story\\history4.png')
history5 = Image(0,0,1080,720,'\\image\\story\\history5.png')
kywshbg = Image(0,0,1080,720,"\\image\\bg\\kywshbg.png")
help1 = Image(0,0,1080,720,"\\image\\help\\help1.png")
help2 = Image(0,0,1080,720,"\\image\\help\\help2.png")
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
recover = Image(buttonsell.X-64*3-20,buttonsell.Y+3, 64*3,16*3,'\\image\\taverna\\recoverybutton.png')
        # Кнопки історії
buttonnext = Image(870,630,200,80,'\\image\\story\\nextbutton.png')
buttonleave = Image(64,593,60*3,20*3,'\\image\\story\\leavebutton.png')
buttontry = Image(64 +(60*3) +20,593,60*3,20*3,'\\image\\story\\trybutton.png')
    # кнопки допомоги
backbutton = Image(10,670,100,40,"\\image\\help\\backbutton.png")
buttonnext1 = Image(970,670,100,40,'\\image\\story\\nextbutton.png')
# Текстури для переходів

heart = Image(359,27,588,675,'\\image\\heart.png')
taverna = Image(400,523,204,152,'\\image\\taverna1.png')
caveentertop = Image(1018,549,62,127,'\\image\\caveentertop.png')
caveenterbottom = Image(1018,608,25,68,'\\image\\caveenterbottom.png')

# Текстури кнопок

C = Image((heart.X + heart.WIDTH)-heart.WIDTH//2-15,heart.Y+100,40,40,'\\image\\C.png')
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
coin8 = Image(recover.X+recover.WIDTH//2-30,recover.Y-30,27,27,'\\image\\taverna\\coin.png')

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

buttonsound = mixer.Sound(os.path.abspath(__file__ + "/..") +'\\sounds\\buttonpressed.wav')
walk_sound = mixer.Sound(os.path.abspath(__file__ + "/..") +'\\sounds\\step.wav')
walk_sound.set_volume(0.3)
orespickup = mixer.Sound(os.path.abspath(__file__ + '/..') + "\\sounds\\orespickup.wav")
pageturn = mixer.Sound(os.path.abspath(__file__ + '/..') + "\\sounds\\pageturn.wav")
tavernaost = mixer.Sound(os.path.abspath(__file__ + '/..') + "\\sounds\\tavernaost.wav")
caveost = mixer.Sound(os.path.abspath(__file__ + '/..') + "\\sounds\\caveost.wav")
# tavernaost = pygame.mixer.music.load(os.path.abspath(__file__ + '/..') + '\\sounds\\tavernaost.wav')
# Весь текст
    # Таверна
        # Ціни
diamondprice = Text(coin2.X+coin2.WIDTH+5,coin2.Y,27,'arial','5',(0,0,0))
emeraldsprice = Text(coin1.X+coin1.WIDTH+5,coin1.Y,27,'arial','4',(0,0,0))
goldprice = Text(coin3.X+coin3.WIDTH+5,coin3.Y,27,'arial','3',(0,0,0))
silverprice = Text(coin5.X+coin5.WIDTH+5,coin5.Y,27,'arial','2',(0,0,0))
ironprice = Text(coin4.X+coin4.WIDTH+5,coin4.Y,27,'arial','1',(0,0,0))
recoverprice = Text(coin8.X+coin8.WIDTH+5,coin8.Y,27,'arial','10',(0,0,0))
        # Для показу що ми маємо в таверні
diamondcount = Text(buttonselldiamond.X+buttonselldiamond.WIDTH//2-10,buttonselldiamond.Y,27,'arial',str(mainchar.diamond),(0,0,0))
emeraldscount = Text(buttonsellemeralds.X+buttonsellemeralds.WIDTH//2-10,buttonsellemeralds.Y,27,'arial',str(mainchar.emeralds),(0,0,0))
goldcount = Text(buttonsellgold.X+buttonsellgold.WIDTH//2-10,buttonsellgold.Y,27,'arial',str(mainchar.gold),(0,0,0))
silvercount = Text(buttonsellsilver.X+buttonsellsilver.WIDTH//2-10,buttonsellsilver.Y,27,'arial',str(mainchar.silver),(0,0,0))
ironcount = Text(buttonselliron.X+buttonselliron.WIDTH//2-10,buttonselliron.Y,27,'arial',str(mainchar.iron),(0,0,0))
monyewehave = Text(coin6.X+coin6.WIDTH + 5,coin6.Y,27,'arial',str(mainchar.coin),(0,0,0))

# вороги
        # chonky
chonky1_1 = Chonky_enemie(391, 137, 40, 26, 1, "\\image\\chonky.png", 0)
chonky1_2 = Chonky_enemie(817, 81, 40, 26, 1, "\\image\\chonky.png", 0)
chonky1_3 = Chonky_enemie(473, 379, 40, 26, 1, "\\image\\chonky.png", 0)
chonky1_4 = Chonky_enemie(171, 486, 40, 26, 1, "\\image\\chonky.png", 0)

chonky2_1 = Chonky_enemie(653, 191 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky2_2 = Chonky_enemie(168, 433 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky2_3 = Chonky_enemie(817, 433 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky2_4 = Chonky_enemie(341, 649 ,40, 26, 1, "\\image\\chonky.png", 0)


chonky3_1 = Chonky_enemie(409, 109, 40, 26, 1, "\\image\\chonky.png", 0)
chonky3_2 = Chonky_enemie(103, 163, 40, 26, 1, "\\image\\chonky.png", 0)
chonky3_3 = Chonky_enemie(583, 407, 40, 26, 1, "\\image\\chonky.png", 0)
chonky3_4 = Chonky_enemie(75, 569, 40, 26, 1, "\\image\\chonky.png", 0)

chonky4_1 = Chonky_enemie(967, 299 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky4_2 = Chonky_enemie(486, 325 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky4_3 = Chonky_enemie(534, 460 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky4_4 = Chonky_enemie(432, 650 ,40, 26, 1, "\\image\\chonky.png", 0)

chonky5_1 = Chonky_enemie(824, 245 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky5_2 = Chonky_enemie(199, 434 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky5_3 = Chonky_enemie(121, 677 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky5_4 = Chonky_enemie(577, 677 ,40, 26, 1, "\\image\\chonky.png", 0)

chonky6_1 = Chonky_enemie(530, 136 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky6_2 = Chonky_enemie(674, 433 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky6_4 = Chonky_enemie(916, 569 ,40, 26, 1, "\\image\\chonky.png", 0)

chonky7_1 = Chonky_enemie(865, 216 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky7_2 = Chonky_enemie(810, 460 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky7_3 = Chonky_enemie(287, 677 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky7_4 = Chonky_enemie(579, 677 ,40, 26, 1, "\\image\\chonky.png", 0)

chonky8_1 = Chonky_enemie(716, 189 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky8_2 = Chonky_enemie(530, 406 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky8_3 = Chonky_enemie(387, 677 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky8_4 = Chonky_enemie(481, 677 ,40, 26, 1, "\\image\\chonky.png", 0)

chonky9_1 = Chonky_enemie(963, 244 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky9_2 = Chonky_enemie(164, 406 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky9_3 = Chonky_enemie(1012, 649 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky9_4 = Chonky_enemie(869, 677 ,40, 26, 1, "\\image\\chonky.png", 0)

chonky10_1 = Chonky_enemie(248, 217 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky10_2 = Chonky_enemie(410, 326 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky10_3 = Chonky_enemie(746, 380 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky10_4 = Chonky_enemie(195, 677 ,40, 26, 1, "\\image\\chonky.png", 0)

chonky11_1 = Chonky_enemie(504, 298 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky11_2 = Chonky_enemie(247, 460 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky11_3 = Chonky_enemie(722, 596 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky11_4 = Chonky_enemie(51, 677 ,40, 26, 1, "\\image\\chonky.png", 0)

chonky12_1 = Chonky_enemie(626, 136 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky12_2 = Chonky_enemie(387, 163 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky12_3 = Chonky_enemie(385, 569 ,40, 26, 1, "\\image\\chonky.png", 0)
chonky12_4 = Chonky_enemie(213, 677 ,40, 26, 1, "\\image\\chonky.png", 0)

chonkys_1 = [
    chonky1_1,
    chonky1_2,
    chonky1_3,
    chonky1_4
]
chonkys_2 = [
    chonky2_1,
    chonky2_2,
    chonky2_3,
    chonky2_4
]
chonkys_3 = [
    chonky3_1,
    chonky3_2,
    chonky3_3,
    chonky3_4
]
chonkys_4 = [
    chonky4_1,
    chonky4_2,
    chonky4_3,
    chonky4_4
]
chonkys_5 = [
    chonky5_1,
    chonky5_2,
    chonky5_3,
    chonky5_4
]
chonkys_6 = [
    chonky6_1,
    chonky6_2,
    chonky6_4
]
chonkys_7 = [
    chonky7_1,
    chonky7_2,
    chonky7_3,
    chonky7_4
]
chonkys_8 = [
    chonky8_1,
    chonky8_2,
    chonky8_3,
    chonky8_4
]
chonkys_9 = [
    chonky9_1,
    chonky9_2,
    chonky9_3,
    chonky9_4
]
chonkys_10 = [
    chonky10_1,
    chonky10_2,
    chonky10_3,
    chonky10_4
]
chonkys_11 = [
    chonky11_1,
    chonky11_2,
    chonky11_3,
    chonky11_4
]
chonkys_12 = [
    chonky12_1,
    chonky12_2,
    chonky12_3,
    chonky12_4
]

"""--------------------------------------------MOVE_Enemys-----------------------------------------------"""
zombie1_1 = Enemie(773, 215, 21, 30, 1, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right', 220, 120)
zombie1_2 = Enemie(105, 243, 21, 30, 1, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right', 200, 120)
zombie1_3 = Enemie(582, 405, 21, 30, 1, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right', 110, 0)
zombie1_4 = Enemie(777, 702, 21, 30, 1, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right', 250, 120)
zombie1_5 = Enemie(780, 702, 21, 30, 1, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right', 250, -120)
zombie1_6 = Enemie(102, 702, 21, 30, 1, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right', 400, -200)
zombie1_7 = Enemie(102, 702, 21, 30, 1, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right', 400, 120)
zombie1_8 = Enemie(200, 702, 21, 30, 1, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right', 200, 120)
zombie1_9 = Enemie(153, 620, 21, 30, 1, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right', 160, 120)
zombie1_10 = Enemie(580, 702, 21, 40, 1, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right', 120, 120)
zombie1_11 = Enemie(490, 487, 21, 40, 1, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right', 160, 120)
zombie1_12 = Enemie(200, 325, 21, 40, 1, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right', 120, 120)

zombie5_1 = Enemie(386, 134, 21, 30, 1, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',120, 120)
zombie5_2 = Enemie(481, 215, 21, 30, 1, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',60, 120)
zombie5_3 = Enemie(721, 269, 21, 30, 1, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',80, 120)
zombie5_4 = Enemie(193, 296, 21, 30, 1, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',110, 120)
zombie5_5 = Enemie(289, 458, 21, 30, 1, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',110, 120)
zombie5_6 = Enemie(530, 512, 21, 30, 1, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',150, 120)
zombie5_7 = Enemie(722, 621, 21, 30, 1, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',110, 120)
zombie5_8 = Enemie(620, 702, 21, 30, 1, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',240, 120)
zombie5_9 = Enemie(386, 702, 21, 30, 1, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',100, 120)

zombie6_1 = Enemie(530, 323, 21, 30, 1.5, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',500, 120)
zombie6_2 = Enemie(534, 431, 21, 30, 1.5, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',130, 120)
zombie6_3 = Enemie(240, 351, 21, 30, 1.5, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',160, 120)
zombie6_4 = Enemie(338, 107, 21, 30, 1.5, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',170, 120)
zombie6_5 = Enemie(721, 594, 21, 30, 1.5, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',120, 120)
zombie6_6 = Enemie(290, 702, 21, 30, 1.5, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',350, 120)
zombie6_7 = Enemie(385, 485, 21, 30, 1.5, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',60, 120)

zombie7_1 = Enemie(625, 242, 21, 30, 1.5, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',160, 120)
zombie7_2 = Enemie(914, 269, 21, 30, 1.5, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',120, 120)
zombie7_3 = Enemie(339, 405, 21, 30, 1.5, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',160, 120)
zombie7_4 = Enemie(529, 431, 21, 30, 1.5, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',160, 120)
zombie7_5 = Enemie(820, 351, 21, 30, 1.5, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',210, 120)
zombie7_6 = Enemie(103, 594, 21, 30, 1.5, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',230, 120)
zombie7_7 = Enemie(483, 567, 21, 30, 1.5, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',150, 120)

zombie8_1 = Enemie(386, 188, 21, 30, 2, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',120, 120)
zombie8_2 = Enemie(914, 269, 21, 30, 2, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',70, 120)
zombie8_3 = Enemie(144, 377, 21, 30, 2, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',150, 120)
zombie8_4 = Enemie(721, 512, 21, 30, 2, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',70, 120)
zombie8_5 = Enemie(626, 702, 21, 30, 2, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',310, 120)
zombie8_6 = Enemie(769, 404, 21, 30, 2, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',120, 120)

zombie9_1 = Enemie(241, 214, 21, 30, 2, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',120, 120)
zombie9_2 = Enemie(528, 160, 21, 30, 2, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',120, 120)
zombie9_3 = Enemie(384, 323, 21, 30, 2, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',170, 120)
zombie9_4 = Enemie(673, 404, 21, 30, 2, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',110, 120)
zombie9_5 = Enemie(288, 702, 21, 30, 2, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',220, 120)
zombie9_6 = Enemie(578, 702, 21, 30, 2, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',210, 120)

zombie10_1 = Enemie(533, 215, 21, 30, 2, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',120, 120)
zombie10_2 = Enemie(819, 188, 21, 30, 2, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',120, 120)
zombie10_3 = Enemie(192, 485, 21, 30, 2, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',120, 120)
zombie10_4 = Enemie(289, 702, 21, 30, 2, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',120, 120)
zombie10_5 = Enemie(530, 648, 21, 30, 2, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',120, 120)

zombie11_1 = Enemie(243, 215, 21, 30, 2, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',170, 120)
zombie11_2 = Enemie(578, 161, 21, 30, 2, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',120, 120)
zombie11_3 = Enemie(387, 431, 21, 30, 2, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',130, 120)
zombie11_4 = Enemie(437, 539, 21, 30, 2, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',180, 120)
zombie11_5 = Enemie(199, 620, 21, 30, 2, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',120, 120)

zombie12_1 = Enemie(436, 702, 21, 30, 2, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',200, 120)
zombie12_2 = Enemie(778, 702, 21, 30, 2, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',260, 120)
zombie12_3 = Enemie(442, 594, 21, 30, 2, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',170, 120)
zombie12_4 = Enemie(200, 296, 21, 30, 2, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',120, 120)
zombie12_5 = Enemie(780, 296, 21, 30, 2, "\\image\\enemiewalk\\walkingdude1.png", 0, 2, 2, 'Right',120, 120)

enemys_1 = [
    zombie1_1, zombie1_2, zombie1_3,
    zombie1_4, zombie1_5, zombie1_6,
    zombie1_7, zombie1_8, zombie1_9,
    zombie1_10, zombie1_11, zombie1_12
]
enemys_5 = [
    zombie5_1,
    zombie5_2,
    zombie5_3,
    zombie5_4,
    zombie5_5,
    zombie5_6,
    zombie5_7,
    zombie5_8,
    zombie5_9
]
enemys_6 = [
    zombie6_1,
    zombie6_2,
    zombie6_3,
    zombie6_4,
    zombie6_5,
    zombie6_6,
    zombie6_7
]
enemys_7 = [
    zombie7_1,
    zombie7_2,
    zombie7_3,
    zombie7_4,
    zombie7_5,
    zombie7_6,
    zombie7_7
]
enemys_8 = [
    zombie8_1,
    zombie8_2,
    zombie8_3,
    zombie8_4,
    zombie8_5,
    zombie8_6
]
enemys_9 = [
    zombie9_1,
    zombie9_2,
    zombie9_3,
    zombie9_4,
    zombie9_5,
    zombie9_6
]
enemys_10 = [
    zombie10_1,
    zombie10_2,
    zombie10_3,
    zombie10_4,
    zombie10_5
]
enemys_11 = [
    zombie11_1,
    zombie11_2,
    zombie11_3,
    zombie11_4,
    zombie11_5
]
enemys_12 = [
    zombie12_1,zombie12_2,
    zombie12_3,zombie12_4,
    zombie12_5
]

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
buttonnext1.load_image()
backbutton.load_image()
help1.load_image()
help2.load_image()
C.load_image()
recoverprice.load_text()
coin8.load_image()
recover.load_image()
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
history1.load_image()
history2.load_image()
history3.load_image()
history4.load_image()
history5.load_image()
buttonnext.load_image()
buttonleave.load_image()
buttontry.load_image()
logo.load_image()
kywshbg.load_image()