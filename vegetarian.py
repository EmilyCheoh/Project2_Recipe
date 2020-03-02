from helper import *
import script
import copy

to_veggie = {
    'ground beef' : 'tofu',
    'lean ground beef' : 'tofu',
    'meat' : 'tofu',
    'beef' : 'tofu',
    'steak': 'mushroom',
    'fish' : 'tofu',
    'goat' : 'tofu',
    'lamb' : 'tofu',
    'meatball' : 'vegetarian meatball',
    'pork' : 'tofu',
    'poultry' : 'tofu',
    'sausage' : 'vegetarian sausage',
    'seafood' : 'tofu',
    'chicken broth' : 'vegetable broths'
}

meats = [
    'lean ground beef', 
    'ground beef','beef', 
    'fish', 
    'goat', 
    'lamb', 
    'meatball', 
    'pork', 
    'poultry', 
    'sausage', 
    'seafood',
    'chicken broth']

def get_recipe(name):
    rf = script.RecipeFetcher()
    recipe = rf.search_recipes(name)[0]
    result = rf.scrape_recipe(recipe)
    ingredients = result['ingredients']
    directions = result['directions']
    return ingredients, directions

def get_tokenized_ingredients_and_steps(ingredients_lst, directions_lst):
    tokenized_ingredients = []
    for ing in ingredients_lst:
        tokenized_ingredients.append(tokenize_ingredient(ing))
    ingredient_names = []
    for ingredient in tokenized_ingredients:
        ingredient_names.append(ingredient['ingredient_name'])
    tools, methods, tokenized_steps = get_steps(directions_lst, ingredient_names)
    return tokenized_ingredients, tokenized_steps

# returns vegetarian recipe
def to_veggie_ingredient(ingredients_lst):
    tokenized_ingredients = copy.deepcopy(ingredients_lst)
    # for ing in ingredients_lst:
    #     tokenized_ingredients.append(tokenize_ingredient(ing))
    for ingredient in tokenized_ingredients:
        ingredient_name = ingredient['ingredient_name']
        for meat in meats:
            if meat in ingredient_name.lower():
                ingredient['ingredient_name'] = to_veggie[meat]
    return tokenized_ingredients
    
def modify_directions_veggies(steps):
    steps_copy = copy.deepcopy(steps)
    for step in steps_copy:
        ingredients = step[1]['ingredient']
        for index, ingredient in enumerate(ingredients):
            for meat in meats:
                if meat in ingredient.lower():
                    ingredients[index] = ingredient.replace(meat, to_veggie[meat])
                break
        instruction = step[0]
        for meat in meats:
            if meat in instruction.lower():
                step[0] = instruction.replace(meat, to_veggie[meat])
                break
    return steps_copy

# def parse_new_recipe(name):
#     ingredients, directions = get_recipe(name)
#     tokenized_ingredients, tokenized_steps = get_tokenized_ingredients_and_steps(ingredients, directions)

#     veggie_ingredients = to_veggie_ingredient(tokenized_ingredients)
#     veggie_directions = modify_directions_veggies(tokenized_steps)

#     parsed_ingredients_lst = []
#     for ing in veggie_ingredients:
#         # text = f'{ing['quantity']} {ing['measurement']} {ing['ingredient_name']}'
#         text = ''.join((ing['quantity'], ing['measurement'], ing['ingredient_name']))
#         parsed_ingredients_lst.append(text)


#     return parsed_ingredients_lst, veggie_directions