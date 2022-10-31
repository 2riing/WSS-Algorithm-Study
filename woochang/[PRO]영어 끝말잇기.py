def solution(n, words):
    answer = [0, 0]

    stack = []

    for i in range(len(words)):
        word = words[i]
        num1 = (i // n) + 1  # 몫 = 자신의 y번째 차례
        num2 = (i % n) + 1  # 나머지 = x번 사람
        if i == 0:
            pass
        else:
            if lastword[-1] != word[0]:
                answer = [num2, num1]
                break

        if word not in stack:  # 들어있으면 짤
            stack.append(word)
        else:
            answer = [num2, num1]
            break
        lastword = words[i]

    return answer