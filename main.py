
import tkinter as tk
from tkinter import ttk
from manage_meals import *

class Main_window(tk.Tk):
    '''
    Class that generates the main menu for the menu app
    '''
    def __init__(self):
        super().__init__()
        self.geometry('1350x200')
        self.resizable(False, False)
        self.title('Main Window')

        # Initialize days of the week
        days = (
            'Monday', 
            'Tuesday', 
            'Wednesday', 
            'Thursday', 
            'Friday', 
            'Saturday', 
            'Sunday'
            )
        
        # Go through days of the week, create frames
        for row, day in enumerate(days):
            self.make_day_frame(day, row)

        btn_height = 3
        btn_width = 15

        # Create buttons
        self.manage_meals_btn = tk.Button(
            self,
            text= 'Manage Meals',
            height= btn_height,
            width= btn_width,
            activebackground= '#FF0000',
            command= Manage_meals
        ).grid(row= 0, column= 7)

        self.manage_ingredients_btn = tk.Button(
            self,
            text= 'Manage Ingredients',
            height= btn_height,
            width= btn_width
        ).grid(row= 1, column= 7)

        self.export_btn = tk.Button(
            self,
            text= 'Export Menu and List',
            height= btn_height,
            width= btn_width
        ).grid(row= 2, column= 7)


    def make_day_frame(self, day: str, column):
        '''
        Generates a frame for a single day for the week calendar
        '''

        self.day_frame = tk.LabelFrame(
            self,
            bg= '#434343',
            width= 166,
            height= 190,
        ).grid(row= 0, column= column, rowspan= 3)

        self.day_label = tk.Label(
            self.day_frame,
            text= day,
            bg= '#434343'
        ).grid(row= 0, column= column)

        self.meals = sample_meals

        self.meal_selector = ttk.Combobox(
            self.day_frame,
            width= 10,
            values= self.meals
        ).grid(row= 1, column= column)


        




if __name__ == '__main__':
    Main_window().mainloop()