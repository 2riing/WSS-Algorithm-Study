n = [5, 6]
arr1 = [[9, 20, 28, 18, 11],[46, 33, 33 ,22, 31, 50]]
arr2 = [	[30, 1, 21, 17, 28],	[27 ,56, 19, 14, 14, 10]]

def solution(n, arr1, arr2):

    answer = []
    for i in range(n):
        arr1[i] = format(arr1[i], 'b') # 이진수 변환 (str로)
        arr2[i] = format(arr2[i], 'b')
        ans = ''
        sum_arr = str(int(arr1[i]) + int(arr2[i])) # 2개 합친거 (2가되도 상관없음 길이만 볼거라)
        if len(sum_arr) < n:
            sum_arr= '0'*(n-len(sum_arr)) + sum_arr # 기존의 앞에다 붙여야됨
        for j in sum_arr:
            if j == '0': # 0이면 빈칸
                ans = ans+' '
            else:        # 1이면 #
                ans = ans+'#'
        answer.append(ans)



    return answer

for i in range(len(n)):
    solution(n[i],arr1[i],arr2[i])