"""
File: parser.py
Author: Arthur Camargo
Email: arthurcamargo13@gmail.com
Description:
    Module that handles parsing and the configuration of the music

    Classes:
        Parser
"""
from pygame import midi
from music import Music
from player import Player
from instrument import Instrument

def remove(string, char=' ', side='after'):
    """ Remove from a string a substring before or afters a
    char, inclusive the char.

        Options:
            string: string to be removed
            char: delimiter of the string, ' ' by default
            side: can be 'before' or 'after',
                parameter that chooses the side that the
                subtring will be removed, 'after' by default """
    return_string = string
    if not char in string:
        return string

    delimiter_index = string.find(char)
    if side == 'after':
        return_string = string[:delimiter_index]

    elif side == 'before':
        # + 1 because te delimiter don't exclude the
        # actual character
        return_string = string[delimiter_index + 1:]

    return return_string

_music = Music()
_player = Player()
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

    def check_alias(self, token):
        """ Check if some substitution is needed in the token"""
        return_string = token

        if str(token) in self.alias:
            return_string =  self.alias[str(token)]

        return return_string

    def config_commands(self, line):
        """ Insert the commands configuration in the dictionary
            of commands"""
        if '[' in line and ']' in line:
            line = remove(line, '[','before')
            line = remove(line, ']','after')

            tokens = line.split("->")
            for i,_ in enumerate(tokens):
                tokens[i] = tokens[i].strip("() ")

            for i,_ in enumerate(tokens):
                tokens[i] = self.check_alias(tokens[i])

                instructions = tokens[i].split(':')
                for j,_ in enumerate(instructions):
                    instructions[j] = self.check_alias(instructions[j])

                tokens[i] = ':'.join(instructions)

            self.commands[tokens[0]] = tokens[1]

    def config_alias(self, line):
        """ Insert the command configuration in the dictionary
            of aliases"""
        if not'[' in line and not ']' in line:
            tokens = line.split("=")

            for i,_ in enumerate(tokens):
                tokens[i] = tokens[i].strip("() ")

            self.alias[tokens[0]] = tokens[1]

    def config_parse(self, file_handler):
        """ Parse the configuration file and transform it
        into a dictionary"""

        for line in file_handler:
            line = remove(line, '*', 'after')

            #remove whitespaces
            line = line.strip()

            #Only operate on non-empty strings
            if line:
                self.config_alias(line)
                self.config_commands(line)

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

        operations = {
            'repeat':self.repeat,
            'instrument':Player.set_instrument,
            'note':Music.add_note,
            'octave':Music.adjust_octave,
            'rand':Music.add_note,
            'silence':Music.add_note,
            'bpm':Music.adjust_bpm,
            'volume':Player.adjust_volume,
        }
        #if there is a default instruction use it,
        #else repeat last note or silence
        default = self.commands.get('\\default', 'repeat')

        #variable used to store number, so it can be used
        # as an argument in the functions
        number = None

        #especial cases
        if char == '\\space':
            instruction = self.commands.get('\\space', default)
        elif char == '\n':
            instruction = self.commands.get('\\n', default)
        elif char.isdigit():
            instruction = self.commands.get('$number', default)
            number = int(char)
        else:
            instruction = self.commands.get(char, default)

        full_instruction = instruction.split(':')
        function = full_instruction[0]
        parameters = full_instruction[1]

        if isinstance(parameters, list):
            parameters = parameters.split()
            options = parameters[0]
            parameter = parameters[1]

            operations[function](options,parameter)
        else:
            parameter = parameters
            operations[function](_music,parameter)


    def repeat(self):
        """repeat the last command"""

    def create_note(self, midi_value):
        """ Creates a note """

    def random_note(self):
        """ Generates a random note """

    def double_volume(self):
        """ Doubles the current volume """

    def default_volume(self):
        """ Defines current volume as it was on the beginning """

    def repeat_note(self):
        """ Repeats the previous note """

    def increase_octave(self):
        """ Increases the current octave """

    def decrease_octave(self):
        """ Decreases the current octave """

    def increase_bpm(self):
        """ Increases the current Bpm """

    def decrease_bpm(self):
        """ Decreases the value of the Bpm """

parser = Parser("config.sw")
parser.load_configuration()
parser.interpret('C')
print(_music.notes)
