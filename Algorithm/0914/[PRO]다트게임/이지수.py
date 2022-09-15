def solution(dartResult):
    answer = []
    result = []
    new_dart = list(dartResult)
    for i in range(len(new_dart)):
        if new_dart[i] == '1' and new_dart[i + 1] == '0':
            result.append('10')
        elif new_dart[i] == '0' and new_dart[i - 1] == '1':
            continue
        else:
            result.append(new_dart[i])
    print(result)

    for i in range(1, len(result)):
        if result[i] == '+':
            continue
        elif result[i] == 'S':
            answer.append(int(result[i - 1]) ** 1)
        elif result[i] == 'D':
            answer.append(int(result[i - 1]) ** 2)
        elif result[i] == 'T':
            answer.append(int(result[i - 1]) ** 3)

        if result[i] == '*':
            if len(answer) >= 2:
                answer[-1] = answer[-1] * 2
                answer[-2] = answer[-2] * 2
            else:
                answer[-1] = answer[-1] * 2
        elif result[i] == '#':
            answer[-1] = answer[-1] * (-1)
    return sum(answer)