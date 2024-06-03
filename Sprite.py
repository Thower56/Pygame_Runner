import pygame

class Sprite():
    def __init__(self, p_sprite, p_pos_x, p_pos_y, p_alpha=False) -> None:
        self.alpha = p_alpha
        if self.alpha == True:
            self.sprite = pygame.image.load(p_sprite).convert_alpha()
            self.sprite_rect = self.sprite.get_rect(center = (p_pos_x, p_pos_y))
        else:
            self.sprite = pygame.image.load(p_sprite).convert()
        
        self.pos_x = p_pos_x
        self.pos_y = p_pos_y
        
    def draw(self, p_screen) -> None:
        if self.alpha:
            p_screen.blit(self.sprite, self.sprite_rect)
        else:
            p_screen.blit(self.sprite, (self.pos_x, self.pos_y))
        
    def set_pos(self, p_pos_x, p_pos_y) -> None:
        self.pos_x, self.pos_y = p_pos_x, p_pos_y
        
    def transform_rotozoom(self, angle, scale) -> None:
        self.sprite = pygame.transform.rotozoom(self.sprite, angle, scale)
        self.sprite_rect = self.sprite.get_rect(center = (self.pos_x, self.pos_y))
        
    def transform_flip(self) -> None:
        self.sprite = pygame.transform.flip(self.sprite, True, False)
        
        
        