import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.01)

    def player_input(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()
        elif keys[pygame.K_a]:
            if self.rect.left >= 10:
                self.rect.left -= 5
        elif keys[pygame.K_d]:
            if self.rect.right <= 800:
                self.rect.right += 5

    def apply_gravity(self) -> None:
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self) -> None:
        if self.rect.bottom < 300:
         self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk) : self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
    
    def reset_pos(self) -> None:
        self.rect = self.image.get_rect(midbottom = (80,300))

    def update(self) -> None:
        self.player_input()
        self.apply_gravity()
        self.animation_state()