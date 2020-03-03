import spacy
import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
import re
import copy
from helper import tokenize_ingredient, get_steps

def Frenchify_ingredients(ingredient_names):
    French = {'vegetable': ['potato', 'wheat', 'green beans', 'carrot', 'leek', 'turnip', 'eggplant', 'zucchini', 'shallot'], 
          'fruit': ['oranges', 'tomatoes', 'tangerines', 'peaches', 'apricots', 'apples', 'pears', 'plums', 'cherries', 'strawberries', 'raspberries', 'redcurrants', 'blackberries', 'grapes', 'grapefruit', 'blackcurrants'],
          'meat': ['chicken', 'squab', 'duck', 'goose', 'beef', 'veal', 'pork', 'lamb', 'mutton', 'quail', 'horse', 'frog', 'snails', 'egg'], 
          'seasoning': ['fleur de sel', 'salt', 'herbes de Provence', 'tarragon', 'rosemary', 'marjoram', 'lavender', 'thyme', 'fennel', 'sage'], 
          'pasta': [ ], 
          'eggs': [ ],
          'cheese': ['chaumes cheese', 'bleu cheese', 'fromage frais', 'fromage blanc', 'chavroux cheese', 'comte cheese', 'reblochon cheese', 'roquefort cheese', 'camembert cheese', 'brie cheese'],
          'seafood': ['cod', 'sardines', 'tuna', 'salmon', 'trout', 'mussels', 'herring', 'oysters', 'shrimp', 'calamari'], 
          'fungus': [ 'truffle', 'button mushroom', 'chanterelle', 'oyster mushrooms', 'porcini']}
    categories = ['vegetable', 'fruit', 'meat', 'spice', 'seasoning', 'herb', 'pasta', 'eggs', 'cheese', 'seafood', 'fungus']
    # receive list of ingredients
    input_ingredients = ingredient_names  
    # for each ingredient, categorize it in one of the 7 categories (add other?)

    nlp = spacy.load("en_core_web_md")  
    categorized_ingredients = []
    for ingredient in input_ingredients:
        token1 = nlp(ingredient)
        best_category_score = 0
        best_category = ''

        for category in categories:
            token2 = nlp(category)
            score = token1.similarity(token2)
            if score > best_category_score:
                best_category = token2.text
                best_category_score = score
        if best_category == 'vegetable':
            score_veg = best_category_score
            score_season = token1.similarity(nlp('seasoning'))
            if score_veg - score_season < .05:
                best_category = 'seasoning'
        if best_category == 'spice' or best_category == 'herb':
            best_category = 'seasoning'
        categorized_ingredients.append((token1.text, best_category))

    # check to see if ingredient is in the list of French cuisine ingredients
    # if so, leave it. If not, replace it with nearest substitute
    # change second part of tuple from category to new Frenchified ingredient
    old_new_ingredients = []
    for ingredient_tuple in categorized_ingredients:
        ingredient = ingredient_tuple[0]
        category = ingredient_tuple[1]
        if ingredient in French[category]:
            old_new_ingredients.append((ingredient, ingredient)) 
        else:
            token1 = nlp(ingredient)
            best_alternate_score = 0
            best_alternate = ''

            for alternate in French[category]:
                token2 = nlp(alternate)
                score = token1.similarity(token2)
                if score > best_alternate_score:
                    best_alternate = token2.text
                    best_alternate_score = score
            if best_alternate == '':
                old_new_ingredients.append((ingredient, ingredient)) 
            else:
                old_new_ingredients.append((ingredient, best_alternate)) 
    return old_new_ingredients





def get_ingredient(word, ingredients):
    bad_words = ['(',')','[',']','{','}']
    for ingredient in  ingredients:
        if word in bad_words:
            continue
        if re.search(word, ingredient):
            return ingredient
    return False

def french_analyze_sentence(text, ingredients, ingredients_french):
    text = text.replace("Watch Now"," ")
    stop_words = set(stopwords.words('english')) 
    tokenized = sent_tokenize(text) 
    steps = {}
    to_be_replaced = []
    for i in tokenized: 
        to_be_replaced = []
        to_be_replaced_with = []
        wordsList = nltk.word_tokenize(i) 
        # removing stop words from wordList 
        stop_words = list(stop_words)
        stop_words.append(',')
        stop_words = set(stop_words)
        wordsList = [w for w in wordsList if not w in stop_words]  
        #  tagged = nltk.pos_tag(wordsList) 
        pre_word = ''
        for word in wordsList:
            gotten_ingredient = get_ingredient(word, ingredients)
            if gotten_ingredient!=False:
                for ingredient_tuple in ingredients_french:
                    if gotten_ingredient == ingredient_tuple[0]:
                        to_be_replaced.append(word)
                        if ingredient_tuple[1][-1] == ' ':
                            to_be_replaced_with.append(ingredient_tuple[1][0:-1])
                        else: 
                            to_be_replaced_with.append(ingredient_tuple[1])
        i = 0
        j = 0
        by_word = text.split()
        for word in by_word:
            if word in to_be_replaced:
                by_word[j] = to_be_replaced_with[i]
                i += 1
            else:
                if word[0:-1] in to_be_replaced:
                    by_word[j] = to_be_replaced_with[i] + ','
                    i += 1
            j = j+1
        text = ''
        for word in by_word:
            text = text + " " + word
        for ingredient_tuple in ingredients_french:
            if ingredient_tuple[1][-1] == ' ':
                ingredient = ingredient_tuple[1][0:-1]
            else:
                ingredient = ingredient_tuple[1]
            if re.search(rf'{ingredient},? (and )?{ingredient}', text):
                searchObj = (re.search(rf'{ingredient},? (and )?{ingredient}', text))
                text = text.replace(text[searchObj.span()[0]:searchObj.span()[1]], rf'{ingredient}')
        
    return text

def merge_ingredient(ingredient):
    return ingredient['quantity']+ ingredient['measurement']+ ingredient['ingredient_name']+ingredient['preparation']

def main(ingredients, tools, methods, steps):
    print('loading...')
    ingredient_names = []
    for ingredient in ingredients:
        ingredient_names.append(ingredient['ingredient_name'])

    
    french_ingredients = Frenchify_ingredients(ingredient_names)
    print("\n\n\nFrenchified Recipe Breakdown\n")
    print('-------Ingredients-----')

    for ingredient_tuple in french_ingredients:
        for ingredient in ingredients:
            if ingredient['ingredient_name'] == ingredient_tuple[0]:
                ingredient['ingredient_name']  = ingredient_tuple[1]

    for ingredient in ingredients:
        print(merge_ingredient(ingredient))
        print(ingredient)
        print('\n')
    print('\n-------Tools-------')
    for tool in tools:
        print(tool)

    print('\n-------Methods-------')
    for method in methods:
        print(method)

    print('\n-------Steps-------')
    cnt = 1
    for step in steps:
        print("Step",cnt)
        cnt += 1
        # step[0]: the sentence
        step[0] = french_analyze_sentence(step[0], ingredient_names, french_ingredients)
        print(step[0].strip())
        print('..........')

        # step[1]: the ingredients list
        for ingredient_tuple in french_ingredients:
            for ingredient in step[1]['ingredient']:
                if ingredient == ingredient_tuple[0]:
                    step[1]['ingredient'].append(ingredient_tuple[1])
                    step[1]['ingredient'].remove(ingredient)
        step[1]['ingredient'] = list(dict.fromkeys(step[1]['ingredient']))  # remove duplicates

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

