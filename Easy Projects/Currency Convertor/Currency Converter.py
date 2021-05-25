# write your code here!
import json
import requests

codes = ['usd', 'eur']
stored_data = {}


def get_rates(code):
    r = requests.get(f'https://www.floatrates.com/daily/{code}.json')
    new = r.text
    stored_data[code] = json.loads(new)


for i in codes:
    get_rates(i)

curr1 = input().lower()
while True:
    curr2 = input().lower()
    if curr2 == '':
        break
    convert = float(input())
    print('Checking the cache...')
    if curr2 in stored_data.keys():
        print('Oh! It is in the cache!')
        amount = stored_data[curr2][curr1]['inverseRate'] * convert
        print(f'You received {amount} {curr2}.')
    else:
        print('Sorry, but it is not in the cache!')
        get_rates(curr2)
        amount = stored_data[curr2][curr1]['inverseRate'] * convert
        print(f'You received {amount} {curr2}.')
