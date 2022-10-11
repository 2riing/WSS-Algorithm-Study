import sys
sys.stdin= open('input.txt')
from collections import deque

def BFS(point, cnt, num):
    di, dj = [1, -1, 0, 0], [0,0,1,-1]
    q = deque()
    i, j = point
    q.append((i,j))
    visited[i][j] = num
    while q:
        row, col = q.popleft()
        for i in range(4):
            ni, nj =  di[i] + row, dj[i] +col
            if 0<= ni < N and 0<= nj < N:
                if visited[ni][nj] == 0 and maps[ni][nj] == 1:
                    q.append((ni, nj))
                    visited[ni][nj] = num
                    cnt += 1
    result.append(cnt)

# 기본 입력
N = int(input())
maps = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
result = []

num = 1
for i in range(N):
    for j in range(N):
        if maps[i][j] == 1 and visited[i][j] == 0:
            cnt = 1
            BFS((i,j), cnt, num)
            num += 1

result.sort()
print(len(result))
for r in result:
    print(r)
