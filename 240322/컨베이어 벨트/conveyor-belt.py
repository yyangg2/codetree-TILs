n, t = map(int,input().split())
# 0 1 2
# 5 4 3

# 0 1 2 ... n-1
# 2n-1 ......n

A = list(map(int,input().split()))
B = list(map(int,input().split()))

for _ in range(t):
    temp1 = A[n-1]
    temp2 = B[n-1]

    for i in range(n-1, 0, -1):
        A[i] = A[i-1]
    A[0] = temp2

    for i in range(n-1, 0, -1):
        B[i] = B[i-1]
    B[0] = temp1

print(*A)
print(*B)