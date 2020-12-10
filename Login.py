''' Login Frame '''

import tkinter as tk 
import data_management as dm
from tkinter import messagebox
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
        self.usernameEntry = tk.Entry(self)
        self.passwordEntry = tk.Entry(self)
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
        self.usernameEntry.config(
            width=15
        )
        self.usernameEntry.grid(row=1, column=1, columnspan=2)

        #Password Entry
        self.passwordEntry.config(
            width=15,
            show='*'
        )
        self.passwordEntry.grid(row=2, column=1, columnspan=2)

        entries = [
            self.usernameEntry,
            self.passwordEntry]

        # ==== BUTTONS ====
        tk.Button(
            self,
            text='Login',
            command=lambda: self.login_user()
        ).grid(row=3, columnspan=3)
        
        tk.Button(
            self,
            text='Sign Up',
            command=lambda: [
                self.controller.change_frame(signUp.SignUpFrame),
                funcs.clear_entries(entries)]
        ).grid(row=4, column=2)


    # Login if username & password matches
    def login_user(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()

        if dm.search_by_name(username):
            with dm.connection:
                dm.cursor.execute(
                    '''
                    SELECT Password FROM Users WHERE Username=?
                    ''', (username,))
                truePass = dm.cursor.fetchone()[0]

                if truePass == password:
                    messagebox.showinfo('Success!', 'You are now logged in!')
                else:
                    messagebox.showinfo("ERROR", 'Wrong Password. Try Again')
        
        else:
            funcs.error_messagebox('Invalid username.')