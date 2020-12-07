''' Main Registration Window '''

# Imports
import tkinter as tk



class RegistrationWindow(tk.Tk):
    '''Display of main registration window'''

    # Intialize window attributes
    def __init__(self):
        super().__init__()
        self.win_attributes()
    
    # Window Attributes
    def win_attributes(self):
        self.title('Registration')
        self.center_window('300x300')

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
        self.mainloop()

    # Exit window
    def exit_window(self):
        self.quit()

    # Resize window
    def resize_window(self, newSize):
        self.center_window(newSize)


