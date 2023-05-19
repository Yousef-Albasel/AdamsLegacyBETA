import pygame
from random import randint
from support import *
from timer import Timer
class Dummy(pygame.sprite.Sprite):
    def __init__(self,pos,group,z):
        super().__init__(group)
        self.pos = pos
        self.group = group
        # Animation Status
        self.import_assets()
        self.running = False
        self.frame_index = 0
        self.status = 'idle_front'
        self.image = self.animations[self.status][self.frame_index]
        self.image = pygame.transform.scale_by(self.image,3)
        self.rect = self.image.get_rect(center = pos)
        self.z=z
        # Movement attributes 
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
        #Timers
        self.timers = {'attack':Timer(350)}
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
        for animation in self.animations:
            full_path = "F:\Projects i work on personally\PopAdam - Adam's Legacy/assets\Peasant_P3/" + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self,dt):
        self.frame_index += 12 *dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]
        self.image = pygame.transform.scale_by(self.image,1.7)


    def get_status(self):
        if self.direction.magnitude() == 0:
            self.status = 'idle'+'_'+self.status.split('_')[1]
        if self.timers['attack'].active:
            self.status = f'attack{self.random_attack}'+'_'+self.status.split('_')[1]
    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def update(self,dt):
        self.animate(dt)
        self.get_status()
        self.update_timers()