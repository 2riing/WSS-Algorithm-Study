import sys
sys.stdin = open('private/input.txt')

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

print(area)