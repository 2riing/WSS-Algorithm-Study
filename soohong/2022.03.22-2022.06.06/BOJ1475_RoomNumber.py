import sys
sys.stdin = open('../0504/input.txt')

N = list(map(int, input())) # room number input list
num_cards = [0] * 9

for i in range(len(N)):
    if N[i] == 9: # 9 이면 6에 더하기
        num_cards[6] += 1
    else:
        num_cards[N[i]] += 1

result = 0
# 가장 큰 빈도수가 6이면, 같은 빈도수가 있는지 찾아보고 없으면 /2
if max(num_cards) == num_cards[6]:
    num_cards.sort(reverse=True)
    if num_cards[0] == num_cards[1]:
        result = num_cards[0]
    else:
        if num_cards[0] % 2: # 홀수
            result = int(num_cards[0]/2)+1
        else:
            result = int(num_cards[0] / 2)
# 아니라면 바로 result = maxnum
else:
    result = max(num_cards)
print(result)