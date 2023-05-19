import os
import pygame 

class SpriteSheet():
    def __init__(self):
        self.idle_front = []
        self.idle_right = []
        self.idle_left = []
        self.idle_back = []
        self.walk_front = []
        self.walk_right = []
        self.walk_left = []
        self.walk_back = []
        
        base_path = os.path.join(os.path.dirname(__file__), "F:\Projects i work on personally\PopAdam - Adam's Legacy\\assets\Peasant_P3/")
        folders = ["idle_front", "idle_right", "idle_left", "idle_back", "walk_front", "walk_right", "walk_left", "walk_back"]
        
        for folder in folders:
            folder_path = os.path.join(base_path, folder)
            for i in range(0, 120):
                file_name = os.path.join(folder_path, f"Peasant_P3-{i}.png")
                print("Loading file:", file_name) # add this line
                frame = pygame.image.load(file_name).convert_alpha()
                if folder == "idle_front":
                    self.idle_front.append(frame)
                elif folder == "idle_right":
                    self.idle_right.append(frame)
                elif folder == "idle_left":
                    self.idle_left.append(frame)
                elif folder == "idle_back":
                    self.idle_back.append(frame)
                elif folder == "walk_front":
                    self.walk_front.append(frame)
                elif folder == "walk_right":
                    self.walk_right.append(frame)
                elif folder == "walk_left":
                    self.walk_left.append(frame)
                elif folder == "walk_back":
                    self.walk_back.append(frame)
        print(len(self.idle_front))
        print(len(self.idle_right))
        print(len(self.idle_left))
        print(len(self.idle_back))
        print(len(self.walk_front))
        print(len(self.walk_right))
        print(len(self.walk_left))
        print(len(self.walk_back))
