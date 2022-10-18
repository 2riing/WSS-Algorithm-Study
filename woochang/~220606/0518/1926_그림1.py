import sys
sys.stdin = open('1926input.txt')
from collections import deque

def bfs():
    global max_trash
    dt = [[1,0],[-1,0],[0,1],[0,-1]]
    for i in range(N):
        for j in range(M):
            p = 1
            if arr[i][j] == 1 and visited[i][j] == 0:
                q = deque([[i,j]])
                visited[i][j] = p
                while q:
                    n = q.popleft()
                    for a in dt:
                        nx, ny = n[0]+a[0] , n[1]+a[1]
                        if 0<=nx<N and 0<=ny<M and arr[nx][ny] == 1 and visited[nx][ny] == 0 :
                            p += 1
                            visited[nx][ny] = p
                            q.append([nx,ny])
                if max_trash <= p:
                    max_trash = p


N, M = map(int,input().split())
# arr = [[0 for _ in range(M)] for _ in range(N)]
arr = [list(map(int, input().split())) for _ in range(N)]


# for i in range(K):
#     j, k = map(int, input().split())
#     arr[j-1][k-1] = 1
visited = [[0 for _ in range(M)] for _ in range(N)]
max_trash = 0
bfs()
cnt = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 1:
            cnt += 1
print(cnt)

print(max_trash)