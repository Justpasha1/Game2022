import pygame
import os
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
        self.Jump_distance = jump_sprite
        #путь к нашему спрайту
        self.Sprite_path = sprite_path
        self.jump_count = 0
        self.Y_VELOCITY = self.Jump_distance
        self.move_left = True
        self.move_right = True
        self.index_image = 0
        self.speed_animation = 0
        self.fall = True
        self.jumping = False
        self.img = None
        self.load_image()
        self.check = True

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
            
    #-----Падение-----#
    def gravity(self):
        if self.fall:
            self.Y_sprite += self.Gravity_sprite
            
    #-----Прижок-----#
    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.fall == False and self.touch:
            self.check = False
            self.Y_sprite -= self.Jump_distance
            self.jump_count += 1
            if self.jump_count == 5:
                self.jump_count = 0
                self.fall = True
                self.check = True
        #     self.jumping = True
            
        # if self.jumping:
        #     self.Y_sprite -= self.Y_VELOCITY
        #     self.Y_VELOCITY -= self.jump_count
        #     if self.Y_VELOCITY < self.jump_count:
        #         self.Y_VELOCITY = self.Jump_distance
        #         self.jumping = False

                
                
    #-----Верхняя коллизия-----#                
    def colision(self):
        for i in list_level:
            if self.X_sprite <= i.X + i.WIDTH  and self.check:
                if self.X_sprite + self.Width_sprite >= i.X:
                    if self.Y_sprite + self.Height_sprite >= i.Y and self.Y_sprite + self.Height_sprite <= i.Y + self.Gravity_sprite + 1:
                        self.fall = False
                        break
                    else:
                        self.fall = True
    def colision_bottom(self):
        for i in list_level:
            if self.X_sprite <= i.X + i.WIDTH:
                if self.X_sprite + self.Width_sprite >= i.X:
                    if self.Y_sprite <= i.Y + i.HEIGHT:
                        self.touch = True
                        break
                    else:
                        self.touch = False
                
            # if self.Y_sprite + self.Height_sprite + 1 >= i.Y:
            #     if self.X_sprite >= i.X:
            #         if self.X_sprite <= i.X + i.WIDTH:
            #             self.fall = False
            #             break
            #         else:
            #             self.fall = True

    # def bottom_colision(self):
    #      for i in list_level:
    #          if self.Y_sprite + 1 <= i.Y + i.HEIGHT:
    #              if self.X_sprite >= i.X:
    #                 if self.X_sprite <= i.X + i.WIDTH:
    #                     if self.X_sprite + self.Width_sprite >= i.WIDTH:
    #                         self.fall = False
    #                         break
    #                     else:
    #                         self.fall = True


                        
                            
    def colisium_right(self):
        for i in list_level:
            if self.Y_sprite + 3 <= i.Y + i.HEIGHT:
                if self.Y_sprite + self.Height_sprite - 5 >= i.Y:
                    if self.X_sprite + self.Width_sprite >= i.X:
                        if self.X_sprite < i.X:
                            self.move_right = False
                            break
                        else:
                            self.move_right = True
                                
    def colisium_left(self):
        for i in list_level:
            if self.Y_sprite + 3 <= i.Y + i.HEIGHT:
                if self.Y_sprite + self.Height_sprite - 5 >= i.Y:
                    if self.X_sprite <= i.X + i.WIDTH:
                        if self.X_sprite + self.Width_sprite > i.X:
                            self.move_left = False
                            break
                        else:
                            self.move_left = True