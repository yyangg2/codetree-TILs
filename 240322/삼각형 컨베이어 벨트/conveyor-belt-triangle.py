n, t = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

for _ in range(t):
    temp1 = A[n-1]
    temp2 = B[n-1]
    temp3 = C[n-1]

    for i in range(n-1, 0, -1):
        A[i] = A[i-1]
    A[0] = temp3

    for i in range(n-1, 0, -1):
        B[i] = B[i-1]
    B[0] = temp1

    for i in range(n-1, 0, -1):
        C[i] = C[i-1]
    C[0] = temp2

print(*A)
print(*B)
print(*C)