import sys
sys.stdin = open('input.txt')
from collections import deque

N = int(input())
q = deque()
for i in range(1, N+1):
    q.append(i)

# 만약에 len(q)==1 이면 print하고 break
# 왼쪽 팝
# 왼쪽 팝해서 append
while q:
    if len(q) == 1:
        print(q.pop())
        break
    else:
        q.popleft()
        q.append(q.popleft())


