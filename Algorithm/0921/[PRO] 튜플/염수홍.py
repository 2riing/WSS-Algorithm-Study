# ntemp 길이가 있는경우 계속 추가해줌
# , 나오는경우 temp에 숫자 추가해주고 ntemp 초기화

def solution(s):
    numbers = []
    temp = []
    ntemp = ''
    pre = ''
    for a in s:
        if a.isdigit() == True: # 이전에가 여는 괄호, 현재가 숫자면
            ntemp += a
        elif len(ntemp) > 0 and a.isdigit() == False:
            temp.append(int(ntemp)) # temp에 숫자를 추가해줌
            ntemp = ''
        if a == '}': # 닫는 괄호면
            numbers.append(temp)  # numbers에 추가하고
            temp = [] # temp 초기화
        pre = a
    numbers.sort(key=len)
    answer = []
    for number in numbers:
        for num in number:
            if num not in answer:
                answer.append(num)
    return answer
            