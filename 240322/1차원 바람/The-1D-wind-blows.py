n,m,q = map(int,input().split())
grid = [[0]*(m+1)] + [[0]+list(map(int,input().split())) for _ in range(n)]

def shiftRight(row):
    temp = grid[row][m]
    for i in range(m, 1, -1):
        grid[row][i] = grid[row][i-1]
    grid[row][1] = temp

def shiftLeft(row):
    temp = grid[row][1]
    for i in range(1, m):
        grid[row][i] = grid[row][i+1]
    grid[row][m] = temp

def checkUp(row):
    flag = False
    for col in range(1, m+1):
        if grid[row][col] == grid[row-1][col]:
            flag = True
    return flag

def checkDown(row):
    flag = False
    for col in range(1, m+1):
        if grid[row][col] == grid[row+1][col]:
            flag = True
    return flag

def changeDirect(now):
    if now == "L":
        return "R"
    else:
        return "L"


for _ in range(q):
    start, direct = input().split()
    start = int(start)

    if direct == "L":
        shiftRight(start)

    else:
        shiftLeft(start)

    upDirect = direct
    downDirect = direct
    for row in range(start-1, 0, -1):
        if checkUp(row+1):
            upDirect = changeDirect(upDirect)
            if upDirect == "L":
                shiftRight(row)
            else:
                shiftLeft(row)
        
        else:
            break

    for row in range(start+1, n+1):
        if checkDown(row-1):
            downDirect = changeDirect(downDirect)
            if downDirect == "L":
                shiftRight(row)
            else:
                shiftLeft(row)
    
        else:
            break


for i in range(1, n+1):
    for j in range(1, m+1):
        print(grid[i][j], end=" ")
    print()