n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

cases = [
    [[1,0,0],
    [1,1,0],
    [0,0,0]],

    [[0,1,0],
    [1,1,0],
    [0,0,0]],

    [[1,1,0],
    [0,1,0],
    [0,0,0]],

    [[1,1,0],
    [1,0,0],
    [0,0,0]],
    
    [[1,1,1],
    [0,0,0],
    [0,0,0]],

    [[1,0,0],
    [1,0,0],
    [1,0,0]]
]

def getSum(x, y):
    ans = 0
    for i in range(6):
        res = 0
        for dx in range(3):
            for dy in range(3):
                # 범위체크
                if x+dx>=n or y+dy>=m:
                    continue

                if cases[i][dx][dy] == 0:
                    continue

                else:
                    res += grid[x+dx][y+dy]
        
        ans = max(ans, res)

    return ans

maxSum = 0
for i in range(n):
    for j in range(m):
        maxSum = max(maxSum, getSum(i, j))

print(maxSum)