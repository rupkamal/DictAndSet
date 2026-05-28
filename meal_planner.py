from contents import pantry,recipes

display_dict={}
for index, key in enumerate(recipes):
    display_dict[index+1]=key
market_list={}
while True:
    print('Please choose your recipe')
    print('*******************************')
    for key,value in display_dict.items():
        print(f'{key} - {value}')
    choice=input(': ')
    if(int(choice)==0):
        break
    elif int(choice) in display_dict:
        print(f'You have chosen {display_dict[int(choice)]}')
        #print('Checking ingredients: {}'.format(recipes[display_dict[int(choice)]]))

        for ingredient,item_required in recipes[display_dict[int(choice)]].items():
            item_available = pantry.get(ingredient,0)
            if(item_available):
                if(item_required>item_available):
                    #print(f'{item_required-item_available} of {ingredient} required.')
                    market_list[ingredient]=item_required-item_available
            else:
                #print(f'{item_required} of {ingredient} required.')
                market_list[ingredient]=item_required

        print(market_list)
        market_list.clear()