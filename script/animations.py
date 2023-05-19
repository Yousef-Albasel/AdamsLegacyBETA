import pygame
class Animation:
    def __init__(self):
        pass
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