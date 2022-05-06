import json

def open_json(file_json):
    try:
        file = open(file_json)
    except FileNotFoundError:
        print('File not found')
fruit = {'name': 'apple', 'colour': 'red' }

with open('exchange_rates.json') as jsonfile:
    exchange_rates = json.load(jsonfile)
    print(exchange_rates['rates'])