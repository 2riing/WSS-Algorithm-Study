import sys
sys.stdin = open('2775input.txt')

N = int(input())

for _ in range(N):
    k = int(input()) # 층
    n = int(input()) # 호
    arr = [x for x in range(1, n+1)]  # [1, 2, 3, 4, 5, ...]
    for i in range(k):
        for j in range(1,n):
            arr[j] += arr[j-1]
    print(arr[-1])


# 0층 1 2 3 4 5 ...
# 1층 1 3 6 10 15
# 2층 1 4 10 20 35
# 왼쪽 더하기 위