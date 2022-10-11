import sys
sys.stdin = open('../0602/input.txt')
S = input()
result, temp, flag = '', '', 0

for s in S:
    if flag == 0:
        if s == "<": # 여는 tag이면 flag 1
            flag = 1
            temp += s
        elif s == " ": # 공백이면
            temp += s
            result += temp # 추가해주고
            temp = '' # 초기화
        else:
            temp = s + temp # 앞쪽에 추가 (reverse word)

    elif flag: # tag안에 들어있는 것일 때
        temp += s
        if s == '>':
            flag = False # end tag word
            result += temp # non-reverse-word
            temp = ''

print(result + temp)

