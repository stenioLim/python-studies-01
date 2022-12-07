import json 

FILE_PATH = 'execise28.json'

class person: 
    def __init__(self, name , old):
        self.name = name
        self.old = old



p1 = person('João', 33)
p2 = person('Helena', 21)
p3 = person('Joana', 11)
bd = [vars(p1),vars(p2),vars(p3)]

def make_dump():
    with open(FILE_PATH, 'w') as file:
        json.dump(bd, file, ensure_ascii=False, indent=2)
    print('fazendo dump')
