import pygame

class Sound():
    def __init__(self) -> None:
        self.bg_music = pygame.mixer.Sound('audio/music.wav')
        self.bg_music.set_volume(0.01)
    def play(self) -> None:
        self.bg_music.play(loops = -1)