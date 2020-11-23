"""
File: note.py
Author: Arthur Camargo
Email: arthurcamargo13@gmail.com
Description:
    Module that handles the notes
"""

class Note:
    """ Class of musical notes """
    def __init__(self, name, midi_number, octave=0,
                 instrument = 1, volume = 30):
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
        string = ("Name:" + str(self.name) + ' '
                 "Midi:" + str(self.midi_number) + ' '
                 "Octave:" + str(self.octave) + ' '
                 "Instrument:" + str(self.instrument) + ' '
                 "Volume:" + str(self.volume))
        return string
