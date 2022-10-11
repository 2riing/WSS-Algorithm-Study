import sys
sys.stdin = open('input.txt')
from collections import deque

def BFS(A, cnt):
    q = deque()
    q.append([A, cnt])
    visited = set()
    while q:
        temp = q.popleft()
        v, cnt = temp[0], temp[1]
        if v == B:
            return cnt + 1
        else:
            next = [2 * v, int(str(v) + '1')]
            for n in next:
                if 1<= n <10**9 and n not in visited:
                    q.append([n, cnt+1])
                    visited.add(n)
    else:
        return -1


A, B = map(int, input().split())
cnt = 0
print(BFS(A, cnt))
