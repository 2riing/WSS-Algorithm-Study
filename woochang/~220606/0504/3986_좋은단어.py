import sys
sys.stdin = open('3986input.txt')
from collections import deque

def archi():
    global total_ans
    # k = len(lis)
    c = -1
    while  len(lis) %2 ==0 and len(lis) >=2 :
        c += 1
        if lis[0] == lis[len(lis)-1]:
            del lis[len(lis)-1]
            del lis[0]
        elif lis[len(lis)-1] == lis[len(lis)-2]:
            del lis[len(lis)-1]
            del lis[len(lis)-1]
        elif lis[c] == lis[c + 1]:
            del lis[c + 1]
            del lis[c]
            c -= 2


    if len(lis) == 0:
        total_ans += 1

# def qq():
#     global total_ans
#
#     stack = []
#     k = 0
#     while len(lis) >= 2 and len(lis) % 2 == 0:
#         stack.append(lis[k])
#         del lis[k]
#
#         if stack[-1] == lis[k]:
#             del stack[-1]
#             del lis[k]
#         elif stack[-1] == lis[-1-k]:
#             del stack[-1]
#             del lis[-1-k]
#             k = 0
#         else: k+=1
#     if len(stack) == 0 and len(lis)==0:
#         total_ans += 1





N = int(input())
# arr = [list(map(str, input().split())) for _ in range(N)]
# print(arr)
total_ans = 0
for i in range(N):
    wor = str(input())
    lis = []
    for j in range(len(wor)):
        lis.append(wor[j])
    # print(lis)
    # print(lis[-1])
    archi()
print(total_ans)