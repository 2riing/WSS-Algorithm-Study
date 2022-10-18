import sys
sys.stdin = open('16953input.txt')
from collections import deque

def bfs():
    global ans
    q = deque([(A, 1)])

    while q:
        i, cnt = q.popleft()
        if i == B:
            ans = cnt
            break
        if i * 2 <= B:
            q.append((i * 2, cnt + 1))
        if 10 * i + 1 <= B:
            q.append((10 * i + 1, cnt + 1))



A, B = map(int, input().split())
ans = -1
bfs()

print(ans)