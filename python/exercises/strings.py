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

