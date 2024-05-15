import pygame
from Obstacle import Obstacle
from random import choice

class GameLogic():
    def __init__(self):
        self.game_active = False
        self.stage_done = False
        self.index_level = 1
        self.score = 0
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1500)
        self.clock = pygame.time.Clock()
        
    def collisions_sprite(self, p_player, p_obstacle_group):
        if pygame.sprite.spritecollide(p_player.sprite, p_obstacle_group,False):
            p_obstacle_group.empty()
            self.game_active = False
            self.index_level = 0
        else: self.game_active = True
        
    def handle_event(self, event, p_obstacle_group):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif not self.game_active and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.game_active = True
            self.start_time = int(pygame.time.get_ticks()/1000)
            self.reset_score()
            if self.stage_done:
                self.index_level += 1
                self.inc_difficulty(p_obstacle_group)
        elif self.game_active and event.type == self.obstacle_timer:
            p_obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
            self.inc_difficulty(p_obstacle_group)


    def calculate_score(self):
        current_time = int(pygame.time.get_ticks()/1000) - self.start_time
        self.score = current_time
    
    def get_score(self):
        return self.score
    
    def check_win_condition(self, p_obstacle_group):
        if self.score == 10:
            self.game_active = False
            p_obstacle_group.empty()
            self.stage_done = True
            
    def reset_score(self):
        self.score = 0
        
    def change_level(self):
        return self.index_level
    
    def inc_difficulty(self, obstacles):
        for obstacle in obstacles:
            obstacle.speed_up((self.index_level + 1) * 2)    