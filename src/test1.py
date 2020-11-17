from tkinter import *

root = Tk()
root.title('sample')
root.geometry("400x400")


class Gui(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        #self.create_widgets()

        login_btn = PhotoImage(file='../icons/grand-piano.png')

        my_button = Button(self, image=login_btn)
        my_button.image=login_btn
        my_button.pack(pady=20)

app = Gui(root)
app.mainloop()
