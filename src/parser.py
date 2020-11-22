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

    def __init__(self, music):
        self.music = music
        self.text_area = []
        self.alias = {}
        self.commands = {}
        self.last_command = None

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

    def load_configuration(self, configuration_file):
        """ Load a configuration to the dictionary """
        file_handler = open(configuration_file, "r")
        self.config_parse(file_handler)
        file_handler.close()

    def parse(self):
        """ Do what was typed in the editor, based on the
        configuration already loaded """
        #if there is a default instruction use it,
        #else repeat last note or silence
        default = self.commands.get('\\default', 'repeat')

        for line in self.text_area:
            for char in line:
                self.interpret(self.music, char, default)

    def interpret(self, _music, char, default):
        """ Interpret a command"""

        operations = {
            'repeat':self.repeat,
            'instrument':_music.adjust_octave,
            'note':_music.add_note,
            'octave':_music.adjust_octave,
            'rand':_music.add_random_note,
            'silence':_music.add_note,
            'bpm':_music.adjust_bpm,
            'volume':_music.adjust_volume,
        }

        #especial cases
        if char == '\\space':
            instruction = self.commands.get('\\space', default)
        elif char == '\n':
            instruction = self.commands.get('\\n', default)
        elif char in self.commands:
            instruction = self.commands.get(char, default)
        else:
            instruction = self.commands.get(char, default)
            return

        full_instruction = instruction.split(':')
        self.last_command = full_instruction

        if len(full_instruction) == 1:
            function = full_instruction[0]

        elif len(full_instruction) == 2:
            function = full_instruction[0]
            parameters = full_instruction[1]

            if isinstance(parameters, list):
                parameters = parameters.split()
                options = parameters[0]
                parameter = int(parameters[1])

                operations[function](options,parameter)

            parameter = int(parameters)
            operations[function](parameter)

        else:
            operations[function]()

    def repeat(self):
        """Repeat the last command"""
        function = self.last_command[0]
        if function == 'note':
            parameter = self.last_command[1]
            self.music.add_note(parameter)
        else:
            self.music.add_note(0)
