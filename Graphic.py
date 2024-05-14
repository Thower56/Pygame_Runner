import pygame
from Label import Label
from Sprite import Sprite

class Graphic():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,400))
        self.start_time = 0
        self.score = 0
        
        self.sky_surface = Sprite('graphics/Sky.png', 0, 0)
        self.ground_surface = Sprite('graphics/ground.png', 0, 300)
        
        self.player_stand = Sprite('graphics/Player/player_stand.png', 400, 200, True)
        self.player_stand.transform_rotozoom(0,2)
        
        self.game_name = Label('Pixel Runner', 400, 80)
        self.game_message = Label('Press space to run', 400, 330)
        self.score_message = Label(f'Your score: {self.score}', 400, 330)
        
    def display_score(self):
        current_time = int(pygame.time.get_ticks()/1000) - self.start_time
        score_onScreen = Label(f'Score: {current_time}', 400, 50, (64,64,64))
        score_onScreen.draw(self.screen)
        self.score = current_time
    
    def draw(self, player, obstacle_group):
        self.sky_surface.draw(self.screen)
        self.ground_surface.draw(self.screen)
        player.draw(self.screen)
        obstacle_group.draw(self.screen)
        
    def gameover(self):
        self.screen.fill((94,129,162))

        self.player_stand.draw(self.screen)

        self.score_message.set_text(f'Your score: {self.score}')
        self.game_name.draw(self.screen)

        if self.score == 0:
            self.game_message.draw(self.screen)
        else:
            self.score_message.draw(self.screen)
        self.start_time = int(pygame.time.get_ticks()/1000)