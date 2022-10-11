

# 97-122

def solution(s):
    answer = ''
    temp = ''
    for i in range(len(s)):
        if s[i] in num: # 숫자는 바로 answer에 더해줌
            answer += s[i]
        else:
            temp += s[i]
            if temp in numbers: # 더하다가 numbers안에 있으면 Convert
                answer += Convert(temp)
                temp = ''
    return int(answer) # 답이 정수형

def Convert(s): # 문자를 숫자로 바꿔줌
    for i in range(len(numbers)):
        if s == numbers[i]:
            return num[i]

numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
s = "one4seveneight"
print(solution(s))