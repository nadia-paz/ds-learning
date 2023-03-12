from collections import deque
# double-ended queue

d = deque('abcdefg')
d.remove('c')
print(d)
print()

print('Add to the right')
# extend -> many values to the right
d.extend('hijk')
# append -> one value to the right
d.append('h')
print(d)
print()

print('Add to the left')
d = deque()
# extend to the right one by one to the left side: deque([4, 3, 2, 1, 0])
d.extendleft(range(5))
d.appendleft(5)
print(list(d))
print()

d.pop() # removes an element from the right side
d.popleft() # from the left side

print(d)

d = deque(range(10))
d.rotate(2) # moves 2 elements from the right side to the left (from the end to the beginning)
print('Right rotation: ', list(d))
d = deque(range(10))
d.rotate(-2) # moves 2 elements from the left to the right
print('Left rotation: ', list(d))

def solution(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    deque(map(lambda x: x[1].rotate(-x[0]), enumerate(res)), 0)
    return [list(d) for d in res]

print(solution([2, 4, 6, 8, 0]))