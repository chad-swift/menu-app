
import tkinter as tk
from tkinter import ttk
from manage_meals import *
from manage_ingredients import *
from classes import *
import pickle
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
        self.days = (
            'Monday', 
            'Tuesday', 
            'Wednesday', 
            'Thursday', 
            'Friday', 
            'Saturday', 
            'Sunday'
            )
        
        self.week_frame = tk.Frame(
            self
        )

        # Go through days of the week, create frames
        for row, day in enumerate(self.days):
            self.make_day_frame(day, row, self.week_frame)

        btn_height = 2
        btn_width = 12

        # Create buttons
        self.manage_meals_btn = tk.Button(
            self,
            text= 'Manage Meals',
            height= btn_height,
            width= btn_width,
            activebackground= '#FF0000',
            command= lambda: Manage_meals(self)
        )
        

        self.manage_ingredients_btn = tk.Button(
            self,
            text= 'Manage Ingredients',
            height= btn_height,
            width= btn_width,
            command= Manage_ingredients
        )
        

        self.export_btn = tk.Button(
            self,
            text= 'Export Menu and List',
            height= btn_height,
            width= btn_width
        )
        
        self.week_frame.grid(row= 0, column= 0, rowspan= 3)
        self.manage_meals_btn.grid(row= 0, column= 7, padx= 10)
        self.manage_ingredients_btn.grid(row= 1, column= 7)
        self.export_btn.grid(row= 2, column= 7)

    def make_day_frame(self, day: str, column, week_frame: tk.Frame):
        '''
        Generates a frame for a single day for the week calendar
        '''

        self.day_frame = tk.LabelFrame(
            week_frame,
            bg= '#434343',
            width= 166,
            height= 190,
        )
        

        self.day_label = tk.Label(
            week_frame,
            text= day,
            bg= '#434343'
        )
        
        with open('meals.dat', 'rb') as f:
            try:
                self.meals: list[Meal] = pickle.load(f)
            except EOFError:
                self.meals = []

        self.meal_list = []

        for meal in self.meals:
            self.meal_list.append(meal.get_name())

        self.meal_selector = ttk.Combobox(
            self.day_frame,
            width= 10,
            values= self.meal_list
        )

        
        self.day_label.grid(row= 0, column= column)
        self.meal_selector.grid(row= 1, column= column, padx= 21,pady= 62)
        self.day_frame.grid(row= 0, column= column, rowspan= 3, pady= 10)

    def remake_week(self):
        self.week_frame.destroy()
        self.new_week_frame = tk.Frame(
            self
        )

        self.new_week_frame.grid(row= 0, column= 0, rowspan= 3)

        for row, day in enumerate(self.days):
            self.make_day_frame(day, row, self.new_week_frame)



if __name__ == '__main__':
    Main_window().mainloop()