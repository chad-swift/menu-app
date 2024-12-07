import tkinter as tk
from add_new_meal import *
from sample_data import *

class Manage_meals(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Manage Meals')
        self.geometry('300x300'),
        self.resizable(False, False)

        self.meals = sample_meals

        self.meal_list_label = tk.Label(
            self,
            text= 'Meal List:'
        ).grid(row= 0, column= 0, sticky= 'w')

        self.selected_meal = tk.IntVar()

        self.meal_list = tk.Listbox(
            self,
            width= '30',
            height= '10',
            selectmode= 'browse'
        )

        for meal in self.meals:
            self.meal_list.insert(tk.END, meal)

        self.meal_list.grid(row= 1, column= 0, sticky= 'we', padx= 15, pady= 3)

        self.delete_meal_btn = tk.Button(
            self,
            text= 'Delete Meal',
            fg= 'red',
            command= self.delete_meal
        ).grid(row= 2, column= 0)

        self.add_meal_btn = tk.Button(
            self,
            text= 'Add New Meal',
            fg= 'green',
            command= Add_new_meal
        ).grid(row= 3, column= 0)

    def delete_meal(self):
        selection = self.meal_list.curselection()

        if selection:
            self.meal_list.delete(selection[0])
