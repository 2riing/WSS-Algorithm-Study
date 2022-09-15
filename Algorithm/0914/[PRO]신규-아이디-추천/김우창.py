new_id = ["z-+.^.","=.=","123_.def","abcdefghijklmn.p"]


def solution(new_id):
    answer = ''
    new_id = new_id.lower()  # 1단계 ㅇ
    # print(new_id)
    leveltwo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_', '.']
    for le in new_id:
        if le in leveltwo: # 2단계 ㅇ
            answer += le

    # print(answer)
    new_ans = list(answer)
    new_ans1 = []
    answer = ''
    for le in new_ans: # 3단계
        if le == '.':
            if len(new_ans1) > 0 and new_ans1[-1] == '.':
                pass
            else:
                new_ans1.append(le)

        else:
            new_ans1.append(le)
    if new_ans1[-1] == '.' and len(new_ans1) >0: # 4단계
        new_ans1.pop()
    if new_ans1 == []:
        pass
    else:

        if new_ans1[0] == '.'  and len(new_ans1) >0:
            for le in range(1, len(new_ans1)):
                answer += new_ans1[le]
        else:
            for le in range(len(new_ans1)):
                answer += new_ans1[le]
    # print(answer)
    if answer == '': # 5단계
        answer += 'a'
    ans3 = list(answer)
    new_ans2= ''
    answer = ''
    if len(ans3) >= 16:
        for ii in range(15):
            new_ans2 += ans3[ii]
    else:
        for ii in ans3:
            new_ans2 += ii
    new_ans3 = list(new_ans2)
    new_ans4 = []
    for i in range(len(new_ans3)):
        if i == len(new_ans3)-1 and new_ans3[i] == '.':
            pass
        else:
            new_ans4.append( new_ans3[i])
    answer = ''
    while len(new_ans4) <=2:
        new_ans4.append(new_ans4[-1])
    for i in new_ans4:
        answer += i
    return answer

for i in range(len(new_id)):
    ans = solution(new_id[i])
    print(ans)