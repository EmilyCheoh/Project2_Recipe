import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
import re
import fractions

def is_measure_word(word):
    quantifier1 = ['bowl','dish','pound','piece','can','box','bag','carton','jar','loaf','slice','package','dash','cube','pack','head','ear','kernel','gain','grain','stalk','spear','clove']
    quantifier2 = ['teaspoon','tablespoon','glass','cup','pint','quart','half gallon','gallon','tank','jug','bottle','keg','shot','drop']
    quantifier3 = ['bar','tube','container','stick','roll','ball','spool','skein','yard','meter','foot','piece','pad','roll','stick','pair']
    for q in quantifier1:
        if re.search(q,word):
            return True
    for q in quantifier2:
        if re.search(q,word):
            return True
    for q in quantifier3:
        if re.search(q,word):
            return True
        
    return False
# print(is_measure_word('jars'))
def tokenize_ingredient(text):
    ingredient = {}
    tokenized = sent_tokenize(text) 
    quantity = ''
    ingredient_name = ''
    measurement = ''
    preparation = ''
    measure_word = False
    ignore = False
    for token in tokenized: 
        wordsList = nltk.word_tokenize(token) 
        tagged = nltk.pos_tag(wordsList) 
        for tag in tagged:
            if tag[1] == 'CD' and not ignore:
                quantity += tag[0]+' '
                measure_word = True
            elif tag[0]== '(':
                m = re.search(r"\(([0-9]* [A-Za-z0-9_]+)\)", text)
                if m==None:
                    continue
                quantity += '(' +m.group(1)+') '
                ignore = True
            elif tag[0] == ')':
                ignore = False
                measure_word = True
            elif (tag[1] == 'NN' or tag[1]=='NNS' or tag[1]=='VBZ') and not ignore:
                word =  tag[0]
#                 print(word)
                if measure_word:
                    if is_measure_word(word):
                        measurement += word+' '
                    else:
                        ingredient_name += word+', '
                    measure_word = False
                else:
                    ingredient_name += word+' '
            elif tag[0]==',':
                preparation = token.split(',')[1]
                break
            elif not ignore:
                ingredient_name+=tag[0]+' '
#         print(tagged) 
    ingredient['ingredient_name']=ingredient_name.lower()
    ingredient['quantity'] = quantity
    ingredient['measurement'] = measurement
    ingredient['preparation'] = preparation
#     print(ingredient)
    return ingredient

def get_ingredient(word, ingredients):
    bad_words = ['(',')','[',']','{','}']
    for ingredient in  ingredients:
        if word in bad_words:
            continue
#         print('word',word,'ingredient',ingredient)
        if re.search(word, ingredient):
            return ingredient
    return False

# print(get_ingredient('heat',['wheat']))

def get_cooking_method(word):
    methods1 = ['[Ss]tand','[Ww]ait','[Bb]oil.*','[Ss]aut[eé]','[Bb]ak(e|ing)','[Ff]r(y|ied)','[Rr]oast', '[Gg]rill','[Ss]team','[Pp]oach','[Ss]immer','[Bb]roil','[Bb]lanch','brais(e|ing)','[Ss]tew']
    methods2 =['[Re]move','[Bb]roil','[Bb]rais(e|ing)','[Cc]hop','[Dd]ic(e|ing)','[Mm]inc(e|ing)','[Mm]uddl(e|ing)','[Ss]i[nm]mer','[G]rat(e|ing)','[Ss]tir','[Ss]hak(e|ing)','[Cc]rush','[Ss]queez(e|ing)','[Cc]ook','[Rr]educ(e|ing)','[Dd]rain','[Mm]ix','[Tt]op','[Ss]prinkl(e|ing)','[Cc]ombin(e|ing)','[Ss]pread','[Ss]ear','[Bb]rown','[Cc]har','[Rr]ub','[Cc]hill','[Rr]inc(e|ing)','[Dd]ip','[Hh]eat','[Cc]over']
    for method in methods1:
        if re.search(method,word):
            return True
        
    for method in methods2:
        if re.search(method,word):
            return True
    return False
result = get_cooking_method("chopped")
# print(result)

def get_cooking_tools(word):
    tools1 = ['[Pp]ot','[Kk]nife','[Pp]an.?','[Kk]nives','[Gg]rater','[Bb]oard','[Oo]pener','[Cc]up.?','[Ss]poon.?','[Bb]owl.?','[Cc]olander.?','[Pp]eeler.?','[Mm]asher.?','[Ww]hisk.?','[Ss]pinner.?','[Gg]rater.?','[Ss]hear.?','[Jj]uicer','[Pp]ress','[Ss]teel','[Ss]harpener.?']
    tools2 = ['[Ff]oil','skillet','plate.?','[Ss]patula.?','[Ss]poon.?','[Tt]ong.?','[Ll]adle.?','[Mm]itt.?','[Oo]ven','[Tt]rivet.?','[Gg]uard','[Tt]hermometer.?','[Bb]lender.?','[Ss]cale.?','[Cc]ontainer.?']
#     print(tools[2])
#     print(re.search(tools[4],'spoon'))
    for tool in tools1:
        if re.search(tool,word):
            return True
    for tool in tools2:
        if re.search(tool,word):
            return True
    return False

import copy
def analyze_sentence(text, ingredients):
    text = text.replace("Watch Now"," ")
    stop_words = set(stopwords.words('english')) 
    tokenized = sent_tokenize(text) 
    steps = {}
    methods = []
    tools = []
    ingredient = []
    time = []
    for i in tokenized: 
        wordsList = nltk.word_tokenize(i) 
        # removing stop words from wordList 
        wordsList = [w for w in wordsList if not w in stop_words]  
        #  tagged = nltk.pos_tag(wordsList) 
        pre_word = ''
        for word in wordsList:
            if get_cooking_method(word):
                methods.append(word.lower())
            
            if get_cooking_tools(word):
                tools.append(word.lower())   
                
            if get_ingredient(word, ingredients)!=False:
                ingredient.append(get_ingredient(word, ingredients))
            
            if word=='minute' or word == 'minutes':
                time.append(pre_word+' '+word)
                
            if word == 'hours' or word=='hour':
                time.append(pre_word+' '+word)
            pre_word = word
                                  
    steps['ingredient'] = ingredient
    steps['cooking tools'] = tools
    steps['cooking methods'] = methods
    steps['time'] = time
    return steps

def refine_step_ingredients(step, ingredients):
    ingredient_names = copy.deepcopy(ingredients) 
    step_ingredients = step['ingredient']
    ingredients = []
    for ingredient in step_ingredients:
        if ingredient in ingredient_names:
            ingredients.append(ingredient)
            ingredient_names.remove(ingredient)
    step['ingredient'] = ingredients
    return step    

def refine_step_methods(step):
    methods1 = ['[Ss]tand','[Ww]ait','[Bb]oil.*','[Ss]aut[eé]','[Bb]ak(e|ing)','[Ff]r(y|ied)','[Rr]oast', '[Gg]rill','[Ss]team','[Pp]oach','[Ss]immer','[Bb]roil','[Bb]lanch','brais(e|ing)','[Ss]tew']
    methods2 =['[Re]move','[Bb]roil','[Bb]rais(e|ing)','[Cc]hop','[Dd]ic(e|ing)','[Mm]inc(e|ing)','[Mm]uddl(e|ing)','[Ss]i[nm]mer','[G]rat(e|ing)','[Ss]tir','[Ss]hak(e|ing)','[Cc]rush','[Ss]queez(e|ing)','[Cc]ook','[Rr]educ(e|ing)','[Dd]rain','[Mm]ix','[Tt]op','[Ss]prinkl(e|ing)','[Cc]ombin(e|ing)','[Ss]pread','[Ss]ear','[Bb]rown','[Cc]har','[Rr]ub','[Cc]hill','[Rr]inc(e|ing)','[Dd]ip','[Hh]eat','[Cc]over']

    step_methods = step['cooking methods'] 
    methods = []
    for method in step_methods:
        for m in methods1:
            flag = False
            if re.search(m, method):
                methods.append(method)
                methods1.remove(m)
                flag = True
                break
            if flag:
                continue
        for m in methods2:
            if re.search(m, method):
                methods.append(method)
                methods2.remove(m)
                break
    step['cooking methods'] = methods
    return step

def refine_step_tools(step):
    tools1 = ['[Pp]ot','[Kk]nife','[Pp]an.?','[Kk]nives','[Gg]rater','[Bb]oard','[Oo]pener','[Cc]up.?','[Ss]poon.?','[Bb]owl.?','[Cc]olander.?','[Pp]eeler.?','[Mm]asher.?','[Ww]hisk.?','[Ss]pinner.?','[Gg]rater.?','[Ss]hear.?','[Jj]uicer','[Pp]ress','[Ss]teel','[Ss]harpener.?']
    tools2 = ['[Ff]oil','skillet','plate.?','[Ss]patula.?','[Ss]poon.?','[Tt]ong.?','[Ll]adle.?','[Mm]itt.?','[Oo]ven','[Tt]rivet.?','[Gg]uard','[Tt]hermometer.?','[Bb]lender.?','[Ss]cale.?','[Cc]ontainer.?']

    step_tools = step['cooking tools'] 
    tools = []
    for tool in step_tools:
        for t in tools1:
            flag = False
            if re.search(t, tool):
                tools.append(tool)
                tools1.remove(t)
                flag = True
                break
            if flag:
                continue
        for t in tools2:
            if re.search(t, tool):
                tools.append(tool)
                tools2.remove(t)
                break
    step['cooking tools'] = tools
    return step
                
def get_tools_and_methods(directions):
    methods1 = ['[Ss]tand','[Ww]ait','[Bb]oil.*','[Ss]aut[eé]','[Bb]ak(e|ing)','[Ff]r(y|ied)','[Rr]oast', '[Gg]rill','[Ss]team','[Pp]oach','[Ss]immer','[Bb]roil','[Bb]lanch','brais(e|ing)','[Ss]tew']
    methods2 =['[Re]move','[Bb]roil','[Bb]rais(e|ing)','[Cc]hop','[Dd]ic(e|ing)','[Mm]inc(e|ing)','[Mm]uddl(e|ing)','[Ss]i[nm]mer','[G]rat(e|ing)','[Ss]tir','[Ss]hak(e|ing)','[Cc]rush','[Ss]queez(e|ing)','[Cc]ook','[Rr]educ(e|ing)','[Dd]rain','[Mm]ix','[Tt]op','[Ss]prinkl(e|ing)','[Cc]ombin(e|ing)','[Ss]pread','[Ss]ear','[Bb]rown','[Cc]har','[Rr]ub','[Cc]hill','[Rr]inc(e|ing)','[Dd]ip','[Hh]eat','[Cc]over']
    tools1 = ['[Pp]ot','[Kk]nife','[Pp]an.?','[Kk]nives','[Gg]rater','[Bb]oard','[Oo]pener','[Cc]up.?','[Ss]poon.?','[Bb]owl.?','[Cc]olander.?','[Pp]eeler.?','[Mm]asher.?','[Ww]hisk.?','[Ss]pinner.?','[Gg]rater.?','[Ss]hear.?','[Jj]uicer','[Pp]ress','[Ss]teel','[Ss]harpener.?']
    tools2 = ['[Ff]oil','skillet','plate.?','[Ss]patula.?','[Ss]poon.?','[Tt]ong.?','[Ll]adle.?','[Mm]itt.?','[Oo]ven','[Tt]rivet.?','[Gg]uard','[Tt]hermometer.?','[Bb]lender.?','[Ss]cale.?','[Cc]ontainer.?']
    
    methods = []
    tools = []
    stop_words = set(stopwords.words('english')) 
    for direction in directions:
        
        tokenized = sent_tokenize(direction) 
        
        for i in tokenized: 
            wordsList = nltk.word_tokenize(i) 
            wordsList = [w for w in wordsList if not w in stop_words]  
            for word in wordsList:
                for m in methods1:
                    flag = False
                    if re.search(m, word):
                        methods.append(word.lower())
                        methods1.remove(m)
                        flag = True
                        break
                    if flag:
                        continue
                for m in methods2:
                    if re.search(m, word):
                        methods.append(word.lower())
                        methods2.remove(m)
                        break
                
                for t in tools1:
                    flag = False
                    if re.search(t, word):
                        tools.append(word.lower())
                        tools1.remove(t)
                        flag = True
                        break
                    if flag:
                        continue
                for t in tools2:
                    if re.search(t, word):
                        tools.append(word.lower())
                        tools2.remove(t)
                        break

    methods = list(dict.fromkeys(methods))
    tools = list(dict.fromkeys(tools))
        
    return methods, tools
             

    
def get_steps(directions, ingredients):
    
    steps = []
    tools = []
    methods = []
    for direction in directions:
        sentences = re.split(r"\.|;", direction)
        for s in sentences:
            if s.strip()=='Watch Now' or s.strip()=='':
                continue
#             print(s)
            step = analyze_sentence(s,ingredients)
            step = refine_step_ingredients(step,ingredients)
            step = refine_step_methods(step)
            step = refine_step_tools(step)
            steps.append([s,step])
#             print(step)
#             print()
    
    methods,tools = get_tools_and_methods(directions)
    return tools, methods, steps
    
def double_ingredient_size(ingredients):
    for ingredient in ingredients:
        quantity = ingredient['quantity']
        fraction_str = ''
        keep_str = ''
        interrupt=False
        for c in quantity:
            if (c=='(' or c=='[') and not interrupt:
                interrupt = True
                
            if not interrupt:
                fraction_str += c
            else:
                keep_str += c
#         print(quantity)
#         print(fraction_str)
        fraction_obj = sum(map(fractions.Fraction, fraction_str.split()))
#         print(float(fraction_obj))
        fraction_obj *= 2
#         print(keep_str)
        ingredient['quantity'] = str(fraction_obj ) + " "+ keep_str
    
#         print("new quantity: ",ingredient['quantity'])
#         print()
    return ingredients    

def cut_ingredient_size(ingredients):
    for ingredient in ingredients:
        quantity = ingredient['quantity']
        fraction_str = ''
        keep_str = ''
        interrupt=False
        for c in quantity:
            if (c=='(' or c=='[') and not interrupt:
                interrupt = True
                
            if not interrupt:
                fraction_str += c
            else:
                keep_str += c
#         print(quantity)
#         print(fraction_str)
        fraction_obj = sum(map(fractions.Fraction, fraction_str.split()))
#         print(float(fraction_obj))
        fraction_obj /= 2
#         print(keep_str)
        ingredient['quantity'] = str(fraction_obj ) + " "+ keep_str
    
#         print("new quantity: ",ingredient['quantity'])
#         print()
    return ingredients    