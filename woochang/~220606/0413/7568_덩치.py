import sys
sys.stdin = open('7568input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
stack = []
index = []
rank_index = []
for i in range(N):
    rank_index.append(i)
for i in arr:
    stack.append(i[0])
stack.sort()
print(stack)
for i in range(N):
    for j in range(N):
        if stack[i] == arr[j][0]:
            index.append(j)
print(index)
print(rank_index)
