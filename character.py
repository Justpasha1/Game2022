import pygame
import os
from Image2 import Image
import random 
pygame.init()

class Character(Image):
    def __init__(self, x, y, width, height, path):
        super().__init__(x, y, width, height, path)
    def load_image(self):
        path = os.path.abspath(__file__ + "/..")
        path = path + self.PATH
        self.IMG = pygame.image.load(path)
        self.IMG = pygame.transform.scale(self.IMG, (self.WIDTH, self.HEIGHT))
    def show_image(self,screen):
        screen.blit(self.IMG, (self.X, self.Y)) 
    def movement(self):
        keys = pygame.key.get_pressed()
