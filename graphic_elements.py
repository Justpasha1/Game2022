from pygame import*
import os

class Graphic_elements():
    def __init__(self,x,y,width,height,path,name = 'name'):
        self.X = x
        self.Y = y
        self.HEIGHT = height
        self.WIDTH = width
        self.PATH = path
        self.NAME = name
    #Метод для подгрузки, задания и отображения 
    def show_image(self,screen_object):
        img = os.path.join(os.path.abspath(__file__ + "/.."), self.PATH)
        img = image.load(img)
        img = transform.scale(img, (self.WIDTH,self.HEIGHT))
        screen_object.blit(img, (self.X,self.Y))