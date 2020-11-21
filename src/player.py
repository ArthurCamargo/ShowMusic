import pygame
from pygame import midi

class Player:
    """
    Class that manages the player, pauses, plays,
        manage the volume, and the music
    """
    def __init__(self, pygame_player, current_music=None, volume=100, state='paused', bpm=100):
        self.pygame_player = pygame_player
        self.current_music = current_music
        self.volume = volume
        self.state = state
        self.bpm = bpm

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
