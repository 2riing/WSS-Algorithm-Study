import sys
sys.stdin = open('private/input.txt')
from collections import deque

def GB(point, cnt):
    q = deque()
    q.append(point)
    while q:
        row, col = q.popleft()
        for i in range(4):
            ni, nj = di[i] + row, dj[i] + col
            if 0 <= ni < N and 0 <= nj < N:
                if color == 'R' or color == 'G':
                    if visited_GB[ni][nj] == 0 and (pan[ni][nj] == 'R' or pan[ni][nj]== 'G'):
                        q.append((ni, nj))
                        visited_GB[ni][nj] = cnt
                elif color == 'B':
                    if visited_GB[ni][nj] == 0 and pan[ni][nj] == color:
                        q.append((ni, nj))
                        visited_GB[ni][nj] = cnt

def BFS(point, cnt):
    q = deque()
    q.append(point)
    while q:
        row, col = q.popleft()
        for i in range(4):
            ni, nj = di[i] + row, dj[i] + col
            if 0<= ni < N and 0<= nj < N:
                if visited_BFS[ni][nj] == 0 and pan[ni][nj] == color:
                    q.append((ni, nj))
                    visited_BFS[ni][nj] = cnt


# 파랑, 빨강, 초록
# 초록 빨강이 같아 보임임
N = int(input())
pan = [list(input()) for _ in range(N)]
visited_GB = [[0]*N for _ in range(N)]
visited_BFS = [[0]*N for _ in range(N)]
di, dj = [1, -1, 0, 0], [0, 0, 1, -1]

cnt_GB = 1
cnt_BFS = 1
for i in range(N):
    for j in range(N):
        # 적록색약
        if visited_GB[i][j] == 0:
            visited_GB[i][j] = cnt_GB
            color = pan[i][j]
            GB((i,j), cnt_GB)
            cnt_GB += 1
        if visited_BFS[i][j] == 0:
            visited_BFS[i][j] = cnt_BFS
            color = pan[i][j]
            BFS((i, j), cnt_BFS)
            cnt_BFS += 1
GB_max = 0
BFS_max = 0

for k in range(N):
    if GB_max < max(visited_GB[k]):
        GB_max = max(visited_GB[k])
    if BFS_max < max(visited_BFS[k]):
        BFS_max = max(visited_BFS[k])

print(f'{BFS_max} {GB_max}')