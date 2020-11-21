
class Instrument:
    """
    Class of Instruments, that have an name, sound
    and other instrument properties
    """
    def __init__(self, name, midi_number):
        self.name = name
        self.midi_number = midi_number
