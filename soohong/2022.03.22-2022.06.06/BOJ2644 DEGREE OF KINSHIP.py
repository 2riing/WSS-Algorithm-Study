import sys
sys.stdin = open('input.txt')
from collections import deque

def BFS():
    q = deque()
    q.append(A)
    while q:
        v = q.popleft()
        if v == B:
            return
        for i in range(N+1):
            if visited[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visited[i] = visited[v] + 1
# 기본 입력
N = int(input()) # 전체 사람의 수
A, B = map(int, input().split())
M = int(input())
graph = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

BFS()
if visited[B]>0:
    print(visited[B])
else:
    print(-1)


