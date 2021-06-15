import json
import re

data = input()
data = json.loads(data)
data.sort(key=lambda x: (x['bus_id']))
errors = {'bus_id': 0, 'stop_id': 0, 'stop_name': 0, 'next_stop': 0, 'stop_type': 0, 'a_time': 0}
template_bus_id = r'\d+$'
template_stop_id = r'\d'
template_stop_name = r'[A-Z][a-zA-Z ]+ (Road|Avenue|Street|Boulevard)$'
template_next_stop = r'\d'
template_stop_type = r'(S|O|F){0,1}$'
template_a_time = r'([01][0-9]|2[0-4]):[0-5][0-9]$'
for field in data:
    if not re.match(template_bus_id, str(field['bus_id'])):
        errors['bus_id'] = errors['bus_id'] + 1
    if not re.match(template_stop_id, str(field['stop_id'])):
        errors['stop_id'] = errors['stop_id'] + 1
    if not re.match(template_stop_name, str(field['stop_name'])):
        errors['stop_name'] = errors['stop_name'] + 1
    if not re.match(template_next_stop, str(field['next_stop'])):
        errors['next_stop'] = errors['next_stop'] + 1
    if not re.match(template_stop_type, str(field['stop_type'])):
        errors['stop_type'] = errors['stop_type'] + 1
    if not re.match(template_a_time, str(field['a_time'])):
        errors['a_time'] = errors['a_time'] + 1

print(f"Type, format and required field validation: {sum(list(errors.values()))} errors")
for field, error in errors.items():
    print(f'{field}: {error}')


bus_id = []
for field in data:
    bus_id.append(field['bus_id'])
number = set(bus_id)
print("Line names and number of stops:")
for _id in number:
    print(f"bus_id: {_id}, stops: {bus_id.count(_id)}")


bus_id = []
stop_name = []
stop_type = []
invalid_1 = False
invalid_2 = False
start = True
while True:
    for field in data:
        bus_id.append((field['bus_id']))
        if len(bus_id) > 1 and (bus_id[-1] != bus_id[-2]):
            if stop_type.count('S') == stop_type.count('F') == len(set(bus_id)) - 1:
                start = True
                pass
            else:
                invalid_2 = True
                break
        if start:
            start = False
            if field['stop_type'] != 'S':
                invalid_1 = True
                break
        stop_name.append(field['stop_name'])
        stop_type.append(field['stop_type'])
    if invalid_1:
        print(f"There is no start or end stop for the line: {bus_id[-1]}.")
        break
    if invalid_2:
        print(f"There is no start or end stop for the line: {bus_id[-2]}.")
        break
    break
if not (invalid_2 or invalid_1):
    start_stops = []
    finish_stops = []
    all_stops = []
    for name, type_, id_ in zip(stop_name, stop_type, bus_id):
        all_stops.append([id_, name])
        if type_ == 'S':
            start_stops.append(name)
        elif type_ == 'F':
            finish_stops.append(name)
    sets = []
    bus_id_1 = bus_id.copy()
    for i in range(len(set(bus_id))):
        sets.append([name[1] for name in all_stops if name[0] == bus_id[0]])
        bus_id = [id_ for id_ in bus_id if id_ != bus_id[0]]
    transfer_stops = []
    for i in range(0, len(set(bus_id_1))):
        for j in range(i + 1, len(set(bus_id_1))):
            transfer_stops.extend(list(set(sets[i]).intersection(set(sets[j]))))
    start_stops = sorted(list(set(start_stops)))
    transfer_stops = sorted(list(set(transfer_stops)))
    finish_stops = sorted(list(set(finish_stops)))
    print(f"Start stops: {len(set(start_stops))} {start_stops}")
    print(f"Transfer stops: {len(set(transfer_stops))} {transfer_stops}")
    print(f"Finish stops: {len(set(finish_stops))} {finish_stops}")


bus_id = []
times = [0000]
incorrect = []
wrong = False
for field in data:
    if wrong:
        if field['bus_id'] == bus_id[-1]:
            continue
        else:
            wrong = False
    bus_id.append(field['bus_id'])
    a_time = field['a_time']
    a_time = a_time.replace(':', '')
    a_time = int(a_time)
    times.append(a_time)
    if times[-1] <= times[-2] and field['bus_id'] == bus_id[-2]:
        incorrect.append([field['bus_id'], field['stop_name']])
        wrong = True
        continue
print("Arrival time test:")
if incorrect:
    for combo in incorrect:
        print(f'bus_id line {combo[0]}: wrong time on station {combo[1]}')
else:
    print('OK')


wrong_stop = []
for field in data:
    if field['stop_name'] in start_stops + transfer_stops + finish_stops and field['stop_type'] == 'O':
        wrong_stop.append(field['stop_name'])
print("On demand stops test:")
if wrong_stop:
    wrong_stop.sort()
    print(f"Wrong stop type: {wrong_stop}")
else:
    print('OK')
