import sys
input = sys.stdin.readline
N=int(input())
cnt = 0
ans = 0
for i in range(9876543211):
    K = str(i)
    k_list = []
    if N == cnt:
        ans = i
        break

    else:
        if i <= 10:
            cnt += 1
        elif 10 < i < 100 and K[0] > K[1]:
            cnt += 1
        elif 100 < i < 1000 and K[0] > K[1] > K[2]:
            cnt += 1
        elif 1000 < i < 10000 and K[0] > K[1] > K[2] > K[3]:
            cnt += 1
        elif 10000 < i < 100000 and K[0] > K[1] > K[2] > K[3] > K[4]:
            cnt += 1
        elif 100000 < i < 1000000 and K[0] > K[1] > K[2] > K[3] > K[4] > K[5]:
            cnt += 1
        elif 1000000 < i < 10000000 and K[0] > K[1] > K[2] > K[3] > K[4] > K[5] > K[6]:
            cnt += 1
        elif 10000000 < i < 100000000 and K[0] > K[1] > K[2] >K[3] > K[4] > K[5] > K[6] > K[7]:
            cnt += 1
        elif 100000000 < i < 1000000000 and K[0] > K[1] > K[2] >K[3] > K[4] > K[5] > K[6] > K[7] > K[8]:

            cnt += 1
        elif 1000000000 < i < 10000000000 and K[0] > K[1] > K[2] >K[3] > K[4] > K[5] > K[6] > K[7] > K[8] > K[9]:
            cnt += 1
if N > cnt:
    print(-1)
else:

    print(ans)

