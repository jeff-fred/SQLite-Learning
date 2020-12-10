''' Sign-Up Frame '''

import tkinter as tk
import funcs
import login

class SignUpFrame(tk.Frame):
    ''' Sign up to main window. '''

    def __init__(self, controller):
        super().__init__()

        #master window call
        self.controller = controller
        
        #setup
        self.grid(row=0, column=0, sticky="nsew")
        funcs.generate_frame_grid(self, 6, 3)

        #widget setup
        self.usernameEntry = tk.Entry(self)
        self.passwordEntry = tk.Entry(self)
        self.passwordConfirmationEntry = tk.Entry(self)
        self.frame_setup()

    
    # Set up all frame attributes
    def frame_setup(self):
        self.create_widgets()

    
    # Create and setup widgets
    def create_widgets(self):
        # ==== LABELS ====
        tk.Label(
            self,
            text='Please Sign Up',
        ).grid(row=0, columnspan=3, sticky='n')
        
        tk.Label(
            self,
            text='New Username:',
            padx=5
        ).grid(row=1, column=0, sticky='e')

        tk.Label(
            self,
            text='Password:',
            padx=5
        ).grid(row=2, column=0, sticky='e')

        tk.Label(
            self,
            text='Confirm Password:',
            padx=5
        ).grid(row=3, column=0, sticky='e')

        tk.Label(
            self,
            text='Already have an account?'
        ).grid(row=5, column=0, columnspan=2)

        # ==== ENTRIES ====

        #Username Entry
        self.usernameEntry.config(
            width=15
        )
        self.usernameEntry.grid(row=1, column=1, columnspan=2)

        #Password Entry
        self.passwordEntry.config(
            show='*',
            width=15
        )
        self.passwordEntry.grid(row=2, column=1, columnspan=2)

        #Password Confirmation Entry
        self.passwordConfirmationEntry.config(
            show='*',
            width=15,
        )
        self.passwordConfirmationEntry.grid(row=3, column=1, columnspan=2)

        entries = [
            self.usernameEntry,
            self.passwordEntry,
            self.passwordConfirmationEntry
        ]

        # ==== BUTTONS ====
        tk.Button(
            self,
            text='Sign Up',
        ).grid(row=4, columnspan=3)
        
        tk.Button(
            self,
            text='Login',
            command=lambda: [
                self.controller.change_frame(login.LoginFrame),
                funcs.clear_entries(entries)]
        ).grid(row=5, column=2)

