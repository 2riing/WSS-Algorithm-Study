
import sys
sys.stdin=open('../0504/input.txt')

N = int(input())
words = [list(input()) for _ in range(N)]

stack = []
cnt = 0
for dans in words:
    for word in dans:
        if len(stack)>0:
            if stack[-1] == word:
                stack.pop()
            else:
                stack.append(word)
        else:
            stack.append(word)
    if len(stack) == 0:
        cnt += 1
    stack = []


print(cnt)