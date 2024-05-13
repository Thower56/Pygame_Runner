import pygame

class Graphic():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,400))
        self.test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
        self.start_time = 0
        self.score = 0
        
        self.sky_surface = pygame.image.load('graphics/Sky.png').convert()
        self.ground_surface = pygame.image.load('graphics/ground.png').convert()
        
        player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
        self.player_stand = pygame.transform.rotozoom(player_stand,0,2)
        self.player_stand_rect = player_stand.get_rect(center = (360,150))
        
        self.game_name = self.test_font.render('Pixel Runner', False, (111,196,169))
        self.game_name_rect = self.game_name.get_rect(center=(400,80))
        self.game_message = self.test_font.render('Press space to run', False, (111,196,169))
        self.game_message_rect = self.game_message.get_rect(center = (400,330))
        
    def display_score(self):
        current_time = int(pygame.time.get_ticks()/1000) - self.start_time
        score_surf = self.test_font.render(f'Score: {current_time}',False,(64,64,64))
        score_rect = score_surf.get_rect(center = (400,50))
        self.screen.blit(score_surf,score_rect)
        self.score = current_time
    
    def draw(self, player, obstacle_group):
        self.screen.blit(self.sky_surface,(0,0))
        self.screen.blit(self.ground_surface,(0,300))
        player.draw(self.screen)
        obstacle_group.draw(self.screen)
        
    def gameover(self):
        self.screen.fill((94,129,162))
        self.screen.blit(self.player_stand,self.player_stand_rect)

        self.score_message = self.test_font.render(f'Your score: {self.score}', False, (111,196,169))
        self.score_message_rect = self.score_message.get_rect(center = (400,330))
        self.screen.blit(self.game_name,self.game_name_rect)

        if self.score == 0:
            self.screen.blit(self.game_message, self.game_message_rect)
        else:
            self.screen.blit(self.score_message,self.score_message_rect)
        self.start_time = int(pygame.time.get_ticks()/1000)