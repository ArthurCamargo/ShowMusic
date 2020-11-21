from pygame import midi
from misc import adjust
from note import Note


class Music:
    """
    Class that manage the channels, instruments,
        notes and composes the music in general
    """
    def __init__(self, name = '', notes = [], bpm=100, octave = 4):
        self.name = name
        self.octave = octave
        self.notes = notes
        self.bpm = bpm

    def add_note(self, note, name):
        """ Add a note to the music stream, so it can be played"""
        self.notes.append(Note)


    def adjust_octave(self, option='set', parameter='1'):
        """ Adjust the octave of the music"""
        self.octave = adjust(self.octave, option, parameter)

    def adjust_bpm(self, option='set', parameter='1'):
        """ Adjust the bpm of the music"""
        self.bpm = adjust(self.bpm, option, parameter)

    def printMusic(self):
        """ Prints the music to save it in a file """
