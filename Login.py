''' Login Frame '''

import tkinter as tk 



class LoginFrame(tk.Frame):
    ''' Login frame attached to main registration window.'''

    def __init__(self, controller):
        super().__init__()

        self.controller = controller

