def solution(s):
    answer = ''
    # print(ord('A')) # 65
    # print(ord('Z')) # 90
    # print(ord('a')) # 97
    # print(ord('z')) # 122
    s = s.lower()
    print(s)
    k = ord(s[0])
    if k >= 97 and k <= 122:
        k -= 32
        p = chr(k)
        answer += p
    else:
        p = chr(k)
        answer += p
    for i in range(1, len(s)):
        k = ord(s[i])
        if s[i - 1] == ' ' and k >= 97 and k <= 122:
            k -= 32
            p = chr(k)
            answer += p
        else:
            p = chr(k)
            answer += p

    return answer