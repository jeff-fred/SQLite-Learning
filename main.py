''' Main Registration Window '''

# Imports
import tkinter as tk
from signUp import SignUpFrame
from login import LoginFrame


class RegistrationWindow(tk.Tk):
    '''Display of main registration window'''

    # Intialize window attributes
    def __init__(self):
        super().__init__()
        self.win_attributes()
    
        #Adding space to window for frame
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        #Frames <dictionary> container
        self.frames = {}
        self.frames[SignUpFrame] = SignUpFrame(self)
        self.frames[LoginFrame] = LoginFrame(self)
        
    # Window Attributes
    def win_attributes(self):
        self.title('Registration')
        self.resizable(width=False, height=False)
        self.center_window('250x250')


    # Place window of <size> in middle of screen
    def center_window(self, size):
        win_size = size.split('x')
        screen_height = self.winfo_screenheight()
        screen_width = self.winfo_screenwidth()

        win_x = int((screen_width/2) - (int(win_size[0])/2))
        win_y = int((screen_height/2) - (int(win_size[1])/2))

        self.geometry("{0}+{1}+{2}".format(size, win_x, win_y))
        
        
    # Run window
    def run_window(self):
        frame = self.frames[SignUpFrame]
        frame.tkraise()
        

    # Show different frame on window
    def change_frame(self, newFrame):
        frame = self.frames[newFrame]
        frame.tkraise()

    # Resize window
    def resize_window(self, newSize):
        self.center_window(newSize)



app = RegistrationWindow()

app.run_window()
app.mainloop()