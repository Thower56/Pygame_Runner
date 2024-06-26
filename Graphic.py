import pygame
from Label import Label
from Sprite import Sprite

class Graphic():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,400))
        
        self.player_stand = Sprite('graphics/Player/player_stand.png', 400, 200, True)
        self.player_stand.transform_rotozoom(0,2)
        
        self.game_name = Label('Pixel Runner', 400, 80)
        self.game_message = Label('Press space to run', 400, 330)
        self.score_message = Label(f'Your score: {0}', 400, 330)
        self.level_message = Label(f'Your level: {0}', 400, 360)
        self.game_level_done = Label('Level Done !', 400, 350)
        
    def display_score(self, p_score: int) -> None:
        score_onScreen = Label(f'Score: {p_score}', 400, 50, (64,64,64))
        score_onScreen.draw(self.screen)
    
    def display_level(self, p_level: int) -> None:
        level_onScreen = Label(f'Level: {p_level}', 60, 50, (64,64,64))
        level_onScreen.draw(self.screen)

    def draw(self, p_player: Sprite, p_level: Sprite) -> None:
        for element in p_level.get_background():
            element.draw(self.screen)
        obstacles = p_level.get_obstacles()
        obstacles.draw(self.screen)
        p_player.draw(self.screen)
        
    def gameover(self, p_score: int, p_level: int) -> None:
        self.screen.fill((94,129,162))

        self.player_stand.draw(self.screen)

        self.score_message.set_text(f'Your score: {p_score}')
        self.level_message.set_text(f'Your level: {p_level}')
        self.game_name.draw(self.screen)

        if p_score == 0:
            self.game_message.draw(self.screen)
        else:
            self.score_message.draw(self.screen)
            self.level_message.draw(self.screen)
        
    def leveldone(self) -> None:
        self.screen.fill((94,129,162))

        self.player_stand.draw(self.screen)
        self.game_name.draw(self.screen)
        self.game_level_done.draw(self.screen)
