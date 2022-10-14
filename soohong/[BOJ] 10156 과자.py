import sys
sys.stdin = open('input.txt')

K, N, M = map(int, input().split())

if ((K * N) - M) > 0:
    print((K * N) - M)
else:
    print(0)