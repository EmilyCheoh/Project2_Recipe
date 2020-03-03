import script
import helper
def merge_ingredient(ingredient):
    return str(ingredient['quantity'])+ ingredient['measurement']+ ingredient['ingredient_name']+ingredient['preparation']

def display(ingredients, tools, methods, steps):
    ingredients = helper.double_ingredient_size(ingredients)
    print('-------Ingredients-----')
    for ingredient in ingredients:
        print(merge_ingredient(ingredient))
        print(ingredient)
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