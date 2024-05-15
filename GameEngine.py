import pygame
from Obstacle import Obstacle
from Player import Player
from Graphic import Graphic
from Sound import Sound
from random import choice
from GameLogic import GameLogic
from Sprite import Sprite
from Levels import Levels

class GameEngine:
    def __init__(self):
        pygame.init()
        
        self.game_logic = GameLogic()
        self.graphic = Graphic()
        
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player())
        
        self.level_1 = Levels('graphics/Sky_1.png' , 'graphics/ground_1.png')
        self.level_2 = Levels('graphics/Sky_2.png' , 'graphics/ground_2.png')
        self.level_3 = Levels('graphics/Sky_3.png' , 'graphics/ground_3.png')

        self.levels = [self.level_1, self.level_2, self.level_3]
        self.level_index = 0
        
        self.music = Sound()
        self.music.play()
        
        self.clock = pygame.time.Clock()

    def update(self):
        self.player.update()
        self.levels[self.level_index % len(self.levels)].get_obstacles().update()
        self.game_logic.calculate_score()
        self.graphic.display_score(self.game_logic.get_score())
        self.game_logic.collisions_sprite(self.player, self.levels[self.level_index % len(self.levels)].get_obstacles())
        self.game_logic.check_win_condition(self.levels[self.level_index % len(self.levels)].get_obstacles())

    def run(self):
        while True:
            for event in pygame.event.get():
                self.game_logic.handle_event(event, self.levels[self.level_index % len(self.levels)].get_obstacles())
                
            if self.game_logic.game_active:
                self.graphic.draw(self.player, self.levels[self.level_index % len(self.levels)])
                self.update()
  
            elif not self.game_logic.game_active:
                if self.game_logic.get_score() >= 10:
                    self.graphic.leveldone()
                    self.level_index = self.game_logic.change_level()
                    self.player.sprite.reset_pos()

                else:
                    self.graphic.gameover(self.game_logic.get_score())
                    self.player.sprite.reset_pos()
                    self.level_index = 0
                    
            pygame.display.update()
            self.clock.tick(60)
