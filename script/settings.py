from pygame.math import Vector2
SCREEN_WIDTH = 1280	
SCREEN_HEIGHT = 720 
SCALE_FACTOR = 2.5
PLAYER_Attack_OFFSET = {
	'left': Vector2(-50,40),
	'right': Vector2(50,40),
	'front': Vector2(0,-10),
	'back': Vector2(0,50)
}
LAYERS = {
	'water': 0,
	'ground': 1,
	'ground plant': 2,
	'main': 3,
}
