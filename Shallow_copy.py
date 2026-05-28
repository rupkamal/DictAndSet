import copy
animals={
    'lion':['scary','Cat','big'],
    'elephant':['big','grey','wrinkled'],
    'teddy':['cuddly','stuffed'],
}

#things = animals.copy()
things=copy.deepcopy(animals)
animals['teddy'].append('toy')
print(things['teddy'])
print(animals['teddy'])