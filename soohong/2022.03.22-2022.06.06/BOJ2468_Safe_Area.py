import sys
sys.stdin = open('../0511/input.txt')

def DFS(point, cnt):
    stack = []
    stack.append(point)
    while stack:
        row, col = stack.pop()
        di, dj = [1, -1, 0, 0], [0, 0, 1, -1]
        for i in range(4):
            ni, nj = di[i] + row, dj[i] + col
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == 0:
                    visited[ni][nj] = cnt
                    stack.append((ni,nj))


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
result = []

# 비는 최대값의 -1만큼 돌려주려고 Find maxnum
M = 0
for i in range(N):
    if max(area[i]) > M: # return max
        M = max(area[i])

for m in range(M): # m == 장마의 높이
    visited = [[0] * N for _ in range(N)] # initialize visited
    for i in range(N): # 비내려주기
        for j in range(N):
            if area[i][j] <= m:
                visited[i][j] = 1
    cnt = 1
    for i in range(N): # dfs 실행해주기
        for j in range(N):
            if visited[i][j] == 0:
                cnt += 1
                visited[i][j] = cnt
                DFS((i, j) , cnt)
    result.append(cnt)
    print(visited)
if result:
    print(max(result)-1)
else:
    print(1)

