from pokemon_get import Pokemon
import json
def write_to_file(item):
    try:
        with open(item['name']+'.json', 'w') as file:
            item = json.dumps(item)
            file.write(item)

    except:
        raise

    finally:
        print('Pokemon Retrieved to json file')

pokemon_name = input('Whats the pokemon name: ')
pokemon = Pokemon()
pokemon.get_my_pokemon(pokemon_name)
jsonstr = json.dumps(pokemon.__dict__)
data = json.loads(jsonstr)
del data['pokemon_data']
write_to_file(data)

