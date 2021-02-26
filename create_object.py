from collections import namedtuple

#função de criar "objeto" chave:valor

def creating (data): 
    return namedtuple('X', data.keys())(*data.values())
