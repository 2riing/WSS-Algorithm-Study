import sys
sys.stdin = open('10828input.txt')

# 얘도 시간초과

N=int(input())
stack = []
for _ in range(N):
    command = input()
    if len(command)>=6:
        stack.append(int(command[5:]))
    elif command == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            a = stack.pop(-1)
            print(a)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if len(stack) >= 1:
            print(0)
        else: print(1)
    else:
        if len(stack) ==0:
            print(-1)
        else:
            print(stack[-1])



# for i in range(N):
#     command = sys.stdin.readline().split()
#
#     if command[0] == 'push':
#         stack.append(command[1])
#
#     elif command[0] == 'pop':
#         if len(stack) == 0:
#             print(-1)
#         else:
#             print(stack.pop())
#
#     elif command[0] == 'size':
#         print(len(stack))
#
#     elif command[0] == 'empty':
#         if len(stack) == 0:
#             print(1)
#         else:
#             print(0)