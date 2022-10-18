import sys
sys.stdin = open('11920input.txt')

N, K = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(K):
    for j in range(N-1):
        if arr[j] >= arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(*arr)



N, K = map(int, input().split())
A = list(map(int,input().split()))
count = 0

for a in range(N - 1):
    for b in range(N - 1):
        if A[b] > A[b + 1]:
            A[b], A[b + 1] = A[b + 1], A[b]
    count += 1

    if count == K:
        print(*A)
        break