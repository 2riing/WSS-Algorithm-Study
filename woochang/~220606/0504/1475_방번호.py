import sys
sys.stdin = open('1475input.txt')


N = str(input())
num = []
num_list = [0]*10
# print(num_list)
for i in range(len(N)):
    num.append(int(N[i]))
# num.sort()
for i in num:
    num_list[i] += 1
num_list[6] += num_list[9]
num_list[9] = 0
if num_list[6] % 2 == 1:
    num_list[6] = (num_list[6] // 2) + 1
else: num_list[6] = (num_list[6] // 2)
# num_list[6] = (num_list[6] // 2) + 1
ans = 0
for i in num_list:
    if ans < i:
        ans = i
print(ans)
# print(num.
# cnt = 0
# for i in num:
#     if i == 6 or i == 9:
#         cnt += 1
# print((cnt // 2) + 1)

# cnt = int(N)
# a = num.pop()
# print(a)


