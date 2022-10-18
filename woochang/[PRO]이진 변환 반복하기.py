def solution(s):
    answer = []
    cnt1 = 0  # 몇번 이진변환 했는지
    cnt2 = 0  # 0으로 제거된놈 개수
    while len(s) > 1:  # 1이 될때까지 반복 = 문자열 길이가 2 이상이면 계속 돌아감
        new_s = ''
        for i in s:
            if i == '1':
                new_s += i
            else:
                cnt2 += 1  # 0으로 제거된 놈 업

        k = bin(len(new_s))
        s = k[2:]
        cnt1 += 1  # 이진변환 한 개수 업

    answer.append(cnt1)
    answer.append(cnt2)
    return answer

