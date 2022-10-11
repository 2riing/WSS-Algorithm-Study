import sys
sys.stdin = open('private/input.txt')
from collections import deque

def BFS() -> int:
    q = deque()
    cnt = 0
    q.append((N, cnt))
    visited = set()
    while q:
        v, cnt = q.popleft()
        if v == M:
            return cnt
        for i in range(3):
            nv = [v-1, v+1, v*2]
            if 0<=nv[i]<1000000 and nv[i] not in visited:
                q.append((nv[i], cnt+1))
                visited.add(nv[i])


N, M = map(int, input().split()) # 현재 숫자, 도달해야하는 숫자
cnt = BFS()
print(f'{cnt}')