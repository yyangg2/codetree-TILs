n = int(input())
arr = []
for i in range(n):
    s = int(input())
    arr.append(s)

temp = [0] * n
endOf = 0
s1, e1 = map(int,input().split())
for i in range(n):
    if s1-1 > i or i > e1-1:
        temp[endOf] = arr[i]
        endOf += 1

for i in range(endOf):
    arr[i] = temp[i]

n = endOf
endOf = 0

s2, e2 = map(int,input().split())
for i in range(n):
    if s2-1 > i or i > e2-1:
        temp[endOf] = arr[i]
        endOf += 1

for i in range(endOf):
    arr[i] = temp[i]

n = endOf

print(n)
for i in range(n):
    print(arr[i])