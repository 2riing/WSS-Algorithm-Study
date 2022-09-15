def solution(dartResult): # 문자열임
    answer = []
    dart = list(dartResult)
    res = []
    for i in range(len(dart)): # 인덱스 고려 안해도 되는게 어차피 숫자는 SDT나 *# 보다 앞에옴
        if dart[i] == '1' and dart[i+1] == '0': # 10은 한번에 묶어서
            res.append('10')
        elif dart[i] == '0' and dart[i-1] == '1': # 이거 해줘야 0일때 안넣고 지나감
            pass
        else:
            res.append(dart[i])
    print(res)
    for i in range(1,len(res)): # 숫자는 무시하고 지나감
        # SDT
        if res[i] == 'S':
            answer.append(int(res[i-1]))
        elif res[i] == 'D':
            answer.append(int(res[i-1]) ** 2) # 점수^2
        elif res[i] == 'T':
            answer.append(int(res[i-1]) ** 3) # 점수^3
        # 옵션
        elif res[i] == '*':
            if len(answer) >= 2:
                answer[-1] = answer[-1] * 2 # 해당 점수
                answer[-2] = answer[-2] * 2 # 바로 전에 얻은 점수
            else:
                answer[-1] = answer[-1] * 2 # 처음것만 ㅇㅇ
        elif res[i] == '#':
            answer[-1] = answer[-1] * -1
    return sum(answer)