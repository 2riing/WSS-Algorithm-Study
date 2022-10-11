import sys
sys.stdin = open('../0606/input.txt')
from collections import deque

q = deque()
count = -1
n = int(input())

for i in range(10): # 0 ~ 9 까지 숫자 넣어줌
    q.append(i)

while q:
    now_num = q.popleft()
    count += 1
    if count == n:
        print(now_num) # 현재 숫자를 출력하고
        exit() # 프로그램 강제 종료
        
    for i in range(now_num % 10):
        q.append(now_num * 10 + i)

        # 0 -> x
        # 1 -> 10
        # 2 -> 20, 21
        # 3 -> 30, 31, 32
        # 4 -> 40, 41, 42, 43

        # 21 -> 나머지 1 -> 210
        # 43 -> 나머지 3 -> 430, 431, 432

print(-1) # 다 돌았는데도 종료가 안되면 -1출력