import pygame
from pygame import midi
from instrument import Instrument
from misc import adjust

class Player:
    """
    Class that manages the player, pauses, plays,
        manage the volume, and the music
    """
    def __init__(self, pygame_player = None, current_music = None, volume=100, state='paused', bpm=100):
        self.pygame_player = pygame_player
        self.current_music = current_music
        self.current_instrument = Instrument("Piano", 1)
        self.volume = volume
        self.state = state
        self.bpm = bpm

    def adjust_volume(self, option = 'raise', parameter = '1'):
        """ Adjust the volume of the player """
        self.volume = adjust(self.volume, option, parameter)

    def set_instrument(self, instrument):
        """Set the current instrument """
        self.current_instrument = instrument

    def playMusic():
        """ Play a given music """

    def pauseMusic():
        """ Pause the music already in play, if it’s played again, start from where it was paused """

    def stopMusic():
        """ Stop the music already in play, if it’s played again, start from the beginning """

    def increaseVolume():
        """ Raise the volume of the player """

    def decreaseVolume():
        """ Lower the volume of the player """

    def increaseBpm():
        """ Increases the current Bpm """

    def decreaseBpm():
        """ Decreases the value of the Bpm """
