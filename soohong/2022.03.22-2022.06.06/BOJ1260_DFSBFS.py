import sys
sys.stdin = open('input.txt')
from collections import deque

def DFS(v):
    visited_dfs[v] = 1  # 방문처리
    print(v, end=' ')
    for i in range(1, N+1):
        if visited_dfs[i] == 0 and num[v][i] == 1:
            DFS(i)


def BFS(v):
    q = deque()
    q.append(v)
    visited_bfs[v] = 1
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, N+1):
            if visited_bfs[i] == 0 and num[v][i] == 1:
                q.append(i)
                visited_bfs[i] = 1

N, M, V = map(int, input().split()) # 정점의 개수, 간선의 개수, 시작할 정점의 번호
visited_bfs = [0]*(N+1) # 방문한적있는지 체크하려고
visited_dfs = [0]*(N+1) # 방문한적있는지 체크하려고
num = [[0] * (N+1) for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    num[a][b] = num[b][a] = 1

DFS(V)
print()
visited = [0]*(N+1)
BFS(V)
