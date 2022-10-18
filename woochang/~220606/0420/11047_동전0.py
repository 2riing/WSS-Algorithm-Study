import sys
sys.stdin = open('11047input.txt')

N, K = map(int, input().split())
value = []
for _ in range(N):
    c = int(input())
    value.append(c)
value.sort(reverse=True)
cnt = 0
for j in value:
    if K // j > 0:
        a = K // j
        K -= j*a
        cnt += a
print(cnt)