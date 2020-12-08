''' Sign-Up Frame '''

import tkinter as tk
import funcs
from login import LoginFrame

class SignUpFrame(tk.Frame):
    ''' Sign up to main window. '''

    def __init__(self, controller):
        super().__init__()

        #master window call
        self.controller = controller
        
        #setup
        self.grid(row=0, column=0, sticky="nsew")
        funcs.generate_frame_grid(self, 4, 2)

        tk.Label(
            self,
            text='SignUp Frame'
        ).grid(row=1, column=2)

        tk.Button(
            self, 
            text='Login',
            command=lambda: controller.change_frame(LoginFrame)
        ).grid(row=0, column=1)
