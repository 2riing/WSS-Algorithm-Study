import sys
sys.stdin = open('input.txt')
from collections import deque

def BFS(b):
    q = deque()
    q.append(b)
    visited[b] = 1
    while q:
        v = q.popleft()
        for i in range(1, N+1):
            if visited[i] == 0 and group[v][i] == 1:
                q.append(i)
                visited[i] = visited[v] + 1

# 기본 입력
N, M = map(int,input().split()) # 유저의 수(노드), 친구 관계의 수(간선)
group = [[0] * (N+1) for _ in range(N+1)]
for i in range(M): # 관계 받아오기
    a, b = map(int, input().split())
    group[a][b] = group[b][a] = 1

result = [0] * (N+1)
for i in range(1, N+1):
    visited = [0] * (N + 1) # visited 초기화
    BFS(i)
    result[i] = (sum(visited)) # 순서대로 알맞은 인덱스에 넣어줌

min_sum = 100
for i in range(1, N+1):
    if result[i] < min_sum:
        min_sum = result[i]
print(result.index(min_sum)) # 의 인덱스를 프린트

