import sys
sys.stdin = open('../0518/input.txt')
from collections import deque

def BFS(point):
    di, dj = [1, -1, 0, 0], [0, 0, 1, -1]
    q = deque()
    q.append(point)
    cnt = 0
    while q:
        row, col = q.popleft()
        for i in range(4):
            ni, nj = row + di[i], col + dj[i]
            if 0<= ni < N and 0<= nj < M:
                if visited[ni][nj] == 0 and matrix[ni][nj] == 1:
                    q.append((ni, nj))
                    visited[ni][nj] = 1
                    cnt += 1
    return cnt

N, M, K = map(int, input().split())
matrix = [[ 0 for _ in range(M)] for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(K):
    i, j = map(int, input().split())
    matrix[i-1][j-1] = 1

results = []
for k1 in range(N):
    for k2 in range(M):
        if matrix[k1][k2] == 1 and visited[k1][k2] == 0:
            visited = [[0 for _ in range(M)] for _ in range(N)]
            results.append(BFS((k1, k2)))
print(max(results))