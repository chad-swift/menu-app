import tkinter as tk
from add_new_meal import *
from sample_data import *

class Manage_meals(tk.Toplevel):
    '''
    Window that allows the user to manage meals stored in memory for the application. Only meals previously added will be shown. The user can then delete meals out of the list or add a new meal by using a different window
    '''
    def __init__(self):
        super().__init__()
        self.title('Manage Meals')
        self.geometry('300x300'),
        self.resizable(False, False)

        # Currently this pulls from a sample meals file. This will eventually pull from a pickled data source. 
        # Todo: update meals to pull from sample meals
        self.meals = sample_meals

        self.meal_list_label = tk.Label(
            self,
            text= 'Meal List:'
        )

        # listbox will display all of the meals currently in memory
        self.meal_list = tk.Listbox(
            self,
            width= '30',
            height= '10',
        )

        for meal in self.meals:
            self.meal_list.insert(tk.END, meal)

        # button to delete any meals out
        self.delete_meal_btn = tk.Button(
            self,
            text= 'Delete Meal',
            fg= 'red',
            command= self.delete_meal
        )
        
        # button that takes the user to the window to create a new meal
        self.add_meal_btn = tk.Button(
            self,
            text= 'Add New Meal',
            fg= 'green',
            command= Add_new_meal
        )
        
        self.meal_list_label.grid(row= 0, column= 0, sticky= 'w')
        self.meal_list.grid(row= 1, column= 0, sticky= 'we', padx= 15, pady= 3)
        self.delete_meal_btn.grid(row= 2, column= 0)
        self.add_meal_btn.grid(row= 3, column= 0)

    def delete_meal(self):
        '''
        This method pulls a list of seleted items and deletes them from the meal list, which in turn should then remove them from memory
        '''
        # curseselection returns an array of selected items
        selection = self.meal_list.curselection()

        # if there is a selection, delete the first one in the selection array. 
        # todo, change this so that the user can select any number of meals and delete them
        if selection:
            self.meal_list.delete(selection[0])
