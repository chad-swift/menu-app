import tkinter as tk
from tkinter import messagebox

from pyparsing import col
from sample_data import *
from classes import *
import pickle
from PIL import Image, ImageTk
class Manage_ingredients(tk.Toplevel):

    def __init__(self):
        super().__init__()
        self.title('Manage Ingredients')
        self.geometry('400x525'),
        self.resizable(False, False)

        image = Image.open('Cucumber.JPEG').resize(size= [75, 50])

        self.image = ImageTk.PhotoImage(image)

        self.icon = tk.Label(self, image= self.image)

        self.ingredients = []

        with open('ingredients.dat', 'rb') as f:
            try:
                ingredient_list: list[Ingredient] = pickle.load(f)
                for ingredient in ingredient_list:
                    self.ingredients.append(ingredient)
            except EOFError:
                ingredient_list = []

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
        
        self.icon.grid(row= 0, column= 0, columnspan= 3)
        self.ingredient_list_label.grid(row= 1, column= 0, sticky= 'w')
        self.ingredient_list.grid(row= 2, column= 0, sticky= 'we', padx= 15, pady= 3)
        self.delete_ingredient_btn.grid(row= 3, column= 0)
        self.add_ingredient_section_label.grid(row= 4, column= 0, padx= 10, sticky= 'w')
        
        self.add_ingredient_frame.grid(row= 5, column= 0, padx= 10, pady= 10, sticky= 'w')
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
            self.ingredients.pop(selection[0])
            with open('ingredients.dat', 'wb') as f:
                pickle.dump(self.ingredients, f)

    def add_ingredient(self):
        ingredient_name = self.add_ingredient_name_input.get()
        ingredient_quantifier = self.add_ingredients_quanitfier_input.get()

        if not ingredient_name and not ingredient_quantifier:
            self.error_message_var.set('Ingredient Name and quanitfier must both be filled out!')
        else:
            for ingredient in self.ingredients:
                if ingredient.get_name() == ingredient_name:
                    messagebox.showerror(
                        title= 'Error',
                        message= 'There is already an ingredient by that name'
                    )
                    return

            new_ingredient = Ingredient(ingredient_name, ingredient_quantifier)

            self.ingredient_list.insert(tk.END, str(new_ingredient))
            self.ingredients.append(new_ingredient)

            with open('ingredients.dat', 'wb') as f:
                pickle.dump(self.ingredients, f)

            self.add_ingredient_name_input.delete(0, tk.END)
            self.add_ingredients_quanitfier_input.delete(0, tk.END)
        
