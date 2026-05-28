entry={*{}}

while len(entry)<5:
    print('Please enter a number: ')
    num = int(input())
    entry.add(num)

print(f'You have entered following set: {entry}')
