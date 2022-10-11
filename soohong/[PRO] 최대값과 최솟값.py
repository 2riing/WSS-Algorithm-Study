def solution(s):
    numbers = s.split(' ')

    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

    answer = str(min(numbers)) + ' ' + str(max(numbers))

    return answer