import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    max_a = 0
    for i in range(len(arr)):
        if max_a < arr[i]:
            max_a = arr[i]
    print(f'#{tc} {max_a}')
