import sys
sys.stdin = open('1389input.txt')
from collections import deque

def bfs(graph, i):

    num = [0] * (N+1)
    q = deque()
    q.append(i)
    visited = [False for _ in range(N+1)]

    while q:

        n = q.popleft()
        visited[n] = True
        for j in graph[n]:
            if not visited[j]:
                num[j] = num[n] + 1
                visited[j] = True
                q.append(j)
    return sum(num)





N, M = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
graph = [[] for _ in range(N+1)]
for ar in arr:
    graph[ar[1]].append(ar[0])
    graph[ar[0]].append(ar[1])
ans = 1000
result = [0]
for i in range(1,N+1):
    K = bfs(graph, i)
    result.append(K)

for j in range(1,N+1):
    if result[j] < ans:
        ans = result[j]
        ans_index = j

print(ans_index)
