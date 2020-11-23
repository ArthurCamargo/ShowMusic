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
    def __init__(self,  current_music = None,
                 volume=100,
                 state='stopped'):
        pygame.mixer.init()
        self.pygame_player = pygame.mixer
        self.current_music = current_music
        self.volume = volume
        self.state = state

    def load_music(self, file_path):
        """ Loads a music into the player"""
        self.pygame_player.music.load(file_path)

    def play(self):
        """ Play a music that already compiled"""
        if self.state == 'stopped':
            self.state = 'playing'
            self.pygame_player.music.play(0)

    def stop(self):
        """ Stop the music already in play, if it’s played again, start from the beginning """
        if self.state == 'playing':
            self.state = 'stopped'
            self.pygame_player.music.stop()
