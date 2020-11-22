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
    def __init__(self, name = 'Sample Name',
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

            old_instrument = self.notes[i-1].instrument
            current_instrument = note.instrument

            if old_instrument != current_instrument:
                self.midi_file.addProgramChange(track, channel, i*2, current_instrument)

            self.midi_file.addNote(track, channel, note.midi_number,
                                   i*2, duration, volume)
        with open("../temp/" + self.name + ".mid" , 'wb') as out:
            self.midi_file.writeFile(out)

    def adjust_instrument(self, option='set', parameter='1'):
        """  Adjust the main instrument of the music"""
        self.instrument.midi_number = adjust(self.instrument.midi_number,
                                             option, parameter)

    def add_note(self, note):
        """ Add a note to the music stream, so it can be played"""
        if int(note) > 127:
            note = 127
        elif int(note) < 0:
            note = 0
        self.notes.append(Note('', int(note), self.octave, self.instrument))

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

    def adjust_octave(self, option='set', parameter='1'):
        """ Adjust the octave of the music"""
        self.octave = adjust(self.octave, option, parameter)

    def adjust_volume(self, option='set', parameter='1'):
        """ Adjust the volume of the music"""
        self.volume = adjust(self.volume, option, parameter)

    def adjust_bpm(self, option='set', parameter='1'):
        """ Adjust the bpm of the music"""
        self.bpm = adjust(self.bpm, option, parameter)

