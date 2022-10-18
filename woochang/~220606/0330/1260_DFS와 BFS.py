import sys
sys.stdin = open('1260input.txt')
from collections import deque


#
# def dfs(n):
#     print(n, end=' ')
#     visited[n] = True
#     for i in graph[n]:
#         if not visited[i]:
#             dfs(i)
#
#
# def bfs(n):
#     visited[n] = True
#     queue = deque([n])
#     while queue:
#         V = queue.popleft()
#         print(V, end= ' ')
#         for i in graph[V]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
#
#
# # node, branch, first node
# n, m, V = map(int, sys.stdin.readline().split())
# graph = [[] for _ in range(n+1)]
# visited = [False] * (n + 1)
#
# # make adjacency list
# for _ in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)
# # sort adjacency list
# for i in range(1, n+1):
#     graph[i].sort()
#
# dfs(V)
# # initialize check list
# visited = [False] * (n + 1)
# print()
# bfs(V)
# #
def dfs(V):
    visited[V] = True
    print(V, end =' ')
    for i in graph[V]:
        if visited[i] == False:
            dfs(i)

def bfs(V, graph):
    queue = deque([V])
    visited[V] = True
    while queue:
        V.queue.popleft()
        print(V, end= ' ')
        for i in graph(V):
            if not visited[i]:
                visited[i] = True
                queue.append(i)




N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N+1):
    graph[i].sort()
# print(arr)

dfs(V)
print()
visited = [False for _ in range(N+1)]
bfs(V, graph)
