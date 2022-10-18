import sys
sys.stdin = open('1259input.txt')

for _ in range(1000000000000):
    N = int(input())
    if N == 0:
        break
    else:
        cnt = 0
        a = str(N)
        for i in range(len(a) // 2):
            if a[i] == a[len(a)-i-1]:
                cnt += 1
        if cnt == (len(a) // 2):
            print('yes')
        else:
            print('no')


