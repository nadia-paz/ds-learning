'''
# first runner up
# find the 2nd biggest number
'''
#n = int(input())
#arr = map(int, input().split())
arr = [2, 4, 3, 6, 6, 6, 5]
# only unique number
arr = [*set(arr)]
# sort them
arr.sort()
# reverse
arr.reverse()
print(arr[1])

