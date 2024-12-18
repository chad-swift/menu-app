
import tkinter as tk
from tkinter import ttk
from manage_meals import *
from manage_ingredients import *
from classes import *
import pickle
class Main_window(tk.Tk):
    '''
    Class that generates the main menu for the menu app
    '''
    def __init__(self):
        super().__init__()
        self.geometry('1630x200')
        self.resizable(False, False)
        self.title('Main Window')

        
        self.week_frame = tk.Frame(
            self
        )

        # open ingredients data that is used for writing the grocery export to file later
        with open('ingredients.dat', 'rb') as f:
            try:
                self.ingredients: list[Ingredient] = pickle.load(f)
            except EOFError:
                self.ingredients = []
       
        self.make_day_frames(self.week_frame)

        btn_height = 2
        btn_width = 12

        # We pass the root on to the children windows so that they can manipulate things within this window later
        self.manage_meals_btn = tk.Button(
            self,
            text= 'Manage Meals',
            height= btn_height,
            width= btn_width,
            activebackground= '#FF0000',
            command= lambda: Manage_meals(self)
        )
        

        self.manage_ingredients_btn = tk.Button(
            self,
            text= 'Manage Ingredients',
            height= btn_height,
            width= btn_width,
            command= Manage_ingredients
        )
        

        self.export_btn = tk.Button(
            self,
            text= 'Export Menu and List',
            height= btn_height,
            width= btn_width,
            command= self.create_menu_list
        )
        
        
        self.week_frame.grid(row= 0, column= 0, rowspan= 3)
        self.manage_meals_btn.grid(row= 0, column= 7, padx= 10)
        self.manage_ingredients_btn.grid(row= 1, column= 7)
        self.export_btn.grid(row= 2, column= 7)


    def make_day_frames(self, week_frame: tk.Frame):
        '''
        Helper method for main class that generates the days for the week. 
        Parameter: week_frame - A Frame class passed to the method that the days are then created within
        '''
        # loading the meal data happens here so that it reloads when this function is called for refreshing purposes
        with open('meals.dat', 'rb') as f:
            try:
                self.meals: list[Meal] = pickle.load(f)
            except EOFError:
                self.meals = []

        self.meal_list = []

        for meal in self.meals:
            self.meal_list.append(meal.get_name())

        SELECTOR_WIDTH = 15

        self.monday_frame = tk.LabelFrame(
            week_frame,
            bg= '#434343',
            width= 166,
            height= 190,
        )

        self.monday_label = tk.Label(
            week_frame,
            text= 'Monday',
            bg= '#434343'
        )

        self.monday_meal_selector = ttk.Combobox(
            self.monday_frame,
            width= SELECTOR_WIDTH,
            values= self.meal_list,
        )

        self.tuesday_frame = tk.LabelFrame(
            week_frame,
            bg= '#434343',
            width= 166,
            height= 190,
        )

        self.tuesday_label = tk.Label(
            week_frame,
            text= 'Tuesday',
            bg= '#434343'
        )

        self.tuesday_meal_selector = ttk.Combobox(
            self.tuesday_frame,
            width= SELECTOR_WIDTH,
            values= self.meal_list
        )

        self.wednesday_frame = tk.LabelFrame(
            week_frame,
            bg= '#434343',
            width= 166,
            height= 190,
        )

        self.wednesday_label = tk.Label(
            week_frame,
            text= 'Wednesday',
            bg= '#434343'
        )

        self.wednesday_meal_selector = ttk.Combobox(
            self.wednesday_frame,
            width= SELECTOR_WIDTH,
            values= self.meal_list
        )

        self.thursday_frame = tk.LabelFrame(
            week_frame,
            bg= '#434343',
            width= 166,
            height= 190,
        )

        self.thursday_label = tk.Label(
            week_frame,
            text= 'Thursday',
            bg= '#434343'
        )

        self.thursday_meal_selector = ttk.Combobox(
            self.thursday_frame,
            width= SELECTOR_WIDTH,
            values= self.meal_list
        )

        self.friday_frame = tk.LabelFrame(
            week_frame,
            bg= '#434343',
            width= 166,
            height= 190,
        )

        self.friday_label = tk.Label(
            week_frame,
            text= 'Friday',
            bg= '#434343'
        )

        self.friday_meal_selector = ttk.Combobox(
            self.friday_frame,
            width= SELECTOR_WIDTH,
            values= self.meal_list
        )

        self.saturday_frame = tk.LabelFrame(
            week_frame,
            bg= '#434343',
            width= 166,
            height= 190,
        )

        self.saturday_label = tk.Label(
            week_frame,
            text= 'Saturday',
            bg= '#434343'
        )

        self.saturday_meal_selector = ttk.Combobox(
            self.saturday_frame,
            width= SELECTOR_WIDTH,
            values= self.meal_list
        )

        self.sunday_frame = tk.LabelFrame(
            week_frame,
            bg= '#434343',
            width= 166,
            height= 190,
        )

        self.sunday_label = tk.Label(
            week_frame,
            text= 'Sunday',
            bg= '#434343'
        )

        self.sunday_meal_selector = ttk.Combobox(
            self.sunday_frame,
            width= SELECTOR_WIDTH,
            values= self.meal_list
        )
        
        self.monday_label.grid(row= 0, column= 0)
        self.monday_meal_selector.grid(row= 1, column= 0, padx= 21,pady= 62)
        self.monday_frame.grid(row= 0, column= 0, rowspan= 3, pady= 10)
        self.tuesday_label.grid(row= 0, column= 1)
        self.tuesday_meal_selector.grid(row= 1, column= 1, padx= 21,pady= 62)
        self.tuesday_frame.grid(row= 0, column= 1, rowspan= 3, pady= 10)
        self.wednesday_label.grid(row= 0, column= 2)
        self.wednesday_meal_selector.grid(row= 1, column= 2, padx= 21,pady= 62)
        self.wednesday_frame.grid(row= 0, column= 2, rowspan= 3, pady= 10)
        self.thursday_label.grid(row= 0, column= 3)
        self.thursday_meal_selector.grid(row= 1, column= 3, padx= 21,pady= 62)
        self.thursday_frame.grid(row= 0, column= 3, rowspan= 3, pady= 10)
        self.friday_label.grid(row= 0, column= 4)
        self.friday_meal_selector.grid(row= 1, column= 4, padx= 21,pady= 62)
        self.friday_frame.grid(row= 0, column= 4, rowspan= 3, pady= 10)
        self.saturday_label.grid(row= 0, column= 5)
        self.saturday_meal_selector.grid(row= 1, column= 5, padx= 21,pady= 62)
        self.saturday_frame.grid(row= 0, column= 5, rowspan= 3, pady= 10)
        self.sunday_label.grid(row= 0, column= 6)
        self.sunday_meal_selector.grid(row= 1, column= 6, padx= 21,pady= 62)
        self.sunday_frame.grid(row= 0, column= 6, rowspan= 3, pady= 10)

    def remake_week(self):
        '''
        Method that refreshes days in the main function so that the comboboxes get all the new meals as options
        '''

        # delete the week_frame, which destroys all children
        self.week_frame.destroy()
        # create a new frame
        self.new_week_frame = tk.Frame(
            self
        )
        self.new_week_frame.grid(row= 0, column= 0, rowspan= 3)

        
        # pass it to the day creation method
        self.make_day_frames(self.new_week_frame)

    def create_menu_list(self):
        '''
        Method that creates the menu and grocery list output file
        '''
        # Capture each days currently selected meal
        monday_meal = self.monday_meal_selector.get()
        tuesday_meal = self.tuesday_meal_selector.get()
        wednesday_meal = self.wednesday_meal_selector.get()
        thursday_meal = self.thursday_meal_selector.get()
        friday_meal = self.friday_meal_selector.get()
        saturday_meal = self.saturday_meal_selector.get()
        sunday_meal = self.sunday_meal_selector.get()

        # store them in an array to make them easier to work with
        meals_for_the_week = [
            monday_meal, 
            tuesday_meal, 
            wednesday_meal, 
            thursday_meal, 
            friday_meal, 
            saturday_meal, 
            sunday_meal
            ]
        
        # create a new empty array for both ingredients and meals
        ingredient_list: list[Ingredient] = []
        meal_list: list[Meal] = []

        # append to the meal_list only the meals that appear within the selected meals
        for meal_name in meals_for_the_week:
            for meal in self.meals:
                if meal.get_name() == meal_name:
                    meal_list.append(meal)

        # go by ingredient so that each ingredient is only listed once and find each ingredient that is used. 
        for ingredient in self.ingredients:
            quantity = 0
            ingredient_name = ''
            quantifier = 'qty'
            for meal in meal_list:
                ingredient_name = ingredient.get_name()
                meal_ingredients = meal.get_ingredient_names()
                if ingredient_name not in meal_ingredients:
                    continue
                quantity += meal.get_specific_ingredient_quantity(ingredient_name)
                quantifier = meal.get_specific_ingredient_quantifier(ingredient_name)
            ingredient_list.append(f'{quantity:.2f} {quantifier} of {ingredient_name}')
        

        # now we need to write all this to a text file
        with open('menu.txt', 'w') as f:
            # clever way to do the days here, initialize a counter
            i = 0

            # make a tuple of the days
            days = (
                'Monday',
                'Tuesday',
                'Wednesday',
                'Thursday',
                'Friday',
                'Saturday',
                'Sunday'
            )

            # write the menu to the file, with a header
            f.write('Menu:\n----------------\n')
            for meal_name in meals_for_the_week:
                # This days of i here is just the index of the tuple, days[0] would be Monday, days[1] would be Tuesday, and so on
                f.write(f'{days[i]}: {meal_name} \n')
                i += 1
            # write the ingredients list to file, with a header
            f.write(f'\nIngredients Needed for Meals selected:\n-----------------\n')
            for ingredient in ingredient_list:
                f.write(ingredient + '\n')
        # tell the user it was successful
        messagebox.showinfo(
            title= 'Sucess!',
            message= 'Menu list sucessfully exported to file, see menu.txt for list'
        )


if __name__ == '__main__':
    Main_window().mainloop()