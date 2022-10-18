import sys
sys.stdin = open('13305input.txt')

N = int(input())
len_list = list(map(int, input().split()))
stop_list = list(map(int, input().split()))

K = len(len_list)
M = len(stop_list)
total_len_oil = sum(len_list) * stop_list[0]
min_price = stop_list[0]
new_len_list = sum(len_list)
for i in range(1, K):
    new_len_list -= len_list[i]
    if stop_list[i] >= min_price :
        pass
    else :
        # sum_len_nam = 0
        # for j in range(i, K):
        #     sum_len_nam += len_list[j]
        # new_len_list -= len_list[i]
        total_len_oil -= (min_price - stop_list[i]) * new_len_list
        min_price = stop_list[i]
print(total_len_oil)


# 처음부터 마지막까지 거리를 다 더해
# 맨 처음 숫자를 곱해서 최솟값으로 내비둬
# 그 다음 숫자가 이전 숫자보다 크다 그러면 pass
# 작으면 맨처음 기름값 / 이후에 나온 숫자만큼의 거리를 빼줘
#
#