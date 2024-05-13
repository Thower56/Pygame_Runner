import pygame

class Sound():
    def __init__(self):
        self.bg_music = pygame.mixer.Sound('audio/music.wav')
        
    def play(self):
        self.bg_music.play(loops = -1)