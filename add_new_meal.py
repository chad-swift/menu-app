import tkinter as tk
from tkinter import ttk
from sample_data import *
class Add_new_meal(tk.Toplevel):
    '''
    This window will allow the user to create a new meal, and add that meal to the meal list, where it will show up in all windows that need it
    '''
    def __init__(self):
        super().__init__()
        self.title('Add New Meal')
        self.geometry('500x600')
        self.resizable(False, False)    
        
        # label and input for name
        self.name_label = tk.Label(
            self,
            text= 'Name of new Meal:'
        )

        self.name_input = tk.Entry(
            self,
            width= 30
        )
        
        #label and listbox showing what ingredients are going to be in the new meal
        self.ingredient_list_label = tk.Label(
            self,
            text= 'List of Ingredients in Meal:'
        )

        self.ingredientList = tk.Listbox(
            self,
            width= 52
        )
        
        #currently this pulls from the sample data, but eventually this will pull from a pickled data source
        self.ingredients = sample_ingredients

        # button to remove ingredients added to the meal
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

        
        self.ingredient_choice_arr = []

        # currently the ingredients list is stored in a dictionary where the key is the name of the ingredient and the value is the quantifier of that 
        # ingredient, example: 'mustard' : 'oz' as mustard is quanitfied in oz. So we take the dictionary, and add the keys to a separate array so that the 
        # combobox has a simple list to pull from
        for key in self.ingredients.keys():
            self.ingredient_choice_arr.append(key)

        self.ingredient_choices = ttk.Combobox(
            self.add_ingredients_frame,
            width= 10,
            values= self.ingredient_choice_arr,
        )

        # This code binds the event of "any time the combobox is updated" to a method that will change the quanitfier label to match what was stored with the 
        # ingredient key. Example, when the user selects "mustard" from the list, the label will update to "oz", to make it very clear to the user what they are 
        # adding and how much of it to their meal. 
        self.ingredient_choices.bind('<<ComboboxSelected>>', self.update_amt_quanitfier)


        self.ingredient_name_label = tk.Label(
            self.add_ingredients_frame,
            text= 'Ingredient Name:'
        )

        self.ingredient_amt_label = tk.Label(
            self.add_ingredients_frame,
            text= 'Ingredient Amount: '
        )

        # doubleVar makes it easy to store, update, and grab the value in the Spinbox
        self.ingredient_amt_var = tk.DoubleVar()

        # the spinbox is a float with an increment of 0.25 simply so that when the quanitfier is something small, like oz, they can select a small amount. It 
        # goes up to 100 in case of large quanifiers, like lbs. 
        self.ingredient_amt_input = tk.Spinbox(
            self.add_ingredients_frame,
            from_= 0,
            to_= 100,
            increment= 0.25,
            textvariable= self.ingredient_amt_var,
            width= 10
        )

        # this variable here is what is being updated with the bound method in comboBox.

        # Right now there is a bug. When this window is called from other windows this text will not show up, but when I add code to call itself it does
        self.amt_quantifier = tk.StringVar(value= 'Qty')


        # this label just pulls the variable stored in the amt_quantifier label. It starts at "Qty" until the user picks something from the combobox, then 
        # updates to the appropriate quanitfier
        self.ingredient_amt_quantifier = tk.Label(
            self.add_ingredients_frame,
            textvariable = self.amt_quantifier
        )

        # button to add ingredient to the listbox above
        self.add_ingredient_to_list_btn = tk.Button(
            self.add_ingredients_frame,
            text= 'Add Ingredient to Meal',
            command= self.add_ingredient_to_meal,
            fg= 'green'
        )

        # this button has not been set up to be functional yet, but it will add the meal to the dictionary, refresh any lists that are currently using that 
        # dictionary, and then will close this window to return to the "manage meals" window
        self.add_to_meal_btn = tk.Button(
            self.add_ingredients_frame,
            text= 'Add Meal',
            fg= 'green'
        )

        self.grid_items()

    def grid_items(self):
        '''
        This method is just for organizational purposes. It contains all the packaging of all of the labels and buttons for the entire app. 
        '''
        self.name_label.grid(row= 0, column= 0, columnspan= 3, sticky= 'w', pady = 10)
        self.name_input.grid(row= 0, column= 1, sticky= 'w')
        self.ingredient_list_label.grid(row= 1, column= 0, sticky= 'w', pady= 10)
        self.ingredientList.grid(row= 3, column= 0, columnspan= 4, sticky= 'w', padx= 10)
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
        This method grabs the selection from the ingredients combobox, takes the amount from the spinbox, and puts them together in a string for the user. This method will also hold an object of everything added until it is ready to submit
        '''

        # right now this method only does the first part, it adds a string containing the amount and ingredient name and adds them to the listbox so the user can see them. More functionality will be added later to form an object in a holding state that would be submitted by a different method

        # this variable returns the index of what has been selected by the combobox
        ingredient_name = self.ingredient_choices.current()

        # this variable then takes that index and searches for the correct item in the values array that the combobox also uses to populate itself, finding its name
        currentSelectionName = self.ingredient_choice_arr[self.currentSelection]

        # this variable then grabs the amount of the ingredient stored in the name
        ingredient_amt = self.ingredient_amt_var.get()

        ingredient_quantifier = self.amt_quantifier.get()

        # a string is then inserted in the Listbox for the user to see, containing the amount added and of what
        if ingredient_name:
            self.ingredientList.insert(tk.END, (f'{ingredient_amt:.1f} {ingredient_quantifier} of {currentSelectionName}'))

        # the spinbox variable is then reset to 0 so the user doesn't accidentally add in the same quantity for the next ingredient
        self.ingredient_amt_var.set(0.0)


        # the comboxbox is then set to a blank so that the user doesn't accidentally add the same ingredient twice
        self.ingredient_choices.set('')

    def update_amt_quanitfier(self, event):
        '''
        Event method that updates the 'qty' label with the stored quanitfier within the ingredients dictionary
        '''

        # this gets the current choice from the combobox in index form
        self.currentSelection = self.ingredient_choices.current()

        # this then retrieves the name in the index spot
        self.currentSelectionName = self.ingredient_choice_arr[self.currentSelection]

        # this sets the stringVar variable equal to the value of ingredient key, which should be its quantifier (oz, lbs, etc)
        self.amt_quantifier.set(self.ingredients[self.currentSelectionName])

    def remove_ingredients_from_meal(self):
        '''
        This method removes ingredients added to the list and should also remove them from the temporary object storage
        '''
        selection = self.ingredientList.curselection()

        if selection:
            self.ingredientList.delete(selection[0])