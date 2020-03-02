import script
import helper
def display(ingredients, tools, methods, steps):
    ingredients = helper.cut_ingredient_size(ingredients)
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
