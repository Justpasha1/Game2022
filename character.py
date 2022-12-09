import pygame
import os
import random 

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
        self.jump_count = 0
        self.Y_VELOCITY = self.Jump_sprite
        self.move_left = True
        self.move_right = True
        self.index_image = 0
        self.speed_animation = 0
        self.fall = True
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

        if keys[pygame.K_LEFT] and self.move_left == True:
            
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


        if keys[pygame.K_RIGHT] and self.move_right == True:
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
        #     self.Speed_s
            
    def gravity(self):
        if self.fall:
            self.Y_sprite += self.Gravity_sprite
    
    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.fall = True

        if self.fall:
            self.Y_sprite -= self.Y_VELOCITY
            self.Y_VELOCITY -= self.jump_count
            if self.Y_VELOCITY < -self.Jump_sprite:
                self.fall = False
                self.Y_VELOCITY = self.Jump_sprite