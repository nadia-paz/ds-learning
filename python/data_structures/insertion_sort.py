arr = [34, 7, 8, 9, -1, 29, 77]

def sort(arr: list) -> list:
    """ 
    Insertion sort. O^2.
    Walks from the 1st element to the last. 
    arr[0] -> sorted
    """
    N = len(arr)
    i = 1
    while i < N:
        # create 2 variables
        # current with value of arr[i], and
        # j -> index in front of current
        current = arr[i]
        j = i - 1

        # if the arr[j] bigger then a next value (current)
        # swap values and check if previous values need to be swaped
        while j >= 0 and arr[j] > current:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = current
        print(arr)
        i += 1
    return arr

print(arr)
print(sort(arr))
