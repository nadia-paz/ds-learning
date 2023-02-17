
# Exercise 1
# Given an array of integers a, your task is to find 
# how many of its contiguous subarrays of length m 
# contain a pair of integers with a sum equal to k.
# s ≠ t
# a[s] + a[t] = k

def exercise1(a: list[int], m:int, k:int) -> int:
    '''
    Creates sublists with length m
    Counts the sum of every pair in each sublist
    If the sum equals to k, counts this sublist as the ine that 
    satisfies the requirments.

    Parameters:
        a: list of integers
        m: length of the sublist
        k: the sum to check
    '''
    length = len(a)
    # case the m is bigger then the length of array, make it equal
    # to the length of the list. It will return only 1 sublist
    if m > length:
        m = length
    n = m
    max_index = length - m
    # create a dictionaty to hold sublists
    subsets = dict()
    for i in range(max_index+1):
        # slice the list
        subset = a[i:n]
        # save the sublist into the dictionary
        subsets[i] = subset
        # increment the 2nd index
        n += 1
    # create a list to hold keys of subsets that satisfy the condiction
    b = []
    # loop through keys and values in the dictionary
    for key, value in subsets.items():
        # create a pair of values a[i] and a[j]
        # i should not be equal to j
        for i in range(m-1):
            for j in range(i+1, m):
                # calculate the sum 
                sum_numbers = value[i] + value[j]
                # check if sum satisfies the condition
                if sum_numbers == k:
                    # if yes, append the key to the list
                    b.append(key)
    # leave only unique values and return how many sublists have the sum = k
    return len(set(b))

# check if works ok
# should return 5
#print(exercise1([2, 4, 7, 5, 3, 5, 8, 5, 1, 7], 4, 10))
# should return 2
#print(exercise1(([15, 8, 8, 2, 6, 4, 1, 7]), 2, 8) )  

# m is bigger than length(a), should return 1
#print(exercise1([2, 4, 7, 5, 3, 5, 8, 5, 1, 7], 12, 10))

# Mini Project 1
'''
Manually (without Python) create a project1.txt file with this information:
alpha, This is the text in alpha
beta, This is the text in beta
charlie, This is the text in charlie


Write a function to read data from the project1.txt file.
Create a nested dictionary from it.

Data structure will be:
{project1: {alpha: This is the text in alpha}, beta: This is the text in beta, charlie: This is the text in charlie}}

Using the nested dictionary write a function to create three files like below:

File = alpha.txt
Text = This is the text in alpha

File = beta.txt
Text = This is the text in beta

File = charlie.txt
Text = This is the text in charlie
'''

filename = 'text_files/project1.txt'
d = dict()
strings = []
try:
    with open (filename, 'r') as f:
        lines = f.readlines()
    for line in lines:
        strings.append(line.strip())
except FileNotFoundError:
    print(f'File {filename} doesn\'t exist')

for string in strings:
    string = string.replace(',', '')
    l = string.split()
    d[l[0]] = ' '.join(l[1:])

def project1_save_txt(d:dict):
    '''
    Saves the information into files
    '''
    for key, value in d.items():
        f_name = 'text_files/' + key + '.txt'
        #print(f_name)
        try:
            with open(f_name, 'w') as f:
                f.write(value)
        except FileNotFoundError:
            print(f'No such file or dircetory {f_name}')

project1_save_txt(d)