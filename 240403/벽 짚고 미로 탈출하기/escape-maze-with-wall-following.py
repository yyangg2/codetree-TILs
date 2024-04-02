import sys

n = int(input())
cur_x, cur_y = map(int,input().split())
grid = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    a = input()
    for j, elem in enumerate(a, start=1):
        grid[i][j] = elem

visited = [[[False]*4 for _ in range(n+1)] for _ in range(n+1)]

time = 0

# 현재 바라보고 있는 방향
# 오른쪽=0 / 아래쪽=1 / 왼쪽=2 / 위쪽=3 
cur_dir = 0

def inRange(x, y):
    return 1<=x and x<=n and 1<=y and y<=n


    # case1) 한 칸 직진했다고 가정한 상태에서, 오른쪽에 벽 있으면 직진
    # next_x, next_y = curr_x + dxs[curr_dir], curr_y + dys[curr_dir]
    # if cur_dir == 0:
    #   if grid[next_x+1][next_y] == '#':
    #       cur_x, cur_y = next_x, next_y

    # elif cur_dir == 1:
    #   if grid[next_x+1][next_y-1] == '#':
    #        cur_x, cur_y = next_x, next_y

    # elif cur_dir == 2:
    #   if grid[next_x-1][next_y] == '#':
    #        cur_x, cur_y = next_x, next_y

    # elif cur_dir == 3:
    #   if grid[next_x][next_y+1]:
    #        cur_x, cur_y = next_x, next_y


    # case2) 한 칸 직진했다고 가정한 상태에서, 오른쪽에 벽 없으면 현재 방향으로 한 칸 직진 후,
    # -> 시계 방향으로 90도 회전 후, 한 칸 직진
    # if cur_dir == 0:
    #   if grid[next_x+1][next_y] == '.':
    #       cur_x, cur_y = next_x, next_y
    #       cur_dir += 1
    #       next_x, next_y = curr_x + dxs[curr_dir], curr_y + dys[curr_dir]
    #       cur_x, cur_y = next_x, next_y


    # case3) 현재 상태에서 한 칸 앞에 벽이 있을 경우, 반시계 방향으로 90도 회전
    # cur_dir = 0 -> grid[next_x][next_y] == '#' -> cur_dir -= 1
    # cur_dir = 1
    # cur_dir = 2
    # cur_dir = 3


    # case4) 현재 상태에서 한 칸 앞이 격자 밖이면, 통과하고 종료
    # if inRange(next_x, next_y):
    # time += 1
    # break

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
while inRange(cur_x, cur_y):
    if visited[cur_x][cur_y][cur_dir]:
        print(-1)
        sys.exit(0)
    
    # 현재 상황이 다시 반복되는지를 나중에 확인하기 위해
    # 현재 상황에 해당하는 곳에 visited 값을 True로 설정합니다.
    visited[cur_x][cur_y][cur_dir] = True

    next_x, next_y = cur_x + dxs[cur_dir], cur_y + dys[cur_dir]

    # case4
    if not inRange(next_x, next_y):
        time += 1
        break

    # case3
    if grid[next_x][next_y] == '#':
        cur_dir = (cur_dir -1 + 4) % 4

    # case 1,2
    else:
        rx = next_x + dxs[(cur_dir + 1) % 4]
        ry = next_y + dys[(cur_dir + 1) % 4]

        # case1: 한 칸 앞에서 우측에 벽 있는 경우
        if grid[rx][ry] == '#':
            cur_x, cur_y = next_x, next_y
            time += 1

        # case2: 한 칸 앞에서 우측에 벽 없는 경우
        else:
            cur_x, cur_y = rx, ry
            cur_dir = (cur_dir + 1) % 4
            time += 2

print(time)