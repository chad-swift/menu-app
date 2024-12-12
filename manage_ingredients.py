import tkinter as tk
from sample_data import *

class Manage_ingredients(tk.Toplevel):
 

    def __init__(self):
        super().__init__()
        self.title('Manage Ingredients')
        self.geometry('400x450'),
        self.resizable(False, False)

        self.ingredients = []

        for key, value in sample_ingredients.items():
            self.ingredients.append(f'{key}, measured in {value}')

        self.ingredient_list_label = tk.Label(
            self,
            text= 'Ingredient List:'
        )

        self.ingredient_list = tk.Listbox(
            self,
            width= '30',
            height= '10',
        )

        for ingredient in self.ingredients:
            self.ingredient_list.insert(tk.END, ingredient)

        
        self.delete_ingredient_btn = tk.Button(
            self,
            text= 'Delete Ingredient',
            fg= 'red',
            command= self.delete_ingredient
        )

        self.add_ingredient_section_label = tk.Label(
            self,
            text= 'Add New Ingredient:'
        )

        self.add_ingredient_frame = tk.LabelFrame(
            self,
            width= 200,
            height= 200
        )

        self.add_ingreient_name_label = tk.Label(
            self.add_ingredient_frame,
            text= 'New Ingredient Name: '
        )

        self.add_ingredient_name_input = tk.Entry(
            self.add_ingredient_frame
        )

        self.add_ingredient_quantifier_label = tk.Label(
            self.add_ingredient_frame,
            text= 'New Ingredient Quantifier:'
        )

        self.add_ingredients_quanitfier_input = tk.Entry(
            self.add_ingredient_frame,
            width= 5
        )

        self.quantifier_examples = tk.Label(
            self.add_ingredient_frame,
            text= '(pcs, oz, lbs, ect)'
        )

        self.error_message_var = tk.StringVar(value= '')
        
        self.error_message_area = tk.Label(
            self.add_ingredient_frame,
            textvariable= self.error_message_var,
            fg= 'red'
        )
    
        self.add_ingredient_btn = tk.Button(
            self.add_ingredient_frame,
            text= 'Add New Ingredient To Ingredient List',
            fg= 'green',
            command= self.add_ingredient
        )
        
        self.ingredient_list_label.grid(row= 0, column= 0, sticky= 'w')
        self.ingredient_list.grid(row= 1, column= 0, sticky= 'we', padx= 15, pady= 3)
        self.delete_ingredient_btn.grid(row= 2, column= 0)
        self.add_ingredient_section_label.grid(row= 3, column= 0, padx= 10, sticky= 'w')
        
        self.add_ingredient_frame.grid(row= 4, column= 0, padx= 10, pady= 10, sticky= 'w')
        self.add_ingreient_name_label.grid(row= 0, column= 0, pady= 10, sticky= 'w')
        self.add_ingredient_name_input.grid(row= 0, column= 1, columnspan= 3, padx= 10, pady= 10, sticky= 'w')
        self.add_ingredient_quantifier_label.grid(row= 1, column= 0, pady= 10, sticky= 'w')
        self.add_ingredients_quanitfier_input.grid(row= 1, column= 1, pady= 10, padx= 10, sticky= 'w')
        self.quantifier_examples.grid(row= 1, column= 3, pady= 10, sticky= 'w')
        self.error_message_area.grid(row= 2, columnspan= 4, padx= 10, pady= 10, sticky= 'we')
        self.add_ingredient_btn.grid(row= 3, columnspan= 4, pady= 10, sticky= 'we')


    def delete_ingredient(self):
        
        selection = self.ingredient_list.curselection()

        if selection:
            self.ingredient_list.delete(selection[0])

    def add_ingredient(self):
        ingredient_name = self.add_ingredient_name_input.get()
        ingredient_quantifier = self.add_ingredients_quanitfier_input.get()

        if not ingredient_name and not ingredient_quantifier:
            self.error_message_var.set('Ingredient Name and quanitfier must both be filled out!')
        else:
            self.ingredient_list.insert(tk.END, f'{ingredient_name}, measured in {ingredient_quantifier}')
            self.add_ingredient_name_input.delete(0, tk.END)
            self.add_ingredients_quanitfier_input.delete(0, tk.END)
        
