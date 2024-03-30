n,r,c = map(int,input().split())
grid = [[0]*(n+1)] + [[0] + list(map(int,input().split())) for _ in range(n)]

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

ans = []

ans.append(grid[r][c])

def inRange(x, y):
    return 1<=x and x<=n and 1<=y and y<=n

cur_x, cur_y = r, c
max_num = grid[r][c]
max_pos = (r, c)
while True:
    flag = False

    for dx, dy in zip(dxs, dys):
        next_x, next_y = cur_x + dx, cur_y + dy

        if inRange(next_x, next_y):
            if grid[next_x][next_y] > max_num:
                max_num = grid[next_x][next_y]
                max_pos = (next_x, next_y)
                flag = True
                break

    if not flag:
        break

    cur_x, cur_y = max_pos
    ans.append(grid[cur_x][cur_y])

for x in ans:
    print(x, end=" ")