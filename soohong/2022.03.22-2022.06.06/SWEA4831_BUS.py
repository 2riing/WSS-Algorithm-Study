import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    M = list(map(int, input().split()))
    print(f'#{tc}')