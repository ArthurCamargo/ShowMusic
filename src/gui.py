"""
File: gui.py
Author: Joao Martins
Email: joaomaieron@gmail.com
Description:
    Main module of the application, handles the graphical user interface
"""

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from editor import Editor
from player import Player
from parser import Parser
from music import Music

class Gui(tk.Frame):
    """
    Class that manages the GUI, windows, buttons
        and visual elements in general
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.editor = Editor(master)
        self.music = Music()
        self.player = Player()
        self.parser = Parser(self.music)
        self.create_widgets()

    def operational_widgets(self):
        """ Operational Widgets

            Buttons:

                Save: Saves the file
                Open: Open the file
                Quit: Quit the app"""
        save_button = tk.Button(self, text="Save", command=self.save_file)
        open_button = tk.Button(self, text="Load", command=self.open_file)
        quit_button = tk.Button(self, text="Quit", command=self.master.destroy)

        quit_button.grid(row = 8, column = 6)
        save_button.grid(row = 8, column = 7)
        open_button.grid(row = 8, column = 8)

    def save_file(self):
        """Save the current file as a new file."""
        filepath = asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = self.editor.txt_area.get(1.0, tk.END)
            output_file.write(text)

    def compile(self):
        """ Compile the current file to generate music. """
        text = self.editor.txt_area.get(1.0, tk.END)
        self.parser.text_area = text
        self.parser.parse()
        self.music.generate()

    def open_file(self):
        """Open a file for editing."""
        filepath = askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        self.editor.txt_area.delete(1.0, tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            self.editor.txt_area.insert(tk.END, text)

    def load_config_file(self):
        """ Load a configuration file into the application"""
        filepath = askopenfilename(
            filetypes=[("Text Files", "*.sm"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        self.parser.load_configuration(filepath)

    def music_widgets(self):
        """ Music related Widgets

            Buttons:
                Play/Pause: Plays and pauses the music
                Stop: Stop the music
                Compile: Compile the song into the music"""

        frame_music = tk.Frame(self, relief=tk.RAISED)
        frame_music.grid(row = 6, column = 1)

        play_pause_button = tk.Button(frame_music, text='play')
                                     #command=self.player.toogle_play())

        stop_button = tk.Button(frame_music, text='stop')
                               #comand=self.player.stop())

        compile_button = tk.Button(frame_music, text='compile',
                                  command=self.compile)

        load_config_button = tk.Button(frame_music, text='load configuration',
                                  command=self.load_config_file)



        play_pause_button.grid(row = 0, column = 0)
        stop_button.grid(row = 0, column = 1)
        compile_button.grid(row = 0, column = 2)
        load_config_button.grid(row = 0, column = 3)

    def instruments_widgets(self):
        """ Instrument related Widgets """
        frame_instruments = tk.Frame(self, relief=tk.RAISED)
        frame_instruments.grid(row = 0, column = 0)

        #Images of the instruments
        photo_harp = tk.PhotoImage(file = '../icons/grand-piano.png')
        photo_tubular= tk.PhotoImage(file = '../icons/tubular.png')
        photo_agogo= tk.PhotoImage(file = '../icons/agogo.png')
        photo_flute= tk.PhotoImage(file = '../icons/pan-flute.png')
        photo_organ= tk.PhotoImage(file = '../icons/organ.png')

        harpsichord = tk.Button(frame_instruments, image=photo_harp,
            compound = tk.CENTER, borderwidth=0)

        tubular_bells = tk.Button(frame_instruments, image=photo_tubular,
            compound = tk.CENTER, borderwidth=0)

        agogo = tk.Button(frame_instruments, image=photo_agogo,
            compound = tk.CENTER, borderwidth=0)

        pan_flute = tk.Button(frame_instruments, image=photo_flute,
            compound = tk.CENTER, borderwidth=0)

        church_organ = tk.Button(frame_instruments, image=photo_organ,
            compound = tk.CENTER, borderwidth=0)

        #Images should be referenciated like that because of a known
        #bug in tkinter http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm
        harpsichord.image = photo_harp
        tubular_bells.image = photo_tubular
        agogo.image = photo_agogo
        church_organ.image= photo_organ
        pan_flute.image = photo_flute

        #Create the gris of the instruments
        harpsichord.grid(row = 1, column = 0)
        tubular_bells.grid(row = 2, column = 0)
        agogo.grid(row = 3, column = 0)
        pan_flute.grid(row = 4, column = 0)
        church_organ.grid(row = 5, column = 0)

    def create_widgets(self):
        """ Create the gui widget of the application """
        self.music_widgets()
        self.instruments_widgets()
        self.operational_widgets()
        self.editor.draw_frame()


_app = Gui(tk.Tk())
_app.parser.load_configuration("../config/config.sm")
_app.mainloop()
