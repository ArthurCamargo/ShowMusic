"""
File: player.py
Author: Joao Maieron
Email: joaomaieron@gmail.com
Description:
    Module that manages the musics, volumes, instruments, and bpm
    of the music
"""

import pygame

class Player:
    """
    Class that manages the player, pauses, plays,
        manage the volume, and the music
    """
    def __init__(self):
        pygame.mixer.init()
        self.pygame_player = pygame.mixer

    def load_music(self, file_path):
        """ Loads a music into the player"""
        self.pygame_player.music.load(file_path)

    def play(self):
        """ Play a music that already compiled"""
        self.pygame_player.music.play(0)

    def stop(self):
        """ Stop the music already in play, if it’s played again, start from the beginning """
        self.pygame_player.music.stop()
