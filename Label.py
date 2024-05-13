import pygame

class Label():
    def __init__(self, p_text, p_pos_x, p_pos_y, p_color=(111,196,169)):
        self.font = pygame.font.Font('font/Pixeltype.ttf', 50)
        self.pos_x = p_pos_x
        self.pos_y = p_pos_y
        self.color = p_color
        self.text = self.font.render(p_text, False, self.color)
        self.text_rect = self.text.get_rect(center = (self.pos_x, self.pos_y))
        
    def draw(self, p_screen):
        p_screen.blit(self.text, self.text_rect)
        
    def set_pos(self,p_pos_x, p_pos_y):
        self.pos_x, self.pos_y = p_pos_x, p_pos_y
    
    def set_color(self, p_color):
        self.color = p_color
        
    def set_font(self, p_font):
        self.font = p_font
    
    def set_text(self, p_text):
        self.text = self.font.render(p_text, False, self.color)