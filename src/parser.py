from pygame import midi
from music import Music
from player import Player
from instrument import Instrument

# Commands needed:
# Notes : anyone 
# Repeat Note if
# Raise volume : any value
# Lower volume : any value
# Instrument : anyone
# Consonants : anyone
# Last Note: just the last one
# Octave: any value



class Parser:
    """ Receives a stream of characters, a file of configuration and do functions 
        based and that configuration

        Attributes:
            configuration_file: file with the configuration of the
                parser
            text_area: string from the text editor
            alias: dictionary of aliases to make the configuration more
                readable
            commands: dictionary used to map the commands with
                and instructions 
            variables: dictionary of variables that can be used to
                get information about the music and about the notes"""

    def __init__(self, configuration_file):
        self.configuration_file = configuration_file
        self.text_area= []
        self.text_lines = []
        self.alias = {}
        self.commands = {}
        self.variables = {}

    def remove(self, string, char=' ', side='after'):
        """ Remove from a string a substring before or afters a
        char, inclusive the char.

            Options:
                string: string to be removed
                char: delimiter of the string, ' ' by default
                side: can be 'before' or 'after',
                    parameter that chooses the side that the
                    subtring will be removed, 'after' by default """
        delimiter_index = string.find(char)
        if delimiter_index == -1:
            return string

        if side == 'after':
            return string[:delimiter_index]
        elif side == 'before':
            # + 1 because te delimiter don't exclue the
            # actual character
            return string[delimiter_index + 1:]
        else:
            return string

    def config_commands(self, line):
        """ Insert the commands configuration in the dictionary
            of commands"""
        if '[' in line and ']' in line:
            line = self.remove(line, '[','before')
            line = self.remove(line, ']','after')

            tokens = line.split("->")
            for i in range(len(tokens)):
                tokens[i] = tokens[i].strip("() ")

            for i in range(len(tokens)):
                if str(tokens[i]) in self.alias:
                    tokens[i] = self.alias[str(tokens[i])]

            self.commands[tokens[0]] = tokens[1]
            print(tokens)

    def config_alias(self, line):
        """ Insert the command configuration in the dictionary
            of aliases"""
        if not'[' in line and not ']' in line:
            tokens = line.split("=")

            for i in range(len(tokens)):
                tokens[i] = tokens[i].strip("() ")

            self.alias[tokens[0]] = tokens[1]
            print(self.alias)

    def config_parse(self, file_handler):
        """ Parse the configuration file and transform it
        into a dictionary"""

        for line in file_handler:
            line = self.remove(line, '*', 'after')

            #remove whitespaces
            line = line.strip()

            #Only operate on non-empty strings
            if line:
                self.config_alias(line)
                self.config_commands(line)
                #self.config_variable(line)


    def load_configuration(self):
        """ Load a configuration to the dictionary """
        file_handler = open(self.configuration_file, "r")
        self.config_parse(file_handler)
        file_handler.close()

    def parse(self):
        """ Do what was typed in the editor, based on the
        configuration already loaded """
        for line in self.text_lines:
            for char in line:
                self.interpret(char)

    def interpret(self, char):
        """ Interpret a command"""
        pass

    def createNote():
        """ Creates a note """

    def randomNote():
        """ Generates a random note """
        print("Pretty random han")

    def doubleVolume():
        """ Doubles the current volume """

    def defaultVolume():
        """ Defines current volume as it was on the beginning """

    def repeatNote():
        """ Repeats the previous note """

    def increaseOctave():
        """ Increases the current octave """

    def decreaseOctave():
        """ Decreases the current octave """

    def increaseBpm():
        """ Increases the current Bpm """

    def decreaseBpm():
        """ Decreases the value of the Bpm """

parser = Parser("config.sw")
parser.load_configuration()
