class Ingredient:
    def __init__(self, ingredient_id, name):
        self.ingredient_id = ingredient_id
        self.name = name

class Recipe:
    def __init__(self, recipe_id, title, ingredients, instructions, user):
        self.recipe_id = recipe_id
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.user = user

class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username

class RecipeManager:
    def __init__(self):
        self.ingredients = []
        self.recipes = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def add_recipe(self, title, ingredient_names, instructions, user):
        ingredients = [ingredient for ingredient in self.ingredients if ingredient.name in ingredient_names]
        if ingredients:
            recipe_id = len(self.recipes) + 1
            recipe = Recipe(recipe_id, title, ingredients, instructions, user)
            self.recipes.append(recipe)
            return recipe
        else:
            return None 

    def search_by_ingredient(self, ingredient_name):
        matching_recipes = []
        for recipe in self.recipes:
            for ingredient in recipe.ingredients:
                if ingredient.name.lower() == ingredient_name.lower():
                    matching_recipes.append(recipe)
                    break  
        return matching_recipes


user1 = User(user_id=1, username="Ankita")
ingredient1 = Ingredient(ingredient_id=101, name="Tomato")
ingredient2 = Ingredient(ingredient_id=102, name="Cheese")
ingredient3 = Ingredient(ingredient_id=103, name="Bread")

recipe_manager = RecipeManager()

recipe_manager.add_ingredient(ingredient1)
recipe_manager.add_ingredient(ingredient2)
recipe_manager.add_ingredient(ingredient3)

recipe = recipe_manager.add_recipe(title="Tomato Sandwich", ingredient_names=["Tomato", "Cheese", "Bread"], instructions="Assemble ingredients and enjoy!", user=user1)

if recipe:
    print("Recipe added successfully by {}!".format(recipe.user.username))
else:
    print("Recipe cannot be added without valid ingredients.")

# Recipes Containing "Cheese"
ingredient_name_to_search = "Cheese"
matching_recipes = recipe_manager.search_by_ingredient(ingredient_name_to_search)

print("\nRecipes containing {}:".format(ingredient_name_to_search))
for matching_recipe in matching_recipes:
    print("{} by {}".format(matching_recipe.title, matching_recipe.user.username))