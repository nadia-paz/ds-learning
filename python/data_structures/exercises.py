
import os
import pprint
from collections import deque

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

directory = 'text_files'
filename = directory + '/project1.txt'
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
    if not os.path.isdir(directory):
        os.mkdir(directory)
    for key, value in d.items():
        f_name = directory + '/' + key + '.txt'
        #print(f_name)
        try:
            with open(f_name, 'w') as f:
                f.write(value)
        except FileNotFoundError:
            print(f'No such file or dircetory {f_name}')

project1_save_txt(d)

# exercise 2
'''
For the upcoming academic year the Coolcoders University should decide which students will get the scholarships. 
Scholarships are considered to be correctly distributed if 

all best students have it, but not all students in the university do. 

Obviously, only university students should be able to get a scholarship, 
i.e. there should be no outsiders in the list of the students that will get a scholarships.

You are given lists of unique student ids bestStudents, scholarships and allStudents, 
representing ids of the best students, students that will get a scholarship and 
all the students in the university, respectively. Return true if the scholarships are 
correctly distributed and false otherwise.
'''

def exercise2(bestStudents:list[int], scholarships:list[int], allStudents:list[int]):
    
    
    # check if there are no oustsiders and NOT ALL students get scolarship 
    # set(scholarships) < set(allStudents)
    # check if all best students get scholarship
    # set(bestStudents) <= set(scholarships)
    return set(bestStudents) <= set(scholarships) < set(allStudents)

'''
Your friend has been doodling during the lecture and wrote down several digits in a circle. 
You're wondering if these digits might form the password to your friend's computer. 
You're planning to prank him some time in the future, and hacking into his computer will definitely help. 
If the digits written in the clockwise order indeed form a password, all you need to do is figure out which digit comes in it first.

Given a list of digits as they are written in the clockwise order, find all other combinations the password could possibly have.
'''

def exercise3(list_of_numbers:list[int]):
    # turn list into deque
    output = [list_of_numbers]
    list_of_numbers = deque(list_of_numbers)
    # every time move the first element to the end rotate(-1)
    for i in range(len(list_of_numbers) - 1):
        list_of_numbers.rotate(-1)
        output.append(list(list_of_numbers))
    return output


'''
Below we will define an n-interesting polygon. 
Your task is to find the area of a polygon for a given n.
A 1-interesting polygon is just a square with a side of length 1. 
An n-interesting polygon is obtained by taking the n - 1-interesting polygon a
nd appending 1-interesting polygons to its rim, side by side. 
1: *
2:
 *
***
 *
3:
  *
 ***
*****
 ***
  *

'''
def exercise4(n):
    if n == 1:
        return n
    else:
        # calculate the side of the square were polygon fits
        side = n * 2 - 1
        # calculate the empty area in each corner of the square
        m = 0
        for i in range(1, n+1):
            m = (i-1) + m
    # calculate the area of the polygon by finding the area of the square
    # and substracting the 4 empty areas in corners
    return side * side - 4 * m

