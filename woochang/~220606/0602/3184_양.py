import sys
sys.stdin = open('3184input.txt')
from collections import deque

def bfs(a,b):
    global cnt, sheep_cnt, wolf_cnt
    q = deque([[a,b]])
    if arr[a][b] == 'o':
        sheep_cnt += 1
    elif arr[a][b] == 'v':
        wolf_cnt += 1
    dt = [[0,1],[0,-1],[1,0],[-1,0]]
    visited[a][b] = cnt
    while q:
        n = q.popleft()
        for d in dt:
            nx, ny = d[0] + n[0] , d[1] + n[1]
            if 0<=nx<=r-1 and 0<=ny<=c-1 and arr[nx][ny] != '#' and visited[nx][ny] == 0:
                visited[nx][ny] = cnt
                q.append([nx,ny])
                if arr[nx][ny] == 'o':
                    sheep_cnt += 1
                elif arr[nx][ny] == 'v':
                    wolf_cnt += 1


r, c = map(int, input().split())
arr = list(str(input()) for _ in range(r))
sheep_cnt = 0
wolf_cnt = 0
sheep_ans = 0
wolf_ans = 0
visited = [[0 for _ in range(c)] for _ in range(r)]
cnt = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] != '#' and visited[i][j] == 0:
            cnt += 1
            bfs(i,j)
            if sheep_cnt > wolf_cnt:
                sheep_ans += sheep_cnt
            else:
                wolf_ans += wolf_cnt
            sheep_cnt = 0
            wolf_cnt = 0

# for i in range(cnt):
#     for a in range(r):
#         for b in range(c):
#             if arr[a][b] == 'o' and visited[a][b] == i:
#                 sheep_cnt += 1
#             elif arr[a][b] == 'v' and visited[a][b] == i:
#                 wolf_cnt += 1
#     if sheep_cnt > wolf_cnt:
#         sheep_ans += sheep_cnt
#     else:
#         wolf_ans += wolf_cnt
#     sheep_cnt = 0
#     wolf_cnt = 0
print(sheep_ans, wolf_ans)