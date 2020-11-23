"""
File: note.py
Author: Arthur Camargo
Email: arthurcamargo13@gmail.com
Description:
    Module that handles the notes
"""

from pygame import midi
from instrument import Instrument

class Note:
    """ Class of musical notes """
    def __init__(self, name, midi_number, octave=4,
                 instrument = 1, volume = 100):
        #Name of the note
        self.name = name
        #Midi number of the note
        self.midi_number = midi_number
        #Current octave of the note
        self.octave = octave
        #Instrument that the note will be played
        self.instrument = instrument
        #Volume of the note
        self.volume = volume

    def __str__(self):
        print(self.name, self.midi_number, self.instrument, self.volume)
