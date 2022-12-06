import pygame
import os

class Graphic_elements():
    def __init__(self,x,y,width,height,path):
        self.X = x
        self.Y = y
        self.HEIGHT = height
        self.WIDTH = width
        self.PATH = path
    #Метод для подгрузки, задания и отображения 
    def load_image(self):
        path = os.path.abspath(__file__ + "/..")
        path = path + self.PATH
        path = pygame.image.load(path)
        self.path = pygame.transform.scale(path, (self.WIDTH, self.HEIGHT))
    def show_image(self,screen):
        screen.blit(self.path, (self.X, self.Y)) 