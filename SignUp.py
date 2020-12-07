''' Sign-Up Frame '''

import tkinter as tk



class SignUpFrame(tk.Frame):
    ''' Sign up to main window. '''

    def __init__(self, controller):
        super().__init__()

        self.controller = controller 

    