cookbook = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10
    },
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60
    },
    'salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15
    }
}


def choose():
    ask = """Please select an option by typing the corresponding number:
    1: Add a recipe
    2: Delete a recipe
    3: Print a recipe
    4: Print the cookbook
    5: Quit"""
    print(ask)
    user_response = input(">>  ")
    if user_response.isdigit():
        return (int(user_response))
    else:
        e = "This option does not exist, please type the corresponding number."
        e2 = "\nTo exit, enter 5."
        while True:
            print(e, e2)
            user_response = input(">>  ")
            if user_response.isdigit():
                return (int(user_response))


def print_recipe(recipe=''):
    if not recipe:
        print("Please enter the recipe's name to get its details:")
        recipe = input(">> ")
    if recipe in cookbook:
        print("")
        name = "Recipe for {name}"
        ingredients = "Ingredients list: {list}"
        meal = "To be eaten for {meal}."
        time = "Takes {time:0>2} minutes of cooking."
        print(name.format(name=recipe))
        print(ingredients.format(list=cookbook[recipe]['ingredients']))
        print(meal.format(meal=cookbook[recipe]['meal']))
        print(time.format(time=cookbook[recipe]['prep_time']))
        print("\n")
    else:
        print("\nThis recipe doesn't exist in the cookbook.\n")


def print_cookbook():
    print("This cookbook contains these recipes:")
    toPrint = " - {name}"
    for recipe in cookbook:
        print(toPrint.format(name=recipe))
    print("")


def delRecipe():
    print("Please enter the recipe's name to delete:")
    recipe = input(">> ")
    if recipe in cookbook:
        del cookbook[recipe]
        print("The recipe has been deleted.\n")
        print_cookbook()
    else:
        print("\nThis recipe doesn't exist in the cookbook.\n")


def addRecipe():
    print("Please enter a recipe name:")
    recipeName = input(">> ")
    ingredients = list()
    ingredient = ""
    pIngre = "Please enter a list of ingredients for your recipe"
    print(pIngre, "  (enter 'done' for finish):")
    while ingredient != "done":
        ingredient = input(">> ")
        if ingredient != "done":
            ingredients.append(ingredient)
    print("Please enter the meal of your recipe (starter, lunch, dessert):")
    meal = input(">> ")
    if meal != "starter" and meal != "lunch" and meal != "dessert":
        while True:
            print("Please enter starter, lunch or dessert:")
            meal = input(">> ")
            if meal == "starter" or meal == "lunch" or meal == "dessert":
                break
    print("Please enter a preparation time for your recipe (only number):")
    prep_time = input(">> ")
    if not prep_time.isdigit():
        while True:
            print("Please enter a number:")
            prep_time = input(">> ")
            if prep_time.isdigit():
                break
    recipeDict = dict()
    recipeDict['ingredients'] = ingredients
    recipeDict['meal'] = meal
    recipeDict['prep_time'] = prep_time
    cookbook[recipeName] = recipeDict
    print("")
    print_cookbook()


if __name__ == "__main__":
    while True:
        user_input = choose()
        if user_input == 1:
            addRecipe()
        if user_input == 2:
            delRecipe()
        if user_input == 3:
            print_recipe()
        if user_input == 4:
            print_cookbook()
        if user_input == 5:
            print("Cookbook closed.")
            exit()
