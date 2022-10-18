# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# num4 = int(input())
# num5 = int(input())
# num6 = int(input())
# num7 = int(input())
# num8 = int(input())
# num9 = int(input())
#
# arr = [num1, num2, num3, num4, num5, num6, num7, num8, num9]
#
# max_num = 0
# max_count = 0
# for i in range(9):
#     if max_num < arr[i]:
#         max_num = arr[i]
# print(max_num)
#
# for j in range(9):
#     if arr[j] = max_num:
#     max_count = j+1
# print(max_count)
#
#
#
# # for i in range(N-1):
# #     for j in range(N-i-1):
# #         if arr[j] > arr[j+1]:
# #             arr[j], arr[j+1] = arr[j+1], arr[j]
#
# # print(arr[0],arr[N-1])

max_num = 0
max_count = 0

for i in range (1,10):
    A = int(input())
    if max_num < A :
        max_num = A
        max_count = i
print(max_num)
print(max_count)