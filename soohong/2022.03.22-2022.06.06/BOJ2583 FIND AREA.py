import sys
sys.stdin = open('input.txt')
from collections import deque

#사각형을 그려주는 함수
def Draw():
    while draw:
        temp = draw.pop()
        row1, col1, row2, col2 = temp[1], temp[0], temp[3], temp[2]
        for i in range(row1, row2):
            for j in range(col1, col2):
                monoon[i][j] = 1

def DFS(point):
    ni, nj = [1, -1, 0, 0], [0, 0, 1, -1]
    q = deque()
    q.append(point)
    visited[point[0]][point[1]] = 1
    cnt = 1
    while q:
        temp = q.pop()
        row, col = temp[0], temp[1]
        for i in range(4):
            di, dj = row + ni[i], col + nj[i]
            if 0 <= di < M and 0 <= dj < N:
                if visited[di][dj] == 0 and monoon[di][dj] == 0:
                    q.append([di, dj])
                    visited[di][dj] = 1
                    cnt += 1
    return cnt

# 기본 입출력 및 사각형 그려주기
M, N, K = map(int, input().split()) # 세로가 M 가로가 N 사각형 개수가 3
draw = [list(map(int, input().split())) for _ in range(K)]
monoon = [[0]*N for _ in range(M)]
visited = [[0]*N for _ in range(M)]
Draw()
dfscnt =0
result = []
for i in range(M):
    for j in range(N):
        if monoon[i][j] == 0 and visited[i][j] == 0:
            dfscnt += 1
            result.append(DFS([i, j]))

print(dfscnt)
result.sort()
print(*result)
