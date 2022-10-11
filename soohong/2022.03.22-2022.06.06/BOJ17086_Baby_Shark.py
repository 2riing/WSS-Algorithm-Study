import sys
sys.stdin= open('input.txt')
from collections import deque

def BFS(point):
    i, j = point
    di, dj = [1, -1, 0, 0, 1, 1, -1, -1], [0, 0, 1, -1, 1, -1, -1, 1]
    q = deque()
    q.append((i, j))
    shark_visited = [[0 for _ in range(M)] for _ in range(N)]
    shark_visited[i][j] = 1
    while q:
        row, col = q.popleft()
        for i in range(8):
            ni, nj = di[i] + row, dj[i] + col
            if 0<= ni < N and 0<= nj < M:
                if shark_visited[ni][nj] == 0 and sharks[ni][nj] == 0:
                    q.append((ni, nj))
                    shark_visited[ni][nj] = shark_visited[row][col] + 1
                elif sharks[ni][nj] == 1:
                    result.append(shark_visited[row][col])
                    return


N, M = map(int, input().split())
sharks = [list(map(int, input().split())) for _ in range(N)]
visited = [ [0 for _ in range(M)] for _ in range(N)]
result = []


for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and sharks[i][j] == 0:
            BFS((i, j))
            visited[i][j] = 1

print(max(result))
