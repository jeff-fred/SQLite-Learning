''' Login Frame '''

import tkinter as tk 
import funcs
import signUp


class LoginFrame(tk.Frame):
    ''' Login frame attached to main registration window.'''

    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        # grid setup
        self.grid(row=0, column=0, sticky="nsew")
        funcs.generate_frame_grid(self, 4, 3)

        # widget setup
        self.widget_setup()


    # Creating and setting up widgets
    def widget_setup(self):
        # ==== LABELS ====
        tk.Label(
            self,
            text='Username:',
        ).grid(row=1, column=1)

        tk.Label(
            self,
            text='Password:'
        ).grid(row=3, column=1)