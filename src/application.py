"""
File: application.py
Author: Arthur Camargo
Email: arthurcamargo13@gmail.com
Description:
    The main module of the show music application,
    initialize the main application
"""

import tkinter as tk
from player import Player
from music import Music
from gui import Gui
from instrument import Instrument
from parser import Parser

class Application:
    """ Main class that runs the app """
    def __init__(self):
        self._music = Music()
        self._player = Player()
        _app = Gui(tk.Tk())
        _app.mainloop()

    def __str__(self):
        return self.__class__.__name__

my_application = Application()
