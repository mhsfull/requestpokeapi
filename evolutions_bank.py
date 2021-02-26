import requests, json
from create_object import creating
from filters import pokemons

#request do pokemon base (ex: bulbasauro)
def evolutions(data, user, password,database,porta,ip):
    poke_id = data.chain['species']['url'].split('/')[-2]
    pokem = pokemons(user, password,database,porta,ip)
    if int(poke_id) in range(1,898):
        data_poke= creating(requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke_id}').json())
        name = data.chain['species']['name']
        image = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{poke_id}.png'
        primary = 1
        evolution_chain = int(data.id)
        regular=1
        if len(data.chain['evolves_to']) > 1:
            regular=0
        pokem.prime(name, image, poke_id, evolution_chain, primary, regular)           
#request das evolução de pokemons não regulares não regular(pode sai de um estado e poder ter mais de 1 evolução. (ex: evee)        
    if len(data.chain['evolves_to']) > 1:
        for i in range(len(data.chain['evolves_to'])):
            poke_id = data.chain['evolves_to'][i]['species']['url'].split('/')[-2]            
            evolution_chain = int(data.id)        
            if int(poke_id) in range(1,898):
                data_poke= creating(requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke_id}').json())
                image = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{poke_id}.png'
                name = data.chain['evolves_to'][i]['species']['name']
                detalhes=data.chain['evolves_to'][i]['evolution_details']
                if len(data.chain['evolves_to'][i]['evolution_details']) != 0:
                    primary = 0
                    regular=1
                    if len(data.chain['evolves_to']) > 1:
                        regular=0
                    pokem.not_regular(poke_id, name, detalhes, image, evolution_chain, primary, regular)
#request pokemons com evoluções regulares intermediárioss (ex: Ivysaur)
    else:
        itens=[]
        counter = 0
        chain = data.chain
        evolution_chain = int(data.id)
        while 'evolves_to' in chain and len(chain['evolves_to']) > 0:            
            poke_id = chain['evolves_to'][0]['species']['url'].split('/')[-2]
            if counter == 0:
                counter +=1
                if int(poke_id) in range(1,898):
                    if len(data.chain['evolves_to'][0]['evolution_details']) != 0:
                        data_poke= creating(requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke_id}').json())
                        image = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{poke_id}.png'
                        poke_evolution = chain['evolves_to'][0]['species']['url'].split('/')[-2]
                        detalhes=data.chain['evolves_to'][0]['evolution_details'][0]
                        name = chain['evolves_to'][0]['species']['name']
                        primary = 0
                        regular=1
                        if len(data.chain['evolves_to']) > 1:
                            regular=0
                        pokem.regular_evo(detalhes, evolution_chain, image, name, poke_id, primary, regular)
#request pokemos com evoluções regulares ultimas (ex: venusaur)
            else:
                if int(poke_id) in range(1,898):
                    if len(data.chain['evolves_to'][0]['evolution_details']) != 0:
                        data_poke= creating(requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke_id}').json())
                        detalhes=data.chain['evolves_to'][0]['evolves_to'][0]['evolution_details'][0]
                        name = chain['evolves_to'][0]['species']['name']
                        image = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{poke_id}.png'
                        primary = 0
                        regular=1
                        if len(data.chain['evolves_to']) > 1:
                            regular=0
                        pokem.regular_evo(detalhes, evolution_chain, image, name, poke_id, primary, regular)
            chain = chain['evolves_to'][0]