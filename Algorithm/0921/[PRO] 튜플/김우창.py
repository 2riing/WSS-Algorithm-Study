s = ["{{2},{2,1},{2,1,3},{2,1,3,4}}","{{1,2,3},{2,1},{1,2,4,3},{2}}","{{20,111},{111}}","{{123}}","{{4,2,3},{3},{2,3,4,1},{2,3}}"]

def solution(s):
    answer = []
    answer1 = []
    result = []
    p = 0
    ans = ''
    while len(s)-1 > p: # 문자열 리스트화 작업
        p += 1
        if s[p] == "{":
            answer = []
        elif s[p] == "}":
            if len(ans) > 0 and int(ans) not in answer:
                answer.append(int(ans))
                answer1.append(answer)
                ans = ''
            else:
                ans = ''
        elif s[p] == ",":
            if s[p-1] == "}":
                pass
            else:
                answer.append(int(ans))
                ans = ''
        else:
            ans += s[p]
    answer1.sort(key=len) # 순서대로 정렬
    for i in answer1:
        for j in i:
            if j not in result:
                result.append(j)


    return result

for i in range(len(s)):
    solution(s[i])