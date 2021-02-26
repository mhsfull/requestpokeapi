import requests, json
from pokemons_capture import pokemon
from evolutions_bank import evolutions
from create_object import creating

#iniciador da request de pokemons e suas caracteristicas básicas
def pokemons_info(run, limit, user, password,database,porta,ip):
    url = creating(requests.get(f'https://pokeapi.co/api/v2/pokemon?offset={run}&limit={limit}').json())
    count = len(url.results)
    print('**************************começou os pokemons*******************************')
    for i in range(count):
        poke = creating(requests.get(url.results[i]['url']).json())
        poke = pokemon(poke, user, password,database,porta,ip)
    #pokemon.localizations()
    print('**************************acabou os pokemons*******************************')
#iniciador da request de evoluções
def pokemons_evolutions(run, limit, user, password,database,porta,ip):
    url = creating(requests.get(f'https://pokeapi.co/api/v2/evolution-chain?limit={limit}&offset={run}/').json())
    print('**************************começou as evoluções *******************************')
    for i in range(len(url.results)):
        poke_evo = creating(requests.get(url.results[i]['url']).json())
        evolutions(poke_evo, user, password,database,porta,ip)
    print('**************************acabou as evoluções *******************************')
