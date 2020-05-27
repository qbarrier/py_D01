import datetime
from recipe import Recipe

class Book:
    def __init__(self):
        self.name = "MyBook"
        self.last_update = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.creation_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.recipes_list = {
        "starter" : [],
        "lunch" : [],
        "dessert" : []
        }

    def __str__(self):
        txt = ""
        for x in self.recipes_list:
            for y in self.recipes_list[x]:
                txt += y.name + ' '
        return "\nBook name:\t{self.name}\nUpdate:\t\t{self.last_update}\nCreation:\t{self.creation_date}\nList:\t\t".format(self=self) + txt + "\n"


    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe):
            print("not a recipe class")
            quit()
        for t in self.recipes_list:
            if t == recipe.recipe_type:
                self.recipes_list[t].append(recipe)
                self.last_update = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        print("New Recipe !:\t" + recipe.name)
        pass




    def get_recipes_by_types(self, recipe_type):
        if not isinstance(recipe_type, str) or recipe_type not in ["lunch", "dessert", "starter"]:
            print("recipe_type must be starter/lunch/dessert only")
            quit()
        print("\nRecipes For: " + recipe_type)
        for name in self.recipes_list[recipe_type]:
            print(name.name)




    def get_recipe_by_name(self, name):
        if not isinstance(name, str):
            print("name must be a str")
            quit()
        print("\nsearch for: " + name)
        for x in self.recipes_list:
            for y in self.recipes_list[x]:
                if y.name == name:
                    print("\nRecipe:\t\t", y.name, "\nLvl:\t\t", y.cooking_lvl, "\nTime:\t\t", y.cooking_time, " minutes\nIngredients:\t", y.ingredients, "\nDescription:\t", y.description, "\nType:\t\t", y.recipe_type, "\n")
