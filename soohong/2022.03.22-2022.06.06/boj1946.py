import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    grade = [list(map(int, input().split())) for _ in range(N)]

    grade.sort()
    print(grade)