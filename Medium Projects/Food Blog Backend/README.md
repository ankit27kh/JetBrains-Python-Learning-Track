This is the next project I completed in this category.

Objectives:

Stage 1:  
1. Create a database. Pass the name of the database to the script as an argument.

2. Create a table named meals with two columns: meal_id of an integer type with the primary key attribute, and meal_name of a text type and with the unique and not null attribute.

3. Create a table named ingredients with two columns: ingredient_id of an integer type with the primary key attribute and ingredient_name of a text type with the unique and not null attribute. Multi-word ingredients are out of scope, you don't need to implement their support in your script.

4. Create a table named measures with two columns: measure_id of an integer type with the primary key attribute, and measure_name of a text type with the unique attribute.

5. Populate the tables. Those tables are the dictionaries for the Food Blog system, you need to fill them once for the rest of the stages.


data = {"meals": ("breakfast", "brunch", "lunch", "supper"),
        "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
        "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")}


6. Tests do not check the output. You can print anything you want. Tests will check only the database file that your script will create.

7. Do not add other items to the dictionaries. This may affect the test results in this and the next stages.

Stage 2:  
1. Create a table named recipes with three columns: recipe_id of an integer type with the primary key attribute, recipe_name of a text type with the not-null attribute, and recipe_description of a text type.

2. Prepare a simple system that allows you to populate this table. Ask for the recipe name and the cooking directions, and insert the data into the table.

3. When a zero-length string is entered for the recipe name the script should terminate. Remember to commit your changes and close the database.

4. Remember! You can print anything you want. Tests will check only the database file that your script will create and populate.

5. You do not need to validate the entered data. The tests will pass the correct values.

Stage 3:  
1. Create a table named serve with three columns: serve_id of an INTEGER type with the PRIMARY KEY attribute, and recipe_id and meal_id, both of INTEGER type with the NOT NULL attribute.

2. Assign the recipe_id and meal_id as Foreign Keys to the following tables: recipes (the recipe_id column) and meals (the meal_id column).

3. Once a user has entered a dish name and a recipe description print all available meals with their primary key numbers.

4. Ask a user when this dish can be served. Users should input numbers separated by a space.

5. Input values to the serve table. If the user has selected three meals when the dish can be served, there should be three new entries in the serve table.

6. You do not need to validate the entered data. The tests will enter the correct values.

7. Tests do not check the output. You can print anything you want. Tests will check only the database file that your script will create.

Stage 4:  
1. Create a table named quantity with five columns: quantity_id of an INTEGER type with the PRIMARY KEY attribute, and four other columns: measure_id, ingredient_id, quantity and recipe_id . They should be of an INTEGER type with the NOT NULL attribute.

2. Assign the following columns measure_id, ingredient_id and recipe_id as Foreign Keys to the following tables (columns): measures (measure_id), ingredients (ingredient_id), and recipes (recipe_id)

3. After asking a user about certain mealtime, make a loop that will gather information about the ingredients. The ingredients should be entered in the following format: quantity measure ingredient.

4. Pressing <Enter> should finish the information gathering.

5. The measure parameter should start with a string provided by a user. If there is more than one measure that starts with the provided string, ask the user again. For example tbs and tbsp both start with the t. So the 1 t sugar entry should not pass.

6. Mind that the measures table contains an entry where the measure_name is empty string, it means, that the measure could be not provided. In this case, use this entry to relate tables. For example, 1 strawberry should have a measure_key from the entry with an empty name.

7. The ingredient parameter should contain strings provided by a user. If there is more than one ingredient that contains the provided string, ask the user again. For example strawberry and blueberry both contain berry as part of the string. So the 10 kg berry entry should not pass.

8. Tests do not check the output. You can print anything you want. Tests will check only the database file that your script will create.

Stage 5:  
1. Pass two new parameters to the script: ingredients and meals. The parameters are not mandatory. If the new parameters are not passed, the script should work like in the previous stage.

2. The --ingredients parameter should contain a list of ingredients separated by commas: --ingredients="milk,sugar,tea".

3. The --meals parameter should contain a list of meals separated by commas --meals="dinner,supper".

4. You should search the database for all the recipes which contain all of the passed ingredients (recipes may contain other ingredients as well) and can be served at a specific mealtime. If there are recipes that meet the conditions, print their names after a colon, separated by a comma. If you find two recipes with the same name print both names.

5. If there are no such recipes, print: There are no such recipes in the database.

6. This time we will check the output, so make sure that the last line you print contains the expected elements.

7. You do not need to validate the arguments The tests will pass the correct values.
