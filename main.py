import script
import helper
import display_recipes
import display_veges
import french
quit = False
while not quit:
    search_term = input("Please enter an ingredient name:\n")
    ingredients, tools, methods, steps = display_recipes.display(search_term)
    while True:
        transform = 'Transformation List:\n 1. To Vegetarian/to Non-Vegetarian \n 2. To healthy/ To unhealthy\n 3. to French Style of cuisine\n 4. Double the amount or cut it by half\n\nPlease select your transformation:  '
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
                select = input(transform)
            select = int(select)
            if select==1:
                display_veges.display_healthy(ingredients, tools, methods, steps)
            else:
                display_veges.display_unhealthy(ingredients, tools, methods, steps)
            # print('to healthy')
        elif select == 3:
            print("to french")
            french.main(ingredients, tools, methods, steps)
        else:
            print("Double")

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
            
    