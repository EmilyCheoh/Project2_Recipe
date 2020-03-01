import script
import re
def transform_to_healthy(ingredients, tools, methods, steps):
    # definintion of eating healthy: less sugar, cheese, salt, and oil, more vegetables, less meat, no fry
    meats = ['beef','pork','lamb','veal','ham','sausage','bacon','chicken','turkey','meat']
    vegetables = ['onion','leaves','artichoke','arugula','asparagus','bamboo','beans','beets','melon','choy','broccoli','sprouts','cabbage','carrot','cassava','cauliflower','celeriac','celery','corn','collards','Crookneck','cucumber','daikon','pepper','potato','tomato','pumpkin','spinach','peas']    
    new_ingredients = []
    for ingredient in ingredients:
        name = ingredient['ingredient_name']
        for meat in meats:
            if re.search(meat,name):
                ingredient['quantity'] = 0.5    
        
        if re.search('oil',name):
            ingredient['quantity'] = 1 
        
        if re.search('salt',name):
            ingredient['quantity'] = 0.25
            ingredient['measurement'] = 'teaspoon'
        
        if re.search('sugar',name):
            continue
        
        if re.search('cheese',name):
            continue
        
        
        for veg in vegetables:
            if re.search(veg, name):
                ingredient['quantity'] =3
                break
                
        new_ingredients.append(ingredient)                          

    for method in methods:
        if method == 'fry':
            methods.remove('fry')
            if 'boil' not in methods and 'boilling' not in methods:
                methods.append('boil')
            
    new_steps=[]
    for step in steps:
        if re.search('sugar',step[0]):
#             print(step,"----------being deleted")
            continue
        print(step,"\n")
        new_steps.append(step)
    return new_ingredients,methods, new_steps 

def transform_to_unhealthy(ingredients, tools, methods, steps):
    # definintion of eating unhealthy: more sugar, cheese, salt, and oil, less vegetables, less meat, no fry
    meats = ['beef','pork','lamb','veal','ham','sausage.?','bacon','chicken','turkey','meat']
    vegetables = ['onion','leaves','artichoke','arugula','asparagus','bamboo','beans','beets','melon','choy','broccoli','sprouts','cabbage','carrot','cassava','cauliflower','celeriac','celery','corn','collards','Crookneck','cucumber','daikon','pepper','potato','tomato','pumpkin','spinach','peas']    
    new_ingredients = []
#     ingredient_names = []
    has_veges = 0
    for ingredient in ingredients:
        name = ingredient['ingredient_name']
#         print("name: ", name)
        for meat in meats:
            if re.search(meat,name):
                ingredient['quantity'] = '3'
        
        if re.search('oil',name):
            ingredient['quantity'] = '3'
        
        if re.search('salt',name):
            ingredient['quantity'] = '3' 
            ingredient['measurement'] = 'teaspoon'
        
        if re.search('sugar',name):
            ingredient['quantity'] = '3' 
        
        if re.search('cheese',name):
            ingredient['quantity'] = '3'
        
        new_ingredients.append(ingredient) 
        for veg in vegetables:
            if re.search(veg, name):
#                 print("----------being deleted")
                new_ingredients.remove(ingredient)
                break
                
                
           
    new_steps=[]
    for step in steps:
        ingredient_names = step[1]['ingredient']
        ignore = False
        for name in ingredient_names:
            for veg in vegetables:
                if re.search(veg, name):
                    ignore = True
                    break
            if ignore:
                break
        if ignore:
            continue
        new_steps.append(step)
    return new_ingredients,methods, new_steps 
