import os
import pygame

class Pers():
    def __inti__(self, x, y, width, height, path):
        self.X = x
        self.Y = y
        self.WIDTH = width
        self.HEIGHT = height
        self.PATH = path
    def loadimages(self,screen):
        path = os.path.join(os.path.abspath(__file__ + "/.."))
        images = path + self.PATH
        images = pygame.image.load(images)
        images = pygame.transform.scale(images, (self.WIDTH, self.HEIGHT))
        screen.blit(images, (self.X, self.Y))

