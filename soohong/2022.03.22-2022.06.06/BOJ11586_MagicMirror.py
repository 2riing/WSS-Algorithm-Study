import sys
sys.stdin = open('input.txt')

N = int(input()) # 거울의 크기
figure = [input() for _ in range(N)]
K = int(input()) # 거울의 심리상태

if K == 1: # 그대로
    for i in range(N):
        print(figure[i])

elif K ==2: # 좌우반전
    for i in range(N):
        for j in range(N-1, -1, -1):
            print(figure[i][j], end='')
        print()

elif K == 3: # 상하반전
    for i in range(N-1, -1, -1):
        for j in range(N):
            print(figure[i][j], end='')
        print()


