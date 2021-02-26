import requests
from requests_poke import request_gender, request_pal_park
from filters import pokemons
from create_object import creating

def pokemon(data, user, password,database,porta,ip):
#apêndice
    sprites=[]
    abilities = []
    types = []
    generos=[]
    request_data_genders=request_gender()
    request_data_pal_parks=request_pal_park()
#padronização de peso e altura
    height= data.height/10
    weight=data.weight/10
    metrics = [height, weight]
#captura de imagens
    for sprite in data.sprites:
        value_sprites=data.sprites[sprite]
        if sprite != 'other' and sprite != 'versions' and value_sprites != None:
            sprites.append({sprite:value_sprites})
#captura habilidades        
    for ability in data.abilities:
        abilities.append(ability['ability']['name'])
#captura dos tipos
    for k in range (len(data.types)):
        url_poke=data.types[k]['type']['url']
        id_type=url_poke.split('/')[-2]
        types.append({'name':data.types[k]['type']['name']})
#captura do informações de encontros
    local_name = None
    local_rate = None
    for locals in request_data_pal_parks:
        for j in range(len(locals.pokemon_encounters)):
            if locals.pokemon_encounters[j]['pokemon_species']['name'] == data.name:
                local_name = locals.name
                local_rate = locals.pokemon_encounters[j]['rate']
#captura de generos
    for genders in request_data_genders:     
        for n in range(len(genders.pokemon_species_details)):
            if genders.pokemon_species_details[n]['pokemon_species']['name'] == data.name:
                generos.append(genders.name)
#captura se é primario
    data_species=creating(requests.get(data.species['url']).json())
    primary=0
    if data_species.evolves_from_species == None:
        primary = 1
#captura se é regular
    data_evolutions=creating(requests.get(data_species.evolution_chain['url']).json())
    regular=1
    if len(data_evolutions.chain['evolves_to']) > 1:
        regular=0
#evolution_chain
    evo=data_species.evolution_chain['url'].split('/')[-2]
#filtros
    init_functions = pokemons(user, password,database,porta,ip)
    op = [primary, regular]
    filters_pass = init_functions.unic(generos, abilities, sprites, data, types, local_name, local_rate, metrics, op, evo)

