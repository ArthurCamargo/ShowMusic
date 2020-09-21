from pygame import midi
from Music import Music

class Player:
    """
    Class that manages the player, pauses, plays,
    manage the volume, and the music
    """
    def __init__(self, pygame_player, current_music=None, volume):
        Player.pygame_player = pygame_player

