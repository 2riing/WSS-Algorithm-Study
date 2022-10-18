import sys
sys.stdin = open('2667input.txt')
from collections import deque

# def bfs(a,b,k):
#
#     q = deque([[a,b]])
#
#     delta = [[-1,0],[1,0],[0,1],[0,-1]]
#     while q:
#         n = q.popleft()
#         visited[n[0]][n[1]] = True
#
#         for dt in delta:
#             dx , dy = n[0]+dt[0], n[1]+dt[1]
#             if 0<=dx<N and 0<=dy<N and visited[dx][dy] == False and arr[dx][dy] == 1:
#                 visited[dx][dy] = True
#                 k += 1
#                 arr[dx][dy] = k
#                 q.append([dx,dy])
#     return k
#
#
# N = int(input())
# arr = [list(map(int, input())) for _ in range(N)]
# visited = [[False for _ in range(N)] for _ in range(N)]
#
# stack = []
# # for _ in range(N):
# a = 0
# b = 0
# k = 1
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 1 and visited[i][j] == False:
#             a = i
#             b = j
#             stack.append(bfs(a,b,k))
#
# # print(arr)
# print(len(stack))
# stack.sort()
# for i in stack:
#     print(i)







def dfs(a,b,k):

    delta = [[-1,0],[1,0],[0,1],[0,-1]]
    stack = []

    visited[a][b] = True
    for dt in delta:
        dx , dy = a+dt[0], b+dt[1]
        if 0<=dx<N and 0<=dy<N and visited[dx][dy] == False and arr[dx][dy] == 1:
            visited[dx][dy] = True
            k += 1
            arr[dx][dy] = k + 1
            dfs(dx,dy,k)



N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
a=0
b=0

k = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == False:
            a = i
            b = j
            dfs(a,b,k)

print(arr)