import requests
import json



class Pokemon():
    def __init__(self):
        self.name = ''
        self.abilities = []
        self.base_experience = []
        self.height = []
        self.weight = []
        self.games = []
        self.pokemon_data = []
        self.location_area_encounters = []

    def get_my_pokemon (self, pokemon_name):
        pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
        my_pokemon = pokemon.content
        my_pokemon = json.loads(my_pokemon)
        self.pokemon_data = my_pokemon
        self.get_abilities()
        self.get_name()
        self.get_base_exp()
        self.get_height()
        self.get_weight()
        self.get_games()
        self.get_LAE()



    def get_abilities(self):
        abilities = self.pokemon_data['abilities']
        for ability in abilities:
            self.abilities.append(ability['ability']['name'])

    def get_name(self):
        self.name = self.pokemon_data['name']

    def get_base_exp(self):
        self.base_experience = self.pokemon_data['base_experience']

    def get_height(self):
        self.height = self.pokemon_data['height']

    def get_weight(self):
        self.weight = self.pokemon_data['weight']

    def get_games(self):
        games_indices = self.pokemon_data['game_indices']
        for game in games_indices:
            self.games.append(game['version']['name'])

    def get_LAE(self):
        lae = requests.get(self.pokemon_data['location_area_encounters'])
        lae = lae.content
        lae = json.loads(lae)
        for areas in lae:
            self.location_area_encounters.append(areas['location_area']['name'])












