import sys
sys.stdin = open('../0504/input.txt')

N, C = map(int, input().split())
numbers = list(map(int, input().split()))
cnt_num = [0]*(C+1)

set_numbers = []
for number in numbers:
    if number not in set_numbers:
        set_numbers.append(number)

for i in range(N): # 버켓에 빈도 수 채워 넣기
    cnt_num[numbers[i]] += 1

new_arr = []
for j in range(C+1):
    if cnt_num[j] > 0:
        new_arr.append([j, cnt_num[j]])
new_arr.append([-1,-1]) # index error prevent

new_arr.sort(key=lambda x: -x[1])
same_fre_num = []
fre_num = 0
result = []

for k in range(len(new_arr)-1):
    if new_arr[k][1] != new_arr[k + 1][1]:  # 같지 않을때
        if len(same_fre_num) > 0:  # 빈도수 같은거 존재할때
            idx = []
            for same_num in same_fre_num:
                idx.append([same_num, numbers.index(same_num)])
            idx.sort(key=lambda x:x[1]) # 오름 차순으로 정렬
            for n in range(len(idx)):
                for new_idx in range(len(new_arr)):
                    if new_arr[new_idx][0] == idx[n][0]:
                        for _ in range(new_arr[new_idx][1]): # 반복 횟수
                            result.append(idx[n][0])
            same_fre_num = []
        else: # 빈도수 같은 것 없으면서 다음거랑 같지 않을 때
            for k1 in range(new_arr[k][1]):
                result.append(new_arr[k][0])

    else: # 다음거랑 빈도수가 같을 때
        if new_arr[k][0] not in same_fre_num :
            same_fre_num.append(new_arr[k][0])
        if new_arr[k][1] not in same_fre_num:
            same_fre_num.append(new_arr[k+1][0])
        fre_num = new_arr[k][1]

print(*result)


