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
                all_blocks.append(block)
            x += 48
        y += 27
        x =0