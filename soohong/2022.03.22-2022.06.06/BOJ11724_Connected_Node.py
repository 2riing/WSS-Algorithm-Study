import sys
sys.stdin = open('../0602/input.txt')
from collections import deque

def BFS(start):
    q.append(start)
    while q:
        now = q.popleft()
        for i in range(len(connect[now])):
            if visited[connect[now][i]] == 0:
                q.append(connect[now][i])
                visited[connect[now][i]] = 1

input = sys.stdin.readline # readline안해주면 시간초과

N, M = map(int, input().split())
connect = [[] for _ in range(N+1)] 
visited = [0 for _ in range(N+1)]
q = deque()

for i in range(M):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

cnt = 0
for i in range(1, N+1):
    if visited[i] == 0: # 방문하지 않은 노드가 있다면
        visited[i] = 1 # 방문처리 해주고
        BFS(i) # BFS돌려봄
        cnt += 1

print(cnt)
