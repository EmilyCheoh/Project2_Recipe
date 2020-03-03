from helper import *
import script
import copy
import re

to_veggie = {
    'clam' : 'mushroom',
    'mussel' : 'mushroom',
    'lobster' : 'lobster mushrooms',
    'octopus' : ' king oyster mushroom',
    'salmon' : 'carrot',
    'ground beef' : 'tofu',
    'lean ground beef' : 'tofu',
    'crab' : 'vegan crab',
    'tuna' : 'tofu',
    'meat' : 'tofu',
    'beef' : 'tofu',
    'steak': 'mushroom',
    'fish' : 'fishless filets',
    'goat' : 'tofu',
    'lamb' : 'tofu',
    'meatball' : 'vegetarian meatball',
    'pork' : 'tofu',
    'poultry' : 'tofu',
    'sausage' : 'vegetarian sausage',
    'seafood' : 'tofu',
    'chicken broth' : 'vegetable broths',
    'fish stock' : 'vegetable stock',
    'oyster sauce' : 'soy sauce',
    'oyster' : 'vegan oyster',
    'shrimp': 'vegan shrimp'
}

to_meat = {
    'tofu' : 'meat',
    'mushroom' : 'beef',
    'vegetarian meatball' : 'meatball',
    'vegan meatball' : 'meatball',
    'vegetarian sausage' : 'sausage',
    'vegan sausage' : 'sausage',
    'beans' : 'ground beef',
    'vegetable broths' : 'chicken broth',
    'vegetable oil' : 'beef fat',
    'oil': 'beef fat',
    'vegetable stock' : 'chicken stock',
    'zucchini' : 'meat',
    'meatless' : 'normal'
}

################################################

def get_recipe(url):
    rf = script.RecipeFetcher()
#     recipe = rf.search_recipes(name)[0]
    result = rf.scrape_recipe(url)
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
    return tools, methods, tokenized_ingredients, tokenized_steps

################################################

# returns VEGETARIAN recipe
def to_veggie_ingredient(ingredients_lst):
    tokenized_ingredients = copy.deepcopy(ingredients_lst)
    for ingredient in tokenized_ingredients:
        ingredient_name = ingredient['ingredient_name'].rstrip(',')
        for meat in to_veggie.keys():
            if re.match(rf'.*{meat}.*', ingredient_name.lower(), re.IGNORECASE):
                ingredient['ingredient_name'] = to_veggie[meat]
                print()
                print('-------------------------')
                print()
                replace_info = f"Replaced {ingredient_name.lower().strip()} with {to_veggie[meat]}."
                print(replace_info)
                print()
                break
    return tokenized_ingredients
    
def modify_directions_veggies(steps):
    steps_copy = copy.deepcopy(steps)
    for step in steps_copy:
        ingredients = step[1]['ingredient']
        for index, ingredient in enumerate(ingredients):
            for meat in to_veggie.keys():
#                 if meat in ingredient.lower():
                if re.match(rf'.*{meat}.*', ingredient.lower(), re.IGNORECASE):
                    ingredients[index] = ingredient.replace(meat, to_veggie[meat])
                break
        instruction = step[0]
        for meat in to_veggie.keys():
            if meat in instruction.lower():
                step[0] = instruction.replace(meat, to_veggie[meat])
                break
    return steps_copy

def parse_new_veggie_recipe(name):
    ingredients, directions = get_recipe(name)
    tools, methods, tokenized_ingredients, tokenized_steps = get_tokenized_ingredients_and_steps(ingredients, directions)

    veggie_ingredients = to_veggie_ingredient(tokenized_ingredients)
    veggie_directions = modify_directions_veggies(tokenized_steps)

    parsed_ingredients_lst = []
    for ing in veggie_ingredients:
        if re.match(r'.*or to taste', ing['preparation'], re.IGNORECASE):
            text = ''.join((ing['quantity'], ing['measurement'], ing['ingredient_name'].strip(), ', or to taste'))
        else:
            text = ''.join((ing['quantity'], ing['measurement'], ing['ingredient_name']))
        parsed_ingredients_lst.append(text.strip())
        
    parsed_directions_lst = []
    for stp in veggie_directions:
        parsed_directions_lst.append(stp[0])


    return parsed_ingredients_lst, veggie_directions, methods, tools

################################################

# returns NON-VEGETARIAN recipe
def to_non_veggie_ingredient(ingredients_lst):
    tokenized_ingredients = copy.deepcopy(ingredients_lst)
    for ingredient in tokenized_ingredients:
        ingredient_name = ingredient['ingredient_name'].rstrip(',')
        for veg in to_meat.keys():
            if re.match(rf'.*{veg}.*', ingredient_name.lower(), re.IGNORECASE):
                ingredient['ingredient_name'] = to_meat[veg]
                replace_info = f"Replaced {ingredient_name.lower().strip()} with {to_meat[veg]}."
                print()
                print('--------------------')
                print()
                print(replace_info)
                print()
                # print('Replaced', ingredient_name.lower(), 'with', to_meat[veg], '. ')
                break
    return tokenized_ingredients
    
def modify_directions_non_veggies(steps):
    steps_copy = copy.deepcopy(steps)
    for step in steps_copy:
        ingredients = step[1]['ingredient']
        for index, ingredient in enumerate(ingredients):
            for veg in to_meat.keys():
                if re.match(rf'.*{veg}.*', ingredient.lower(), re.IGNORECASE):
                    ingredients[index] = ingredient.replace(veg, to_meat[veg])
                break
        instruction = step[0]
        for veg in to_meat.keys():
            if veg in instruction.lower():
                step[0] = instruction.replace(veg, to_meat[veg])
                break
    return steps_copy

def parse_new_non_veggie_recipe(name):
    ingredients, directions = get_recipe(name)
    tools, methods, tokenized_ingredients, tokenized_steps = get_tokenized_ingredients_and_steps(ingredients, directions)

    non_veggie_ingredients = to_non_veggie_ingredient(tokenized_ingredients)
    non_veggie_directions = modify_directions_non_veggies(tokenized_steps)

    parsed_ingredients_lst = []
    for ing in non_veggie_ingredients:
        # text = f'{ing['quantity']} {ing['measurement']} {ing['ingredient_name']}'
        text = ''.join((ing['quantity'], ing['measurement'], ing['ingredient_name']))
        parsed_ingredients_lst.append(text.strip())
        
    parsed_directions_lst = []
    for stp in non_veggie_directions:
        parsed_directions_lst.append(stp[0].strip())


    return parsed_ingredients_lst, non_veggie_directions, methods, tools