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
    def __init__(self, name: str, ingredients: list[tuple[Ingredient, float]]):
        self.name = name
        self.ingredients = ingredients

        self.ingredient_list = {}

        for ingredient, quantity in self.ingredients:
            self.ingredient_list[ingredient.get_name()] = {
                "ingredient": ingredient,
                "quantity": quantity
            }

    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name

    def get_ingredients(self):
        ingredients = []

        for _, value in self.ingredient_list.items():
            ingredients.append(value['ingredient'])

        return ingredients

    def get_ingredient_names(self):
        names = []

        for key, value in self.ingredient_list.items():
            names.append(key)

        return names
    
    def get_ingredient_quantities(self):
        quantities = []

        for key, value in self.ingredient_list.items():
            quantities.append((key, value['quantity']))

        return quantities
    
    def get_specific_ingredient_quantity(self, ingredient_name):
        return self.ingredient_list[ingredient_name]['quantity']
    
    def set_specific_ingredient_quantity(self, ingredient_name, new_quantity):
        self.ingredient_list[ingredient_name]['quantity'] = new_quantity

    def get_specific_ingredient_quantifier(self, ingredient_name: str):
        return self.ingredient_list[ingredient_name]['ingredient'].get_quantifier()
    
    def append_ingredient(self, ingredient: Ingredient, quantity):
        self.ingredient_list[ingredient] = {
            "ingredient": ingredient,
            "quantity": quantity
        }