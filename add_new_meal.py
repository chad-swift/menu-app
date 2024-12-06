import tkinter as tk
from tkinter import ttk

class add_new_meal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Add New Meal')
        self.geometry('500x600')
        self.resizable(False, False)

        self.name_label = tk.Label(
            self,
            text= 'Name of new Meal:'
        ).grid(row= 0, column= 0, columnspan= 3, sticky= 'w')

        self.name_input = tk.Entry(
            self,
            width= 30
        ).grid(row= 0, column= 1, sticky= 'w')

        self.ingredient_list_label = tk.Label(
            self,
            text= 'List of Ingredients in Meal:'
        ).grid(row= 1, column= 0, sticky= 'w')

        self.ingredientList = tk.Listbox(
            self,
            width= 45
        )

        self.ingredientList.grid(row= 3, column= 0, columnspan= 4, sticky= 'w', padx= 10)

        sample_ingredients = (
            'pepperoni',
            'ham',
            'sausage',
            'tomato',
            'mustard',
            'black olives',
            'cheese'
        )

        #self.ingredients_section_label = tk.Label(
         #   self,
          #  text= 'Add Existing Ingredient To Ingredients List in Meal:'
       # ).grid(row= 4, columnspan= 4, sticky= 'w')

        self.ingredient_choices = ttk.Combobox(
            self,
            values= sample_ingredients,
            width= 25
        )


        self.ingredient_name_label = tk.Label(
            self,
            text= 'Ingredient Name:'
        ).grid(row= 5, column= 0, sticky= 'w', columnspan= 3)


        self.ingredient_choices.grid(row= 5, column= 1, sticky= 'w')

        self.ingredient_amt_label = tk.Label(
            self,
            text= 'Ingredient Amount: '
        ).grid(row= 6, column= 0, sticky= 'w')

        self.ingredient_amt_var = tk.IntVar()

        self.ingredient_amt = tk.Spinbox(
            from_= 0,
            to_= 100,
            increment= 0.25,
            textvariable= self.ingredient_amt_var,
            width= 4
        ).grid(row= 6, column= 1, sticky= 'w')

        self.add_ingredient_to_list_btn = tk.Button(
            self,
            text= 'Add Ingredient to Meal'
        ).grid(row= 7, column= 0, columnspan= 4)


def run_window():
    add_new_meal().mainloop()

run_window()