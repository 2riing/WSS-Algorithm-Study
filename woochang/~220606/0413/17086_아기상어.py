import sys
sys.stdin = open('17086input.txt')
from collections import deque

def bfs(shark):
    q = deque(shark)
    visited = [[False for _ in range(M)] for _ in range(N)]

    delta = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    for i in shark:
        visited[i[0]][i[1]] = 1

    while q:
        n = q.popleft()
        v = visited[n[0]][n[1]]
        for dx, dy in delta:
            nx, ny = n[0]+dx , n[1]+dy
            if 0<=nx<N and 0<=ny<M:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = v+1
                    q.append([nx,ny])
                elif visited[nx][ny] > v+1:
                    visited[nx][ny] = v + 1
                    q.append([nx,ny])
    max_num = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] > max_num:
                max_num = visited[i][j]
    return max_num








N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
shark = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            shark.append([i,j])
print(bfs(shark)-1)

