import script
import helper
import display_recipes
quit = False
while not quit:
    search_term = input("Please enter an ingredient name:\n")
    # display_recipes.display(search_term)
    
    while True:
        transform = 'Transformation List:\n 1. To Vegetarian/to Non-Vegetarian \n 2. To healthy/ To unhealthy\n 3. to Frech Style of cuisine\n 4. Double the amount or cut it by half\n\nPlease select your transformation:  '
        select = input(transform)
        while not select.isdigit() or int(select)<1 or int(select)>4:
            print("invalid input, please enger digit\n\n")
            select = input(transform)
            
        select = int(select)
        if select==1:
            print("to vege")
        elif select==2:
            print('to healthy')
        elif select == 3:
            print("to french")
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
            
    