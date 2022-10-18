import sys
sys.stdin = open('1764input.txt')
import

N, M = map(int, input().split())
d_list = []
b_list = []
ans_list = []
cnt = 0
for i in range(N):
    d_list.append(input())
s1 = set(d_list)
for i in range(M):
    b_list.append(input())
s2 = set(b_list)
a1 = s1 & s2
print(len(a1))
for i in a1:
    print(i)
# for _ in range(M):
#     a = input()
#     if a in d_list:
#         cnt += 1
#         ans_list.append(a)
# print(cnt)
# for i in ans_list:
#     print(i)