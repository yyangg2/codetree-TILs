def shift(arr):
    temp = arr[-1]
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = temp

    return arr

def change(arr):
    cnt = 1
    res = ""
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            cnt += 1
        else:
            res += arr[i] + str(cnt)
            cnt = 1
        
        if i+1 == len(arr) - 1:
            res += arr[i] + str(cnt)
    
    return len(res)


arr = list(input())
ans = change(arr)
for i in range(1, len(arr)):
    shiftArr = shift(arr)
    lenArr = change(shiftArr)
    ans = min(ans, lenArr)

print(ans)