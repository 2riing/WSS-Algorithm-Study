import sys
sys.stdin = open('2910input.txt')


# def ppp():

N, M = map(int, input().split())

num_list = []
num_count = []
arr = list(map(int, input().split()))
for i in arr:
    if i not in num_list:
        num_list.append(i)
k = len(num_list)
num_count = [0]*k
for j in arr:
    for l in range(k):
        if j == num_list[l]:
            num_count[l] += 1
for _ in range(len(num_list)):
    max_num = 0
    max_index = 0
    for i in range(len(num_list)):
        if num_count[i] > max_num:
            max_num = num_count[i]
            max_index = i
    for i in range(max_num):
        print(num_list[max_index], end=' ')
    num_list[max_index] = 0
    num_count[max_index] = 0



# 스택을 2개 만든다
# 하나는 그 숫자가 뭔지 확인하는 리스트
# 다른 하나는 그 숫자의 빈도 개수 리스트
# 그러면 for문을 주구장창 돌려서 빈도 제일 많은거를 먼저 빈도만큼 출력 그리고 지우고 리셋 반복 프린트 end=''