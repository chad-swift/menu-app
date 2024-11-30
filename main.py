
import tkinter as tk
from tkinter import ttk

class Main_window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1000x200')
        self.resizable(False, False)
        self.title('Main Window')

        days = (
            'Monday', 
            'Tuesday', 
            'Wednesday', 
            'Thursday', 
            'Friday', 
            'Saturday', 
            'Sunday'
            )


    def make_day_frame(Main_window, day: str):
        day_frame = tk.Frame(
            Main_window,
            border= 5
        ).pack(side= 'left')

        




if __name__ == '__main__':
    Main_window().mainloop()