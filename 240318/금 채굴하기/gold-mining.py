# n:격자크기, m:금 개당 가격
n, m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

def costArea(k):
    return k*k + (k+1)*(k+1)

def gold(row, col, k):
    cnt = 0

    for i in range(n):
        for j in range(n):
            if abs(row-i) + abs(col-j) <= k:
                if grid[i][j] == 1:
                    cnt += 1

    return cnt


ans = 0
for row in range(n):
    for col in range(n):
        for k in range((n-1)*2 + 1):
            goldCount = gold(row, col, k)

            if goldCount*m >= costArea(k):
                ans = max(ans, goldCount)

print(ans)