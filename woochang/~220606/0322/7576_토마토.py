import sys
sys.stdin = open('input3.txt')
from collections import deque

def tomato(r):
    q= deque(r)
    dt = [[1,0],[0,1],[-1,0],[0,-1]]
    while q:
        n = q.popleft()
        for i in dt:
            nx,ny = i[0] + n[0] , i[1]+n[1]
            if 0<=nx<N and 0<=ny<M and arr[nx][ny] == 0:
                arr[nx][ny] = n[2]
                q.append([nx,ny,n[2]+1])

M, N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

cnt0 = 0
cntday = 1
arr1 = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            cnt0 += 1
        elif arr[i][j] == 1:
            arr1.append([i,j,cntday])
tomato(arr1)
minnum = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            minnum = 99999999
        elif arr[i][j] > minnum:
            minnum = arr[i][j]
if minnum == 99999999:
    print(-1)
elif minnum == 1:
    print(0)
else:
    print(minnum)