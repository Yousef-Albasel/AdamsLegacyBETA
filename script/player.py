# Importing Game Files
import pygame
import sys
from random import randint
from spritesheet import SpriteSheet
from support import *
from timer import Timer
from settings import *

# Player Creation

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,group,collision_sprites):
        super().__init__(group)
        # General Setup
        self.pos = pos
        self.group = group
        self.z = LAYERS['main']
        # Animation Status
        self.import_assets()
        self.running = False
        self.frame_index = 0
        self.status = 'idle_front' # initial value
        # Surface setup
        self.image = self.animations[self.status][self.frame_index]
        self.image = pygame.transform.scale(self.image, (int(64 * SCALE_FACTOR), int(64 * SCALE_FACTOR)))  # Scale the image
        self.rect = self.image.get_rect(center = pos)
        # Collision Setup
        self.hitbox = self.rect.copy().inflate((-((64*SCALE_FACTOR)-15*SCALE_FACTOR),-((64*SCALE_FACTOR)-25*SCALE_FACTOR)))        
        self.collision_sprites = collision_sprites
        
        # Movement attributes 
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 100
        #Timers   
        self.timers = {
            'attack' : Timer(500)
            # add more timers           
                       }
        
    # importing assets for player
    def import_assets(self):
        self.animations = {'idle_front':[],
                           'idle_back':[],
                           'idle_right':[],
                           'idle_left':[],
                          
                           'walk_front':[],
                           'walk_back':[],
                           'walk_right':[],
                           'walk_left':[],
                           
                           'attack1_front':[],
                           'attack1_back':[],
                           'attack1_right':[],
                           'attack1_left':[],
                           
                           'run_front':[],
                           'run_back':[],
                           'run_right':[],
                           'run_left':[],

                           'attack2_front':[],
                           'attack2_back':[],
                           'attack2_right':[],
                           'attack2_left':[],
                           
                           'attack3_front':[],
                           'attack3_back':[],
                           'attack3_right':[],
                           'attack3_left':[],
                           
                           'hurt_front':[],
                           'hurt_back':[],
                           'hurt_right':[],
                           'hurt_left':[]
                           }
        # this will loop in the assets folder, and fill the dictionary
        for animation in self.animations:
            full_path = "F:\Projects i work on personally\PopAdam - Adam's Legacy/assets\Peasant_P3/" + animation
            self.animations[animation] = import_folder(full_path)
    # create a loop for animations
    def animate(self,dt):
        self.frame_index += 15 *dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]
        self.image = pygame.transform.scale_by(self.image,SCALE_FACTOR)
    # inputs for game 
    def input(self):

        keys = pygame.key.get_pressed()
        if not self.timers['attack'].active:
            # Simple movement :
            if keys[pygame.K_w]:
                self.direction.y = -1
                self.status = 'walk_back'
                if keys[pygame.K_w] and keys[pygame.K_LCTRL]:
                    self.status = self.status.replace("walk", "run")
                    self.running = True

 
            elif keys[pygame.K_s]:
                self.direction.y = 1
                self.status = 'walk_front'
                if keys[pygame.K_s] and keys[pygame.K_LCTRL]:
                    self.status = self.status.replace("walk", "run")
                    self.running = True


            else:
                self.direction.y = 0
                if self.direction.x == 0:
                    self.running = False


            if keys[pygame.K_a]:
                self.direction.x = -1
                self.status = 'walk_left'
                if keys[pygame.K_a] and keys[pygame.K_LCTRL]:
                    self.status = self.status.replace("walk", "run")
                    self.running = True

            elif keys[pygame.K_d]:
                self.direction.x = 1
                self.status = 'walk_right'
                if keys[pygame.K_d] and keys[pygame.K_LCTRL]:
                    self.status = self.status.replace("walk", "run")
                    self.running = True

            else:
                self.direction.x = 0
                if self.direction.y == 0:
                    self.running = False
            # attack movement

            if keys[pygame.K_p]:
                self.random_attack = randint(1,3)
                self.frame_index = 0
                self.timers['attack'].activate()
                self.direction = pygame.math.Vector2()
    
    # this one is changing status for idling and attacking

    def get_status(self):
        if self.direction.magnitude() == 0:
            self.status = 'idle'+'_'+self.status.split('_')[1]
        if self.timers['attack'].active:
            self.status = f'attack{self.random_attack}'+'_'+self.status.split('_')[1]
    # later for making damage system
    def get_target_pos(self):
            self.target_pos = self.rect.center + PLAYER_Attack_OFFSET[self.status.split('_')[1]]
    # Moving the rectangle
    def move(self,dt):
        if (self.status[:3] == 'run'):
            self.speed = 300
        else:
            self.speed=200
        #Normalizing a vector 
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # Horizental movement
        self.pos.x += self.direction.x * self.speed * dt
        self.hitbox.centerx = round(self.pos.x)
        self.rect.centerx = self.hitbox.centerx
        self.collision('horizontal')

        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.hitbox.centery = round(self.pos.y)
        self.rect.centery = self.hitbox.centery
        self.collision('vertical')

    # Collision system
    def collision(self,direction):
        for sprite in self.collision_sprites.sprites():
            if hasattr(sprite,'hitbox'):
                if sprite.hitbox.colliderect(self.hitbox):
                    if direction == 'horizontal':
                        if self.direction.x > 0: # Moving Right
                            self.hitbox.right = sprite.hitbox.left

                        if self.direction.x < 0: # Moving Left
                            self.hitbox.left = sprite.hitbox.right
                        self.rect.centerx = self.hitbox.centerx 
                        self.pos.x = self.hitbox.centerx
                    if direction == 'vertical':
                        if self.direction.y > 0: # Moving Right
                            self.hitbox.bottom = sprite.hitbox.top

                        if self.direction.y < 0: # Moving Left
                            self.hitbox.top = sprite.hitbox.bottom
                        self.rect.centery = self.hitbox.centery 
                        self.pos.y = self.hitbox.centery        
    
    # updating the timers
    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def update(self,dt):
        self.input()
        self.move(dt)
        self.animate(dt)
        self.get_status()
        self.update_timers()
        self.get_target_pos()