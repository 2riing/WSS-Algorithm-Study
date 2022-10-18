import sys
sys.stdin = open('13458input.txt')

N = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0

for i in range(N):
    if arr[i]<= B:
        cnt += 1
    else: # arr[i] > B
        abc = arr[i] - B
        cnt += 1

        # cnt += ((arr[i]-B) // C) + 1
        if abc % C ==0:
            cnt += abc // C
        else:
            cnt += (abc // C )+ 1
print(cnt)