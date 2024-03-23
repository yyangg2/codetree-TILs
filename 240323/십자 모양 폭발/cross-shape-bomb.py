n = int(input())

grid = [[0]*(n+1)] + [[0] + list(map(int,input().split())) for _ in range(n)]

r, c = map(int,input().split())

v = grid[r][c]


for row in range(r, r+v):
    grid[row][c] = 0

for row in range(r, r-v, -1):
    grid[row][c] = 0

for col in range(c, c+v):
    grid[r][col] = 0

for col in range(c, c-v, -1):
    grid[r][col] = 0

temp = [[0]*(n+1) for _ in range(n+1)]

for col in range(1, n+1):
    tempRow = n
    for row in range(n, 0, -1):
        if grid[row][col] != 0:
            temp[tempRow][col] = grid[row][col]
            tempRow -= 1

for col in range(1, n+1):
    for row in range(1, n+1):
        grid[row][col] = temp[row][col]

for i in range(1, n+1):
    for j in range(1, n+1):
        print(grid[i][j], end=" ")
    print()