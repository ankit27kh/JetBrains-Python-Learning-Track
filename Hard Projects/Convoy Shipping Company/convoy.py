import pandas as pd
import sqlite3
import json
from lxml import etree

"""Get file name and get it's extension"""
file = input("Input file name\n")
name, ext = file.split('.')

"""If file is .xlsx convert it into .csv"""
if ext == 'xlsx':
    df = pd.read_excel(f'{file}', sheet_name='Vehicles', dtype=str)
    df.to_csv(f'{name}.csv', index=None, header=True)
    df = pd.read_csv(f'{name}.csv')
    index = df.index
    lines = len(index)
    if lines == 1:
        print(f'1 line was imported to {name}.csv')
    else:
        print(f'{lines} lines were imported to {name}.csv')

"""Correct entries of the .csv file if not already corrected"""
if '[CHECKED]' not in name and ext in ['csv', 'xlsx']:
    with open(f'{name}.csv', 'r') as f:
        lines = f.readlines()
        count = 0
        new_lines = [lines[0]]
        for line in lines[1:]:
            line = line.split(',')
            new_line = []
            for cell in line:
                new_cell = ''
                for i in cell:
                    if i.isdigit() or i == '\n':
                        new_cell = new_cell + i
                    else:
                        pass
                if new_cell != cell:
                    count = count + 1
                new_line.append(new_cell)
            new_lines.append(new_line)

    """Make a new .csv file with the correct entries"""
    with open(f'{name}[CHECKED].csv', 'w') as file:
        print(new_lines[0], file=file, end='')
        for line in new_lines[1:]:
            print(','.join(line), file=file, end='')
    if count == 1:
        print(f'1 cell was corrected in {name}[CHECKED].csv')
    else:
        print(f'{count} cells were corrected in {name}[CHECKED].csv')


def get_score(items):
    engine_capacity = int(items[1])
    fuel_consumption = int(items[2])
    maximum_load = int(items[3])
    score = 0
    route = 450
    one_time_drive = engine_capacity / fuel_consumption * 100
    stops = route // one_time_drive
    if stops == 0:
        score = score + 2
    elif stops == 1:
        score = score + 1
    else:
        score = score + 0
    total_fuel = route / 100 * fuel_consumption
    if total_fuel <= 230:
        score = score + 2
    else:
        score = score + 1
    if maximum_load >= 20:
        score = score + 2
    else:
        score = score + 0
    return score

"""Make sqlite3 database from the .csv file"""
if ext != 's3db':
    if '[CHECKED]' in name:
        name = name.replace('[CHECKED]', '')
    conn = sqlite3.connect(f'{name}.s3db')
    cursor = conn.cursor()

    command = """CREATE TABLE IF NOT EXISTS convoy (
    vehicle_id INTEGER PRIMARY KEY,
    engine_capacity INTEGER NOT NULL,
    fuel_consumption INTEGER NOT NULL,
    maximum_load INTEGER NOT NULL,
    score INTEGER NOT NULL);"""

    cursor.execute(command)
    conn.commit()

    with open(f'{name}[CHECKED].csv', 'r') as file:
        lines = file.readlines()
        count = 0
        for line in lines[1:]:
            line = line.split(',')
            command = f"""INSERT INTO convoy
            (vehicle_id, engine_capacity, fuel_consumption, maximum_load, score)
            VALUES 
            ({int(line[0])}, {int(line[1])}, {int(line[2])}, {int(line[3])}, {get_score(line)});"""
            cursor.execute(command)
            conn.commit()
            count = count + 1
    conn.close()
    if count == 1:
        print(f'1 record was inserted into {name}.s3db')
    else:
        print(f'{count} records were inserted into {name}.s3db')

"""Crete .json file from the database of trucks with score >= 3 """
conn = sqlite3.connect(f'{name}.s3db')
cursor = conn.cursor()

command = """SELECT * FROM convoy;"""
result = cursor.execute(command)
result = result.fetchall()
dic = {'convoy': []}
count = 0
for row in result:
    if row[4] > 3:
        dic['convoy'].append({'vehicle_id': row[0], 'engine_capacity': row[1], 'fuel_consumption': row[2], 'maximum_load': row[3]})
        count = count + 1
with open(f'{name}.json', "w") as json_file:
    json.dump(dic, json_file)
if count == 1:
    print(f'1 vehicle was saved into {name}.json')
else:
    print(f'{count} vehicles were saved into {name}.json')
conn.close()

"""Create .xml file from the database of trucks with score < 3"""
conn = sqlite3.connect(f'{name}.s3db')
cursor = conn.cursor()

command = """SELECT * FROM convoy;"""
result = cursor.execute(command)
result = result.fetchall()
count = 0
vehicles = ''
for row in result:
    if row[4] <= 3:
        vehicle = f"""<vehicle>
    <vehicle_id>{row[0]}</vehicle_id>
    <engine_capacity>{row[1]}</engine_capacity>
    <fuel_consumption>{row[2]}</fuel_consumption>
    <maximum_load>{row[3]}</maximum_load>
</vehicle>"""
        vehicles = vehicles + vehicle
        count = count + 1
xml_string = f"""<convoy> {vehicles} </convoy>"""
root = etree.fromstring(xml_string)
tree = etree.ElementTree(root)
tree.write(f"{name}.xml")
conn.close()
if count == 1:
    print(f'1 vehicle was saved into {name}.xml')
else:
    print(f'{count} vehicles were saved into {name}.xml')
