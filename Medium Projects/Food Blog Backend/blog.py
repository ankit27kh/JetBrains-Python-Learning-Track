import sqlite3
import argparse

parser = argparse.ArgumentParser(description='Name of database:')
parser.add_argument('name', metavar='', type=str)
parser.add_argument('--ingredients', type=str)
parser.add_argument('--meals', type=str)
args = parser.parse_args()

data_base_name = args.name
conn = sqlite3.connect(data_base_name)
cursor_name = conn.cursor()

if args.meals and args.ingredients:
    ingredients = args.ingredients
    ingredients = ingredients.split(',')
    meals = args.meals
    meals = meals.split(',')
    in_id = []
    me_id = []
    stop = 0
    try:
        for ingredient in ingredients:
            command = f"SELECT ingredient_id FROM ingredients WHERE ingredient_name = '{ingredient}'"
            result = cursor_name.execute(command)
            in_id.append(result.fetchone()[0])
        for meal in meals:
            command = f"SELECT meal_id FROM meals WHERE meal_name = '{meal}'"
            result = cursor_name.execute(command)
            me_id.append(result.fetchone()[0])
    except Exception as error:
        print('There are no such recipes in the database.', error)
    re_id = []
    for i in in_id:
        command = f"SELECT recipe_id FROM quantity WHERE ingredient_id = {i}"
        result = cursor_name.execute(command)
        re_id.append(result.fetchall())
    if len(re_id) == 1:
        re_id = re_id[0]
        re_id = [r[0] for r in re_id]
        re_id = set(re_id)
    else:
        sets = []
        for i in re_id:
            r = [j[0] for j in i]
            r = set(r)
            sets.append(r)
        re_id = sets[0]
        for set_ in sets:
            re_id = re_id.intersection(set_)
    re_id1 = re_id
    re_id = []
    for i in me_id:
        command = f"SELECT recipe_id FROM serve WHERE meal_id = {i}"
        result = cursor_name.execute(command)
        re_id.append(result.fetchall())
    if len(re_id) == 0:
        stop = 1
    if not stop:
        if len(re_id) == 1:
            re_id = re_id[0]
            re_id = [r[0] for r in re_id]
            re_id = set(re_id)
        else:
            sets = []
            for i in re_id:
                r = [j[0] for j in i]
                r = set(r)
                sets.append(r)
            re_id = sets[0]
            for set_ in sets:
                re_id = re_id.union(set_)
        re_id2 = re_id
        re_id = re_id1.intersection(re_id2)
        names = []
        for i in re_id:
            command = f"SELECT recipe_name FROM recipes WHERE recipe_id = {i}"
            result = cursor_name.execute(command)
            names.append(result.fetchone()[0])
        if not names:
            print('There are no such recipes in the database.')
        else:
            names = ', '.join(names)
            print(f'Recipes selected for you: {names}')
    else:
        print('There are no such recipes in the database.')
else:
    table1 = f'CREATE TABLE IF NOT EXISTS meals(' \
             f'meal_id INTEGER PRIMARY KEY,' \
             f'meal_name TEXT UNIQUE NOT NULL' \
             f');'
    table2 = f'CREATE TABLE IF NOT EXISTS ingredients(' \
             f'ingredient_id INTEGER PRIMARY KEY,' \
             f'ingredient_name TEXT UNIQUE NOT NULL' \
             f');'
    table3 = f'CREATE TABLE IF NOT EXISTS measures(' \
             f'measure_id INTEGER PRIMARY KEY,' \
             f'measure_name TEXT UNIQUE' \
             f');'
    cursor_name.execute(table1)
    cursor_name.execute(table2)
    cursor_name.execute(table3)
    conn.commit()

    data = {"meals": ("breakfast", "brunch", "lunch", "supper"),
            "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
            "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")}

    for i in data['meals']:
        cursor_name.execute(f"INSERT INTO meals (meal_name) VALUES ('{i}')")
    for i in data['ingredients']:
        cursor_name.execute(f"INSERT INTO ingredients (ingredient_name) VALUES ('{i}')")
    for i in data['measures']:
        cursor_name.execute(f"INSERT INTO measures (measure_name) VALUES ('{i}')")
    conn.commit()

    table4 = f'CREATE TABLE IF NOT EXISTS recipes(' \
             f'recipe_id INTEGER PRIMARY KEY,' \
             f'recipe_name TEXT NOT NULL,' \
             f'recipe_description TEXT' \
             f');'
    cursor_name.execute(table4)
    conn.commit()

    cursor_name.execute('PRAGMA foreign_keys = ON;')
    conn.commit()

    table5 = f'CREATE TABLE IF NOT EXISTS serve(' \
             f'serve_id INTEGER PRIMARY KEY,' \
             f'meal_id INTEGER NOT NULL,' \
             f'recipe_id INTEGER NOT NULL,' \
             f'FOREIGN KEY (meal_id)' \
             f'REFERENCES meals (meal_id),' \
             f'FOREIGN KEY (recipe_id)' \
             f'REFERENCES recipes (recipe_id)' \
             f');'
    cursor_name.execute(table5)
    conn.commit()

    table6 = f'CREATE TABLE IF NOT EXISTS quantity (' \
             f'quantity_id INTEGER NOT NULL PRIMARY KEY,' \
             f'quantity INTEGER NOT NULL,' \
             f'recipe_id INTEGER NOT NULL,' \
             f'measure_id INTEGER NOT NULL,' \
             f'ingredient_id INTEGER NOT NULL,' \
             f'FOREIGN KEY (recipe_id)' \
             f'REFERENCES recipes (recipe_id),' \
             f'FOREIGN KEY (measure_id)' \
             f'REFERENCES measures (measure_id),' \
             f'FOREIGN KEY (ingredient_id)' \
             f'REFERENCES ingredients (ingredient_id)' \
             f');'
    cursor_name.execute(table6)
    conn.commit()

    print('Pass the empty recipe name to exit.')
    while True:
        name = input('Recipe name: ')
        if name == '':
            break
        else:
            desc = input('Recipe description: ')
            cursor_name.execute(f"INSERT INTO recipes (recipe_name, recipe_description) VALUES ('{name}', '{desc}')")
            conn.commit()
            result = cursor_name.execute(f"SELECT recipe_id FROM recipes WHERE recipe_name = '{name}'")
            r_id = result.fetchall()
            r_id = r_id[-1][0]
            print('1) breakfast  2) brunch  3) lunch  4) supper ')
            m_id = input('When the dish can be served: ').split()
            for i in m_id:
                command = f"INSERT INTO serve (meal_id, recipe_id) VALUES (({int(i)}), {int(r_id)})"
                cursor_name.execute(command)
                conn.commit()
            while True:
                quantity = input('Input quantity of ingredient <press enter to stop>: ')
                quantity = quantity.split()
                if not quantity:
                    break
                if len(quantity) == 3:
                    result = cursor_name.execute(f"SELECT measure_name FROM measures;")
                    possible_measures = result.fetchall()
                    possible_measures = [i[0] for i in possible_measures]
                    if quantity[1] not in possible_measures:
                        print('The measure is not conclusive!')
                        continue
                    else:
                        result = cursor_name.execute(f"SELECT measure_id FROM measures WHERE measure_name = '{quantity[1]}';")
                        me_id = result.fetchone()[0]
                if len(quantity) == 2:
                    me_id = 8  # empty measure
                result = cursor_name.execute(f"SELECT ingredient_name FROM ingredients;")
                possible_ingredients = result.fetchall()
                possible_ingredients = [i[0] for i in possible_ingredients]
                if quantity[-1] not in possible_ingredients:
                    count = 0
                    for ingre in possible_ingredients:
                        if quantity[-1] in ingre:
                            count = count + 1
                            temp = ingre
                    if count != 1:
                        print('The ingredient is not conclusive!')
                        continue
                    elif count == 1:
                        ingre = temp
                else:
                    ingre = quantity[-1]
                result = cursor_name.execute(f"SELECT ingredient_id FROM ingredients WHERE ingredient_name = '{ingre}';")
                in_id = result.fetchone()[0]
                qt = quantity[0]
                command = f"INSERT INTO quantity (quantity, recipe_id, measure_id, ingredient_id) VALUES ({int(qt)}, {int(r_id)}, {int(me_id)}, {int(in_id)})"
                cursor_name.execute(command)
                conn.commit()

conn.close()
