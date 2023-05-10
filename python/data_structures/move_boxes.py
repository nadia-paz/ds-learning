matrix = [
    ['.', '#', '*', '#', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '#', '*'],
    ['#', '#', '.', '.', '.'],
    ['#', '#', '.', '.', '.'],
]

rows = len(matrix)
cols = len(matrix[0])
for r in range(rows):
    print(matrix[r])
print()
# Find the positions of all the boxes
boxes = []
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == '#':
            boxes.append((i, j))

obstacles = {}
for i in range(rows):
    obstacles[i] = []
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == '*':
            obstacles[i].append(j)
# Move the boxes to the right
# for box in boxes:
#     i, j = box
#     while j < cols - 1 and matrix[i][j+1] == '.':
#         matrix[i][j] = '.'
#         matrix[i][j+1] = '#'
#         j += 1

for key, value in obstacles.items():
    prev = key
    print(key)
    print(value)

