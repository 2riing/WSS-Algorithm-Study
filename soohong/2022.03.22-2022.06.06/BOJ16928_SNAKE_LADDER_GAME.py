import sys
sys.stdin = open('../0504/input.txt')

N, M = map(int, input().split())
ladder = [list(map(int, input().split())) for _ in range(N)]
snake = [list(map(int, input().split())) for _ in range(M)]

# 숨바꼭질
[x+1,x+2,x+3,4,5,6]