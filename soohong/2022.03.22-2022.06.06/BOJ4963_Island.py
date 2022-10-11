import sys
sys.stdin = open('input.txt')
from collections import deque


di = [1, -1, 0, 0, 1, 1, -1, -1] # 상하좌우 대각선
dj = [0, 0, 1, -1, 1, -1, 1, -1]

def BFS(point):
    global cnt
    q = deque()
    q.append(point)
    while q:
        temp = q.popleft()
        row, col = temp[0], temp[1]
        for i in range(8):
            ni, nj = di[i] + row, dj[i] + col
            if 0<= ni < h and 0<= nj < w:
                if visited[ni][nj] == 0 and maps[ni][nj] == 1:
                    q.append([ni, nj])
                    visited[ni][nj] = cnt

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    else:
        maps = [list(map(int, input().split())) for _ in range(h)]
        visited = [[0] * w for _ in range(h)]

        cnt = 1
        for i in range(h):
            for j in range(w):
                if maps[i][j] == 1 and visited[i][j] == 0:
                    visited[i][j] = cnt
                    BFS([i, j])
                    cnt += 1

    print(cnt-1)