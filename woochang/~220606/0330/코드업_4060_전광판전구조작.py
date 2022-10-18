import sys
sys.stdin = open('4060input.txt')
#
# def turnon(cnt_1):
#     visited = [[0] * N for _ in range(M)]
#     cnt_1 = 0
#     for i in range(M):
#         for j in range(N):
#             if visited[i][j] == 0 and matrix[i][j] == 0:
#                 queue = [[i, j]]
#                 while queue:
#                     v = queue.pop(0)
#                     visited[v[0]][v[1]] = 1
#                     for k in range(4):
#                         next_y = v[0] + dy[k]
#                         next_x = v[1] + dx[k]
#                         if 0 <= next_y < M and 0 <= next_x < N:
#                             if visited[next_y][next_x] == 0:
#                                 if matrix[next_y][next_x] == 0:
#                                     visited[next_y][next_x] = 1
#                                     queue.append([next_y, next_x])
#                 cnt_1 += 1
#     return cnt_1
#
# def turnoff(cnt_2):
#     visited2 = [[0] * N for _ in range(M)]
#     cnt_2 = 0
#     for i in range(M):
#         for j in range(N):
#             if visited2[i][j] == 0 and matrix[i][j] == 1:
#                 queue = [[i, j]]
#                 while queue:
#                     v = queue.pop(0)
#                     visited2[v[0]][v[1]] = 1
#                     for k in range(4):
#                         next_y = v[0] + dy[k]
#                         next_x = v[1] + dx[k]
#                         if 0 <= next_y < M and 0 <= next_x < N:
#                             if visited2[next_y][next_x] == 0:
#                                 if matrix[next_y][next_x] == 1:
#                                     visited2[next_y][next_x] = 1
#                                     queue.append([next_y, next_x])
#                 cnt_2 += 1
#     return cnt_2


M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]
dx = [-1, 1, 0, 0]
dy = [ 0, 0, 1,-1]
# cnt_1 = 0
# cnt_2 = 0
# turnon(cnt_1)
# turnoff(cnt_2)
# print(cnt_1, cnt_2)
# print(matrix)


def bfs():
    visited=[[0]*N for _ in range(M)]
    visited2=[[0] * N for _ in range(M)]
    cnt_1=0
    cnt_2=0
    for i in range(M):
        for j in range(N):
            if visited[i][j]==0 and matrix[i][j]==0:
                queue = [[i,j]]
                while queue:
                    v = queue.pop(0)
                    visited[v[0]][v[1]] = 1
                    for k in range(4):
                        next_y=v[0]+dy[k]
                        next_x=v[1]+dx[k]
                        if 0<=next_y<M and 0<=next_x<N:
                            if visited[next_y][next_x]==0:
                                if matrix[next_y][next_x]==0:
                                    visited[next_y][next_x]=1
                                    queue.append([next_y,next_x])
                cnt_1+=1

            elif visited2[i][j] == 0 and matrix[i][j] == 1:
                queue = [[i, j]]
                while queue:
                    v = queue.pop(0)
                    visited2[v[0]][v[1]] = 1
                    for k in range(4):
                        next_y = v[0] + dy[k]
                        next_x = v[1] + dx[k]
                        if 0 <= next_y < M and 0 <= next_x < N:
                            if visited2[next_y][next_x] == 0:
                                if matrix[next_y][next_x] == 1:
                                    visited2[next_y][next_x] = 1
                                    queue.append([next_y, next_x])
                cnt_2 += 1

    print(cnt_1,cnt_2)

bfs()