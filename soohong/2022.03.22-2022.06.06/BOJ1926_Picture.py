import sys
sys.stdin = open('../0518/input.txt')
from collections import deque

def BFS(point):
    di, dj = [1, -1, 0, 0], [0, 0, 1, -1]
    q = deque()
    q.append(point)
    cnt = 1
    while q:
        row, col = q.popleft()
        for i in range(4):
            ni, nj = row + di[i], col + dj[i]
            if 0<= ni < N and 0<= nj < M:
                if visited[ni][nj] == 0 and matrix[ni][nj] == 1:
                    q.append((ni, nj))
                    cnt += 1
                    visited[ni][nj] = 1
    return cnt


N, M  = map(int, input().split())
matrix = [ list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

results = []
pic_cnt = 0
for k1 in range(N):
    for k2 in range(M):
        if matrix[k1][k2] == 1 and visited[k1][k2] == 0:
            visited[k1][k2] = 1
            results.append(BFS((k1, k2)))
            pic_cnt += 1

if len(results) > 0:
    print(pic_cnt)
    print(max(results))
else:
    print(0)
    print(0)
