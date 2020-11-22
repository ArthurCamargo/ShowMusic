"""
File: music.py
Author: Diego Affonso
Email: dieguinho.affonso@gmail.com
Description:
    Module that manages the music of the application
"""

import random as rng
from midiutil.MidiFile import MIDIFile
from misc import adjust
from note import Note
from instrument import Instrument

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
        self.volume = volume
        self.bpm = bpm

    def generate(self):
        """ Generate a temporary midi_file for the music"""
        track = 0 #Only track
        time = 0 #Start at the beginning
        self.midi_file.addTrackName(track, time, self.name)
        self.midi_file.addTempo(track, time, self.bpm)

        channel = 0
        volume = self.volume
        duration = 1

        for i,note in enumerate(self.notes):
            current_instrument = note.instrument
            if i > 0:
                old_instrument = self.notes[i-1].instrument
            else:
                old_instrument = current_instrument

            if old_instrument != current_instrument:
                self.midi_file.addProgramChange(track, channel, i*2,
                                                current_instrument)

            self.midi_file.addNote(track, channel, note.midi_number,
                                   i*2, duration, volume)

        with open("../temp/" + self.name + ".mid" , 'wb') as out:
            self.midi_file.writeFile(out)

    def adjust_instrument(self, parameter = 1, option='set'):
        """  Adjust the main instrument of the music"""
        self.instrument.midi_number = adjust(self.instrument.midi_number,
                                             parameter, option)

    def add_note(self, note):
        """ Add a note to the music stream, so it can be played"""
        if int(note) > 127:
            note = 127
        elif int(note) < 0:
            note = 0
        current_instrument= self.instrument.midi_number
        self.notes.append(Note('', int(note), self.octave, current_instrument))

    def add_random_note(self, minimum = 0, maximum = 127):
        """ Add a random note in the music strem"""
        if minimum < 0:
            minimum = 0
        elif maximum > 127:
            maximum = 127
        elif minimum > maximum:
            minimum = maximum

        note_number  = rng.randint(min, max)
        self.add_note(note_number)

    def adjust_octave(self, parameter = 1, option='set'):
        """ Adjust the octave of the music"""
        self.octave = adjust(self.octave, parameter, option)

    def adjust_volume(self,  parameter=1, option='set'):
        """ Adjust the volume of the music"""
        self.volume = adjust(self.volume, parameter, option)

    def adjust_bpm(self,  parameter=1, option='set'):
        """ Adjust the bpm of the music"""
        self.bpm = adjust(self.bpm, parameter, option)
