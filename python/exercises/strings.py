''' 
sWAP Case
'''
def swap_case(s):
    return s.swapcase()

# split by space, join by hyphen
def split_and_join(line):
    s = line.split()
    return '-'.join(s)

# replace the character
string = 'abracadabra'
position = 5
character = 'k'
string[:position] + character + string[position+1:]

# how many times substring is in the string
def count_substring1(string, sub_string):
    # run time error
    sub_l = len(sub_string)
    str_l = len(string)
    counter = 0
    for i in range(str_l - sub_l):
        if string[i:i+sub_l] == subs:
            counter += 1
    return

def count_substring(string, sub_string):
    # no error
    sub_l = len(sub_string)
    str_l = len(string)
    counter = 0
    i = 0
    while(i < (str_l - sub_l)):
        index = string.find(sub_string, i)
        if index == -1:
            break
        else:
            i = index + 1
            counter += 1
    return counter

def print_string_properties(s:str) -> None:
    ''' 
    In the first line, print True if s has any alphanumeric characters. 
    In the second line, print True if s has any alphabetical characters. 
    In the third line, print True if s has any digits. 
    In the fourth line, print True if s has any lowercase characters. 
    In the fifth line, print True if s has any uppercase characters. 
    '''
    print(any([char.isalnum() for char in s]))
    print(any([char.isalpha() for char in s]))
    print(any([char.isdigit() for char in s]))
    print(any([char.islower() for char in s]))
    print(any([char.isupper() for char in s]))

# Logo print
#Replace all ______ with rjust, ljust or center. 

# thickness = int(input()) #This must be an odd number
# c = 'H'
def print_logo(c: str='H', thickness: int=6):
    #Top Cone
    for i in range(thickness):
        print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

    #Top Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

    #Middle Belt
    for i in range((thickness+1)//2):
        print((c*thickness*5).center(thickness*6))    

    #Bottom Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

    #Bottom Cone
    for i in range(thickness):
        print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

def wrap(string, max_width):

    return textwrap.fill(string, max_width)

def disigner_door_mat(n ,m):
    # n rows, m columns
#n, m = list(map(int, input().split()))
#n, m = 7, 21
    welcome = 'WELCOME'
    lw = len(welcome)

    for i in range(n//2):
        print(('-'*(m // 2 - 1 - i*3))+'.' + ('|..' * i) + '|' + ('..|' * i) + '.' + ('-'*(m // 2 - 1 - i*3)))

    print(('-' * ((m - lw) // 2 ))+welcome+('-' * ((m - lw) // 2)))

    for i in range(n//2 - 1, -1, -1):
        print(('-'*(m // 2 - 1 - i*3))+'.' + ('|..' * i) + '|' + ('..|' * i) + '.' + ('-'*(m // 2 - 1 - i*3)))

def print_formatted(number):
    # your code goes here
    b = len(format(number, 'b'))
    for i in range(1, number+1):
        binary = format(i, 'b')
        # print(f'{i:>2}', end='')
        # print('{0:3o}'.format(i), end='')
        # print(('{0:3X}').format(i), end='')
        print(str(i).rjust(b), format(i, 'o').rjust(b), format(i, 'X').rjust(b), end=' ')
        print(binary.rjust(b))
        #print('{0:b}').format(i)

def print_rangoli(size):
    # your code goes here
    ''' 
# rangoli of size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
    '''
    from string import ascii_lowercase
    letters = (list(ascii_lowercase)[:size])
    letters = list(reversed(letters))
    #letters = list(reversed(letters)) + letters[1:]
    s = ''
    rows = size * 2 - 1
    cols = size + (size - 1) * 3

    for i in range(size):
        l = letters[:i+1] + list(reversed(letters[:i+1]))[1:]
        dashed = '-' * (cols // 2 - 2*i)
        alpha = '-'.join(l)
        s = s +  dashed + alpha + dashed + '\n'
        
    for i in range(size-2, -1, -1):
        l = letters[:i+1] + list(reversed(letters[:i+1]))[1:]
        dashed = '-' * (cols // 2 - 2*i)
        alpha = '-'.join(l)
        s = s +  dashed + alpha + dashed + '\n'
    #print(s)
    return s

def merge_the_tools(string, k):
    # your code goes here
    #substr = []
    for i in range(0, len(string), k):
        s = string[i:i+k]
        # unique values with the same order
        s = list(dict.fromkeys(s))
        #substr.append(s)
        print(''.join(s))

# Roman numbers
regex_pattern = r'^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

import re
print(str(bool(re.match(regex_pattern, input()))))
