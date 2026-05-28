data = [
    ("orange", "a sweet, orange, citrus fruit"),
    ("apple", "good for making cider"),
    ("lemon", "a sour, yellow citrus fruit"),
    ("grape", "a small, sweet fruit growing in bunches"),
    ("melon", "sweet and juicy"),
]

def simple_hash(s:str)->int:
    return ord(s[0])%10
keys=['']*10
values=keys.copy()

for key,value in data:
    h=simple_hash(key)
    keys[h]=key
    values[h]=value

print(keys)
print(values)

def get(k:str)->str:
    index = simple_hash(k)
    if(values[index]):
        return values[index]
    else:
        return None
print(get('apple'))


