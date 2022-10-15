def solution(s):
    answer = []
    zero = 0
    cnt = 0
    for _ in range(5):
        if s == '1':
            break
        numbers = ''
        cnt += 1
        for i in range(len(s)):
            if s[i] == '0':
                zero += 1
            else:
                numbers += s[i]
        s = bin(len(numbers))[2:]

    return cnt, zero