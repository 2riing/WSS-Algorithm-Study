import sys
sys.stdin = open('2164input.txt')
from collections import deque
#
N = int(input())
queue = deque([])
for i in range(1,N+1):
    queue.append(i)

# print(len(queue))
while len(queue) >1:
    queue.popleft()
    n = queue.popleft()

    queue.append(n)

print(queue[0])

