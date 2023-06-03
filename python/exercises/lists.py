''' 
You are given three integers  x, y and z representing the dimensions of a cuboid 
along with an integer n. 
Print a list of all possible coordinates given by (i, j, k) on a 3D 
grid where the sum of  is not equal to n. 
Here, 0 <= i <= x, 0<= j<= y, 0 <= k <= z. 
Please use list comprehensions rather than multiple loops.

'''
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

# l = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)\
#     if i+j+k != n]

''' 
Nested lists
Given the names and grades for each student in a class of  students, 
store them in a nested list and print the name(s) of any student(s) 
having the second lowest grade.

Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.

Example

The ordered list of scores is , so the second lowest score is . 
There are two students with that score: . Ordered alphabetically, 
the names are printed as:
alpha
beta
'''

records = []

# correct but complicated from me

# if __name__ == '__main__':
#     for _ in range(int(input('int: '))):
#         name = input('name: ')
#         score = float(input('float: '))
#         records.append([name, score])
#     second_lowest = []
#     first_lowest = []
#     if records[0][1] < records[1][1]:
#         min1 = records[0][1]
#         min2 = records[1][1]
#         first_lowest.append(records[0])
#         second_lowest.append(records[1])
#     elif records[0][1] > records[1][1]:
#         min2 = records[0][1]
#         min1 = records[1][1]
#         first_lowest.append(records[1])
#         second_lowest.append(records[0])
#     else:
#         min1, min2 = records[0][1], records[0][1]
#         second_lowest.append(records[0])
#         second_lowest.append(records[1])
#         first_lowest.append(records[0])
#         first_lowest.append(records[1])
    
#     for i in range(2, len(records)):
#         if records[i][1] > min2 and min1 != min2:
#             continue
#         elif records[i][1] > min2 and min1 == min2:
#             min2 = records[i][1]
#             second_lowest.clear()
#             second_lowest.append(records[i])
#         elif records[i][1] == min2:
#             second_lowest.append(records[i])
#         elif records[i][1] == min1:
#             first_lowest.append(records[i])
#         elif records[i][1] < min1:
#             min2 = min1
#             min1 = records[i][1]
#             second_lowest.clear()
#             second_lowest = first_lowest.copy()
#             first_lowest.clear()
#             first_lowest.append(records[i])
#         elif records[i][1] < min2:
#             min2 = records[i][1]
#             second_lowest.clear()
#             second_lowest.append(records[i])
    # names = [n[0] for n in second_lowest]
    # names.sort()
    # print(names)

# easy elegant and short from internet
records, scores = [], []
if __name__ == '__main__':
    for _ in range(int(input('int: '))):
        name = input('name: ')
        score = float(input('float: '))
        records.append([name, score])
        scores.append(score)
    scores = sorted(set(scores))
    names = [n[0] for n in records if n[1] == scores[1]]
    names.sort()
    print(names)
