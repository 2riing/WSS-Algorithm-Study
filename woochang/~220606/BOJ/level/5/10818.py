N = int(input())

arr = list(map(int, input().split()))

max_num = 0
min_num = 1000000
for i in range(N):
    if max_num < arr[i]:
        max_num = arr[i]
    if min_num > arr[i]:
        min_num = arr[i]

print(f'{min_num} {max_num}')

# for i in range(N-1):
#     for j in range(N-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
#
# print(arr[0],arr[N-1])
# 단순한 이중 포문인데 왜 시간 초과 .. ?










