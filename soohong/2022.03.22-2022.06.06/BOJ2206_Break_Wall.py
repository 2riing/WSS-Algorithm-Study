import sys
sys.stdin = open('private/input.txt')
from collections import deque

# 시작 0,0 도착 N-1, M-1
def BFS():
    di, dj = [1, -1, 0, 0], [0, 0, 1, -1]
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        row, col = q.popleft()
        if row == N - 1 and col == M - 1:
            return
        for i in range(4):
            ni, nj = di[i] + row, dj[i] + col
            if 0 <= ni < N and 0 <= nj < M:
                if visited[ni][nj] == 0 and maps[ni][nj] == 0:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[row][col] + 1

# 한개 뿌셨을 때, 하나도 안뿌셨을 때
N, M = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
result = []

# 벽 안뿌수고 실행
BFS()
result.append(visited[N - 1][M - 1])

max_num = 0
# 벽 차례대로 한 번씩 부셔보고 실행
for i in range(N):
    for j in range(M):
        if maps[i][j] == 1:
            visited = [[0 for _ in range(M)] for _ in range(N)]
            maps[i][j] = 0
            BFS()
            result = visited[N - 1][M - 1]
            maps[i][j] = 1  # 원상복구
            if result > max_num:
                max_num = result

if max_num > 0:
    print(max_num)
else:
    print(-1)
