import pygame
from Obstacle import Obstacle
from random import choice

class GameLogic():
    def __init__(self):
        self.game_active = False
        
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1500)
        self.clock = pygame.time.Clock()
        
    def collisions_sprite(self, p_player, p_obstacle_group):
        if pygame.sprite.spritecollide(p_player.sprite, p_obstacle_group,False):
            p_obstacle_group.empty()
            self.game_active = False
        else: self.game_active = True
        
    def handle_event(self, event, p_obstacle_group):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif not self.game_active and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.game_active = True
            self.start_time = int(pygame.time.get_ticks()/1000)
        elif self.game_active and event.type == self.obstacle_timer:
            p_obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
