import script
import helper
def display(search_term):
    rf = script.RecipeFetcher()
    meat_lasagna = rf.search_recipes(search_term)[0]
    result = rf.scrape_recipe(meat_lasagna)
    ings = result['ingredients']
    ingredients = []
    for ingredient in ings:
        ingredients.append(helper.tokenize_ingredient(ingredient))

    ingredient_names = []
    for ingredient in ingredients:
        ingredient_names.append(ingredient['ingredient_name'])

    directions = result['directions']
    tools, methods, steps = helper.get_steps(directions, ingredient_names)

    print('-------ingredients-----')
    for ingredient in ingredients:
        print(ingredient)
    print('\n-------tools-----')
    print(tools)

    print('\n-------methods-----')
    print(methods)

    print('\n-------steps------')
    cnt = 1
    for step in steps:
        print("step ",cnt)
        print(step[0])
        print(step[1])
        print()
        cnt+=1

    return ingredients, tools, methods, steps
