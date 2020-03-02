import script
import helper
def merge_ingredient(ingredient):
    return str(ingredient['quantity'])+ ingredient['measurement']+ ingredient['ingredient_name']+ingredient['preparation']

def display(ingredients, tools, methods, steps):
    ingredients = helper.double_ingredient_size(ingredients)
    print('-------ingredients-----')
    for ingredient in ingredients:
        print(merge_ingredient(ingredient))
        print(ingredient)
        print()

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
