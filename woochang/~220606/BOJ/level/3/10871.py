import sys
sys.stdin = open('input.txt')

N, X = map(int,input().split())

A = list(map(int,input().split()))

# for i in range(1, X+1):
#     for j in range(1, A+1):
#         if j < int(i):
#             print(j)
#         else: None
li = []
for i in range(N):
    if A[i] < X:
        li.append(A[i])
for j in li:
    print(j)        
# print(li)