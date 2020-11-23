"""
File: music.py
Author: Diego Affonso
Email: dieguinho.affonso@gmail.com
Description:
    Module that manages the music of the application
"""

import random as rng
from midiutil.MidiFile import MIDIFile
from note import Note
from instrument import Instrument

def adjust(variable, parameter = 1, option='set'):
    """ Adjust the variable of the current music
        Attributes:

            option:
                option about how to ajust, can be:
                    'set' to set a raw value
                    'raise' to increase the actual value
                    'lower' to decrease the actual value
                    'half' to half the actual value
                    'double' to double the actual value

            parameter:
                parameter about how to adjust,
                    'set' will set the actual to that parameter
                    'raise' will increase that parameter
                    'lower' will decrease that parameter
                    'half' will half parameter times
                    'double' will double the parameter times
                    """
    operation = {
        'set': parameter,
        'raise': variable + parameter,
        'lower': variable - parameter,
        'half': variable / 2**parameter,
        'double': variable * 2**parameter,
    }
    result = operation[option]
    return result

class Music:
    """
    Class that manage the channels, instruments,
        notes and composes the music in general
    """
    def __init__(self, name = 'sample',
                 notes = [], bpm=120,
                 instrument = Instrument("Piano", 1),
                 volume = 100, octave = 4, actual_time = 0):
        self.midi_file = MIDIFile(1)
        self.actual_time = actual_time
        self.instrument = instrument
        self.octave = octave
        self.name = name
        self.notes = notes
        self.bpm = bpm
        self.volume = volume

    def generate(self):
        """ Generate a temporary midi_file for the music"""
        track = 0 #Only track
        time = 0 #Start at the beginning
        self.midi_file.addTrackName(track, time, self.name)
        self.midi_file.addTempo(track, time, self.bpm)

        channel = 0
        duration = 1

        for i,note in enumerate(self.notes):
            print(note.midi_number)
            current_instrument = note.instrument
            if i > 0:
                old_instrument = self.notes[i-1].instrument
            else:
                old_instrument = current_instrument

            if old_instrument != current_instrument:
                self.midi_file.addProgramChange(track, channel, i*2,
                                                current_instrument)

            self.midi_file.addNote(track, channel, note.midi_number * note.octave,
                                   i*2, duration, note.volume)

        with open("../temp/" + self.name + ".mid" , 'wb') as out:
            self.midi_file.writeFile(out)

    def adjust_instrument(self, parameter = 1, option='set'):
        """  Adjust the main instrument of the music"""
        self.instrument.midi_number = adjust(self.instrument.midi_number,
                                             parameter, option)

    def add_note(self, note):
        """ Add a note to the music stream, so it can be played"""
        note_volume = self.volume
        if int(note) >= 23:
            note = 23
        elif int(note) <= 12:
            note = 12
        current_instrument= self.instrument.midi_number
        self.notes.append(Note('', int(note), self.octave, current_instrument, note_volume))

    def add_random_note(self, minimum = 12, maximum = 23):
        """ Add a random note in the music strem"""
        if minimum < 12:
            minimum = 12
        elif maximum > 23:
            maximum = 23
        elif minimum > maximum:
            minimum = maximum

        note_number = rng.randint(min, max)
        self.add_note(note_number)

    def adjust_octave(self, parameter = 1, option='set'):
        """ Adjust the octave of the music"""
        self.octave = adjust(self.octave, parameter, option)
        if self.octave > 8:
            self.octave = 8
        elif self.octave < 0:
            self.octave = 0

    def adjust_volume(self,  parameter=1, option='double'):
        """ Adjust the volume of the music"""
        self.volume = adjust(self.volume, parameter, option)
        if self.volume> 127:
            self.volume= 127
        elif self.volume< 0:
            self.volume= 0

    def adjust_bpm(self,  parameter=1, option='set'):
        """ Adjust the bpm of the music"""
        self.bpm = adjust(self.bpm, parameter, option)
