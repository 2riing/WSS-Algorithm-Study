import sys
sys.stdin = open('11586input.txt')

N = int(input())

arr = [list(map(str, input())) for _ in range(N)]
T = int(input())

if T == 1:
    for j in range(N):
        print(*arr[j], sep='')

elif T == 2:
    for i in range(N):
        for j in range(N//2):
            arr[i][j], arr[i][N-j-1] = arr[i][N-j-1], arr[i][j]
    for j in range(N):
        print(*arr[j], sep='')
elif T == 3:
    for i in range(N//2):
        arr[N-i-1], arr[i] = arr[i], arr[N-i-1]
    for j in range(N):
        print(*arr[j], sep='')