import spacy
import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
import re
import copy
from helper import tokenize_ingredient, get_steps


def italianify_ingredients(ingredient_names):
    italian = {'vegetable': ['olive', 'peppers', 'potato', 'artichoke', 'eggplant', 'zucchini', 'string beans', 'squash', 'broccoli rabe', 'head cabbages', 'black leaf kale', 'cardoons', 'radish', 'arugala', 'cucumbers', 'spinach'], 
          'fruit': ['tomatoes', 'oranges', 'lemons', 'pears', 'figs', 'cherries'],
          'meat': ['ham', 'prosciutto', 'sausage', 'salami', 'pork', 'beef'], 
          'seasoning': ['basil', 'pesto', 'olive oil', 'garlic', 'oregano', 'chili pepper', 'parsley', 'bay leaf', 'sage', 'rosemary', 'thyme'], 
          'pasta': ['penne', 'maccheroni', 'spaghetti', 'linguine', 'fusilli', 'lasagne', 'tortellini', 'ravioli', 'rigatoni', 'gnocchi'], 
          'eggs': [ ],
          'cheese': ['mozzerella chees', 'ricotta cheese', 'provolone cheese', 'gorgonzola cheese', 'asiago cheese', 'parmigian cheese', 'pecorino cheese', 'mascarpone cheese'],
          'seafood': ['cod', 'baccala', 'anchovies', 'sea bass', 'calamari', 'shrimp', 'tilapia', 'swordfish', 'eel', 'clam', 'mussels', 'octopus', 'tuna', 'sardines'], 
          'fungus': [ 'truffle', 'portobello mushrooms']}
    categories = ['vegetable', 'fruit', 'meat', 'spice', 'seasoning', 'herb', 'pasta', 'eggs', 'cheese', 'seafood', 'fungus']
    # categories = ['vegetable', 'spice', 'seasoning', 'herb']
    # receive list of ingredients
    input_ingredients = ingredient_names  # ['pear', 'garlic', 'salt', 'potato', 'duck', 'tilapia', 'truffle']
    # for each ingredient, categorize it in one of the 7 categories (add other?)
    # input_ingredients = ['fleur de sel', 'herbes de Provence', 'tarragon', 'rosemary', 'marjoram', 'lavender', 'thyme', 'fennel', 'sage', 'carrot', 'eggplant', 'potato']

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

    # check to see if ingredient is in the list of italian cuisine ingredients
    # if so, leave it. If not, replace it with nearest substitute
    # change second part of tuple from category to new italianified ingredient
    old_new_ingredients = []
    for ingredient_tuple in categorized_ingredients:
        ingredient = ingredient_tuple[0]
        category = ingredient_tuple[1]
        if ingredient in italian[category]:
            old_new_ingredients.append((ingredient, ingredient)) 
        else:
            token1 = nlp(ingredient)
            best_alternate_score = 0
            best_alternate = ''

            for alternate in italian[category]:
                token2 = nlp(alternate)
                score = token1.similarity(token2)
                if score > best_alternate_score:
                    best_alternate = token2.text
                    best_alternate_score = score
            if best_alternate == '':
                old_new_ingredients.append((ingredient, ingredient)) 
            else:
                old_new_ingredients.append((ingredient, best_alternate)) 
    #print(old_new_ingredients)
    return old_new_ingredients





def get_ingredient(word, ingredients):
    bad_words = ['(',')','[',']','{','}']
    for ingredient in  ingredients:
        if word in bad_words:
            continue
        if re.search(word, ingredient):
            return ingredient
    return False

def italian_analyze_sentence(text, ingredients, ingredients_italian):
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
                for ingredient_tuple in ingredients_italian:
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
        for ingredient_tuple in ingredients_italian:
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

    
    italian_ingredients = italianify_ingredients(ingredient_names)
    print("\n\n\nItalianified Recipe Breakdown\n")
    #print('ingredient_names: ', ingredient_names)
    print('-------ingredients-----')
    # print(ingredients)
    for ingredient_tuple in italian_ingredients:
        for ingredient in ingredients:
    #         print('ingredients', type(ingredients))
            if ingredient['ingredient_name'] == ingredient_tuple[0]:
                ingredient['ingredient_name']  = ingredient_tuple[1]

    for ingredient in ingredients:
        print(merge_ingredient(ingredient))
        print(ingredient)
        print('\n')
    print('\n-------tools-----')
    print(tools)

    print('\n-------methods-----')
    print(methods)

    print('\n-------steps------')
    cnt = 1
    for step in steps:
        print("Step ",cnt)
        cnt += 1
        # step[0]: the sentence
        step[0] = italian_analyze_sentence(step[0], ingredient_names, italian_ingredients)
        print(step[0])

        # step[1]: the ingredients list
        for ingredient_tuple in italian_ingredients:
            for ingredient in step[1]['ingredient']:
                if ingredient == ingredient_tuple[0]:
                    step[1]['ingredient'].append(ingredient_tuple[1])
                    step[1]['ingredient'].remove(ingredient)
        step[1]['ingredient'] = list(dict.fromkeys(step[1]['ingredient']))  # remove duplicates

        print(step[1])
        print('\n')

