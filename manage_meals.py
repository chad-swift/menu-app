import tkinter as tk

class Manage_meals(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Manage Meals')
        self.geometry('300x800'),
        self.resizable(False, False)

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

        self.meal_list_label = tk.Label(
            self,
            text= 'Meal List:'
        ).grid(row= 0, column= 0, sticky= 'w')

        self.selected_meal = tk.IntVar()

        self.meal_list = tk.Listbox(
            self,
            width= '30',
            height= '10',
            selectmode= 'browse'
        )

        for meal in sampleMeals:
            self.meal_list.insert(tk.END, meal)

        self.meal_list.grid(row= 1, column= 0, sticky= 'we', padx= 15, pady= 3)

        self.delete_meal_btn = tk.Button(
            self,
            text= 'Delete Meal',
            fg= 'red',
            command= self.delete_meal
        ).grid(row= 2, column= 0)

    def delete_meal(self):
        selection = self.meal_list.curselection()

        if selection:
            self.meal_list.delete(selection[0])

def run_window():
    Manage_meals().mainloop()

run_window()