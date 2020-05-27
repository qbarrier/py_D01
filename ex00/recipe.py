class Recipe:
    def check(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if not isinstance(name, str):
            print("name must be str!")
            quit()
        if not isinstance(cooking_lvl, int) or cooking_lvl not in range(1,6):
            print("lvl must be in range(1-5)")
            quit()
        if not isinstance(cooking_time, int) or cooking_time <= 0:
            print("time must be positiv digit")
            quit()
        if not isinstance(ingredients, list):
            print("ingredients must be a list of string!")
            quit()
        for x in ingredients:
            if not isinstance(x, str):
                print("ingredients must be a list of string!")
                quit()
        if not isinstance(description, str):
            print("description must be a string")
            quit()
        if not isinstance(recipe_type, str) or recipe_type not in ["lunch", "starter", "dessert"]:
            print("type must be lunch/starter/dessert only")
            quit()

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.check(name, cooking_lvl, cooking_time, ingredients, description, recipe_type)
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        return "\nRecipe:\t\t{self.name}\nLvl:\t\t{self.cooking_lvl}\nTime:\t\t{self.cooking_time} minutes\nIngredients:\t{self.ingredients}\nDescription:\t{self.description}\nType:\t\t{self.recipe_type}\n".format(self=self)

