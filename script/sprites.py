from settings import *
import pygame
class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z=LAYERS['main']):
        super().__init__(groups)
        self.image = pygame.transform.scale(surf, (int(surf.get_width() * SCALE_FACTOR), int(surf.get_height() * SCALE_FACTOR)))  # Scale the image
        self.rect = self.image.get_rect(topleft=pos)
        self.z = z
        self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.2, -self.rect.height * 0.75)

class Trees(Generic):
    def __init__(self,pos,surf,groups):
        super().__init__(pos,surf,groups)