my_list = ['eric', 'bike', 'cycling', 'pool']

# access the 1st element and capitalize the name
son = f'My son\'s name is {my_list[0].title()}'
print(son)
print()

# append to the end of the list
my_list.append(33)
print('List after using append')
print(my_list)
print()

# insert into beginning 0 or any other position
my_list.insert(0, '1st')
my_list.insert(len(my_list) // 2, 'midlle_object')
print('List after inserting objects')
print(my_list)
print()

# remove objects from the list
# del
# remove the last object
del my_list[len(my_list) - 1]
# remove the last object using pop()
last_item = my_list.pop()
print('Removed 2 last items')
print(my_list)
print()

# remove by value
# using remove(value)
# removes only the 1st occurance. If needed to remove all -> loop
cycl = 'cycling'
my_list.remove(cycl)
print('Cycling removed')
print(my_list)
print()

# reassing values
my_list = ['1st', 'eric', 'bike', 'midlle_object', 'Cycling', 'pool']

# sorting throws an error if integers and strings are together
# case affects sorting! fist numbers, then Upper case, then lower case
# takeaway: it is better to store items lower case! when needed to be capitalized: use item.title()

# sort without changing the list
print('Sorted list')
print(sorted(my_list))
print(my_list)  
print()

# sort and change the list to be sorted
my_list.sort()

# reverse sort and change the list
my_list.sort(reverse=True)
print('Sort backwards')
print(my_list)
print()

# reassing values
my_list = ['1st', 'eric', 'bike', 'midlle_object', 'Cycling', 'pool']

# reverse order and change original (without changing original -> for loop)
print('Reverse order')
my_list.reverse()
print(my_list)
print()

# create a copy of the list
copy_list = my_list[:]

m_o = copy_list.pop(2)
print('Removed 3rd element from copy_list')
print(copy_list)
print('My list stays without changes')
print(my_list)
print()

# just assign without copying [:] or .copy()
duplic_list = my_list
m_o = duplic_list.pop(2)
print('Removed 3rd element from duplic_list')
print(copy_list)
print('My list changed as well')
print(my_list)
print()

# while loops with lists use pop()
users = ['alice', 'cathie', 'michael']
confirmed_users = []

while users:
    current_user = users.pop(0)
    print('Verifying user: ', end='')
    print(current_user.title())
    confirmed_users.append((current_user))

print('\nThe following users have been verified:')
for u in confirmed_users:
    print(f'  {u.title()}')

# while loops with remove()
pets = ['horse', 'cat', 'mouse', 'dog', 'cat', 'rabbit']

print()
while 'cat' in pets:
    pets.remove('cat')

print(pets)