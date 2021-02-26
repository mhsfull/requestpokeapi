from sqlalchemy import (create_engine, MetaData, Column, Table, Integer, String, Float, Boolean, DateTime, ForeignKey, ForeignKeyConstraint)

class mysql_connect():
    def __init__(self,user, password,database,porta,ip):
        self.user = user
        self.password = password
        self.database = database
        self.porta = porta
        self.ip = ip
        self.engine = create_engine(f'mysql+pymysql://{self.user}:{self.password}@{self.ip}:{self.porta}/{self.database}', echo=False)
        self.metadata = MetaData(bind=self.engine)
        self.poke_table = Table('pokemons', self.metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(100), primary_key=True),
                    Column('height', Float),
                    Column('weight', Float),
                    Column('primary', Boolean),
                    Column('regular', Boolean),
                    Column('male', Boolean),
                    Column('female', Boolean),
                    Column('genderless', Boolean),
                    Column('type_one', String(45)),
                    Column('type_two', String(45)),
                    Column('id_localization', Integer),
                    Column('rate', Integer),
                    Column('front_default', String(200)),
                    Column('back_default', String(200)),
                    Column('front_female', String(200)),
                    Column('back_female', String(200)),
                    Column('front_default_shiny', String(200)),
                    Column('back_default_shiny', String(200)),
                    Column('front_female_shiny', String(200)),
                    Column('back_female_shiny', String(200)),
                    Column('evolution_chain', Integer)
                    )                    
        self.evo_table = Table('evolutions', self.metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(100), primary_key=True),
                    Column('primary', Boolean),
                    Column('regular', Boolean),
                    Column('gender', String(200)),
                    Column('held_item', String(200)),
                    Column('item', String(200)),
                    Column('know_move', String(200)),
                    Column('know_move_type', String(200)),
                    Column('location', String(200)),
                    Column('min_affection', String(200)),
                    Column('min_beauty', String(200)),
                    Column('min_happiness', String(200)),
                    Column('min_level', String(200)),
                    Column('needs_overworld_rain', String(200)),
                    Column('party_species', String(200)),
                    Column('party_type', String(200)),
                    Column('relative_physical_stats', String(200)),
                    Column('time_of_day', String(200)),
                    Column('trader_species', String(200)),
                    Column('turn_upside_down', String(200)),
                    Column('url_imagem_evolute', String(500)),
                    Column('evolution_chain', Integer),
                    Column('image', String(300))
                    )
        self.lock_table = Table('location', self.metadata,
                    Column('id', Integer, autoincrement=True),
                    Column('name', String(100))
                    )
#criador de tableas sem foreing key
class cria():
    def __init__(self,user, password,database,porta,ip):
        self.user = user
        self.password = password
        self.database = database
        self.porta = porta
        self.ip = ip
        self.engine = create_engine(f'mysql+pymysql://{self.user}:{self.password}@{self.ip}:{self.porta}/{self.database}', echo=False)
        self.metadata = MetaData(bind=self.engine)
        self.poke_table = Table('pokemons', self.metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(100), primary_key=True),
                    Column('height', Float),
                    Column('weight', Float),
                    Column('primary', Boolean),
                    Column('regular', Boolean),
                    Column('male', Boolean),
                    Column('female', Boolean),
                    Column('genderless', Boolean),
                    Column('type_one', String(45)),
                    Column('type_two', String(45)),
                    Column('id_localization', Integer),
                    Column('rate', Integer),
                    Column('front_default', String(200)),
                    Column('back_default', String(200)),
                    Column('front_female', String(200)),
                    Column('back_female', String(200)),
                    Column('front_default_shiny', String(200)),
                    Column('back_default_shiny', String(200)),
                    Column('front_female_shiny', String(200)),
                    Column('back_female_shiny', String(200)),
                    Column('evolution_chain', Integer)
                    )                   
        self.evo_table = Table('evolutions', self.metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(100), primary_key=True),
                    Column('primary', Boolean),
                    Column('regular', Boolean),
                    Column('gender', String(200)),
                    Column('held_item', String(200)),
                    Column('item', String(200)),
                    Column('know_move', String(200)),
                    Column('know_move_type', String(200)),
                    Column('location', String(200)),
                    Column('min_affection', String(200)),
                    Column('min_beauty', String(200)),
                    Column('min_happiness', String(200)),
                    Column('min_level', String(200)),
                    Column('needs_overworld_rain', String(200)),
                    Column('party_species', String(200)),
                    Column('party_type', String(200)),
                    Column('relative_physical_stats', String(200)),
                    Column('time_of_day', String(200)),
                    Column('trader_species', String(200)),
                    Column('turn_upside_down', String(200)),
                    Column('url_imagem_evolute', String(500)),
                    Column('evolution_chain', Integer),
                    Column('image', String(300))
                    )
        self.lock_table = Table('location', self.metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(100))
                    )
        self.user_table = Table('user', self.metadata,
                    Column('id', Integer),
                    Column('username', String(80)),
                    Column('email', String(80)),
                    Column('senha', String(130))
                    )
        self.back_table = Table('backpack', self.metadata,
                    Column('id', Integer, primary_key=True),
                    Column('id_user', Integer),
                    Column('captured', Boolean),
                    Column('id_pokemon', Integer),
                    Column('name', String(80)),
                    Column('image', String(200)),
                    Column('date', DateTime)
                    )
        self.metadata.create_all()