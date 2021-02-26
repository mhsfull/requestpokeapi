from mysql_tables import mysql_connect
import requests
from create_object import creating
from sqlalchemy import engine, insert

class pokemons:
    def __init__(self,user, password,database,porta,ip):
        self.user = user
        self.password = password
        self.database = database
        self.porta = porta
        self.ip = ip
        self.conecta = mysql_connect(self.user, self.password, self.database, self.porta, self.ip)
        self.conn = self.conecta.engine.connect()
        self.table = self.conecta.poke_table
        self.ins = self.table.insert()
        self.table_evo = self.conecta.evo_table
        self.ins_evo = self.table_evo.insert()
        self.table_lock = self.conecta.lock_table
        self.ins_lock = self.table_lock.insert()
        
#filtro gênero
    def filter_gender(self, genders):
        female=0
        male=0
        genderless=0
        for gender in genders:
            if gender == 'female':
                female=1
            if gender == 'male':
                male= 1
            if gender == 'genderless':
                genderless=1
        generos=[female, male, genderless]
        return generos
#filtro abilidades
    def filter_abilities(self, ability):
        one='None'
        two='None'
        three='None'
        contador=0
        for i in ability:
            if contador == 0:
                one=i
                contador+=1
            elif contador==1:
                two=i
                contador+=1
            elif contador==2:
                three = i
                contador+=1
        abi = [ one, two, three]
        return abi
#filtro imagens
    def filter_sprites(self, sprites, data):
        back_default='None'
        back_female='None'
        back_shiny = 'None'
        back_shiny_female = 'None'
        front_default = 'None'
        front_female='None'
        front_shiny ='None'
        front_shiny_female='None'
        for i in sprites:
            for j in i:
                if j == 'back_default':
                    back_default = data.sprites[j]
                if j == 'back_female':
                    back_female = data.sprites[j]
                if j == 'back_shiny':
                    back_shiny = data.sprites[j]
                if j == 'back_shiny_female':
                    back_shiny_female = data.sprites[j]
                if j == 'front_default':
                    front_default = data.sprites[j]
                if j == 'front_female':
                    front_female = data.sprites[j]
                if j == 'front_shiny':
                    front_shiny = data.sprites[j]
                if j == 'front_shiny_female':
                    front_shiny_female = data.sprites[j]
        image = [front_default, back_default, front_female, back_female, front_shiny, back_shiny, front_shiny_female, back_shiny_female]
        return image
#filtro tipos (ex: fogo)
    def filter_types(self, type):
        type_one = 'None'
        type_two = 'None'
        contador=0
        for types in type:
            if contador == 0:
                type_one=types['name']
                contador+=1
            else:
                type_two=types['name']
        typ = [type_one, type_two]
        return typ
#filtro localização
    def filter_loc(self, locality):
        local = 'None'
        local_id = None
        if locality != None:
            local = str(locality)
        else:
            local = 'secret'
        if local == 'field':
            local_id = 1
        if local == 'pond':
            local_id = 2
        if local == 'forest':
            local_id = 3
        if local == 'mountain':
            local_id = 4
        if local == 'sea':
            local_id = 5
        if local == 'secret':
            local_id = 6
        locals = [local, local_id]
        return locals
#iniciador de filtros e adiciona forma final no banco
    def unic(self, genders, ability, sprites, data, type, locality, rate, metrics, op, evo):
        poke=[]
        infos = [data.id, data.name]
        poke.append(infos)
        poke.append(metrics)
        poke.append(self.filter_abilities(ability))
        poke.append(op)
        poke.append(self.filter_gender(genders))
        poke.append(self.filter_types(type))
        loc_name=self.filter_loc(locality)
        rates = rate
        if rates == None:
            rates = 1
        locs = [loc_name, rates]
        poke.append(locs)
        poke.append(self.filter_sprites(sprites, data)) 
        evo = int(evo)
        poke_bank = self.ins.values(id= poke[0][0],name=poke[0][1],height=poke[1][0],weight=poke[1][1],primary=poke[3][0], regular= poke[3][1],male=poke[4][1], female=poke[4][0], genderless=poke[4][2],type_one=poke[5][0], type_two=poke[5][1], id_localization=poke[6][0][1], rate=poke[6][1], front_default=poke[7][0], back_default=poke[7][1], front_female=poke[7][2], back_female=poke[7][3], front_default_shiny=poke[7][4], back_default_shiny=poke[7][5], front_female_shiny=poke[7][6], back_female_shiny=poke[7][7], evolution_chain=evo)
        print(poke[0][0],poke[0][1])
        self.conn.execute(poke_bank)        
#locais pré-definidos do tabela de locais
    def localizations(self):
        lock = [['field', 1],['pond', 2], ['forest', 3], ['mountain', 4], ['sea', 5], ['secret', 6]]
        for i in lock:
            poke_lock = self.ins_lock.values(id=i[1], name=i[0])
            self.conn.execute(poke_lock)
#filtro de evoluções da request dos não regulares
    def not_regular(self, poke_id, name, detalhes, image, evolution_chain, primary, regular):
        gender = 'None'
        held_item = 'None'
        item = 'None'
        know_move = 'None'
        know_move_type = 'None'
        localization = 'None'
        min_affection = 'None'
        min_beauty = 'None'
        min_happiness = 'None'
        min_level = 'None'
        needs_overworld_rain = 'None'
        party_species = 'None'
        party_type = 'None'
        relative_physical_stats = 'None'
        time_of_day = 'None'
        trade_species = 'None'
        url_image_evolution = 'None'
        turn_upside_down = 'None'
        name_item = 'None'
        image_item = 'None'
        for detalhe in detalhes:
            for topics in detalhe:
                if topics == 'gender' and detalhe[topics] != None:
                    gender = detalhe[topics]
                    if gender == '1':
                        gender = 'Female'
                    if gender == '2':
                        gender = 'Male'
                    if gender == '3':
                        gender = 'Genderless'
                if topics == 'held_item' and detalhe[topics] != None:
                    name_item=detalhe[topics]['name']
                    request_item=self.creating(requests.get((detalhe[topics]['url'])).json()) 
                    image_item=request_item.sprites['default']
                    held_item = name_item
                    url_image_evolution = image_item
                if topics == 'known_move' and detalhe[topics] != None:
                    know_move = detalhe[topics]['name']
                if topics == 'known_move_type' and detalhe[topics] != None:
                    know_move_type = detalhe[topics]['name']
                if topics == 'location' and detalhe[topics] != None:
                    localization = detalhe[topics]['name']
                if topics == 'min_affection' and detalhe[topics] != None:
                    min_affection = detalhe[topics]
                if topics == 'min_beauty' and detalhe[topics] != None:
                    min_beauty = detalhe[topics]
                if topics == 'min_happiness' and detalhe[topics] != None:
                    min_happiness = detalhe[topics]
                if topics == 'min_level' and detalhe[topics] != None:
                    min_level = detalhe[topics]
                if topics == 'needs_overworld_rain' and detalhe[topics] != None:
                    needs_overworld_rain = detalhe[topics]
                    if needs_overworld_rain == False:
                        needs_overworld_rain = 'None'
                if topics == 'party_species' and detalhe[topics] != None:
                    party_species = detalhe[topics]['name']
                if topics == 'party_type' and detalhe[topics] != None:
                    party_type = detalhe[topics]['name']
                if topics == 'relative_physical_stats' and detalhe[topics] != None:
                    relative_physical_stats = detalhe[topics]
                if topics == 'time_of_day' and detalhe[topics] != None:
                    time_of_day = detalhe[topics]
                    if time_of_day == '':
                        time_of_day = 'None'
                if topics == 'trade_species' and detalhe[topics] != None:
                    trade_species = detalhe[topics]['name']
                if topics == 'turn_upside_down' and detalhe[topics] != None:
                    turn_upside_down = detalhe[topics]
                    if turn_upside_down == False:
                        turn_upside_down = 'None'
                if topics == 'item' and detalhe[topics] != None:
                    name_item = detalhe[topics]['name']
                    request_item=self.creating(requests.get((detalhe[topics]['url'])).json()) 
                    image_item=request_item.sprites['default']
                    url_image_evolution = image_item
        poke_evo_bank = self.ins_evo.values(id=poke_id, name=name, gender=gender, primary= primary,regular=regular, held_item=held_item, item=name_item, know_move=know_move, know_move_type=know_move_type, location=localization, min_affection=min_affection, min_beauty=min_beauty, min_happiness=min_happiness, min_level=min_level, needs_overworld_rain=needs_overworld_rain,party_species=party_species, party_type=party_type, relative_physical_stats=relative_physical_stats, time_of_day=time_of_day, trader_species=trade_species, turn_upside_down=turn_upside_down, url_imagem_evolute=image, evolution_chain=evolution_chain, image=image_item)
        self.conn.execute(poke_evo_bank)
        print(poke_id, name)
#filtro de evoluções da request dos regulares
    def regular_evo(self, detalhes, evolution_chain, image_front, name_poke, poke_id, primary, regular):
        gender = 'None'
        held_item = 'None'
        know_move= 'None'
        know_move_type = 'None'
        localization = 'None'
        min_affection = 'None'
        min_beauty = 'None'
        min_happiness = 'None'
        min_level = 'None'
        needs_overworld_rain = 'None'
        party_species = 'None'
        party_type = 'None'
        relative_physical_stats = 'None'
        time_of_day = 'None'
        trade_species = 'None'
        url_image_evolution = 'None'
        turn_upside_down = 'None'
        name_item = 'None'
        image_item = 'None'
        for detalhe in detalhes:
            if detalhe == 'gender' and detalhes[detalhe] != None:
                gender = detalhes[detalhe]
                if gender == '1':
                    gender = 'Female'
                if gender == '2':
                    gender = 'Male'
                if gender == '3':
                    gender = 'Genderless'
            if detalhe == 'held_item' and detalhes[detalhe] != None:
                request_item=self.creating(requests.get((detalhes[detalhe]['url'])).json())
                held_item = detalhes[detalhe]['name']
                image_item=request_item.sprites['default']
                url_image_evolution = image_item
            if detalhe == 'known_move' and detalhes[detalhe] != None:
                know_move = detalhes[detalhe]['name']
            if detalhe == 'known_move_type' and detalhes[detalhe] != None:
                know_move_type = detalhes[detalhe]['name']
            if detalhe == 'location' and detalhes[detalhe] != None:
                localization = detalhes[detalhe]['name']
            if detalhe == 'min_affection' and detalhes[detalhe] != None:
                min_affection = detalhes[detalhe]
            if detalhe == 'min_beauty' and detalhes[detalhe] != None:
                min_beauty = detalhes[detalhe]
            if detalhe == 'min_happiness' and detalhes[detalhe] != None:
                min_happiness = detalhes[detalhe]
            if detalhe == 'min_level' and detalhes[detalhe] != None:
                min_level = detalhes[detalhe]
            if detalhe == 'needs_overworld_rain' and detalhes[detalhe] != None:
                needs_overworld_rain = detalhes[detalhe]
                if needs_overworld_rain == False:
                    needs_overworld_rain = 'None'
            if detalhe == 'party_species' and detalhes[detalhe] != None:
                party_species = detalhes[detalhe]['name']
            if detalhe == 'party_type' and detalhes[detalhe] != None:
                party_type = detalhes[detalhe]['name']
            if detalhe == 'relative_physical_stats' and detalhes[detalhe] != None:
                relative_physical_stats = detalhes[detalhe]
            if detalhe == 'time_of_day' and detalhes[detalhe] != None:
                time_of_day = detalhes[detalhe]
                if time_of_day == '':
                    time_of_day = 'None'
            if detalhe == 'trade_species' and detalhes[detalhe] != None:
                trade_species = detalhes[detalhe]['name']
            if detalhe == 'turn_upside_down' and detalhes[detalhe] != None:
                turn_upside_down = detalhes[detalhe]
                if turn_upside_down == False:
                    turn_upside_down = 'None'
            if detalhe == 'item' and detalhes[detalhe] != None:
                name_item=detalhes['item']['name']
                request_item=self.creating(requests.get((detalhes['item']['url'])).json()) 
                image_item=request_item.sprites['default']
        poke_evo_bank = self.ins_evo.values(id=poke_id, name=name_poke, primary= primary,regular=regular, gender=gender, held_item=held_item, item=name_item, know_move=know_move, know_move_type=know_move_type, location=localization, min_affection=min_affection, min_beauty=min_beauty, min_happiness=min_happiness, min_level=min_level, needs_overworld_rain=needs_overworld_rain,party_species=party_species, party_type=party_type, relative_physical_stats=relative_physical_stats, time_of_day=time_of_day, trader_species=trade_species, turn_upside_down=turn_upside_down, url_imagem_evolute=image_front, evolution_chain=evolution_chain, image=image_item)
        self.conn.execute(poke_evo_bank)
        print(poke_id, name_poke)
#filtro de evoluções da request dos pokemons base
    def prime(self, name, image_poke, poke_id, evolution_chain, primary, regular):
        gender = 'None'
        held_item = 'None'
        know_move= 'None'
        know_move_type = 'None'
        localization = 'None'
        min_affection = 'None'
        min_beauty = 'None'
        min_happiness = 'None'
        min_level = 'None'
        needs_overworld_rain = 'None'
        party_species = 'None'
        party_type = 'None'
        relative_physical_stats = 'None'
        time_of_day = 'None'
        trade_species = 'None'
        url_image_evolution = 'None'
        turn_upside_down = 'None'
        name_item = 'None'
        image_item = 'None'
        trader_species = 'None'
        location = 'None'
        poke_evo_bank = self.ins_evo.values(id=poke_id, name=name, primary= primary,regular=regular, gender=gender, held_item=held_item, item=name_item, know_move=know_move, know_move_type=know_move_type, location=location, min_affection=min_affection, min_beauty=min_beauty, min_happiness=min_happiness, min_level=min_level, needs_overworld_rain=needs_overworld_rain,party_species=party_species, party_type=party_type, relative_physical_stats=relative_physical_stats, time_of_day=time_of_day, trader_species=trader_species, turn_upside_down=turn_upside_down, url_imagem_evolute=image_poke, evolution_chain=evolution_chain, image=image_item)
        self.conn.execute(poke_evo_bank)
        print(poke_id, name)