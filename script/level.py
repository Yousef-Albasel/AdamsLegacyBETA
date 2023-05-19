# importing game files
import pygame
import sys
from settings import *
from player import Player
from spritesheet import SpriteSheet
from dummy import Dummy
from sprites import *
from pytmx.util_pygame import load_pygame
BLACK = (255, 255, 255)

# Creating the level
class Level():
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = CameraGroup()
        self.collision_sprites = pygame.sprite.Group()
        self.setup()

    # importing all game assets

    def setup(self):
        # map creation:
        tmx_data = load_pygame(
            "F:\Projects i work on personally\PopAdam - Adam's Legacy/map/map.tmx")

        self.map = pygame.image.load(
            "F:\Projects i work on personally\PopAdam - Adam's Legacy\map/map.png").convert_alpha()

        Generic(pos=(0, 0), surf=self.map,
                groups=self.all_sprites, z=LAYERS['ground'])
        
        # creating the players
        self.player = Player((1500, 900), self.all_sprites,self.collision_sprites)

        # Import the trees :
        for obj in tmx_data.get_layer_by_name('Trees'):
            pos = (obj.x*SCALE_FACTOR, obj.y*SCALE_FACTOR )  # Scale up the position
            Trees(pos, obj.image, [self.all_sprites,self.collision_sprites])
        
        
        # importing the Bushes
        for layer in ['Bushes-main']:
            for x, y, surf in tmx_data.get_layer_by_name(layer).tiles():
                pos = (x * 16 * SCALE_FACTOR, y *  16* SCALE_FACTOR)  # Scale up the position
                Generic(pos,
                        surf,
                        [self.all_sprites,self.collision_sprites],
                        )
        # importing the statues

        for layer in ['Statue']:
            for x, y, surf in tmx_data.get_layer_by_name(layer).tiles():
                pos = (x * 16*SCALE_FACTOR, y *  16*SCALE_FACTOR)  # Scale up the position
                Generic(pos,
                        surf,
                        [self.all_sprites,self.collision_sprites],
                        )
        # importing the borders 
        for x , y , surf in tmx_data.get_layer_by_name('Collision').tiles():
            Generic((x*16*SCALE_FACTOR,y*16*SCALE_FACTOR),pygame.Surface((16,16)),self.collision_sprites)
    # running the level:
    def run(self, dt):
        self.display_surface.fill('black')
        # show frame image

        # self.all_sprites.draw(self.display_surface)
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)

# Creating the camera
class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
# drawing the images
    def custom_draw(self, player):
        # Centering the character
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2
        # draw it in sorted way 
        for layer in LAYERS.values():
            for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
                if sprite.z == layer:
                    # take the pos of each sprites
                    offset_rect = sprite.rect.copy()
                    
                    # offset_rect.x *=SCALE_FACTOR 
                    # offset_rect.y *= SCALE_FACTOR
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)
                    # debug
                    # pygame.draw.rect(self.display_surface,'red',offset_rect,5)
                    # hitbox_rect=sprite.hitbox.copy()
                    # hitbox_rect.center = offset_rect.center
                    # pygame.draw.rect(self.display_surface,'green',hitbox_rect,5)