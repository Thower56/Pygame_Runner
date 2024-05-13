import pygame

class Sprite():
    def __init__(self, p_sprite, p_pos_x, p_pos_y, p_alpha=False):
        if p_alpha == True: self.sprite = pygame.image.load(p_sprite).convert_alpha()
        else: self.sprite = pygame.image.load(p_sprite).convert()
        
        self.pos_x = p_pos_x
        self.pos_y = p_pos_y
        
    def draw(self, p_screen):
        p_screen.blit(self.sprite, (self.pos_x, self.pos_y))
        
    def set_pos(self, p_pos_x, p_pos_y):
        self.pos_x, self.pos_y = p_pos_x, p_pos_y