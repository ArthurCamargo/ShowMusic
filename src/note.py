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
