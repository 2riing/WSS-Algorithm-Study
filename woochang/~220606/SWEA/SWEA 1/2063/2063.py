import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))
mid_N = (N // 2)

for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr[mid_N])
