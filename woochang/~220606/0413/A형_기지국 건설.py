from itertools import combinations
from collections import deque
import sys
sys.stdin = open('기지국input.txt')

def dfs(cc, cc_list):
    global cnt
    if (cc % W) // 2 == 1:
        dt = [-W - 1, -W, -W + 1, -1, +1, +W]
    else:
        dt = [-W, -1, +1, W - 1, W, W + 1]
    cnt += 1
    cc_stack.append(cc)

    for j in dt:
        if 1 <= (cc + j) <= comb:
            if cc + j not in cc_list:
                pass
            else:
                cc_list.remove(cc + j)
                dfs(cc + j, cc_list)
    if cnt == 4:
        newcom_list.append(cc_stack)


T = int(input())
for tc in range(1, T + 1):
    W, H = map(int, input().split())

    ##############
    comb = W * H
    stack = []
    for i in range(1, comb + 1):
        stack.append(i)
    com_list = list(combinations(stack, 4))
    newcom_list = []

    ################
    arr = [list(map(int, input().split())) for _ in range(H)]
    ans = 0
    arr_list = [0]
    for a in range(H):
        for b in range(W):
            arr_list.append(arr[a][b])

    for cc in com_list:
        cnt = 0
        list_cc = list(cc)
        cc_stack = []
        dfs(cc[0], list_cc)
    for com1 in newcom_list:
        if (arr_list[com1[0]] + arr_list[com1[1]] + arr_list[com1[2]] + arr_list[com1[3]]) ** 2 > ans:
            ans = (arr_list[com1[0]] + arr_list[com1[1]] + arr_list[com1[2]] + arr_list[com1[3]]) ** 2
    print(f'#{tc} {ans}')

# 1번 아웃풋 2250000 (440 + 190 + 450 + 420) ^ 2


