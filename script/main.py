import pygame, sys
from settings import *
from level import Level

class Game:
	def __init__(self):
		pygame.init()
		WINDOW_FLAGS = pygame.SCALED | pygame.RESIZABLE
		self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),WINDOW_FLAGS)
		pygame.display.set_caption('PopAdam: Adam\'s Legacy')
		self.clock = pygame.time.Clock()
		self.level = Level()
		 
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			dt = self.clock.tick() / 1000
			self.level.run(dt)
			pygame.display.update()

if __name__ == '__main__':
	game = Game()
	game.run()