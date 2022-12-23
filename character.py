import pygame
import os

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
        self.start_jump_distance = jump_sprite
        #путь к нашему спрайту
        self.Sprite_path = sprite_path
        self.jump_count = 0
        self.Y_VELOCITY = self.Jump_distance
        # self.Jump_distance = self.Height_sprite*2
        self.Jump_speed = 27
        self.move_left = True
        self.move_right = True
        self.index_image = 0
        self.speed_animation = 0
        self.fall = False
        self.jumping = False
        self.img = None
        self.load_image()
        self.flag_jump = True

    def load_image(self):
        self.img = os.path.abspath(__file__ + "/..")
        self.img = self.img + self.Sprite_path
        self.img = pygame.image.load(self.img).convert_alpha()
        self.img = pygame.transform.scale(self.img, (self.Width_sprite,self.Height_sprite))
    def show_image(self, screen):
        screen.blit(self.img, (self.X_sprite, self.Y_sprite)) 
    def move_character(self, list_level):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] :
            self.colisium_left(list_level)
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
            self.colisium_right(list_level)
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
        if keys[pygame.K_UP]:
            self.flag_jump = True
        if self.flag_jump: 
            self.jump(list_level)
        if not self.flag_jump:
            self.gravity()
    #-----Падение-----#
    def gravity(self):
        if self.fall:
            self.Y_sprite += self.Gravity_sprite
            
    #-----Прижок-----#
    def jump(self, list_level):
        self.colision_up(list_level)
        if self.fall == False:
            self.Y_sprite -= self.Jump_speed
            self.Jump_distance -= self.Jump_speed
            if self.Jump_distance <= 0:
                self.flag_jump = False
                self.Jump_distance = self.start_jump_distance
                
    #-----Верхняя коллизия-----#                
    def colision_bottom(self,list_level):
        for i in list_level:
            if self.X_sprite <= i.X + i.WIDTH  and not self.flag_jump:
                if self.X_sprite + self.Width_sprite >= i.X:
                    if self.Y_sprite + self.Height_sprite + 2 >= i.Y and self.Y_sprite + self.Height_sprite <= i.Y + self.Gravity_sprite + 1:
                         #and self.Y_sprite + self.Height_sprite <= i.Y + self.Gravity_sprite + 1:
                        self.fall = False
                        break
                    else:
                        self.fall = True
                else:
                    self.fall = True

    def colision_up(self,list_level):
        for i in list_level:
            if self.X_sprite <= i.X + i.WIDTH:
                if self.X_sprite + self.Width_sprite >= i.X:
                    if self.Y_sprite <= i.Y + i.HEIGHT and self.Y_sprite >= i.Y:
                        self.fall = True
                        break
                    else:
                        self.fall = False
                else:
                    self.fall = False
            else:
                self.fall = False

    def colisium_right(self,list_level):
        for i in list_level:
            if self.Y_sprite + 3 <= i.Y + i.HEIGHT:
                if self.Y_sprite + self.Height_sprite - 5 >= i.Y:
                    if self.X_sprite + self.Width_sprite >= i.X:
                        if self.X_sprite < i.X:
                            self.move_right = False
                            break
                        else:
                            self.move_right = True
                    else:
                        self.move_right = True
                else:
                    self.move_right = True
         
    def colisium_left(self,list_level):
        for i in list_level:
            if self.Y_sprite + 3 <= i.Y + i.HEIGHT:
                if self.Y_sprite + self.Height_sprite - 5 >= i.Y:
                    if self.X_sprite <= i.X + i.WIDTH:
                        if self.X_sprite + self.Width_sprite >= i.X:
                            self.move_left = False
                            break
                        else:
                            self.move_left = True
                    else:
                        self.move_left = True
                else:
                    self.move_left = True