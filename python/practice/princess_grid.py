#!/usr/bin/python

#def displayPathtoPrincess(n,grid):
#print all the moves here

#m = int(input())

def get_grid(m:int, princess:str = ''):
    ''' 
    draw the grid with or without a princess
    recursive function
    '''
    grid = []
    if princess == '':
        for i in range(0, m): 
            #grid.append(input().strip())
            # m is always odd
            # automate grid print
            if i < m//2 or i > m//2:
                s = '-' * m
                grid.append('-' * m)
            else:
                s = '-' * (m//2)
                grid.append(s + 'm' + s)
        return grid
    else:
        grid = get_grid(m)
        #print(grid)
        place_princess(m, grid, princess=princess)
        return grid

def place_princess(m:int, grid: list[str], princess='UL'):
    s = '-' * (m-1)
    princess = princess.upper()
    if princess not in ['UL', 'UR', 'BL', 'BR']:
        princess = 'UL'
    if princess == 'UL':
        grid[0] = 'p' + s
    elif princess == 'UR':
        grid[0] = s + 'p'
    elif princess == 'BL':
        grid[m-1] = 'p' + s
    else:
        grid[m-1] = s + 'p'
    return grid

    

# m = 7
# grid = get_grid(m, 'BL')

def displayPathtoPrincess(m,grid):
    ''' 
    prints the way from bot(m) to princess(p)
    '''
    s = '-' * (m-1)
    sl = 'p' + s
    sr = s + 'p'
    if 'p' in grid[0]:
        s = grid[0]
        for i in range(m // 2):
            print('UP')
    else:
        s = grid[m-1]
        for i in range(m // 2):
            print('DOWN')
    if s == sl:
        for i in range(m // 2):
            print('LEFT')
    elif s == sr:
        for i in range(m // 2):
            print('RIGHT')

def displayPathtoPrincess1(n,grid):
    if grid[0][0] == 'p':
        print('UP\nLEFT\n'* ((n-1)//2))
    elif grid[n-1][0] == 'p':
        print('DOWN\nLEFT\n'* ((n-1)//2))
    elif grid[0][n-1] == 'p':
        print('UP\nRIGHT\n'* ((n-1)//2))
    elif grid[n-1][n-1] == 'p':
        print('DOWN\nRIGHT\n'* ((n-1)//2))

if __name__ == '__main__':
    m = int(input('Enter odd number:\n'))
    message = 'Enter princess location\nUL, BL, UR or BR\n'
    princess = input(message)

    grid = get_grid(m, princess)

    displayPathtoPrincess(m,grid)
