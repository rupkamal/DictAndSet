vehicles = {
    'dream':'Honda',
    'nexon':'Tata',
    'Xuv700':'Mahindra',
    'Hector':'MG'
}
a=vehicles.keys()
for key in vehicles:
    print(key)
vehicles['nexon']='Jio'
vehicles.pop('nexon')
print(vehicles)