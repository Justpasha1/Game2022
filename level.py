from Image2 import Image


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
                elif p == 'g':
                    block = Image(x,y,48,27,'\\image\\stoneupbot.png')
                elif p == 'f':
                    block = Image(x,y,48,27,'\\image\\stoneupbotleft.png')
                elif p == 'h':
                    block = Image(x,y,48,27,'\\image\\stoneupbotright.png')
                all_blocks.append(block)
            x += 48
        y += 27
        x =0
def create_grass(list, all_blocks):
    block = None
    x = 0
    y = 0
    for i in list:
        for p in i:
            if p != '0':
                if p == '1':
                    block = Image(x,y,48,27,'\\image\\grass\\grassbot.png')
                if p == '2':
                    block = Image(x,y,48,27,'\\image\\grass\\grassup.png')
                elif p == '3':
                    block = Image(x,y,48,27,'\\image\\grass\\grasssideright.png')
                elif p == '4':
                    block = Image(x,y,48,27,'\\image\\grass\\grasssideleft.png')
                elif p == '5':
                    block = Image(x,y,48,27,'\\image\\grass\\grassangl8.png')
                elif p == '6':
                    block = Image(x,y,48,27,'\\image\\grass\\grassangl5.png')
                elif p == '7':
                    block = Image(x,y,48,27,'\\image\\grass\\grassangl7.png')
                elif p == '8':
                    block = Image(x,y,48,27,'\\image\\grass\\grassangl6.png')
                elif p == 'p':
                    block = Image(x,y,48,27,'\\image\\grass\\grassnothing.png')
                all_blocks.append(block)
            x += 48
        y += 27
        x =0

def create_kywsh(list, all_blocks):
    block = None
    x = 0
    y = 0
    for i in list:
        for p in i:
            if p != '0':
                if p == '1':
                    block = Image(x,y,48,27,'\\image\\kywsh\\kywshbot.png')
                if p == '2':
                    block = Image(x,y,48,27,'\\image\\kywsh\\kywshup.png')
                elif p == '3':
                    block = Image(x,y,48,27,'\\image\\kywsh\\kywshright.png')
                elif p == '4':
                    block = Image(x,y,48,27,'\\image\\kywsh\\kywshleft.png')
                elif p == '5':
                    block = Image(x,y,48,27,'\\image\\kywsh\\kywshangl4.png')
                elif p == '6':
                    block = Image(x,y,48,27,'\\image\\kywsh\\kywshangl1.png')
                elif p == '7':
                    block = Image(x,y,48,27,'\\image\\kywsh\\kywshangl3.png')
                elif p == '8':
                    block = Image(x,y,48,27,'\\image\\kywsh\\kywshangl2.png')
                elif p == 'p':
                    block = Image(x,y,48,27,'\\image\\kywsh\\kywshnothing.png')
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
              "30001000000000111111004",
              "30000100000001000000004",
              "30000011100110000000014",
              "300000000010000000000p4",
              "3000000000p0000011111p4",
              "3011111011p000000000004",
              "30000000000100000000004",
              "30000000000010100000004",
              "30001110000000p11000004",
              "30010001000000000010004",
              "300p0000100000000001004",
              "300p0000p11011100000000",
              "300p0001000000010000000",
              "30000010000000001000114",
              "30000000001111000001004",
              "30111000010000100010004",
              "30000100100000p00000004",
              "30000001000000p00100004",
              "3000000p000011p01p00004",
              "3001111p010000000000004",
              "31000000000000000000004",
              "3p000000000100010000004",
              "5p111111111p111p1111117",          
]
list_block3 = [
              "62222222222222222222222",
              "30000000000000000000000",
              "30000000000000000000000",
              "30000000000000000000114",
              "31100111101111000001004",
              "30010000000000011110004",
              "300p0000000000000000004",
              "300p1100000000000000004",
              "30000000000001100000004",
              "31000001000010010000004",
              "3p11111p1110000p1110004",
              "300000000000000pp001004",
              "300000000000000p0000004",
              "30000000011111100000014",
              "300000000000000000000p4",
              "00000000000000000000104",
              "00000000000000000001004",
              "31111001111111101110004",
              "30000010000000000000004",
              "300000p0000000000000104",
              "300011p0001111111111004",
              "3001000000p000000000004",
              "3010000000p000000000004",
              "30000100002000000001114",
              "31001p10000000000000004",
              "3p01ppp1000000110000004",
              "5p1ppppp111111pp1111007",
]
list_block4 = [
              "62222222222222222220028",
              "30000000000000000000004",
              "30000000000000000000004",
              "30000000000000000001114",
              "30000000000000000010004",
              "00001110110000000100004",
              "000100000p0110000000004",
              "311000000p0p00110000004",
              "300000000p0p00001000004",
              "30000000100010000000004",
              "30000001000001000011004",
              "31101110000000100000004",
              "30000000001110010000004",
              "300000000000000p0001004",
              "3000000000000010100p004",
              "3000000000000100000p004",
              "3001110011111000001p004",
              "300000110000000111pp014",
              "30000000000000020000004",
              "30000000001111000000004",
              "30001111000000000000004",
              "30000000100000000000114",
              "31100000010001111101004",
              "30000110000000000002004",
              "30001pp1000000000000000",
              "3001pppp100000110000000",
              "511pppppp11111pp1111117",
]
list_block5 = [
              "62222p00022222222222228",
              "30000200000000000000004",
              "30000011000000000000004",
              "30000000101100000000004",
              "31100000000011110000114",
              "30001000000000000010004",
              "30000010000000000100004",
              "30000000100000011000004",
              "30000100001000000000014",
              "31001000000011000000004",
              "30000000000000111100004",
              "30100000000000000001004",
              "30011000000100000000114",
              "31100010001001000000004",
              "30000001110000010000004",
              "30001000000000000100004",
              "30100000000000000010004",
              "30000001000011100000014",
              "300001100001000000001p4",
              "30011000000000000001pp4",
              "31100000000000000100004",
              "30000000000000010000004",
              "30000000001001000000004",
              "3000001100010000000011p",
              "000001pp100000000001ppp",
              "00001pppp1000001001pppp",
              "1111pppppp11111p11ppppp"
]          
list_block6= [
              '22222222222222222222228',
              '00000000000000000000004',
              '00000000000000000000004',
              '11100000000000001110004',
              '30001000000000010001004',
              '30000010111001100000004',
              '3000000000001p000000004',
              '3000000000000p000000114',
              '30000000001102000001004',
              '30000000010000100010004',
              '30000000100000011100004',
              '30001110000000000000004',
              '30000000000000000000004',
              '31100000000000000000014',
              '30010000000101000001004',
              '30000000010000010010004',
              '30000100000000000100004',
              '30001p11100000000000114',
              '30000000001000010000004',
              '30100000000111100000004',
              '30000000000000000000004',
              '30010000000000000000014',
              '31000100100000000001004',
              '30000000010001011100004',
              '30000000000000000000004',
              '30000000000100000001104',
              '51111100111p1111111pp17'
]
list_block7 =  [
              '62222222222222222222228',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000001100000004',
              '31001101111000000000004',
              '3010000000p000000000000',
              '3000000000p100000000000',
              '30010000000000011100111',
              '30001000000011000000004',
              '30000100100000000000004',
              '31000000001000000000004',
              '3000000000p000000000004',
              '3000000001p111111111114',
              '30100111100000000000004',
              '30000000000000000000004',
              '30010000000000001100004',
              '30000000000111000000104',
              '30000100001000100001004',
              '30001010110000010110004',
              '30010000000000000000004',
              '30000000000000000000004',
              '31000000000000000000114',
              '3p000000000011011101004',
              '3p100001011000000000004',
              '3pp01000000000000000004',
              '3pp0p100000000100000004',
              '5pp1pp11111111p11001117'
]
list_block8 = [
              '62222222222222222002228',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000001100000000010004',
              '300011000100000001p0004',
              '30010000000111001001004',
              '31000000000000000000004',
              '3p000000000000000000004',
              '30100100110010000100004',
              '30000001000001111010004',
              '30010000000000000001114',
              '30000000001100000000004',
              '30000100000010000000004',
              '30001p00000000000111114',
              '30010010000000001000004',
              '300p0001111000010000004',
              '310p0000000111100000014',
              '300p0100000000000000104',
              '301p0011100000001111004',
              '30000000000000010000004',
              '31000000000000000000004',
              '3p000000001111000000004',
              '3p111111000000000000004',
              '3p020000010000000100004',
              '3p0000000p1000001p10000',
              '3p0001001pp10100ppp0000',
              '51111p11pppp1p11ppp1111'
]
list_block9 = [
              '62222222222222222222228',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000001104',
              '30000000000000000010014',
              '31111100000000000000004',
              '30000001000100000000000',
              '30000000111001001000000',
              '30000100000000110000004',
              '30001000000000000010014',
              '30010000000000000001104',
              '30000000000000000000004',
              '31000000000000000000004',
              '30100001000000000000004',
              '30011110000000010001004',
              '30000000010000001110004',
              '30000000001110000000004',
              '30000000000000000000004',
              '30000000000000100100004',
              '30000000000000011000014',
              '30000000000000000001104',
              '30000000000000000000000',
              '30000000000000001100000',
              '30000000000000010010001',
              '0000011101000000000001p',
              '00010ppp0p01100000001pp',
              '111p1ppp1p1pp1111111ppp'
]
list_block10 =[
              '62222222222222222222228',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000001000104',
              '30000000001000100111004',
              '00000000000111000000004',
              '00001000100000000000004',
              '31100111000000000000000',
              '30000000000000100101000',
              '30000000000000011000114',
              '30000001000010000000004',
              '30000000111100000000004',
              '30000000000000000000004',
              '30000000000001000100004',
              '30100100000000111000004',
              '30011000110000000000004',
              '30000001pp1000000000004',
              '00000000000000000000114',
              '00000000000000000000000',
              '00000000000000000010000',
              '00000000000000000000000',
              '00000000000000011000001',
              '1100000000000100000000p',
              'pp11000000000000000010p',
              'pppp1100000100000101p1p',
              'pppppp11111p11111p1pppp'

]
list_block11 = [
              '62222222222222222222228',
              '30000000000000000000004',
              '30000000000000000000000',
              '30000000000000000000000',
              '30000000000000000000000',
              '30000000010000010000114',
              '30000000001000101000p04',
              '3000000100p000p00111004',
              '00000010000111000000004',
              '00011100000000000000004',
              '31100000000000000000004',
              '30000000000000000000004',
              '30000010001000000010004',
              '30000001110000000001114',
              '30000000000000100100004',
              '30000000000000011000004',
              '30000000000000000000004',
              '30010001000000000000004',
              '30001110000000000000004',
              '00000000000000000000004',
              '00000000000000000000004',
              '00000000000000000000004',
              '11100000000000000100004',
              'ppp10000001000100011114',
              'pppp000000p111p00000004',
              'pppp010001ppppp10000004',
              'pppp1p111ppppppp1111115'
]
list_block12 = [
              '62222222222222222222228',
              '30000000000000000000004',
              '30000000000000000000004',
              '00000000000000000000004',
              '00010000000000000100014',
              '31100000000100010011104',
              '30000000000011100000004',
              '30001000010000000000004',
              '30000111100000000000004',
              '30000000000000010001004',
              '30000000000000001110004',
              '30000000010001000000014',
              '310010000011100000000p4',
              '301100000000000000001p4',
              '30000000000000000000pp4',
              '30000000000000000110224',
              '30000000111000011p00004',
              '30000011p000001p0000004',
              '300001p0000001000000004',
              '30001p00000000000000004',
              '3111p000011111000111104',
              '300000001p000p000000004',
              '30000001pp000p100000004',
              '3000111ppp000pp10000004',
              '3000000000000ppp1000004',
              '3010000000000pppp100004',
              '71p1111111000ppppp11115'
]
list_block13 = [
              '62222222220002222222228',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000001110000000004',
              '3000000001ppp1000000004',
              '300000001p000p100000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '30001110000000001110004',
              '30000pp100000001pp00004',
              '3100002p1100011p2000004',
              '3p000002pp111pp20000004',
              '301000002ppppp200000004',
              '3000000002ppp2000000004',
              '30001000002220000100004',
              '3001p100000000000p11114',
              '300p0p000000000000pppp4',
              '31100p10000000000002pp4',
              '300000p1000000000000224',
              '3000000p111110000000004',
              '300000002000p1000000004',
              '30000000000000000000004',
              '30000000000000010000004',
              '700011111111111p1111115'
]
list_blockfinal = [
              '60002222222222222222228',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '30000000000000000000004',
              '51111111111111111111117'
]
list_level_2 = list()
list_level_3 = list()
list_level_4 = list()
list_level_5 = list()
list_level_6 = list()
list_level_7 = list()
list_level_8 = list()
list_level_9 = list()
list_level_10 = list()
list_level_11 = list()
list_level_12 = list()
list_level_final = list()
list_levelstart = list()
list_level_1 = list()
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
create_blocks(list_block5,list_level_4)
for i in list_level_4:
    i.load_image()
create_blocks(list_block6,list_level_5)
for i in list_level_5:
    i.load_image()
create_grass(list_block7,list_level_6)
for i in list_level_6:
    i.load_image()
create_grass(list_block8,list_level_7)
for i in list_level_7:
    i.load_image()
create_grass(list_blockfinal,list_level_final)
for i in list_level_final:
    i.load_image()
create_kywsh(list_block9,list_level_8)
for i in list_level_8:
    i.load_image()
create_kywsh(list_block10,list_level_9)
for i in list_level_9:
    i.load_image()
create_kywsh(list_block11,list_level_10)
for i in list_level_10:
    i.load_image()
create_kywsh(list_block12,list_level_11)
for i in list_level_11:
    i.load_image()
create_kywsh(list_block13,list_level_12)
for i in list_level_12:
    i.load_image()