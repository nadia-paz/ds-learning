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

