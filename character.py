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
        self.move_left = True
        self.move_right = True
        self.index_image = 0
        self.speed_animation = 0



        
        
#super().__init__(x, y, width, height, path)
    #def load_image(self):
        #path = os.path.abspath(__file__ + "/..")
        #path = path + self.PATH
       # self.IMG = pygame.image.load(path)
        #self.IMG = pygame.transform.scale(self.IMG, (self.WIDTH, self.HEIGHT))
    def show_image(self,screen):
        img= os.path.abspath(__file__ + "/..")
        img = img + self.Sprite_path
        img = pygame.image.load(img).convert_alpha()
        img = pygame.transform.scale(img, (self.Width_sprite,self.Height_sprite))
        screen.blit(img, (self.X_sprite, self.Y_sprite)) 
    def move_character(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.move_left == True:
            self.X_sprite -= self.Speed_sprite
        if keys[pygame.K_RIGHT] and self.move_right == True:
            self.X_sprite += self.Speed_sprite

            # if self.speed_animation == 0:
            #     self.index_image += 1
            # #если номер костюма доходит до пределов воможного 
            # if self.index_image == 5:
            #     self.index_image = 1





