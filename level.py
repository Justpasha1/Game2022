from Image2 import Image
from random import randint

def create_blocks(list, all_blocks):
    block = None
    x = 0
    y = 0
    for i in list:
        for p in i:
            if p != '0':
                if p == '1':
                    block = Image(x,y,48,27,'\\image\\stonebot.png')
                if p == '2':
                    block = Image(x,y,48,27,'\\image\\stoneup.png')
                elif p == '3':
                    block = Image(x,y,48,27,'\\image\\stonesidel.png')
                elif p == '4':
                    block = Image(x,y,48,27,'\\image\\stonesider.png')
                elif p == '5':
                    block = Image(x,y,48,27,'\\image\\stoneangld.png')
                elif p == '6':
                    block = Image(x,y,48,27,'\\image\\stoneanglu.png')
                elif p == '7':
                    block = Image(x,y,48,27,'\\image\\stoneangrd.png')
                elif p == '8':
                    block = Image(x,y,48,27,'\\image\\stoneangru.png')
                elif p == '9':
                    block = Image(x,y,48,27,'\\image\\brick\\brickbot.png')
                elif p == 'n':
                    block = Image(x,y,48,27,'\\image\\brick\\bricknothing.png')
                elif p == 'p':
                    block = Image(x,y,48,27,'\\image\\stonenoth.png')
                all_blocks.append(block)
                

            x += 48
        y += 27
        x =0

list_block_1 = [
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
               "0000000000000000000000000000000000000000",
               "0000000000000000000000000000000000000000",
               "0000000000000000000000000000000000000000",
               "0000000000000000000000000000000000000000",
               "0000000000000000000000000000000000000000",
               "9999999999999999999999999999999999999999",
               "nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn",
]
list_block2 = [
               "62222222222222222222228",
               "00000000000000000000004",
               "00000000000000000000004",
               "11110000000000000000004",
               "30001000000000111111014",
               "30000100000001000000004",
               "30000011101110000000004",
               "30000000000000000000004",
               "30000000000000001111114",
               "30111110111000000000004",
               "30000000000100000000004",
               "30000000000010100000004",
               "30001110000000111000004",
               "30010001000000000010004",
               "30010000100000000001004",
               "30010000111011100000000",
               "30010011000000010000000",
               "30000000000000001000114",
               "30000000001111000001004",
               "30111000010000100010004",
               "30000100100000100000004",
               "30000001000000100100004",
               "30000001001011101100004",
               "30011111010000000000004",
               "31000000000000000000004",
               "31000000000100010000004",
               "51111111111111111111117",          
]
list_block3 = [
                "62222222222222222222228",
                "30000000000000000000004",
                "30000000000000000000004",
                "30000000000000000000114",
                "31100111101111000001004",
                "30010000000000011110004",
                "30010000000000000000004",
                "30051100000000000000004",
                "30000000000001100000004",
                "31000000000010010000004",
                "31111111111000011110004",
                "30000000000000017001004",
                "30000000000000010000004",
                "30000000011111100000014",
                "30000000000000000000014",
                "00000000000000000000100",
                "00000000000000000001000",
                "31111001111111101110004",
                "30000010000000000000004",
                "30000010000000000000104",
                "30001170001111111111004",
                "30010000001000000000004",
                "30100000001000000000004",
                "30000100001000000001114",
                "31001110000000000000004",
                "31017p51000000110000004",
                "5117ppp5111111751111007",
]
list_block4 = [
              "62222222222222222220028",
              "30000000000000000000004",
              "30000000000000000000004",
              "30000000000000000001114",
              "30000000000000000010004",
              "00001110110000000100004",
              "00010000010110000000004",
              "31100000010100110000004",
              "30000000010100001000004",
              "30000000100010000000004",
              "30000001000001000011004",
              "31101110000000100000004",
              "30000000001110010000004",
              "30000000000000010001004",
              "30000000000000101001004",
              "30000000000001000001004",
              "30011100111110000011004",
              "30000011000000011111014",
              "30000000000000010000004",
              "30000000001111000000004",
              "30001111000000000000004",
              "30000000100000000000114",
              "31100000010001111101004",
              "30000110000000000001004",
              "30001001000000000000000",
              "30017pp5100000110000000",
              "5117pppp511111111111117",
]
list_level_2 = list()
list_level_3 = list()
list_levelstart = list()
list_level_1 = list()
# create_blocks(list_block, list_level)
create_blocks(list_block_1, list_levelstart)
for i in list_levelstart:
    i.load_image()
create_blocks(list_block2,list_level_1)
for i in list_level_1:
    i.load_image()
create_blocks(list_block3,list_level_2)
for i in list_level_2:
    i.load_image()
create_blocks(list_block4,list_level_3)
for i in list_level_3:
    i.load_image()
# def generate_ores():
#     silver = 