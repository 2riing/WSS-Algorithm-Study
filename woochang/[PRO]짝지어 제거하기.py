def solution(s):
    answer = -1

    while True:
        c = 0
        if s[c] == s[c + 1]:
            s = s[0:c] + s[c + 2:]
        break
    return answer

s = 'baabaa'
a = solution(s)
print(a)
