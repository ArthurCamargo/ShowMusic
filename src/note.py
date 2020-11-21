from pygame import midi

class Note:
    """ Class of musical notes """
    def __init__(self, name, midi_number, octave=4):
        #Name of the note
        self.name = name
        #Midi number of the note
        self.midi_number = midi_number
        #Current octave of the note
       self.octave = octave

    def __str__(self):
        string = ('Name(name=' + str(self.name) + '), '
                  +'Number(number=' + str(self.midi_number) + '), '
                  +'Octave(octave=' + str(self.octave) +')' )
        return string

    def increaseOctave():
        """ Increase the octave of the note """

    def decreaseOctave():
        """ Decrease the octave of the note """
