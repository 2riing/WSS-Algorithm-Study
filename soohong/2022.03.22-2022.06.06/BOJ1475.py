import sys
sys.stdin = open('input.txt')

N = input()
num_list = [0] * 10
for num in N:
    num_list[int(num)] += 1

max_num = 0
max_index = 0
for i in range(10):
    if num_list[i] > max_num:
        max_num = num_list[i]
        max_index = i

if max_index == 6 or max_index == 9:
    max_num = num_list[6] + num_list[9]
    if max_num % 2:
        print(int(max_num/2)+1)
    else:
        print(int(max_num/2))
else:
    print(max_num)

