import sys
sys.stdin = open('4963input.txt')

def dfs(i,j):
    visited[i][j] = True
    for a,b in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
        ni, nj = i+a, j+b
        if 0<= ni < M and 0<=nj< N and visited[ni][nj] == False and arr[ni][nj] == 1:
            arr[ni][nj] = 0
            dfs(ni,nj)



for _ in range(100):
    N, M = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    visited = [[False] * (N) for _ in range(M)]
    cnt = 0
    for n in range(M):
        for m in range(N):
            if arr[n][m] == 1:
                cnt += 1
                dfs(n,m)

    print(cnt)

    if N == 0:
        break

#런타임 에러 (RecursionError)
# https://help.acmicpc.net/judge/rte/RecursionError