import pickle

class Ingredient():
    def __init__(self, name: str, quantifier: str):
        self.name = name
        self.quantifier = quantifier
    
    def get_name(self):
        return self.name
    
    def set_name(self, new_name: str):
        self.name = new_name

    def get_quantifier(self):
        return self.quantifier

    def set_quantfier(self, new_quantifier):
        self.quantifier = new_quantifier

    def __str__(self):
        return (f'{self.name: <15}|{self.quantifier: >10}')

class Meal():
    def __init__(self, name, ingredients: list[Ingredient]):
        self.name = name
        self.ingredients = ingredients

    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name

    def get_ingredients(self):
        return self.ingredients
    
    def append_ingredient(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)


def createSampleData():
    banana = Ingredient('Banana', 'oz')
    ham = Ingredient('Ham', 'lbs')
    mustard = Ingredient('Mustard', 'tsp')

    ingredientList1 = [banana, ham, mustard]

    sample_meal = Meal('Sample Meal', ingredientList1)

    list_of_meals = [sample_meal]

    with open('meals.dat', 'wb') as f:
        pickle.dump(list_of_meals, f)

    with open('ingredients.dat', 'wb') as f:
        pickle.dump(ingredientList1, f)

createSampleData()