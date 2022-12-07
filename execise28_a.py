
import json
from execise28 import FILE_PATH, person, make_dump

make_dump()


with open(FILE_PATH, 'r') as file:
    people = json.load(file)
    p1 = person(**people[0])
    p2 = person(**people[1])
    p3 = person(**people[2])

    print(p1.name, p1.old)
    print(p2.name, p2.old)
    print(p3.name, p3.old)
    

