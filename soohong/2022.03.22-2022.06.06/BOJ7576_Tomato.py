import sys
sys.stdin = open('input.txt')
from collections import deque
# 며칠이 되면 다 익게 되는지 최소일 수
# 다 끝났는데도 익지 못하면 -1

def BFS():
    di, dj = [1, -1, 0, 0], [0, 0, 1, -1]
    while q:
        row, col = q.popleft()
        for i in range(4):
            ni, nj = di[i] + row, dj[i] + col
            if 0<= ni < N and 0<= nj < M:
                if visited[ni][nj] == 0 and tomato_box[ni][nj] == 0:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[row][col] + 1
    return visited[row][col]-1

# 기본 입출력 및 선언
M, N = map(int, input().split())
tomato_box = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
q = deque()

# q에 시작 포인트 넣어주기
for i in range(N):
    for j in range(M):
        if tomato_box[i][j] == 1:
            q.append((i, j))
            visited[i][j] = 1
print(BFS())

total = 0
max_num = 0
for k1 in range(N):
    if max_num < max(visited[k1]):
        max_num = max(visited[k1])
    for k2 in range(M):
        if visited[k1][k2] >= 1 or tomato_box[k1][k2] == -1:
            total += 1

if total == M*N:
    print(max_num-1)
elif total < M*N:
    print(-1)


