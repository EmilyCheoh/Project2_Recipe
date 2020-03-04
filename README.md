# Project 2: Recipe Transformer

## Usage: 
1. Run the command: 
      python -m spacy download en_core_web_md
2. To run the program: 
      python main.py

## To/From Vegetarian: 
Eggs and dairy products are allowed in vegetarian recipes. Meats and seafoods are removed. 

## To/From Healthy: 
Our definintion of eating healthy: less sugar, cheese, salt, and oil, more vegetables, less meat, no frying.
Basically, we remove any sugar, cheese from our ingredients, set less quantity in meat, salt, and oil, and add more quantity of vegetables in to our ingredients. Also, no "fry" is allowed in our cooking methods.

## To French/Italian Cuisine: 
Important methods for this transformation are contained in french.py and italian.py. This transformation is done by categorizing the ingredients into several predetermined categories (e.g. meat, vegetables). This categorization is done using vectors (using spaCy), marking the distance between each ingredient and the category title (or similar words, like "spice" for "seasoning"). There is a hardcoded set of typically French/Italian ingredients stored and categorized. (There are some empty categories, indicating common food types of which French/Italian cuisine does not have specific varieties, but which would be bad to misclassify - e.g. pasta for French). Each original ingredient is compared to other ingredients of its category, and if there is a close enough match, it is replaced by the French/Italian version. The ingredients are replaced in the ingredient listings and also in the steps. 

## Double/Halve Amount:
Simply doubling quantity of ingredients or cutting it by half.

## Example Output:
Please enter a URL from AllRecipes.com:<br>
https://www.allrecipes.com/recipe/218091/classic-and-simple-meat-lasagna/<br>
-------Ingredients-----<br>
12 whole wheat, lasagna noodles <br>
..........<br>
name: whole wheat, lasagna noodles <br>
quantity: 12 <br>
measurement: <br>
preparation: <br>

1 pound lean ground beef <br>
..........<br>
name: lean ground beef <br>
quantity: 1 <br>
measurement: pound <br>
preparation: <br>

2 cloves garlic  chopped<br>
..........<br>
name: garlic <br>
quantity: 2 <br>
measurement: cloves <br>
preparation:  chopped<br>

1/2 teaspoon garlic powder <br>
..........<br>
name: garlic powder <br>
quantity: 1/2 <br>
measurement: teaspoon <br>
preparation: <br>

1 teaspoon dried oregano  or to taste<br>
..........<br>
name: dried oregano <br>
quantity: 1 <br>
measurement: teaspoon <br>
preparation:  or to taste<br>

salt and ground black pepper to taste <br>
..........<br>
name: salt and ground black pepper to taste <br>
quantity: <br>
measurement: <br>
preparation: <br>

1 (16 ounce) package cottage cheese <br>
..........<br>
name: cottage cheese <br>
quantity: 1 (16 ounce) <br>
measurement: package <br>
preparation: <br>

2 eggs<br> 
..........<br>
name: eggs<br>
quantity: 2 <br>
measurement: <br>
preparation: <br>

1/2 cup shredded parmesan cheese <br>
..........<br>
name: shredded parmesan cheese <br>
quantity: 1/2 <br>
measurement: cup <br>
preparation: <br>

1 1/2 (25 ounce) jars tomato-basil pasta sauce <br>
..........<br>
name: tomato-basil pasta sauce <br>
quantity: 1 1/2 (25 ounce) <br>
measurement: jars <br>
preparation: <br>

2 cups shredded mozzarella cheese <br>
..........<br>
name: shredded mozzarella cheese <br>
quantity: 2 <br>
measurement: cups <br>
preparation: <br>


-------Tools-----<br>
oven<br>
pot<br>
plate<br>
skillet<br>
bowl<br>
pan<br>
foil<br>

-------Methods-----<br>
preheat<br>
boil<br>
cook<br>
uncovered<br>
stirring<br>
remove<br>
chopping<br>
drain<br>
mix<br>
combined<br>
baking<br>
top<br>
sprinkle<br>
brown<br>
stand<br>

-------Steps------<br>
step 1<br>
Preheat oven to 350 degrees F (175 degrees C)<br>
..........<br>
cooking tools: oven<br>
cooking methods: preheat<br>

step 2<br>
Fill a large pot with lightly salted water and bring to a rolling boil over high heat<br>
..........<br>
ingredients: whole wheat, lasagna noodles <br>
cooking tools: pot<br>
cooking methods: boil, heat<br>

step 3<br>
Once the water is boiling, add the lasagna noodles a few at a time, and return to a boil<br>
..........<br>
ingredients: whole wheat, lasagna noodles <br>
cooking methods: boiling<br>

step 4<br>
Cook the pasta uncovered, stirring occasionally, until the pasta has cooked through, but is still firm to the bite, about 10 minutes<br>
..........<br>
ingredients: tomato-basil pasta sauce, whole wheat, lasagna noodles <br>
cooking methods: cook, uncovered, stirring
cooking time: 10 minutes<br>

step 5<br>
Remove the noodles to a plate<br>
..........<br>
ingredients: whole wheat, lasagna noodles <br>
cooking tools: plate<br>
cooking methods: remove<br>

step 6<br>
Place the ground beef into a skillet over medium heat, add the garlic, garlic powder, oregano, salt, and black pepper to the skillet<br>
..........<br>
ingredients: lean ground beef, whole wheat, lasagna noodles, garlic, garlic powder, dried oregano, salt and ground black pepper to taste <br>
cooking tools: skillet<br>
cooking methods: heat<br>

step 7<br>
Cook the meat, chopping it into small chunks as it cooks, until no longer pink, about 10 minutes<br>
..........<br>
ingredients: whole wheat, lasagna noodles <br>
cooking methods: cook, chopping<br>
cooking time: 10 minutes<br>

step 8<br>
Drain excess grease<br>
..........<br>
cooking methods: drain<br>

step 9<br>
In a bowl, mix the cottage cheese, eggs, and Parmesan cheese until thoroughly combined<br>
..........<br>
ingredients: whole wheat, lasagna noodles, cottage cheese, eggs<br>
cooking tools: bowl<br>
cooking methods: mix, combined<br>

step 10<br>
Place 4 noodles side by side into the bottom of a 9x13-inch baking pan<br>
..........<br>
ingredients: whole wheat, lasagna noodles <br>
cooking tools: pan<br>
cooking methods: baking<br>

step 11<br>
top with a layer of the tomato-basil sauce, a layer of ground beef mixture, and a layer of the cottage cheese mixture<br>
..........<br>
ingredients: tomato-basil pasta sauce, whole wheat, lasagna noodles, lean ground beef, cottage cheese <br>
cooking methods: top, mixture<br>

step 12<br>
Repeat layers twice more, ending with a layer of sauce<br>
..........<br>
ingredients: whole wheat, lasagna noodles, tomato-basil pasta sauce <br>

step 13<br>
sprinkle top with the mozzarella cheese<br>
..........<br>
ingredients: shredded mozzarella cheese, cottage cheese <br>
cooking methods: sprinkle, top<br>

step 14<br>
Cover the dish with aluminum foil<br>
..........<br>
cooking tools: foil<br>
cooking methods: cover<br>

step 15<br>
Bake in the preheated oven until the casserole is bubbling and the cheese has melted, about 30 minutes<br>
..........<br>
ingredients: cottage cheese, whole wheat, lasagna noodles <br>
cooking tools: oven<br>
cooking methods: bake, preheated<br>
cooking time: 30 minutes<br>

step 16<br>
Remove foil and bake until cheese has begun to brown, about 10 more minutes<br>
..........<br>
ingredients: cottage cheese, whole wheat, lasagna noodles <br>
cooking tools: foil<br>
cooking methods: remove, bake, brown<br>
cooking time: 10 minutes<br>

step 17<br>
Allow to stand at least 10 minutes before serving<br>
..........<br>
cooking methods: stand<br>
cooking time: 10 minutes<br>

Transformation List:<br>
 1. To Vegetarian/to Non-Vegetarian <br>
 2. To healthy/ To unhealthy<br>
 3. to French/Italian Style of cuisine<br>
 4. Double the amount or cut it by half<br>

Please select your transformation:  1<br>

 Press 1 to transform to Vegetarian <br>
 Press 2 to transform to Non-Vegetarian<br>

Please select your transformation:  1<br>

Transforming from Non-Vegetarian to Vegetarian... <br>

-------------------------<br>

Replaced lean ground beef with tofu.<br>

-------Ingredients-----<br>
12 whole wheat, lasagna noodles<br>
..........<br>
ingredient name: whole wheat, lasagna noodles <br>
quantity: 12 <br>
measurement: <br>
preparation: <br>

1 pound tofu<br>
..........<br>
ingredient name: tofu<br>
quantity: 1 <br>
measurement: pound <br>
preparation: <br>

2 cloves  chopped garlic<br>
..........<br>
ingredient name: garlic <br>
quantity: 2 <br>
measurement: cloves <br>
preparation:  chopped<br>

1/2 teaspoon garlic powder<br>
..........<br>
ingredient name: garlic powder <br>
quantity: 1/2 <br>
measurement: teaspoon <br>
preparation: <br>

1 teaspoon dried oregano, or to taste<br>
..........<br>
ingredient name: dried oregano <br>
quantity: 1 <br>
measurement: teaspoon <br>
preparation:  or to taste<br>

salt and ground black pepper to taste<br>
..........<br>
ingredient name: salt and ground black pepper to taste <br>
quantity: <br>
measurement: <br>
preparation: <br>

1 (16 ounce) package cottage cheese<br>
..........<br>
ingredient name: cottage cheese <br>
quantity: 1 (16 ounce) <br>
measurement: package <br>
preparation: <br>

2 eggs,<br>
..........<br>
ingredient name: eggs, <br>
quantity: 2 <br>
measurement: <br>
preparation: <br>

1/2 cup shredded parmesan cheese<br>
..........<br>
ingredient name: shredded parmesan cheese <br>
quantity: 1/2 <br>
measurement: cup <br>
preparation: <br>

1 1/2 (25 ounce) jars tomato-basil pasta sauce<br>
..........<br>
ingredient name: tomato-basil pasta sauce <br>
quantity: 1 1/2 (25 ounce) <br>
measurement: jars <br>
preparation: <br>

2 cups shredded mozzarella cheese<br>
..........<br>
ingredient name: shredded mozzarella cheese <br>
quantity: 2 <br>
measurement: cups <br>
preparation: <br>


-------Tools-----<br>
oven<br>
pot<br>
plate<br>
skillet<br>
bowl<br>
pan<br>
foil<br>

-------Methods-----<br>
preheat<br>
boil<br>
cook<br>
uncovered<br>
stirring<br>
remove<br>
chopping<br>
drain<br>
mix<br>
combined<br>
baking<br>
top<br>
sprinkle<br>
brown<br>
stand<br>

-------Steps------<br>
step 1<br>
Preheat oven to 350 degrees F (175 degrees C)<br>
..........<br>
cooking tools: oven<br>
cooking methods: preheat<br>

step 2<br>
Fill a large pot with lightly salted water and bring to a rolling boil over high heat<br>
..........<br>
ingredients: whole wheat, lasagna noodles 
cooking tools: pot<br>
cooking methods: boil, heat<br>

step 3<br>
Once the water is boiling, add the lasagna noodles a few at a time, and return to a boil<br>
..........<br>
ingredients: whole wheat, lasagna noodles <br>
cooking methods: boiling<br>

step 4<br>
Cook the pasta uncovered, stirring occasionally, until the pasta has cooked through, but is still firm to the bite, about 10 minutes<br>
..........<br>
ingredients: tomato-basil pasta sauce, whole wheat, lasagna noodles <br>
cooking methods: cook, uncovered, stirring
cooking time: 10 minutes<br>

step 5<br>
Remove the noodles to a plate<br>
..........<br>
ingredients: whole wheat, lasagna noodles 
cooking tools: plate<br>
cooking methods: remove<br>

step 6<br>
Place the tofu into a skillet over medium heat, add the garlic, garlic powder, oregano, salt, and black pepper to the skillet<br>
..........<br>
ingredients: lean ground beef, whole wheat, lasagna noodles, garlic, garlic powder, dried oregano, salt and ground black pepper to taste <br>
cooking tools: skillet<br>
cooking methods: heat<br>

step 7<br>
Cook the tofu, chopping it into small chunks as it cooks, until no longer pink, about 10 minutes<br>
..........<br>
ingredients: whole wheat, lasagna noodles <br>
cooking methods: cook, chopping<br>
cooking time: 10 minutes<br>

step 8<br>
Drain excess grease<br>
..........<br>
cooking methods: drain<br>

step 9<br>
In a bowl, mix the cottage cheese, eggs, and Parmesan cheese until thoroughly combined<br>
..........<br>
ingredients: whole wheat, lasagna noodles, cottage cheese, eggs, <br>
cooking tools: bowl<br>
cooking methods: mix, combined<br>

step 10<br>
Place 4 noodles side by side into the bottom of a 9x13-inch baking pan<br>
..........<br>
ingredients: whole wheat, lasagna noodles 
cooking tools: pan<br>
cooking methods: baking<br>

step 11<br>
top with a layer of the tomato-basil sauce, a layer of tofu mixture, and a layer of the cottage cheese mixture<br>
..........<br>
ingredients: tomato-basil pasta sauce, whole wheat, lasagna noodles, lean ground beef, cottage cheese <br>
cooking methods: top, mixture<br>

step 12<br>
Repeat layers twice more, ending with a layer of sauce<br>
..........<br>
ingredients: whole wheat, lasagna noodles, tomato-basil pasta sauce <br>

step 13<br>
sprinkle top with the mozzarella cheese<br>
..........<br>
ingredients: shredded mozzarella cheese, cottage cheese <br>
cooking methods: sprinkle, top<br>

step 14<br>
Cover the dish with aluminum foil<br>
..........<br>
cooking tools: foil<br>
cooking methods: cover<br>

step 15<br>
Bake in the preheated oven until the casserole is bubbling and the cheese has melted, about 30 minutes<br>
..........<br>
ingredients: cottage cheese, whole wheat, lasagna noodles <br>
cooking tools: oven<br>
cooking methods: bake, preheated<br>
cooking time: 30 minutes<br>

step 16<br>
Remove foil and bake until cheese has begun to brown, about 10 more minutes<br>
..........<br>
ingredients: cottage cheese, whole wheat, lasagna noodles <br>
cooking tools: foil<br>
cooking methods: remove, bake, brown<br>
cooking time: 10 minutes<br>

step 17<br>
Allow to stand at least 10 minutes before serving<br>
..........<br>
cooking methods: stand<br>
cooking time: 10 minutes<br>



Do you want to continue transforming?<br>
 Press 1 to continue transforming <br>
 Press 2 to restart new recipe<br>
 Press 3 to quit the program<br>

Please select your transformation: 
<br>