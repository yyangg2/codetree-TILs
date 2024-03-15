N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]

def partMax(row, col):
    partSum = 0
    for i in range(row, row+3):
        for j in range(col, col+3):
            partSum += grid[i][j]
    
    return partSum

maxSum = 0
for row in range(N):
    for col in range(N):
        if row+2 >= N or col+2 >= N:
            continue
        
        res = partMax(row, col)
        maxSum = max(maxSum, res)

print(maxSum)