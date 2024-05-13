import pygame
from Obstacle import Obstacle
from Player import Player
from Graphic import Graphic
from Sound import Sound
from random import choice
from GameLogic import GameLogic

class GameEngine:
    def __init__(self):
        pygame.init()
        
        self.game_logic = GameLogic()
        self.graphic = Graphic()
        
        self.player = pygame.sprite.GroupSingle()
        self.obstacle_group = pygame.sprite.Group()
        self.player.add(Player())
        
        self.music = Sound()
        self.music.play()
        
        self.clock = pygame.time.Clock()

    def update(self):
        self.graphic.display_score()
        self.player.update()
        self.obstacle_group.update()
        self.graphic.display_score()
        self.game_logic.collisions_sprite(self.player, self.obstacle_group)

    def run(self):
        while True:
            for event in pygame.event.get():
                self.game_logic.handle_event(event, self.obstacle_group)
            if self.game_logic.game_active:
                self.graphic.draw(self.player, self.obstacle_group)
                self.update()
            elif self.game_logic.game_active == False:
                self.graphic.gameover()
            pygame.display.update()
            self.clock.tick(60)
