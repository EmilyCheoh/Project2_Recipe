import script
import helper

def merge_ingredient(ingredient):
    return ingredient['quantity']+ ingredient['measurement']+ ingredient['ingredient_name']+ingredient['preparation']
def display(search_url):
    rf = script.RecipeFetcher()
    # meat_lasagna = rf.search_recipes(search_term)[0]
    result = rf.scrape_recipe(search_url)
    ings = result['ingredients']
    ingredients = []
    for ingredient in ings:
        ingredients.append(helper.tokenize_ingredient(ingredient))

    ingredient_names = []
    for ingredient in ingredients:
        ingredient_names.append(ingredient['ingredient_name'])

    directions = result['directions']
    tools, methods, steps = helper.get_steps(directions, ingredient_names)

    print('-------Ingredients-----')
    
    for ingredient in ingredients:
        print(merge_ingredient(ingredient).rstrip(','))
        print('..........')
        print('name:', ingredient['ingredient_name'].rstrip(','))
        print('quantity:', ingredient['quantity'])
        print('measurement:', ingredient['measurement'])
        print('preparation:', ingredient['preparation'])
        print()
    print('\n-------Tools-----')
    for tool in tools:
        print(tool)

    print('\n-------Methods-----')
    for method in methods:
        print(method)

    print('\n-------Steps------')
    cnt = 1
    for step in steps:
        print("step", cnt)
        print(step[0].strip())
        print('..........')
        
        if len(step[1]['ingredient']) != 0:
            print('ingredients: ', end = '')
            for ing in step[1]['ingredient'][:-1]:
                print(ing.strip(), end = ', ')
            print(step[1]['ingredient'][-1])
        
        if len(step[1]['cooking tools']) != 0:
            print('cooking tools: ', end = '')
            for ing in step[1]['cooking tools'][:-1]:
                print(ing.strip(), end = ', ')
            print(step[1]['cooking tools'][-1])

        if len(step[1]['cooking methods']) != 0:
            print('cooking methods: ', end = '')
            for ing in step[1]['cooking methods'][:-1]:
                print(ing.strip(), end = ', ')
            print(step[1]['cooking methods'][-1])

        if len(step[1]['time']) != 0:
            print('cooking time: ', end = '')
            for ing in step[1]['time'][:-1]:
                print(ing.strip(), end = ', ')
            print(step[1]['time'][-1])
        print()
        cnt+=1

    return ingredients, tools, methods, steps
