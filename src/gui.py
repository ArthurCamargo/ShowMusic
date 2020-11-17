import tkinter as tk

class Gui(tk.Frame):
    """
    Class that manages the GUI, windows, buttons
        and visual elements in general
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def operational_widgets(self):
        quit_button = tk.Button(self, text="Quit", command=self.master.destroy)
        quit_button.grid(row = 6, column = 0)

    def music_widgets(self):
        pass

    def parser_widgets(self):
        pass

    def instruments_widgets(self):
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

        harpsichord.image = photo_harp
        tubular_bells.image = photo_tubular
        agogo.image = photo_agogo
        church_organ.image= photo_organ
        pan_flute.image = photo_flute

        harpsichord.grid(row = 1, column = 0)
        tubular_bells.grid(row = 2, column = 0)
        agogo.grid(row = 3, column = 0)
        pan_flute.grid(row = 4, column = 0)
        church_organ.grid(row = 5, column = 0)

    def text_editor(self):
        txt_edit = tk.Text(self)
        self.columnconfigure(1, pad=5, weight=1)
        self.rowconfigure(0, pad=1, weight=1)
        txt_edit.grid(row=0, column=1, sticky="nsew")

    def create_widgets(self):
        self.instruments_widgets()
        self.text_editor()
        self.operational_widgets()

root = tk.Tk()
app = Gui(root)
app.mainloop()
