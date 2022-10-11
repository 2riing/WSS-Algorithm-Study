import sys
sys.stdin = open('../0602/input.txt')
from collections import deque

def BFS(point, o, v):
    q.append(point)
    global result_sheep, result_wolf, visited
    sheep, wolf = o, v
    while q:
        row, col = q.popleft()
        visited[row][col] = 1
        for i in range(4):
            ni, nj = row + di[i], col + dj[i]
            if 0 <= ni < R and 0 <= nj < C:
                if madang[ni][nj] != '#' and visited[ni][nj] == 0: # 벽이 아니고, 방문한적 없을 때
                    if madang[ni][nj] == 'o':
                        sheep += 1
                    elif madang[ni][nj] == 'v':
                        wolf += 1
                    q.append((ni, nj))
                    visited[ni][nj] = 1
    if sheep > wolf:
        result_sheep += sheep
    else:
        result_wolf += wolf


R, C = map(int, input().split())
madang = list(input() for _ in range(R))
visited = [[0 for _ in range(C)] for _ in range(R)]
result_sheep, result_wolf = 0, 0

di, dj = [1, -1, 0, 0], [0, 0, 1, -1]
q = deque()

for i in range(R):
    for j in range(C):
        if madang[i][j] == 'o' and visited[i][j] == 0 :
            BFS((i, j), 1, 0)
        elif madang[i][j] == 'v' and  visited[i][j] == 0:
            BFS((i, j), 0, 1)


print(result_sheep, result_wolf)
