n,m = map(int,input().split())
arr = []

for i in range(n):
    s = int(input())
    arr.append(s)


def getEnd(startIdx, num):
    for i in range(startIdx+1, len(arr)):
        if arr[i] != num:
            return i-1
    
    return len(arr)-1


# 먼저 제거할거를 0으로 표시해두고, temp 배열에 0이 아니면 추가하는 방식으로
while True:
    flag = False
    temp = []
    for cur, num in enumerate(arr):
        if num == 0:
            continue

        endIdx = getEnd(cur, num)
        if endIdx - cur + 1 >= m:
            for i in range(cur, endIdx+1):
                arr[i] = 0
                flag = True

    for x in arr:
        if x != 0:
            temp.append(x)

    arr = temp
    
    #폭탄이 안 터졌다면 종료
    if not flag:
        break

print(len(arr))
for x in arr:
    print(x)