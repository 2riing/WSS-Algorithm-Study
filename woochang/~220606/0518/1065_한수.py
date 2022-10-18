import sys
sys.stdin = open('1065input.txt')

N = int(input())
cnt = 99
if N < 100:
    # cnt = N
    print(N)
elif 100 <= N < 1000:
    # K = str(N)
    # n_1 = K[0]
    # n_2 = K[1]
    # n_3 = K[2]
    for i in range(110, N+1):
        K = str(i)
        n_1 = int(K[0])
        n_2 = int(K[1])
        n_3 = int(K[2])
        if n_1 <= n_2 <= n_3:
            if (n_2 - n_1) == (n_3 - n_2):
                cnt += 1
        elif n_1 >= n_2 >= n_3:
            if (n_1 - n_2) == (n_2 - n_3):
                cnt += 1
    print(cnt)
elif N == 1000:
    print(144)

