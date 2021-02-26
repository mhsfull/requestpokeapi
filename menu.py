from pokemons_bank import pokemons_evolutions, pokemons_info
from mysql_tables import cria



class menu:
    def __init__(self):
        self.user = input('Digite o nome do usuário do banco mysql::::> ')
        self.password = input('Digite a senha do banco mysql::::> ')
        self.database = input('Digite o nome da database do banco mysql::::> ')
        self.porta = input('Digite o número da porta do banco mysql::::> ')
        self.ip = input('Digite o ip do banco de dados. Ex: 182.168.1.23 ou localhost ::::> ')
#captura as inteções de request do quantos pokemons e o inicio da busca
    def op_one(self):
        limit = input('Digite o limite de pokemons (pokemons que existem: de 1 a 1118, obs: recmendamos do 1 a 898  pois eles também tem características de evolução)(ex: 10)::::>')
        offset = int(input('Digite o inicio da requeset de pokemons (pokemons que existem: de 1 a 1118, obs: recmendamos do 1 a 898  pois eles também tem características de evolução)(ex: 37)::::>'))
        offset = str(offset - 1)
        info = [offset, limit]
        return info
#captura as inteções de request do quantas evoluções e o inicio da busca
    def op_two(self): 
        limit_evo = input('Digite o limite de evoluções (O limite de cadeias de evoluções que exitem é de 1 a 467)(ex: 357)::::>')
        offset_evo = int(input('Digite o inicio da requeset de evoluções (O limite de cadeias de evoluções que exitem é de 1 "a 467 )(ex: 2)::::>'))
        offset_evo = str(offset_evo - 1)
        info = [offset_evo, limit_evo]  
        return info
#itens menu
    def inicilization(self):
        #menu
        while True:
            op = input('********************MENU******************** \n'
               '1 - request de apenas os pokemons \n'
               '2 - request de apenas as características de evolução \n'
               '3 - para os dois \n'
               '4 - para criar as tabelas \n'
               '951 - para sair \n'
               'Digite aqui :::::> ')
            if op == '1':
                info = self.op_one()        
                pokemons_info(info[0], info[1], self.user, self.password, self.database, self.porta, self.ip)
            elif op == '2':
                infotwo = self.op_two()
                pokemons_evolutions(infotwo[0], infotwo[1], self.user, self.password, self.database, self.porta, self.ip)
            elif op == '3':
                info = self.op_one()
                infotwo = self.op_one()
                pokemons_info(info[0], info[1], self.user, self.password, self.database, self.porta, self.ip)
                pokemons_evolutions(infotwo[0], infotwo[1], self.user, self.password, self.database, self.porta, self.ip)
            elif op == '951':
                print('Obrigado pela preferência !!!!!!! :)')
                break
            elif op == '4':
                print('Criando as tabelas !!!!!!!')
                cria(self.user, self.password, self.database, self.porta, self.ip)
                print('Tabelas criadas com sucesso !!!!!!!! :)')
            else:
                print('Opção invalida')
#inicia menu
init_menu = menu()
init_menu.inicilization()

