import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from sample_data import *
from classes import *
from main import *
import pickle
class Add_new_meal(tk.Toplevel):
    '''
    This window will allow the user to create a new meal, and add that meal to the meal list, where it will show up in all windows that need it. The root is being passed to this function so that it has access to its methods
    '''
    def __init__(self, root: Main_window):
        super().__init__()
        self.title('Add New Meal')
        self.geometry('500x600')
        self.resizable(False, False)    
        self.root = root

        # open meals from the database
        with open('meals.dat', 'rb') as f:
            try: 
                self.meals: list[Meal] = pickle.load(f)
            except EOFError:
                self.meals = []

        # label and input for name
        self.name_label = tk.Label(
            self,
            text= 'Name of new Meal:'
        )

        self.name_input = tk.Entry(
            self,
            width= 30
        )

        self.ingredient_list_label = tk.Label(
            self,
            text= 'List of Ingredients in Meal:'
        )

        # this is blank right now and it is supposed to be: a new meal will have no ingredients added to start with
        self.ingredient_list = tk.Listbox(
            self,
            width= 52
        )

        self.remove_added_ingredients_btn = tk.Button(
            self,
            text= 'Remove Selected Ingredients',
            fg= 'red',
            command= self.remove_ingredients_from_meal
        )

        # label for the "Add Ingredient" section
        self.ingredients_section_label = tk.Label(
           self,
            text= 'Add Ingredient:'
        )

        # nice label frame to keep everyting organized in a box
        self.add_ingredients_frame = tk.LabelFrame(
            self,
            width= 200,
            height= 200
        )

        # now we pull the ingredients from the data base in order to load it into the comboxbox so that the user can select it
        with open('ingredients.dat', 'rb') as f:
            try:
                self.ingredients: list[Ingredient] = pickle.load(f)
            except EOFError:
                self.ingredients = []

        self.ingredient_choice_arr = []

        for ingredient in self.ingredients:
            self.ingredient_choice_arr.append(ingredient.get_name())

        self.ingredient_choices = ttk.Combobox(
            self.add_ingredients_frame,
            width= 10,
            values= self.ingredient_choice_arr,
        )


        self.ingredient_name_label = tk.Label(
            self.add_ingredients_frame,
            text= 'Ingredient Name:'
        )

        self.ingredient_amt_label = tk.Label(
            self.add_ingredients_frame,
            text= 'Ingredient Amount: '
        )

        self.ingredient_amt_var = tk.DoubleVar()

   
        self.ingredient_amt_input = tk.Spinbox(
            self.add_ingredients_frame,
            from_= 0,
            to_= 100,
            increment= 0.25,
            textvariable= self.ingredient_amt_var,
            width= 10
        )

     
        self.amt_quantifier = tk.StringVar(value= 'Qty')

   
        self.ingredient_amt_quantifier = tk.Label(
            self.add_ingredients_frame,
            textvariable = self.amt_quantifier
        )

        # this is an event listener that listens for the combo box being activated
        self.ingredient_choices.bind('<<ComboboxSelected>>', self.update_amt_quanitfier)

        self.add_ingredient_to_list_btn = tk.Button(
            self.add_ingredients_frame,
            text= 'Add Ingredient to Meal',
            command= self.add_ingredient_to_meal,
            fg= 'green'
        )

        self.add_to_meal_btn = tk.Button(
            self.add_ingredients_frame,
            text= 'Add Meal',
            fg= 'green',
            command= self.add_meal_and_close
        )

        self.grid_items()

        # this is the holding array for the ingredients
        self.ingredients_to_add = []

    def grid_items(self):
        '''
        This method is just for organizational purposes. It contains all the packaging of all of the labels and buttons for the entire app. 
        '''
        self.name_label.grid(row= 0, column= 0, columnspan= 3, sticky= 'w', pady = 10)
        self.name_input.grid(row= 0, column= 1, sticky= 'w')
        self.ingredient_list_label.grid(row= 1, column= 0, sticky= 'w', pady= 10)
        self.ingredient_list.grid(row= 3, column= 0, columnspan= 4, sticky= 'w', padx= 10)
        self.remove_added_ingredients_btn.grid(row= 4, columnspan= 4, pady= 10)

        self.ingredients_section_label.grid(row= 5, columnspan= 4, sticky= 'w', pady= 20)

        self.ingredient_name_label.grid(row= 1, column= 0, sticky= 'w', columnspan= 3, pady= 10)
        # this is a spacer created at the end of the name label in order to make the frame box quite a bit wider
        self.ingredient_spacer = tk.Label(self.add_ingredients_frame, text= '').grid(row= 1, column= 2, padx= 110)
        self.ingredient_choices.grid(row= 1, column= 1, sticky= 'w')
        self.ingredient_amt_label.grid(row= 2, column= 0, sticky= 'w', pady= 10)
        self.ingredient_amt_input.grid(row= 2, column= 1, sticky= 'w')
        self.ingredient_amt_quantifier.grid(row= 2, column= 2, columnspan= 2, sticky= 'w')
        self.add_ingredient_to_list_btn.grid(row= 3, column= 0, columnspan= 4)
        self.add_to_meal_btn.grid(row= 4, columnspan= 4, pady= 10)
        self.add_ingredients_frame.grid(row= 6, column= 0, columnspan= 4, sticky= 'w', padx= 10)

    def add_ingredient_to_meal(self):
        '''
        This method grabs the selection from the ingredients combobox, takes the amount from the spinbox, and puts them together in a string for the user. It creates a new Meal class, appends it to the meals list, and then pickles the the meals list
        '''

        current_ingredient_index = self.ingredient_choices.current()

        current_selection_name = self.ingredient_choice_arr[current_ingredient_index]

        current_selection_ingredient: Ingredient = self.ingredients[current_ingredient_index]

        ingredient_amt = self.ingredient_amt_var.get()

        ingredient_quantifier = self.amt_quantifier.get()

        ingredient_names = []

        # this will grab the names of all of the ingredients in the holding array and add them to a different array, to make it easier to find everything
        for ingredient, _ in self.ingredients_to_add:
            ingredient_names.append(ingredient.get_name())

        # this code checks if an ingredient with the same name has already been added, it would not makes sense to have two of the same ingredient
        if current_selection_name not in ingredient_names:
            self.ingredient_list.insert(tk.END, (f'{ingredient_amt:.1f} {ingredient_quantifier} of {current_selection_name}'))
            self.ingredients_to_add.append((current_selection_ingredient, ingredient_amt))
        else:
            messagebox.showerror(
                'Alert', 
                message= 'You already have an ingredient by that name in your meal!'
            )

        # clear the combobox and the spinbox
        self.ingredient_amt_var.set(0.0)
        self.ingredient_choices.set('')

    def update_amt_quanitfier(self, event):
        '''
        Event method that updates the 'qty' label with the stored quanitfier within the ingredients dictionary
        '''

        current_selection = self.ingredient_choices.current()

        self.amt_quantifier.set(self.ingredients[current_selection].get_quantifier())

    def remove_ingredients_from_meal(self):
        '''
        This method removes ingredients added to the list and should also remove them from the temporary object storage
        '''
        selection = self.ingredient_list.curselection()

        if selection:
            self.ingredient_list.delete(selection[0])
            self.ingredients_to_add.pop(selection[0])

    def add_meal_and_close(self):
        
        name = self.name_input.get()

        # this bit makes sure that it does not save a meal if that meal already exists
        for meal in self.meals:
            if name == meal.get_name():
                messagebox.showerror(
                    title= 'Error',
                    message= 'You already have a meal by that name saved in meals'
                )
                return
        
        # if it does not already exist, it creates a new meal using the Meal class
        new_meal = Meal(self.name_input.get(), self.ingredients_to_add)

        # appends that new meal to the meals data
        self.meals.append(new_meal)

        # and writes that data to file
        with open('meals.dat', 'wb') as f:
            pickle.dump(self.meals, f)

        # it will then refresh the main window, and close itself, keeping all the data fresh
        self.root.remake_week()
        self.root.deiconify()
        self.destroy()
