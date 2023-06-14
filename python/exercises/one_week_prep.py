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
