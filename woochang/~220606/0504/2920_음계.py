import sys
sys.stdin = open('2920input.txt')

N = list(map(int,input().split()))
# print(N)

if N[0] < N[1] < N[2] < N[3] < N[4] < N[5] < N[6] < N[7] :
    print('ascending')
elif N[0] > N[1] > N[2] > N[3] > N[4] > N[5] > N[6] > N[7] :
    print('descending')
else:
    print('mixed')