from pygame import midi

class Music:
    """
    Class that manage the channels, instruments,
        notes and composes the music in general
    """
    def __init__(self, pygame_player, name = '',  active_channels=[], bpm=100):
        self.pygame_player = pygame_player
        self.name = name
        self.active_channels = active_channels
        self.bpm = bpm

    def printMusic():
        """ Prints the music to save it in a file """
        pass
