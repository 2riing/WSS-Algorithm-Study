import sys
sys.stdin = open('1427input.txt')

N = list(map(int, input()))
for _ in range(len(N)):

    for i in range(len(N)-1):
        if N[i] <= N[i+1]:
            N[i], N[i+1] = N[i+1], N[i]
print(*N, sep='')