import pygame
import os
import random 
from matrix import *

class Character():
    def __init__(self, x_sprite, y_sprite, width_sprite, height_sprite,speed_sprite,gravity_sprite,jump_sprite,sprite_path,):
        #путь к спрайту
        self.Sprite_path = sprite_path
        #координата х спрайта
        self.X_sprite = x_sprite
        #координата у спрайта 
        self.Y_sprite = y_sprite
        #ширина нашего спрайта
        self.Width_sprite = width_sprite
        #высота нашего спрайта
        self.Height_sprite = height_sprite
        #скорость нашего спрайта
        self.Speed_sprite = speed_sprite
        #графитация спрайта
        self.Gravity_sprite = gravity_sprite
        #прыжок нашего спрайта
        self.Jump_sprite = jump_sprite
        #путь к нашему спрайту
        self.Sprite_path = sprite_path
        self.jump_count = 0.5
        self.Y_VELOCITY = self.Jump_sprite
        self.move_left = True
        self.move_right = True
        self.index_image = 0
        self.speed_animation = 0
        self.fall = False
        self.img = None
        self.load_image()

    def load_image(self):
        self.img = os.path.abspath(__file__ + "/..")
        self.img = self.img + self.Sprite_path
        self.img = pygame.image.load(self.img).convert_alpha()
        self.img = pygame.transform.scale(self.img, (self.Width_sprite,self.Height_sprite))
    def show_image(self, screen):
        screen.blit(self.img, (self.X_sprite, self.Y_sprite)) 
    def move_character(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] :
            self.colisium_left()
            if self.move_left == True:
                
                self.X_sprite -= self.Speed_sprite
                if self.speed_animation == 10:
                    self.index_image += 1
                    self.Sprite_path = "\\image\\charl" + str(self.index_image) + ".png"
                elif self.speed_animation == 20:
                    self.index_image += 1
                    self.Sprite_path = "\\image\\charl" + str(self.index_image) + ".png"
                elif self.speed_animation == 30:
                    self.index_image += 1
                    self.Sprite_path = "\\image\\charl" + str(self.index_image) + ".png"
                elif self.speed_animation == 40:
                    self.index_image += 1
                    self.Sprite_path = "\\image\\charl" + str(self.index_image) + ".png"
                    self.speed_animation += 1
                    self.index_image = 0 
                    self.speed_animation = 0 
                self.load_image()
                self.speed_animation += 1 
            

        if keys[pygame.K_RIGHT]:
            self.colisium_right()
            if self.move_right == True:
            
                self.X_sprite += self.Speed_sprite
                if self.speed_animation == 10:
                    self.index_image += 1
                    self.Sprite_path = "\\image\\char" + str(self.index_image) + ".png"
                elif self.speed_animation == 20:
                    self.index_image += 1
                    self.Sprite_path = "\\image\\char" + str(self.index_image) + ".png"
                elif self.speed_animation == 30:
                    self.index_image += 1
                    self.Sprite_path = "\\image\\char" + str(self.index_image) + ".png"
                elif self.speed_animation == 40:
                    self.index_image += 1
                    self.Sprite_path = "\\image\\char" + str(self.index_image) + ".png"
                    self.speed_animation += 1
                    self.index_image = 0 
                    self.speed_animation = 0 
                self.load_image()
                self.speed_animation += 1
            
        # if keys[pygame.K_LEFT] == False and keys[pygame.K_RIGHT] == False:
        #     self.move_right = True
            
    def gravity(self):
        if self.fall:
            self.Y_sprite += self.Gravity_sprite
    
    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if self.fall != True:
                self.Y_sprite -= self.Y_VELOCITY
                self.Y_VELOCITY -= self.jump_count
                if self.Y_VELOCITY < -self.Jump_sprite:
                    self.fall = True
                    self.Y_VELOCITY = self.Jump_sprite
    def colision(self):
        for i in list_level:
            if self.Y_sprite <= i.Y:
                if self.X_sprite + self.Width_sprite >= i.X:
                    if   self.X_sprite <= i.X + i.WIDTH:
                        if self.Y_sprite + self.Height_sprite >= i.Y:
                            
                            self.fall = False
                        else:
                            self.fall = True
    def colisium_right(self):
        for i in list_level:
            if self.Y_sprite + 1 >= i.Y and self.Y_sprite - 1 <= i.Y + i.HEIGHT:
                if self.Y_sprite + self.Height_sprite - 4 <= i.Y + i.HEIGHT:
                    if self.Y_sprite + self.Height_sprite - 1 >= i.Y:
                        if self.X_sprite + self.Width_sprite >= i.X:
                            if self.X_sprite + self.Width_sprite <= i.X:
                                self.move_right = False
                                break
                            else:
                                self.move_right = True
    def colisium_left(self):
        for i in list_level:
            if self.Y_sprite + 1 >= i.Y and self.Y_sprite - 1 <= i.Y + i.HEIGHT:
                if self.Y_sprite + self.Height_sprite - 4 <= i.Y + i.HEIGHT:
                    if self.Y_sprite + self.Height_sprite - 1 >= i.Y:
                        if self.X_sprite <= i.X + i.WIDTH:
                            if self.X_sprite + self.Width_sprite >= i.X + i.WIDTH:
                                self.move_left = False
                                break
                            else:
                                self.move_left = True