import sys
sys.stdin = open('input.txt')
from collections import deque

def BFS(root):
    q = deque()
    q.append(root)
    visited[root] = 1
    while q:
        v = q.popleft()
        for i in tree[v]: # 시간초과 해결 노력흔적
            if visited[i] == 0 and i in tree[v]:
                q.append(i)
                visited[i] = v

N = int(sys.stdin.readline()) # 노드의 개수
tree = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

BFS(1)
for v in range(2, len(visited)):
    print(visited[v])

