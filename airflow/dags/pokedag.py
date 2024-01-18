import json
import pendulum
import requests
from airflow.decorators import dag, task


@dag(start_date=pendulum.now(), catchup=False, schedule='@daily')
def pokedag():
    @task()
    def get_pokemon():
        pokemon = []
        response = requests.get('https://pokeapi.co/api/v2/pokemon').json()
        while next_page := response['next']:  # assignment expression
            pokemon += response['results']  # combine lists
            response = requests.get(next_page).json()
        return pokemon

    @task()
    def get_pokemon_names(pokemon):
        return [p['name'] for p in pokemon]  # list comprehension

    @task()
    def store_pokemon(pokemon_names):
        with open('pokemon.txt', 'w') as f:
            json.dump(pokemon_names, f)  # serialize

    pokemon = get_pokemon()
    pokemon_names = get_pokemon_names(pokemon)
    store_pokemon(pokemon_names)


pokedag()
