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
        funcs.generate_frame_grid(self, 5, 3)

        # widget setup
        self.usernameEntry = tk.StringVar()
        self.passwordEntry = tk.StringVar()
        self.frame_setup()

    # Set up whole frame
    def frame_setup(self):
        self.create_widgets()

    # Creating and setting up widgets
    def create_widgets(self):
        # ==== LABELS ====
        tk.Label(
            self,
            text='Please Login',
        ).grid(row=0, columnspan=3, sticky='n')
        
        tk.Label(
            self,
            text='Username:',
            padx=5
        ).grid(row=1, column=0, sticky='e')

        tk.Label(
            self,
            text='Password:',
            padx=5
        ).grid(row=2, column=0, sticky='e')

        tk.Label(
            self,
            text='Don\'t have an account?'
        ).grid(row=4, column=0, columnspan=2)

        # ==== ENTRIES ====

        #Username Entry
        tk.Entry(
            self,
            textvariable=self.usernameEntry,
            width=15
        ).grid(row=1, column=1, columnspan=2)

        #Password Entry
        tk.Entry(
            self,
            textvariable=self.passwordEntry,
            width=15
        ).grid(row=2, column=1, columnspan=2)

        # ==== BUTTONS ====
        tk.Button(
            self,
            text='Login',
        ).grid(row=3, columnspan=3)
        
        tk.Button(
            self,
            text='Sign Up',
            command=lambda: self.controller.change_frame(signUp.SignUpFrame)
        ).grid(row=4, column=2)
