import sys
sys.stdin = open('7576input.txt')
from collections import deque


def bfs(a, b):
    global ans, cnt
    cnt = 0
    q = deque([(a,b,0)])
    visited = [[False] * (M) for _ in range(N)]
    visited[a][b] = True

    while q:
        ca, cb, cnt = q.popleft()
        for aa,bb in [(-1,0),(1,0),(0,1),(0,-1)]:
            na, nb = ca+aa, cb+bb
            if visited[na][nb] == False and 0 <= na <N and 0 <= nb < M and arr[na][nb] == 0 and arr[na][nb] != -1 :
                   # 방문 X           범위 안 ,                    -1 아닌거 not visited[na][nb] and
                visited[na][nb] = True
                arr[na][nb] = cnt+1
                q.append((na, nb, cnt+1))
            else: continue
    ans = cnt
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                ans = -1
    print(ans)


T = int(input())
for tc in range(1, T+1):
    M, N = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    a = b = 0
    ans = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                a = i
                b = j

    bfs(a, b)