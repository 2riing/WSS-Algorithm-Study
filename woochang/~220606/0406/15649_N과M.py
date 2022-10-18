from itertools import permutations
import sys
sys.stdin = open('15649input.txt')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    permu = []
    for i in range(1,N+1):

        permu.append(i)
    for j in permutations(permu,M):
        print(*j)

    print()




# stack = []
    # for i in range(N):
    #     stack.append(i+1)
    # for i in range(1,N+1):
    #
    #     stack.pop(i)
    #     for j in stack:
    #         print(i, j)
    #     stack.append(i)

