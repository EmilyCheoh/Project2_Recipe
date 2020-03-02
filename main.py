import script
import helper
import display_recipes
import display_veges
import display_double
import display_half
import french
import italian
import copy
quit = False
while not quit:
    search_term = input("Please enter an ingredient name:\n")
    ingredients_orig, tools_orig, methods_orig, steps_orig = display_recipes.display(search_term)
    while True:
        ingredients = copy.deepcopy(ingredients_orig)
        tools = copy.deepcopy(tools_orig)
        steps = copy.deepcopy(steps_orig)
        methods = copy.deepcopy(methods_orig)
        transform = 'Transformation List:\n 1. To Vegetarian/to Non-Vegetarian \n 2. To healthy/ To unhealthy\n 3. to French/Italian Style of cuisine\n 4. Double the amount or cut it by half\n\nPlease select your transformation:  '
        select = input(transform)
        while not select.isdigit() or int(select)<1 or int(select)>4:
            print("invalid input, please enger digit\n\n")
            select = input(transform)
            
        select = int(select)
        if select==1:
            print("to vege")
        elif select==2:
            healthy_str = "\n Press 1 to transform to healthy \n Press 2 to transform to unhealthy\n\nPlease select your transformation:  "
            select = input(healthy_str)
            while not select.isdigit() or int(select)<1 or int(select)>2:
                print("invalid input, please enger digit\n\n")
                select = input(healthy_str)
            select = int(select)
            if select==1:
                display_veges.display_healthy(ingredients, tools, methods, steps)
            else:
                display_veges.display_unhealthy(ingredients, tools, methods, steps)
            # print('to healthy')
        elif select == 3:
            cuisine_str = "\n Press 1 to transform to French \n Press 2 to transform to Italian\n\nPlease select your transformation:  "
            select = input(cuisine_str)
            while not select.isdigit() or int(select)<1 or int(select)>2:
                print("invalid input, please enger digit\n\n")
                select = input(cuisine_str)
            select = int(select)
            if select==1:
                print("to French")
                french.main(ingredients, tools, methods, steps)
            else:
                print("to Italian")
                italian.main(ingredients, tools, methods, steps)
        else:
            size_str= "\n Press 1 to double ingredients size \n Press 2 to cut it by half\n\nPlease select your transformation:  "
            select = input(size_str)
            while not select.isdigit() or int(select)<1 or int(select)>2:
                print("invalid input, please enger digit\n\n")
                select = input(size_str)
            select = int(select)
            if select==1:
                display_double.display(ingredients, tools, methods, steps)
            else:
                display_half.display(ingredients, tools, methods, steps)

        select_str = "\n\nDo you want to continue transforming?\n Press 1 to continue transforming \n Press 2 to restart new recipe\n Press 3 to quit the program\n\nPlease select your transformation: "
        select = input(select_str)
        while not select.isdigit() or int(select)<1 or int(select)>3:
            print("invalid input, please enger digit\n\n")
            select = input(select_str)
        select = int(select)
        if select==1:
            print("continue transforming\n\n")
        elif select == 2:
            break
            print("restart new recipe\n\n")
        else:
            quit = True
            break
            
    