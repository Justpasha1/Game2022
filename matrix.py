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
                # elif p == '2':
                #     block = Graphic_elements(x,y,78,78,'images/grass2.png')
                # elif p == '3':
                #     block = Graphic_elementsk(x,y,78,78,'images/grassadirt1.png')
                # elif p == '4':
                #     block = Graphic_elementsk(x,y,78,78,'images/dirt1.png')
                # elif p == '5':
                #     block = Graphic_elements(x,y,78,78,'images/dirt2.png')
                # elif p == '6':
                #     block = Graphic_elements(x,y,78,78,'images/grassadirt2.png')
                all_blocks.append(block)
            x += 48
        y += 27
        x =0