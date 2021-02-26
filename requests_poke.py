import requests, json
from create_object import creating

#request de género (female, male, genderless)
def request_gender():
    genders=[]
    for m in range (1,4):
            url_gender=f'https://pokeapi.co/api/v2/gender/{m}/'
            data_three = requests.get(url_gender).json()
            data_three=creating(data_three)
            genders.append(data_three)
    return genders
#request de local que se encontra os pokemons
def request_pal_park():
    pal_park=[]
    for i in range (1,6):
        url_pal_park=f'https://pokeapi.co/api/v2/pal-park-area/{i}/'
        data_two = requests.get(url_pal_park).json()
        data_two=creating(data_two)
        pal_park.append(data_two)
    return pal_park