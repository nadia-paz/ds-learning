import math
import os
import random
import re
import sys

'''
.DS_Store
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of  6 to 20, print Weird
If  is even and greater than 20, print Not Weird
'''

if __name__ == '__main__':
    #n = int(input('Number:').strip())
    for n in range(1, 101):
        if n %2 == 1:
            print(f'{n} Weird')
        else:
            if n > 20 or n < 5:
                print(f'{n} Not Weird')
            else:
                print(f'{n} Weird')

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 400 == 0:
        leap = True
    elif year % 100 != 0 and year % 4 == 0:
        leap = True

    
    return leap