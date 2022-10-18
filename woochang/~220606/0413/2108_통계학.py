import sys
sys.stdin = open('2108input.txt')

N = int(input())
stack = []
for i in range(N):
    stack.append(int(input()))
# print(stack)
stack.sort()
sansul = 0
for i in stack:
    sansul += i

a = round(sansul/len(stack),0)
print('%d' % (a))   # 산술평균
# ------------------------------------------------
print(stack[len(stack)//2]) # 중앙값
#------------------------------------------
max_num = 0
max_count = 1
max_stack1 = []
max_stack2 = []
for i in range(len(stack)-1):
    if stack[i] == stack[i+1]:  # 일단 겹치는거는
        max_num = stack[i]      # 최빈값 - max_num
        max_count += 1
        max_stack1.append(stack[i])  # 그리고 max_stack에 넣어줌
        if stack[i] not in max_stack2:
            max_stack2.append(stack[i])
    elif stack[i] != stack[i+1]:
        max_count = 1
if max_stack1 == []:
    if len(stack) == 1:
        print(stack[0])
    else:
        print(stack[1])
elif len(max_stack2)>=2:
    ms_count = 0
    for k in range(len(max_stack-1)):
        if max_stack[k] == max_stack[k+1]:
            ms_count += 1

    print(max_stack[1])
else: print(max_num)              # 최빈값
# -------------------------------------
print(stack[N-1] - stack[0])   # 범위

