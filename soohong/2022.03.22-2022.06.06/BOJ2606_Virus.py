import sys
sys.stdin= open('input.txt')
from collections import deque

def BFS(node):
    q = deque()
    q.append(node)
    visited[node] = 1
    while q:
        v = q.popleft()
        for nv in graph[v]:
            if visited[nv] == 0:
                q.append(nv)
                visited[nv] = 1

N = int(input())
line = int(input())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
# 그래프 그리기
for i in range(line):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

BFS(1)
print(visited[2:].count(1))
