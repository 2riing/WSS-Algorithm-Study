import sys
sys.stdin = open('2644input.txt')
from collections import deque

def BFS(graph, A):
    visited = []
    queue = deque([A])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited

N = int(input())


A, B = map(int, input().split())
graph = [[] for _ in range(N+1)]
# visited = [False] * (N + 1)
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N+1):
    graph[i].sort()
# print(graph)
BFS(graph, A)
