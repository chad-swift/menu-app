import tkinter as tk
from tkinter import ttk

class Manage_meals(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Manage Meals')
        self.geometry('300x800')    

        sampleMeals = (
            'meatballs',
            'sandwhich',
            'pasta',
            'spaghet',
            'bananas',
            'oatmeal',
            'tacos',
            'porcupine soup',
            'silly rabbits',
            'cereal',
            'footballs',
            'christmas trees',
            'stuff I can not pronounce'
        )

        self.mealListLabel = tk.Label(
            self,
            text= 'Meal List:'
        ).grid(row= 0, column= 0, sticky= 'w')

        self.mealList = tk.Listbox(
            self,
            width= '30',
            height= '10',
        )

        for meal in sampleMeals:
            self.mealList.insert(0, meal)

        self.mealList.grid(row= 1, column= 0, columnspan= 3, sticky= 'we', padx= 15, pady= 3)

def runWindow():
    Manage_meals().mainloop()

runWindow()