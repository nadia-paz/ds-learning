'''
Given an integer, n , and n space-separated integers as input, create a tuple, t, of those n integers. 
Then compute and print the result of hash(t).

'''

if __name__ == 'main':
    n = int(input())
    s = input()
    l = map(int, s.split())
    t = tuple(l[:n])
    print(hash(t))
    # code is not accepted by hacker rank
    # success if removed if __name__ == 'main' :o)