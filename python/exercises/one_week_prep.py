# Day 1
def plusMinus(arr):
    # Write your code here
    pos, neg, zero = 0, 0, 0
    for a in arr:
        if a == 0:
            zero += 1
        elif a > 0:
            pos += 1
        elif a < 0:
            neg += 1
    n = len(arr)
    print(f'{(pos / n):.6f}')
    print(f'{(neg / n):.6f}')
    print(f'{(zero / n):.6f}')

def miniMaxSum(arr):
    # arr: array of 5 integers
    # find the min and max sum of 4 integers
    arr.sort()
    print(f'{sum(a[:-1])} {sum(a[1:])}')

def timeConversion(s):
    # from AM/PM to 24 hrs format
    hr = s[:2]
    ampm = s[-2:]
    if ampm == 'AM':
        if hr == '12':
            return '00' + s[2:-2]
        else:
            return s[:-2]
    else:
        if hr == '12':
            return s[:-2]
        else:
            hr = str(int(hr) + 12)
            return hr + s[2:-2]

# Day 2
from collections import Counter
from operator import itemgetter

def lonelyinteger(a):
    # Write your code here
    c = Counter(a)
    for k, v in c.items():
        if v == 1:
            lonely = k
    return lonely

def lonelyinteger(a):
    # Write your code here
    c = Counter(a)
    for k, v in c.items():
        continue
    return k
def lonelyinteger(a):
    # Write your code here
    return min(Counter(a).items(), key=itemgetter(1))[0]

def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    sum1, sum2 = 0, 0
    for i, j in zip(range(n), reversed(range(n))):
        sum1 += arr[i][i]
        sum2 += arr[i][j]
    return abs(sum1 - sum2)

def frequencySort(arr):
    # Write your code here
    max_arr = max(arr)
    freq = [0] * (max_arr + 1)
    for i in range(len(arr)):
        freq[arr[i]] += 1
    sorted_arr = []
    for i in range(len(freq)):
        #print('i: ' + str(i))
        if freq[i] == 0:
            continue
        else:
            sorted_arr.extend([i] * freq[i])
    return sorted_arr

def max_upper_quadrant(matrix):
    '''
    You can flip rows and columns as many times as needed to place numbers the way, 
    upper left corner has the maximum sum of elements. Return the maximum sum
    '''
    row, col = len(matrix), len(matrix[0])
    # Find the maximum sum by finding the maximum elements in symmetrical positions
    # symmetrical elements for top left corner:
    # [matrix[0][0], matrix[0][row - 1], matrix[col - 1][0], matrix[col - 1][col - 1]]
    max_sum = 0
    for i in range(row // 2):
        for j in range(col // 2):
            max_sum += max(
                [matrix[i][j], matrix[i][row - j - 1], matrix[col - i - 1][0], matrix[col - i - 1][col - j - 1]]
                )
    return max_sum

# Day 3
def findZigZagSequence(a, n):
    ''' 
    rearrange elements the way they increase till the mid and decrease after
    '''
    a.sort()
    mid = int(n/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

def towerBreakers(n, m):
    '''
    Two players are playing a game of Tower Breakers! Player 1 always moves first, and both players always play optimally.The rules of the game are as follows:

- Initially there are `n` towers.
- Each tower is of height `m`.
- The players move in alternating turns.
- In each turn, a player can choose a tower of height `x` and reduce its height to `y`, where `1 <= y < x` and `y` evenly divides `x`.
- If the current player is unable to make a move, they lose the game.
Given the values of `n` and `m`, determine which player will win. If the first player wins, return `1`. Otherwise, return `2`.
    '''

    '''
    Logic:
    - The player will always reduce till 1
    - If there is only 1 tower (n == 1) with m > 1, player 1 wins
    - If all towers are with height 1, player 2 wins
    - If # of towers is even, player 2 wins, else player 1 wins 
    '''
    if n == 1 and m == 1:
        return 2
    elif n == 1:
        return 1
    elif m == 1:
        return 2
    elif n % 2 == 0:
        return 2
    else:
        return 1

def caesarCipher(s, k):
    # Write your code here
    chiper = []
    k = k % 26
    for character in s:
        if not character.isalpha():
            chiper.append(character)
        else: 
            c = ord(character) + k
            if character.isupper() and c > 90:
                c = c - 90 - 1 + 65
            elif character.islower() and c > 122:
                c = c - 122 - 1 + 97
            chiper.append(chr(c))
    return ''.join(chiper)

# Day 4

def gridChallenge(grid):
    '''
    Given a square grid of characters in the range ascii[a-z], 
    rearrange elements of each row alphabetically, ascending. 
    Determine if the columns are also in ascending alphabetical order, 
    top to bottom. Return YES if they are or NO if they are not.
    '''
    for i in range(len(grid)):
        # create a sorted list of charaters for each row
        g = sorted(grid[i]) # turns into a list of sorted chars
        # turn it back to string
        grid[i] = ''.join(g)
    result = 'YES'
    transposed = list(map(list, zip(*grid)))
    for i in range(len(transposed)):
        if transposed[i] != sorted(transposed[i]):
            result = 'NO'
            break
    return result

def superDigit(n, k):
    # Write your code here
    
    while len(n) > 1:
        l = [int(x) for x in n]
        n = str(sum(l))
        if k != 1:
            # moved multiplication because if n parameter is very long, 
            # i get a runtime error
            n = n * k
            k = 1
    return int(n)

def truckTour(petrolpumps):
    # Write your code here
    litres = [x[0] for x in petrolpumps]
    kilometers = [x[1] for x in petrolpumps]
    gas, truck_loc = 0, 0
    l_sum, k_sum = sum(litres), sum(kilometers)
    N = len(petrolpumps)
    
    for i in range(N):
        #print('i: ', i)
        gas += (litres[i] - kilometers[i])
        #print('gas: ', gas)
        if gas < 0:
            #print('inside IF')
            gas = 0
            truck_loc = i + 1
            #print('truck location ', truck_loc)
        #print()
    return(truck_loc)

# Day 5

''' FIFO '''
''' 
In this challenge, you must first implement a queue using two stacks. 
Then process  queries, where each query is one of the following  types:

1 x: Enqueue element  into the end of the queue.
2: Dequeue the element at the front of the queue.
3: Print the element at the front of the queue.
'''

# q = Queue() # FIFO
# LifoQueue() fir last in first out
# q.put(3)
# q. put(5)
# #q.join()
# print(q.queue) # deque([3, 5])
# print(q.queue[0]) # 3  


from queue import Queue
q = Queue()

queries = int(input().strip())

for _ in range(queries):
    query = list(map(int, input().split(' ')))
    if query[0] == 1:
        q.put(query[1])
    elif query[0] == 2:
        q.get()
    elif query[0] == 3:
        print(q.queue[0])

def isBalanced(s):
    # balanced brackets 3/21 tests failed
    out = 'YES'
    stack = []
    open = ['(', '[', '{']
    close = [')', ']', '}']
    n = len(s)
    if n % 2 != 0 or s[0] in close:
        out = 'NO'
    for ch in s:
        #print(stack)
        if ch in open:
            stack.append(ch)
        elif ch in close:
            #print('remove from stack ', br)
            if len(stack) > 0:
                br = stack.pop()
                if br != open[close.index(ch)]:
                    out = 'NO'
                    break
            else:
                out = 'NO'
                break
    return out  

def pairs(k, arr):
    # passes 13/18 tests
    
    from itertools import combinations

    pairs = combinations(arr, 2)
    #print(pairs)
    counter = 0
    for pair in pairs:
        if abs(pair[0] - pair[1]) == k:
            counter += 1
    return counter

def pairs1(k, arr):
    # passes 1/18 tests
    counter = 1
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            #print(f'pair: {arr[i]} -  {arr[j]}')
            if abs(arr[i] - arr[j]) == k:
                counter += 1
    return counter