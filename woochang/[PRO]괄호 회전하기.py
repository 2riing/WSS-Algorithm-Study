def spin(sen):
    stack = [0]
    for i in range(len(sen)):
        if sen[i] in ['[', '{', '(', ]:
            stack.append(sen[i])
        elif sen[i] == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                stack.append(sen[i])
        elif sen[i] == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                stack.append(sen[i])
        elif sen[i] == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(sen[i])
    if stack == [0]:
        return 1
    else:
        return 0


def solution(s):
    answer = 0
    for i in range(len(s)):
        res = spin(s)
        answer += res
        new_s = s[1:] + s[0]
        s = new_s
    return answer