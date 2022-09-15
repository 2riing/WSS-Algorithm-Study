def solution(n, arr1, arr2):
    answer = []
    fullmap = []
    for i in range(n):
        fullmap.append(arr1[i] | arr2[i])

    for i in range(n):
        x = bin(fullmap[i])[2:]
        if len(x) < n:
            x = '0' * (n - len(x)) + x
        fullmap[i] = x

    for secret in fullmap:
        haedok = ''
        for i in range(n):
            if secret[i] == '1':
                haedok += '#'
            elif secret[i] == '0':
                haedok += ' '
        answer.append(haedok)
    return answer