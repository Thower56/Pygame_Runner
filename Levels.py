import pygame
from Sprite import Sprite

class Levels():
    def __init__(self, p_sky, p_ground):
        self.sky = Sprite(p_sky,0,0)
        self.ground = Sprite(p_ground, 0, 300)
        
        self.sky_r = Sprite(p_sky,800,0)
        self.sky_r.transform_flip()
        self.ground_r = Sprite(p_ground, 800, 300)
        self.ground_r.transform_flip()
        
        self.obstacles = pygame.sprite.Group()
        
    def get_background(self) -> list[Sprite]:
        return [self.sky, self.sky_r, self.ground, self.ground_r]
    
    def get_obstacles(self) -> pygame.sprite.Group:
        return self.obstacles
    
    def reflect_background(self) -> list[Sprite]:
        return [(pygame.transform.flip(self.sky, True, False)), (pygame.transform.flip(self.ground, True, False))]
    
    def moving(self):
        if self.sky.pos_x > -800:
            self.sky.pos_x = self.sky.pos_x - 2
        elif self.sky.pos_x <= -800:
            self.sky.pos_x = 800
            
        if self.sky_r.pos_x > -800:
            self.sky_r.pos_x = self.sky_r.pos_x - 2
        elif self.sky_r.pos_x <= -800:
            self.sky_r.pos_x = 800
            
        if self.ground.pos_x > -800:
            self.ground.pos_x = self.ground.pos_x - 5
        elif self.ground.pos_x <= -800:
            self.ground.pos_x = 800
            
        if self.ground_r.pos_x > -800:
            self.ground_r.pos_x = self.ground_r.pos_x - 5
        elif self.ground_r.pos_x <= -800:
            self.ground_r.pos_x =  800
        
    