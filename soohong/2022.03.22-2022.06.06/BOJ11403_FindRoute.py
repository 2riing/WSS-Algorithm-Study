import sys
sys.stdin = open('input.txt')
from collections import deque

def BFS(point):
    q = deque()
    q.append(point)
    while q:
        v = q.popleft()
        for i in maps[v]:
            if maps[v][i] == 1 and visited[v][i] == 0:
                visited[v][i] = 1
                q.append(i)

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
graph = [[0]*N for _ in range(N)]
visited = [[0]*N for _ in range(N)]
routes = []
for i in range(N): # 그래프 그려주기
    for j in range(N):
        if maps[i][j] == 1:
            routes.append((i,j))
# for route in routes:
#     a, b = map(int, route)
#     graph[a][b] = 1
print(routes)
for i in range(N):
    BFS(i)

for i in range(N):
    print(*visited[i])



