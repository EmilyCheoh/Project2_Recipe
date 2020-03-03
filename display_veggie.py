import script
import helper
import vegetarian

def display_veggie_recipe(url):
    ingredients, directions, methods, tools = vegetarian.parse_new_veggie_recipe(url)
    print('-------Ingredients-----')
    for ingredient in ingredients:
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
    for step in directions:
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

def display_non_veggie_recipe(url):
    ingredients, directions, methods, tools = vegetarian.parse_new_non_veggie_recipe(url)
    print('-------Ingredients-----')
    for ingredient in ingredients:
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
    for step in directions:
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