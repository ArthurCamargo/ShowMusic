"""
File: player.py
Author: Joao Maieron
Email: joaomaieron@gmail.com
Description:
    Module that manages the musics, volumes, instruments, and bpm
    of the music
"""

import pygame
import time
from pygame import mixer
from instrument import Instrument
from misc import adjust

class Player:
    """
    Class that manages the player, pauses, plays,
        manage the volume, and the music
    """
    def __init__(self,  current_music = None,
                 current_instrument = Instrument("Piano", 1),
                 volume=100,
                 state='paused',
                 bpm=100):
        pygame.mixer.init()
        self.pygame_player = pygame.mixer
        self.current_music = current_music
        self.current_instrument = current_instrument
        self.volume = volume
        self.state = state

    def adjust_volume(self, option = 'raise', parameter = '1'):
        """ Adjust the volume of the player """
        self.volume = adjust(self.volume, option, parameter)

    def load_music(self, file_path):
        """ Loads a music into the player"""
        self.pygame_player.music.load(file_path)

    def set_instrument(self, instrument):
        """Set the current instrument """
        self.current_instrument = instrument

    def toogle_play_pause(self):
        """ Pause the music already in play, if it’s played again,
        start from where it was paused """
        if self.state == 'playing':
            self.state = 'paused'
            self.pygame_player.music.pause()
        else:
            self.state = 'playing'
            self.pygame_player.music.play()

    def stop_music(self):
        """ Stop the music already in play, if it’s played again, start from the beginning """
