from pygame import midi

class Parser:
    """ Receives a stream of characters, a file of configuration and do functions based and that configuration """
    def __init__(self, configuration_file, stream_char, dictionary):
        self.configuration_file = configuration_file
        self.stream_char = stream_char
        self.octave = dictionary

    def loadConfiguration():
        """ Load a configuration to the dictionary """
        pass
        
    def parse():
        """ Do what was typed in the editor, based on the configuration already loaded """
        pass
    
    def createNote():
        """ Creates a note """
        pass
    
    def randomNote():
        """ Generates a random note """
        pass
    
    def doubleVolume():
        """ Doubles the current volume """
        pass
    
    def defaultVolume():
        """ Defines current volume as it was on the beginning """
        pass
    
    def repeatNote():
        """ Repeats the previous note """
        pass
        
    def increaseOctave():
        """ Increases the current octave """
        pass
        
    def decreaseOctave():
        """ Decreases the current octave """
        pass
    
    def increaseBpm():
        """ Increases the current Bpm """
        pass
    
    def decreaseBpm():
        """ Decreases the value of the Bpm """
        pass
