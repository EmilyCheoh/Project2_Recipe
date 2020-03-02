# Project 2: Recipe Transformer

## Usage: 
1. Running the command: 
      python -m spacy download en_core_web_md
2. Running the program: 
      python main.py

## To/From Vegetarian: 

## To/From Healthy: 
Our definintion of eating healthy: less sugar, cheese, salt, and oil, more vegetables, less meat, no fry.
Basically, we remove any sugar, cheese from our ingredients, set less quantity in meat, salt, and oil, and add more quantity of vegetables in to our ingredients. Also, no fry is allowed in our cooking methods.

## To French Cuisine: 
Important methods for this transformation are contained in french.py. This transformation is done by categorizing the ingredients into several predetermined categories (e.g. meat, vegetables). This categorization is done using vectors (using spaCy), marking the distance between each ingredient and the category title (or similar words, like "spice" for "seasoning"). There is a hardcoded set of typically French ingredients stored and categorized. (There are some empty categories, indicating common food types of which French cuisine does not have specific varieties, but which would be bad to misclassify - e.g. pasta). Each original ingredient is compared to other ingredients of its category, and if there is a close enough match, it is replaced by the French version. The ingredients are replaced in the ingredient listings and also in the steps. 

## Double/Halve Amount:
Simply doubling quantity of ingredients or cut it by half.
