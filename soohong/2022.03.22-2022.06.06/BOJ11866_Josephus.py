import sys
sys.stdin = open('../0518/input.txt')
from collections import deque

N, K = map(int, input().split())

q = deque()
for i in range(1,N+1):
    q.append(i)

result = []
while q:
    q.rotate(-(K-1))
    result.append(q.popleft())

print('<', end='')
print(*result, sep=', ', end='')
print('>', end='')