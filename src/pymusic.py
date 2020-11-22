import pygame
import time
import pygame.midi
from midiutil.MidiFile import MIDIFile

pygame.mixer.init()
pygame.mixer.music.load("../temp/Sample Name.mid")
pygame.mixer.music.play(0)
length = pygame.time.get_ticks()
while pygame.mixer.music.get_busy():
    pygame.time.wait(length)
