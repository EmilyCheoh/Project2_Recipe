import script
import helper
import healthy
def display_healthy(ingredients, tools, methods, steps):
    ingredients,methods, steps = healthy.transform_to_healthy(ingredients, tools, methods, steps)
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

def display_unhealthy(ingredients, tools, methods, steps):
    ingredients,methods, steps = healthy.transform_to_unhealthy(ingredients, tools, methods, steps)
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
