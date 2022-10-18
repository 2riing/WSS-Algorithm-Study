import sys
sys.stdin = open('10816input.txt')

N = int(input())
N_list = list(map(int ,input().split()))
M = int(input())
M_list = list(map(int ,input().split()))

# for i in M_list:
#     cnt = 0
#     for j in N_list:
#         if j == i:
#             cnt += 1
#     print(cnt, end=' ')

M_index = [0]*M
for i in range(len(M_list)):
    M_index[i] = N_list.count(M_list[i])
print(*M_index)