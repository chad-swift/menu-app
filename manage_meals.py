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

        self.mealListLabel = tk.Label(
            self,
            text= 'Meal List:'
        ).grid(row= 0, column= 0, sticky= 'w')

        self.selectedMeal = tk.IntVar()

        self.mealList = tk.Listbox(
            self,
            width= '30',
            height= '10',
            selectmode= 'browse'
        )

        for meal in sampleMeals:
            self.mealList.insert(tk.END, meal)

        self.mealList.grid(row= 1, column= 0, columnspan= 3, sticky= 'we', padx= 15, pady= 3)

        self.deleteMealBtn = tk.Button(
            self,
            text= 'Delete Meal',
            fg= 'red',
            command= self.deleteMeal
        ).grid(row= 2, column= 0, columnspan= 3)

    def deleteMeal(self):
        selection = self.mealList.curselection()

        if selection:
            self.mealList.delete(selection[0])

def runWindow():
    Manage_meals().mainloop()

runWindow()