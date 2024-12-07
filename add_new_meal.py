import tkinter as tk
from tkinter import ttk
from sample_data import *
class Add_new_meal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Add New Meal')
        self.geometry('500x600')
        self.resizable(False, False)

        for i in range(5):
            tk.Label(self, text= "   ").grid(row= 0, column= i)

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
        

        self.ingredientList = tk.Listbox(
            self,
            width= 52
        )


        self.ingredients = sample_ingredients

        self.remove_added_ingredients_btn = tk.Button(
            self,
            text= 'Remove Selected Ingredients',
            fg= 'red',
            command= self.remove_ingredients_from_meal
        )
        

        self.ingredients_section_label = tk.Label(
           self,
            text= 'Add Ingredient:'
        )
        

        self.add_ingredients_frame = tk.LabelFrame(
            self,
            width= 200,
            height= 200
        )

        self.ingredient_choice_arr = []

        for key in self.ingredients.keys():
            self.ingredient_choice_arr.append(key)

        self.ingredient_choices = ttk.Combobox(
            self.add_ingredients_frame,
            width= 10,
            values= self.ingredient_choice_arr,
        )

        self.ingredient_choices.bind('<<ComboboxSelected>>', self.update_amt_quanitfier)

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
        

        self.add_ingredient_to_list_btn = tk.Button(
            self.add_ingredients_frame,
            text= 'Add Ingredient to Meal',
            command= self.add_ingredient_to_meal,
            fg= 'green'
        )

        self.add_to_meal_btn = tk.Button(
            self.add_ingredients_frame,
            text= 'Add Meal',
            fg= 'green'
        )

        self.grid_items()

    def grid_items(self):
        
        self.name_label.grid(row= 0, column= 0, columnspan= 3, sticky= 'w', pady = 10)
        self.name_input.grid(row= 0, column= 1, sticky= 'w')
        self.ingredient_list_label.grid(row= 1, column= 0, sticky= 'w', pady= 10)
        self.ingredientList.grid(row= 3, column= 0, columnspan= 4, sticky= 'w', padx= 10)
        self.remove_added_ingredients_btn.grid(row= 4, columnspan= 4, pady= 10)

        self.ingredients_section_label.grid(row= 5, columnspan= 4, sticky= 'w', pady= 20)

        self.ingredient_name_label.grid(row= 1, column= 0, sticky= 'w', columnspan= 3, pady= 10)
        self.ingredient_spacer = tk.Label(self.add_ingredients_frame, text= '').grid(row= 1, column= 2, padx= 110)
        self.ingredient_choices.grid(row= 1, column= 1, sticky= 'w')
        self.ingredient_amt_label.grid(row= 2, column= 0, sticky= 'w', pady= 10)
        self.ingredient_amt_input.grid(row= 2, column= 1, sticky= 'w')
        self.ingredient_amt_quantifier.grid(row= 2, column= 2, columnspan= 2, sticky= 'w')
        self.add_ingredient_to_list_btn.grid(row= 3, column= 0, columnspan= 4)
        self.add_to_meal_btn.grid(row= 4, columnspan= 4, pady= 10)
        self.add_ingredients_frame.grid(row= 6, column= 0, columnspan= 4, sticky= 'w', padx= 10)

    def add_ingredient_to_meal(self):
        ingredient_name = self.ingredient_choices.current()

        currentSelectionName = self.ingredient_choice_arr[self.currentSelection]

        ingredient_amt = self.ingredient_amt_var.get()

        if ingredient_name:
            self.ingredientList.insert(tk.END, (f'{ingredient_amt:.1f}   {currentSelectionName}'))

        self.ingredient_amt_var.set(0.0)

        self.ingredient_choices.set('')

    def update_amt_quanitfier(self, event):
        self.currentSelection = self.ingredient_choices.current()

        self.currentSelectionName = self.ingredient_choice_arr[self.currentSelection]

        self.amt_quantifier.set(self.ingredients[self.currentSelectionName])

    def remove_ingredients_from_meal(self):
        selection = self.ingredientList.curselection()

        if selection:
            self.ingredientList.delete(selection[0])
