from pygame import midi

class Note:
    """ Class of musical notes """
    def __init__(self, name, note_number, octave=4):
        self.name = name
        self.note_number = note_number
        self.octave = octave
        #Name of the note
        self.name = name
        #Midi number of the note
        self.midi_number = note_number
        #Current octave of the note
        self.octave = octave

    def __str__(self):
        string = ('Name(name=' + str(self.name) + '), '
                  +'Number(number=' + str(self.note_number) + '), '
                  +'Octave(octave=' + str(self.octave) +')' )
        return string

    def increaseOctave():
        """ Increase the octave of the note """
        pass

    def decreaseOctave():
        """ Decrease the octave of the note """
        pass
