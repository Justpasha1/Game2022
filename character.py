import pygame
import os

class Character():
    def __init__(self, x_sprite, y_sprite, width_sprite, height_sprite,speed_sprite,gravity_sprite,jump_sprite,sprite_path):
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
        self.Jump_speed = 6
        self.move_left = True
        self.move_right = True
        self.index_image = 0
        self.speed_animation = 0
        self.fall = False
        self.img = None
        self.load_image()
        self.flag_jump = False
        self.ores_balance = 0
        self.side = False #False - Лево, True - Право
        self.space = False
        self.can_entern_taverna = False
        self.diamond = 0
        self.emeralds = 0
        self.gold = 0
        self.iron = 0
        self.silver = 0
        self.coin = 0
        self.hp = 100
        self.hp_max = 100
        self.space = False
        self.where_watching = 'right'
        
    def load_image(self):
        self.img = os.path.abspath(__file__ + "/..")
        self.img = self.img + self.Sprite_path
        self.img = pygame.image.load(self.img).convert_alpha()
        self.img = pygame.transform.scale(self.img, (self.Width_sprite,self.Height_sprite))
    def show_image(self, screen):
        screen.blit(self.img, (self.X_sprite, self.Y_sprite)) 
    def move_character(self, list_level,walk_sound):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] :
            self.where_watching = 'left'
            self.colisium_left(list_level)
            if self.move_left == True:
                self.side = False
                self.X_sprite -= self.Speed_sprite
                if self.speed_animation >= 5:
                    self.index_image += 1
                    self.Sprite_path = "\\image\\charl" + str(self.index_image) + ".png"
                    self.speed_animation = 0
                    self.load_image()
                    if self.index_image == 4:
                        self.index_image = 0
                # elif self.speed_animation >= 10:
                #     self.index_image += 1
                #     self.Sprite_path = "\\image\\charl" + '2' + ".png"
                #     # if not self.flag_jump:
                #     #     walk_sound.play()
                # elif self.speed_animation >= 15:
                #     self.index_image += 1
                #     self.Sprite_path = "\\image\\charl" + '3' + ".png"
                #     if not self.flag_jump:
                #         walk_sound.play()
                # elif self.speed_animation >= 20:
                #     self.index_image += 1
                #     self.Sprite_path = "\\image\\charl" + '4' + ".png"
                #     self.speed_animation += 1
                #     self.index_image = 0 
                #     self.speed_animation = 0 
                    
                
                self.speed_animation += 1 


        if keys[pygame.K_RIGHT]:
            self.where_watching = 'right'
            self.colisium_right(list_level)
            if self.move_right == True:
                self.side = True
                self.X_sprite += self.Speed_sprite
                if self.speed_animation >= 5:
                    self.index_image += 1
                    self.Sprite_path = "\\image\\char" + str(self.index_image) + ".png"
                    self.speed_animation = 0
                    self.load_image()
                    if self.index_image == 4:
                        self.index_image = 0
                # elif self.speed_animation >= 10:
                #     self.index_image += 1
                #     self.Sprite_path = "\\image\\char" + '2' + ".png"
                #     # if not self.flag_jump:
                #     #     walk_sound.play()
                # elif self.speed_animation >= 15:
                #     self.index_image += 1
                #     self.Sprite_path = "\\image\\char" + '3' + ".png"
                #     if not self.flag_jump:
                #         walk_sound.play()
                # elif self.speed_animation >= 20:
                #     self.index_image += 1
                #     self.Sprite_path = "\\image\\char" + '4' + ".png"
                #     self.speed_animation += 1
                #     self.index_image = 0 
                #     self.speed_animation = 0
                    
                
                # self.load_image()
                self.speed_animation += 1
                
            #Если персонаж смотрит вправо
        # else:
        #     #То наш персонаж будет стоять и смотреть вправо
        #     if self.where_watching == 'right':
        #         if self.can_flying_now:
        #                 self.Sprite_path = 'image/' + 'char1' + '.png'
        #                 self.load_image()
        #     else:
        #         #То наш персонаж будет стоять и смотреть влево
        #         if self.can_flying_now:
        #             self.Sprite_path = 'image/' + 'charl1' + '.png'
        #             self.load_image()


        if keys[pygame.K_UP] and not self.fall and self.space == False:
            self.flag_jump = True
            self.space = True
            
        if keys[pygame.K_UP] == False:
            self.space = False
        if self.flag_jump:
            self.jump(list_level)
        if not self.flag_jump:
            self.gravity()
       
        # else:
        #     #То наш персонаж будет стоять и смотреть вправо
        #     if self.where_watching == 'right':
        #             self.Sprite_path = '\\image\\' + 'char1' + '.png'
        #             self.load_image()
        #     else:
        #         #То наш персонаж будет стоять и смотреть влево
        #         self.Sprite_path = '\\image\\' + 'charl1' + '.png'
        #         self.load_image()
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not self.fall and not self.flag_jump:
            self.speed_animation = 0
            self.index_image = 0
            if self.where_watching == 'right':
                self.Sprite_path = '\\image\\char1.png'
                self.load_image()
            if self.where_watching == 'left':
                self.Sprite_path = '\\image\\charl1.png'
                self.load_image()
        self.colision_bottom(list_level)
    #-----Падение-----#
    def gravity(self):
        if self.fall:
            self.Y_sprite += self.Gravity_sprite
            if self.side == True:
                self.Sprite_path = "\\image\\char6.png"
            elif self.side == False:
                self.Sprite_path = "\\image\\charl6.png"
            self.load_image()

    #-----Прижок-----#
    def jump(self, list_level):
        self.colision_up(list_level)
        if self.fall == False:
            self.flag_jump = True
            self.Y_sprite -= self.Jump_speed
            self.Jump_distance -= self.Jump_speed
            if self.Jump_distance <= 0:
                self.flag_jump = False
                self.Jump_distance = self.start_jump_distance
            if self.side == True:
                self.Sprite_path = "\\image\\char5.png"
            elif self.side == False:
                self.Sprite_path = "\\image\\charl5.png"
            self.load_image()

    #-----Верхняя коллизия-----#                
    def colision_bottom(self,list_level):
        for block in list_level:
            if self.X_sprite <= block.X + block.WIDTH  and not self.flag_jump:
                if self.X_sprite + self.Width_sprite >= block.X:
                    if self.Y_sprite + self.Height_sprite >= block.Y and self.Y_sprite + self.Height_sprite <= block.Y + self.Gravity_sprite:
                         #and self.Y_sprite + self.Height_sprite <= i.Y + self.Gravity_sprite + 1:
                        self.Y_sprite = block.Y - self.Height_sprite 
                        # print(block.Y, self.Y_sprite + self.Height_sprite)
                        self.fall = False
                        break
                    else:
                        self.fall = True
                else:
                    self.fall = True
            else:
                self.fall = True

    def colision_up(self,list_level):
        for block in list_level:
            if self.X_sprite <= block.X + block.WIDTH:
                if self.X_sprite + self.Width_sprite >= block.X:
                    # if self.Y_sprite <= block.Y + block.HEIGHT and self.Y_sprite >= block.Y:
                    if self.Y_sprite <= block.Y + block.HEIGHT + 10 and self.Y_sprite + self.Height_sprite >= block.Y + block.HEIGHT:
                        self.Jump_distance = 0
                        self.fall = True
                    else:
                        self.fall = False
                else:
                    self.fall = False
            else:
                self.fall = False

    def colisium_right(self,list_level):
        for block in list_level:
            if self.Y_sprite + 1  <= block.Y + block.HEIGHT:
                if self.Y_sprite + self.Height_sprite - 1 >= block.Y:
                    if self.X_sprite + self.Width_sprite >= block.X - self.Speed_sprite :
                        if self.X_sprite <= block.X + block.WIDTH:
                            self.X_sprite = block.X - self.Width_sprite  - 1
                            self.move_right = False
                            break
                        else:
                            self.move_right = True
                    else:
                        self.move_right = True
                else:
                    self.move_right = True
            else:
                self.move_right = True
         
    def colisium_left(self,list_level):
        for block in list_level:
            if self.Y_sprite + 1  <= block.Y + block.HEIGHT:
                if self.Y_sprite + self.Height_sprite - 1 >= block.Y:
                    if self.X_sprite <= block.X + block.WIDTH + self.Speed_sprite:
                        if self.X_sprite + self.Width_sprite >= block.X:
                            self.X_sprite = block.X + block.WIDTH + 1
                            self.move_left = False
                            break
                        else:
                            self.move_left = True
                    else:
                        self.move_left = True
                else:
                    self.move_left = True
            else:
                self.move_left = True
    def ores_collision(self,list_ores):
        #Перебераем список руды
        for i in list_ores:
            #Условие касания с рудой
            if self.Y_sprite + self.Height_sprite >= i.Y and  self.Y_sprite <= i.Y + i.HEIGHT and self.X_sprite + self.Width_sprite >= i.X and self.X_sprite <= i.X + i.WIDTH:
                #Руда перемеается за экран(пропадает)
                i.X = -100
                #Увеличиваем счетчик руды
                if i.TYPE == 'diamond':
                    self.diamond += 1
                if i.TYPE == 'emerald':
                    self.emeralds += 1
                if i.TYPE == 'gold':
                    self.gold += 1
                if i.TYPE == 'silver':
                    self.silver += 1
                if i.TYPE == 'iron':
                    self.iron += 1

    def taverna(self, button, taverna, screen):
        keys = pygame.key.get_pressed()
        if self.X_sprite + self.Width_sprite >= taverna.X:
            if self.X_sprite <= taverna.X + taverna.WIDTH:
                if self.Y_sprite <= taverna.Y + taverna.HEIGHT:
                    if self.Y_sprite + self.Height_sprite >= taverna.Y:
                        button.show_image(screen)  
                        if keys[pygame.K_x]:
                            self.can_entern_taverna = True
    def leave_taverna(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] and self.can_entern_taverna:
            self.can_entern_taverna = False

    def damage(self, enemies, scene):
        for enemy in enemies:
            if enemy.cd == 0:
                # left
                if self.Y_sprite + 1 <= enemy.y_enemie + enemy.height_enemie:
                    if self.Y_sprite + self.Height_sprite - 1 >= enemy.y_enemie:
                        if self.X_sprite <= enemy.x_enemie + enemy.width_enemie + self.Speed_sprite:
                            if self.X_sprite + self.Width_sprite >= enemy.x_enemie:
                                self.hp -= enemy.damage
                                enemy.cd = 120
                # right
                elif self.Y_sprite + 1  <= enemy.y_enemie + enemy.height_enemie:
                    if self.Y_sprite + self.Height_sprite - 1 >= enemy.y_enemie:
                        if self.X_sprite + self.Width_sprite >= enemy.x_enemie - self.Speed_sprite :
                            if self.X_sprite <= enemy.x_enemie + enemy.width_enemie:
                                self.hp -= enemy.damage
                                enemy.cd = 120


            if enemy.cd > 0:
                enemy.cd -= 1
    def show_hp(self, screen):
        if self.hp >= self.hp_max-(self.hp_max*0.2):
            self.heart_path = "\\image\\hearts\\heart5.png"
        elif self.hp >= self.hp_max-(self.hp_max*0.4):
            self.heart_path = "\\image\\hearts\\heart4.png"
        elif self.hp >= self.hp_max-(self.hp_max*0.6):
            self.heart_path = "\\image\\hearts\\heart3.png"
        elif self.hp >= self.hp_max-(self.hp_max*0.8):
            self.heart_path = "\\image\\hearts\\heart2.png"
        elif self.hp > self.hp_max-(self.hp_max*1):
            self.heart_path = "\\image\\hearts\\heart1.png"
        elif self.hp <= 0:
            self.heart_path = "\\image\\hearts\\heart0.png"
            
        self.heart = os.path.abspath(__file__ + "/..")
        self.heart = self.heart + self.heart_path
        self.heart = pygame.image.load(self.heart).convert_alpha()
        self.heart = pygame.transform.scale(self.heart, (19*2, 25*2))
        # self.f1 = pygame.font.Font(None, 36)
        # self.text1 = self.f1.render(str(self.hp), True, (180, 0, 0))
        # screen.blit(self.text1, (200, 50))
        screen.blit(self.heart, (2, 2))
      