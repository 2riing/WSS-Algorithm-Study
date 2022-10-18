import sys
sys.stdin = open('2504input.txt')

N = list(map(str, input()))

# print(N)
# print(len(N))
# print(N[0]
#       )
# print(N[2])
stack = []
cnt = 0
sum_cnt = 0
for i in range(len(N)):
    if N[i] == '(' or N[i] == '[':
        stack.append(N[i])

    elif N[i] == ')':
        # stack.pop()
        if N[i-1]== '(':
            cnt += 2
            stack.pop()
        else:
            cnt *= 2
            stack.pop()
    else: #]
        if N[i - 1] == '[':
            cnt += 3
            stack.pop()
        else:
            cnt *= 3
            stack.pop()
    if len(stack) == 0:
        sum_cnt = cnt
        cnt = 0
if len(stack) == 0:
    print(sum_cnt)
else: print(0)



# for문 전에 스택이 없을때 새로운 sum 계산 만들기
# pop을 맞지않는걸 뺄때 에러