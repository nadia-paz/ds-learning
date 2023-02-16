
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
print(exercise1([2, 4, 7, 5, 3, 5, 8, 5, 1, 7], 4, 10))
# should return 2
print(exercise1(([15, 8, 8, 2, 6, 4, 1, 7]), 2, 8) )  

# m is bigger than length(a), should return 1
print(exercise1([2, 4, 7, 5, 3, 5, 8, 5, 1, 7], 12, 10))