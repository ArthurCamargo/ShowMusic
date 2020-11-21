import tkinter as tk

class Editor(tk.Frame):
    """
    Class that manage the editor
        for composing the musics
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.txt_area = tk.Text()
        self.stream_of_char = None

    def draw_frame(self):
        """ Create the editor frame """
        self.columnconfigure(1, pad=5, weight=1)
        self.rowconfigure(0, pad=1, weight=1)
        self.txt_area.grid(row=0, column=1, sticky="nsew")
        self.stream_of_char = self.txt_area.get(1.0, tk.END)
