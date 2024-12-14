import tkinter as tk

from numpy import imag
from pyparsing import col
from add_new_meal import *
from sample_data import *
from classes import *
from main import *
import pickle
from PIL import Image, ImageTk

class Manage_meals(tk.Toplevel):
    '''
    Window that allows the user to manage meals stored in memory for the application. Only meals previously added will be shown. The user can then delete meals out of the list or add a new meal by using a different window. This window is passed the root so that it has access to its methods
    '''
    def __init__(self, root: Main_window):
        super().__init__()
        self.root = root
        self.title('Manage Meals')
        self.geometry('300x350'),
        self.resizable(False, False)
        # This controls what happens when the user closes the window. It will destroy the window if it hasn't already and then it'll run the function update_main_window()
        self.protocol("WM_DELETE_WINDOW", lambda: self.destroy() or self.update_main_window())

        # setup code for the image
        image = Image.open('stew.JPEG').resize(size= [75, 50])

        self.image = ImageTk.PhotoImage(image)

        self.icon = tk.Label(self, image= self.image)
        

        # this opens the meals from the database
        
        with open('meals.dat', 'rb') as f:
            try:
                self.meals: list[Meal] = pickle.load(f)
            except EOFError:
                self.meals = []

        self.meal_list_label = tk.Label(
            self,
            text= 'Meal List:'
        )

        # listbox will display all of the meals currently in memory
        self.meal_list = tk.Listbox(
            self,
            width= '30',
            height= '10'
        )

        # add meal names to listbox for display
        for meal in self.meals:
            self.meal_list.insert(tk.END, meal.get_name())

        self.delete_meal_btn = tk.Button(
            self,
            text= 'Delete Meal',
            fg= 'red',
            command= self.delete_meal
        )
        
        # button that takes the user to the window to create a new meal. This passes the root along to the next window as well so that it can also run the update method on the main window
        self.add_meal_btn = tk.Button(
            self,
            text= 'Add New Meal',
            fg= 'green',
            command= lambda: self.destroy() or Add_new_meal(root)
        )
        
        self.icon.grid(row= 0, column= 0, columnspan= 4)
        self.meal_list_label.grid(row= 1, column= 0, sticky= 'w')
        self.meal_list.grid(row= 2, column= 0, sticky= 'we', padx= 15, pady= 3)
        self.delete_meal_btn.grid(row= 3, column= 0)
        self.add_meal_btn.grid(row= 4, column= 0)

    def delete_meal(self):
        '''
        This method pulls a list of seleted items and deletes them from the meal list, which in turn should then remove them from the database
        '''
        # curseselection returns an array of selected items
        selection = self.meal_list.curselection()

        # if there is a selection, delete the first one in the selection array. remove it from both the listbox and the meals array
        if selection:
            self.meal_list.delete(selection[0])
            self.meals.pop(selection[0])

        # once anything is deleted, save over the database with the current list of meals, to keep things up-to-date
            with open('meals.dat', 'wb') as f:
                pickle.dump(self.meals, f)

    def update_main_window(self):
        '''
        This method simply redraws the main window's screen, making sure that the freshly added or deleted meals are either removed and they cannot be selected or added so the user can now select them
        '''
        self.root.remake_week()
        self.root.deiconify()
            
