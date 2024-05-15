import pygame
from Sprite import Sprite

class Levels():
    def __init__(self, p_sky, p_ground):
        self.sky = Sprite(p_sky,0,0)
        self.ground = Sprite(p_ground, 0, 300)
        self.obstacles = pygame.sprite.Group()
        
    def get_background(self):
        return [self.sky, self.ground]
    
    def get_obstacles(self):
        return self.obstacles
        
    