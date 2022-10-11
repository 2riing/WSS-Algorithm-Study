import sys
sys.stdin = open('input.txt')

# 쇠막대기

# 이전, 다음 것을 비교해주기 위해서 문자열 0을 붙여주었음
brackets = '0' + input() + '0'
stack = []
cnt = 0

for i in range(len(brackets)):
    if brackets[i] == '(': # 여는괄호를 만났을 때
        if brackets[i+1] == '(': # 다음괄호도 여는 괄호일 때
            stack.append('(') # 처음 괄호를 열면 cnt
            cnt += 1
        elif brackets[i+1] ==')': # 레이저
            cnt += len(stack) # 스택에 쌓여있는 길이만큼 cnt

    elif brackets[i] == ')': # 닫는괄호를 만났을 때
        if brackets[i-1] == ')': # 이전도 닫는 괄호일 때
            stack.pop()
        elif brackets[i-1] =='(': # 레이저
            pass
print(cnt)
