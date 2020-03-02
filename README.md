# Project 2: Recipe Transformer

## Usage: 

## To/From Vegetarian: 

## To/From Healthy: 

## To French Cuisine: 
Important methods for this transformation are contained in french.py. This transformation is done by categorizing the ingredients into several predetermined categories (e.g. meat, vegetables). This categorization is done using vectors (using spaCy), marking the distance between each ingredient and the category title (or similar words, like "spice" for "seasoning"). There is a hardcoded set of typically French ingredients stored and categorized. (There are some empty categories, indicating common food types of which French cuisine does not have specific varieties, but which would be bad to misclassify - e.g. pasta). Each original ingredient is compared to other ingredients of its category, and if there is a close enough match, it is replaced by the French version. The ingredients are replaced in the ingredient listings and also in the steps. 

## Double/Halve Amount:
