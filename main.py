
import tkinter as tk
from tkinter import ttk

class Main_window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1350x200')
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
        
        for row, day in enumerate(days):
            self.make_day_frame(day, row)

        btn_height = 3
        btn_width = 15

        self.manage_meals_btn = tk.Button(
            self,
            text= 'Manage Meals',
            height= btn_height,
            width= btn_width,
            activebackground= '#FF0000'
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


    def make_day_frame(Main_window, day: str, column):
        day_frame = tk.LabelFrame(
            Main_window,
            bg= '#434343',
            width= 166,
            height= 190,
        ).grid(row= 0, column= column, rowspan= 3)

        day_label = tk.Label(
            day_frame,
            text= day,
            bg= '#434343'
        ).grid(row= 0, column= column)

        meal_selector = ttk.Combobox(
            day_frame,
            width= 10
        ).grid(row= 1, column= column)


        




if __name__ == '__main__':
    Main_window().mainloop()