import pygame
from Obstacle import Obstacle
from Player import Player
from Graphic import Graphic
from Sound import Sound
from random import choice

class GameEngine:
    def __init__(self):
        pygame.init()
        self.game_active = False
        self.start_time = None
        self.score = 0
        
        self.graphic = Graphic()
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player())
        self.music = Sound()
        self.music.play()
        
        self.obstacle_group = pygame.sprite.Group()
        
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1500)
        self.clock = pygame.time.Clock()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif not self.game_active and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.game_active = True
            self.start_time = int(pygame.time.get_ticks()/1000)
        elif self.game_active and event.type == self.obstacle_timer:
            self.obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))

    def collisions_sprite(self):
        if pygame.sprite.spritecollide(self.player.sprite, self.obstacle_group,False):
            self.obstacle_group.empty()
            return False
        else: return True

    def update(self):
        self.graphic.display_score()
        self.player.update()
        self.obstacle_group.update()
        self.graphic.display_score()
        self.game_active = self.collisions_sprite()
        
        

    def run(self):
        while True:
            for event in pygame.event.get():
                self.handle_event(event)
            if self.game_active:
                self.graphic.draw(self.player, self.obstacle_group)
                self.update()
            elif self.game_active == False:
                self.graphic.gameover()
                self.score = 0
            pygame.display.update()
            self.clock.tick(60)
