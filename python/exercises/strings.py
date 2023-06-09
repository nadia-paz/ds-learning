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