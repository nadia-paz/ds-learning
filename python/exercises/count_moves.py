def countMoves(arr):
    ''' 
    every time increase len(arr) - 1 elements until all elements are equal
    return number of iterations

    brute force solution O(N^2)
    '''
    equal = False
    iter = 0
    while(not equal):
        # find max index   
        index = arr.index(max(arr))
        for i in range(len(arr)):
            # change all elements except 1st max
            if i != index:
                arr[i] += 1
        # check if elements are equal
        equal = all(x == arr[0] for x in arr)
        iter += 1
    return iter

def countMoves1(arr):
    ''' 
    same as above but O(N)
    since we need to get just number of moves and 
    don't need to print out we can use the reverse logic:
    [5, 5, 5, 5] needs 0 moves
    [5, 4, 4, 4] -> 1 move
    [5, 5, 4, 4] -> 2 moves
    [5, 5, 3, 3] -> 4 moves
    [5, 5, 2, 2] -> 6 moves
    [5, 5, 2, 1] -> 9 moves
    -------
    [5, 5, 5, 4] -> 3 moves
    [5, 5, 5, 3] -> 6 moves
    [5, 5, 5, 2] -> 9 moves
    [5, 5, 5, 1] -> 12 moves
    [5, 5, 5, 0] -> 15 moves
    ------
    [5, 1, 1, 1] - 4 
    [5, 5, 5, 5, 1] -> 16 moves
    ------
    [5, 5, 5, 1, 1] -> 12 (same as [5, 5, 5, 1], same as [5, 5, 5, 1, 1, 1, 1, ..., 1])
    [5, 5, 5, 2, 1] -> 13
    [5, 5, 5, 2, 2] -> 9 (same as [5, 5, 5, 2])
    ------
    There is no connection between min/max and length of elements but we can see that 
    all max elements but 1 increase the number of moves a lot (bigger sum of array)
    Increasing the number of min elements doesn't change the number of moves at all. 
    Decreasing the minimum value increaes # of moves 
   
    It means there is a connection between the sum of all elements and the minimum element.
    in the next examples there are 4 elements in array, min = 4 max = 5
    [5, 4, 4, 4] - 1 move, sum - 17,  17 - 16
    [5, 5, 4, 4] - 2 moves, sum 18, 18 - 16
    [5, 5, 5, 4] - 3 moves, sum 19, 19 - 16
    ---
    [5, 5, 5, 5] - 0 moves, sum 20, min = 5. 20 - 5*4 = 0
    sum - (number of elements * minimum element)
    '''
    return sum(arr) - (len(arr) * min(arr))
