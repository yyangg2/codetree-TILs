n,m,q = map(int,input().split())
grid = [[0]*(m+1)] + [[0]+list(map(int,input().split())) for _ in range(n)]


def shift(row1,col1,row2,col2):
    temp = grid[row1][col1]

    for row in range(row1, row2):
        grid[row][col1] = grid[row+1][col1]

    for col in range(col1, col2):
        grid[row2][col] = grid[row2][col+1]

    for row in range(row2, row1, -1):
        grid[row][col2] = grid[row-1][col2]

    for col in range(col2, col1+1, -1):
        grid[row1][col] = grid[row1][col-1]

    grid[row1][col1+1] = temp

def avg(row1, col1, row2, col2, A):
    for row in range(row1, row2+1):
        for col in range(col1, col2+1):
            A[row][col] = check(row, col)

            
def inRange(row, col):
    return row >= 1 and row <= n and col >= 1 and col <= m


def check(x, y):
    dxs, dys = [0, 0, 0, 1, -1], [0, 1, -1, 0, 0]
    res = []
    for dx, dy in zip(dxs, dys):
        if inRange(x+dx, y+dy):
            res.append(grid[x+dx][y+dy])
    
    return sum(res) // len(res)


for _ in range(q):
    r1,c1,r2,c2 = map(int,input().split())
    shift(r1,c1,r2,c2)

    A = [[0]*(m+1) for _ in range(n+1)]
    avg(r1,c1,r2,c2,A)

    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            grid[i][j] = A[i][j]


for i in range(1, n+1):
    for j in range(1, m+1):
        print(grid[i][j], end=" ")
    print()