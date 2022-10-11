import sys
sys.stdin = open('input.txt')
from itertools import permutations

N, M = map(int, input().split())

result = list(permutations(range(1,N+1), M))
for i in range(len(result)):
    print(*result[i])