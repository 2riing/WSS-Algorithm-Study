import sys
sys.stdin = open('1978input.txt')


def sosu(a):
    error = 0
    for j in range(2, a//2+1):
        if a % j == 0:
            error += 1
    if error != 0: # 소수가 아니라는거
        return 0
    else:
        return 1




N = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(N):
    if arr[i] == 1:
        pass
    else:
        cnt += sosu(arr[i])
print(cnt)