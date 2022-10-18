import sys
sys.stdin = open('2606input.txt')
from collections import deque

def bfs(graph, start):
    global cnt
    q = deque([start])
    visited = [False for _ in range(N+1)]
    visited[start] = cnt
    while q:
        n = q.popleft()
        for i in graph[n]:
            if not visited[i]:
                cnt += 1
                visited[i] = cnt
                q.append(i)





N = int(input())
T = int(input())
graph = [[] for _ in range(N+1)]
cnt = 1
for i in range(T):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
bfs(graph,1)
print(cnt-1)