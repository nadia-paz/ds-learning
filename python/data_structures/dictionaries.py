alien_0 = {'color':'green'}
print(alien_0)
print()

print('Modify value')
alien_0['color'] = 'yellow'
print(alien_0)

print('Add more key-value pairs')
alien_0['points'] = 25
alien_0['x_position'] = 0
alien_0['y_position'] = 10
print(alien_0)

# remove items from dictionary
# pop to save the value
points = alien_0.pop('points')
print(points)
print(alien_0)

# alien_0.remove('x_position') no remove for dictionaries
alien_0['points'] = points
alien_0['to_delete'] = 'delete me!'
print(alien_0)
# permanent removal
del alien_0['to_delete']
print((alien_0))

for key in alien_0: # or for key in alien_0.keys()
    print(f'{key:10} : {alien_0[key]}')
print()

for key, value in alien_0.items():
    print(f'{key:10} : {value}')
print()

print('Sorted keys')

for key in sorted(alien_0):
    print(f'{key:10} : {alien_0[key]}')

# looping through values
list_of_values = []
for value in alien_0.values():
    list_of_values.append(value)
print(list_of_values) # ['yellow', 0, 10, 25]

# append only unique values, the order will be changed with set
list_of_values = []
for value in set(alien_0.values()):
    list_of_values.append(value)
print(list_of_values) # [0, 'yellow', 10, 25]

# dictionary of dictionaries
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}

for uname, uinfo in users.items():
    print(f'\nUsername {uname}:')
    fullname = f"{uinfo['first']} {uinfo['last']}"
    location = uinfo['location']

    print(f'\tFull name: {fullname.title()}')
    print(f'\tLocation: {location.title()}')

# generate a dictionary with diff keys and same values
d = dict.fromkeys(['a', 'b', 'c'], 0)
print(d)